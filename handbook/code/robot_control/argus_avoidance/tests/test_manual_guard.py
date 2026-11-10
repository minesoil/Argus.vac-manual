import sys
from pathlib import Path
from unittest import TestCase,mock
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from argus_avoidance.manual_guard import GuardPublisher,observation_code
from argus_avoidance.follow import ControlError

class GuardPublisherTests(TestCase):
    def test_only_fresh_finite_bounded_processing_can_be_clear(self):
        good={'state':'clear','captured_at':10,'processing_ms':20}
        self.assertEqual(observation_code(good,10.1),0)
        self.assertEqual(observation_code({**good,'state':'blocked'},10.1),1)
        for patch in ({'captured_at':9},{'captured_at':11},{'captured_at':float('nan')},{'processing_ms':201},{'processing_ms':-1},{'state':'unknown'}):
            self.assertEqual(observation_code({**good,**patch},10.1),2)
        self.assertEqual(observation_code({},10.1),2)
    def test_status_failure_publishes_fault_and_replay_cannot_resume(self):
        controller=mock.Mock()
        controller.request.side_effect=[{'guard_token':'123456789abcdef0'}, {'status':200}, ControlError('superseded',409)]
        publisher=GuardPublisher(controller,'local',fetch=mock.Mock(side_effect=OSError('offline')))
        self.assertEqual(publisher.tick({'epoch':5}),2)
        self.assertEqual(controller.request.call_args.args[1]['code'],2)
        self.assertEqual(publisher.tick({'epoch':5}),2)
        self.assertIsNone(publisher.token)
    def test_claim_token_and_monotonic_sequence_scope_reports(self):
        c=mock.Mock();c.request.side_effect=[{'guard_token':'123456789abcdef0'}, {}, {}]
        publisher=GuardPublisher(c,'local',fetch=lambda _: {'state':'clear','captured_at':10,'processing_ms':5},clock=lambda:10.1)
        self.assertEqual(publisher.tick({'epoch':8}),0)
        self.assertEqual(publisher.tick({'epoch':8}),0)
        calls=c.request.call_args_list
        self.assertEqual(calls[0].args,('/guard/arm',{'epoch':8}))
        self.assertEqual([calls[i].args[1]['seq'] for i in (1,2)],[1,2])
        self.assertEqual(calls[2].args[1]['session'],'123456789abcdef0')
