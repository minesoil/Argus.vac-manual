"""Activate the standalone simulator collision guard for direct driving."""
import os
import time
import rclpy
from rclpy.node import Node
from lifecycle_msgs.srv import GetState, ChangeState


def main():
    rclpy.init()
    node = Node(f'vacuum_guard_start_{os.getpid()}')
    get = node.create_client(GetState, '/collision_monitor/get_state')
    change = node.create_client(ChangeState, '/collision_monitor/change_state')

    def result(future):
        deadline = time.monotonic() + 15
        while not future.done() and time.monotonic() < deadline:
            rclpy.spin_once(node, timeout_sec=.05)
        if not future.done():
            raise RuntimeError('Collision guard lifecycle request timed out.')
        return future.result()

    try:
        if not get.wait_for_service(timeout_sec=20) or not change.wait_for_service(timeout_sec=20):
            raise RuntimeError('Collision guard is not available.')
        state = result(get.call_async(GetState.Request())).current_state.id
        for expected, transition in ((1, 1), (2, 3)):
            if state == expected:
                request = ChangeState.Request()
                request.transition.id = transition
                if not result(change.call_async(request)).success:
                    raise RuntimeError('Collision guard could not be activated.')
                state = result(get.call_async(GetState.Request())).current_state.id
        if state != 3:
            raise RuntimeError(f'Collision guard is in state {state}, not active.')
        print('Collision guard active.', flush=True)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
