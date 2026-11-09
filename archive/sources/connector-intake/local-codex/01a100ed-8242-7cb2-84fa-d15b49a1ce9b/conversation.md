# Reduce NEMA 17 motor noise

Source: local Codex messages for `01a100ed-8242-7cb2-84fa-d15b49a1ce9b`

## 2026-10-03T10:34:25.022Z — user

increase speed to 2 cm a second. btw the wheel diam is 6cm

## 2026-10-03T10:34:31.249Z — assistant

Justin, I’ll update the tracked sketch for a 6 cm wheel at 2 cm/second, keeping quarter-step mode.

## 2026-10-03T10:35:59.297Z — assistant

Justin, updated the [tracked sketch to revision 1.2](</[REDACTED_HOME_PATH]>) for:

- **6 cm wheel**
- **2 cm/second**
- **1/4 microstepping**
- Approximately **2.8 seconds** ramping from 1 to 2 cm/second

It compiled successfully for the Mega; it hasn’t been uploaded.

Keep **MS2 at 5 V**, **MS1/MS3 disconnected**, and **EN on D8**. Upload the updated file, open Serial Monitor at **115200**, and send `r` to drive or `s` to disable.

## 2026-10-03T10:39:26.920Z — user

<external_codex_apps_open_page>{"page_id":null}</external_codex_apps_open_page>

## 2026-10-03T10:39:26.977Z — user

try full speed


## 2026-10-03T10:39:58.978Z — assistant

Justin, there isn’t a fixed “full speed” for this motor under load. I’ll set up an adjustable faster-speed test with a gentle start; you can choose the target before running it.

## 2026-10-03T10:40:52.552Z — user

<send_user_message_question_reply>
[{"questionItemId":"[\"request_user_input_async\",\"call_7lxY4iaX8yOeO0DnrmMdPNzL\",0]","question":"What speed should the next test target?","answer":"30 cm/second — fifteen times the current speed"}]
</send_user_message_question_reply>

## 2026-10-03T10:41:22.027Z — assistant

Justin, I’ll set the target to **30 cm/second**, about **95.5 wheel RPM** with the 6 cm wheel. It will start at 1 cm/second and ramp up over three seconds.

## 2026-10-03T10:43:04.663Z — assistant

Justin, updated the [tracked sketch to revision 1.3](</[REDACTED_HOME_PATH]>) for **30 cm/second**, approximately **95.5 RPM** with your 6 cm wheel.

It starts at **1 cm/second** and ramps up over **3 seconds**. Compilation passed for the Mega; it hasn’t been uploaded.

Keep quarter-step wiring: **MS2 → 5 V; MS1/MS3 disconnected**. Upload, open Serial Monitor at **115200**, and send `r` to run or `s` to disable.

Test with the wheels raised first. This is a speed-test target, not a verified maximum under the robot’s weight.

## 2026-10-03T10:43:29.189Z — user

<external_codex_apps_open_page>{"page_id":null}</external_codex_apps_open_page>

## 2026-10-03T10:43:29.226Z — user

update the code to using the accelstepper library, and also make it so that I can increas the speed and decrease it through serial moniotr


## 2026-10-03T10:43:37.566Z — assistant

Justin, I’ll switch the tracked sketch to AccelStepper and add Serial Monitor commands to raise or lower the speed. I’ll keep the 6 cm wheel, quarter-step wiring, and disabled startup.

## 2026-10-03T10:45:27.505Z — assistant

I’ll add `+` and `-` to change speed by 1 cm/second, plus numeric entries such as `10` for an exact target. Changes will ramp gradually. The existing `r`, `s`, and `h` commands will remain.

## 2026-10-03T10:50:26.527Z — assistant

AccelStepper is already installed. The sketch will start disabled, use the same quarter-step wiring, and ramp speed changes up or down. I’m checking the Serial commands and compiling it for your Mega.


## 2026-10-03T10:54:21.144Z — assistant

The Mega compile passed. Simulated checks also passed for `+`/`-`, exact speed entries, gradual acceleration and deceleration, and stop/hold commands. I’m updating the wiring record to match this version.


## 2026-10-03T10:55:51.510Z — assistant

Updated the [full Arduino sketch]([REDACTED_HOME_PATH] to use **AccelStepper**, with gradual speed increases and decreases. It compiled successfully for your Mega; it hasn’t been uploaded.

Set Serial Monitor to **115200 baud** and **Newline**, then send:

| Command | Action |
|---|---|
| `r` | Start running |
| `+` | Increase target by 1 cm/s |
| `-` | Decrease target by 1 cm/s |
| `2.5` | Set target to 2.5 cm/s |
| `0` | Gradually stop and hold |
| `s` | Immediately stop and disable |
| `h` | Immediately stop and hold |
| `p` | Show status and speed |
| `?` | Show help |

The motor starts disabled. **Send `2`, then `r` to test at 2 cm/s.** Otherwise, the default target is 30 cm/s.

It assumes your **6 cm wheel and quarter-step wiring**: MS2 HIGH, MS1/MS3 disconnected. The adjustable range is 0–60 cm/s; 60 is a software limit.

## 2026-10-03T11:00:29.289Z — user

even at 10 cm per second, it feels jittery/jumpy


## 2026-10-03T11:00:34.945Z — assistant

I’ll check whether the current ramp and step timing could explain the jumping at 10 cm/s, then work out the next test.


## 2026-10-03T11:01:31.240Z — user

<send_user_message_question_reply>
[{"questionItemId":"[\"request_user_input_async\",\"call_dsRUkSJOPb015g2SyoNHsNKP\",0]","question":"What is the current MS-pin wiring? The sketch assumes quarter stepping.","answer":"MS1 disconnected, MS2 connected to 5 V, MS3 disconnected"},{"questionItemId":"[\"request_user_input_async\",\"call_dsRUkSJOPb015g2SyoNHsNKP\",1]","question":"After it has run at 10 cm/s for at least 5 seconds, what does the wheel do?","answer":"Keeps turning forward, but vibrates"}]
</send_user_message_question_reply>

## 2026-10-03T11:02:03.318Z — assistant

That confirms the wiring matches the code. Steady forward rotation with vibration points more toward motor resonance or uneven microsteps than obvious stalling. At 10 cm/s, the sketch requests about 424 quarter steps per second; I’ll check the guidance for smoothing that motion.


## 2026-10-03T11:02:53.405Z — user

<external_codex_apps_open_page>{"page_id":null}</external_codex_apps_open_page>

## 2026-10-03T11:02:53.429Z — user

nvm, 10 cm per second is ok, not jittery, but its louder than 60cm per second


## 2026-10-03T11:03:27.722Z — assistant

I’ll update the record: 10 cm/s runs smoothly, but sounds louder than 60 cm/s.


## 2026-10-03T11:04:08.885Z — assistant

That can happen—**slower doesn’t always mean quieter**. Motor resonance and the driver’s current regulation can produce more noise at particular speeds. [Allegro explains these effects](https://www.allegromicro.com/en/insights-and-innovations/technical-documents/stepper-decay).

Since **10 cm/s runs smoothly**, the extra noise alone doesn’t show that it’s losing steps. Keep the current code and choose the speed your robot needs.

## 2026-10-03T11:04:54.678Z — user

at 1-5 cm per second, it can skip, and sounds very loud. once at 6-8, its less, at 9-10, it becomes quite minimal


## 2026-10-03T11:04:58.874Z — assistant

That speed pattern suggests a resonance band, though sound alone can’t confirm missed steps. I’ll check the current ramp and the A4988’s low-speed behavior before changing the code.


## 2026-10-03T11:06:28.842Z — user

<send_user_message_question_reply>
[{"questionItemId":"[\"request_user_input_async\",\"call_Inz6vkPYJ9Q0K15XBxKNLJbr\",0]","question":"With the wheel raised off the ground, does the skipping at 1–5 cm/s continue after at least 5 seconds at a fixed speed?","answer":"It only happens during startup or speed changes"}]
</send_user_message_question_reply>

## 2026-10-03T11:07:25.675Z — assistant

That points to the ramp as the first thing to tune. I’ll reduce acceleration from 10 to 2 cm/s² and add an `a` command so you can adjust it through Serial Monitor without uploading again. The steady low-speed noise may remain.


## 2026-10-03T11:10:44.824Z — assistant

Since the skipping happens **during startup or speed changes**, a gentler ramp is the next test.

I updated the [full sketch, revision 1.5]([REDACTED_HOME_PATH] default acceleration is now **2 cm/s²**, down from 10. Compilation and simulated command tests passed.

Upload it, raise the wheel, and use **115200 baud + Newline**. Send these separately:

```text
a2
2
r
```

This starts at **2 cm/s**. Wait five seconds, then send `3` to test a speed change.

- `a1` → gentler ramp.
- `a10` → restore the previous ramp if slowing it makes things worse.
- `s` → stop and disable.

The existing `+` and `-` commands still work. This adjustment targets transitional skipping; low-speed noise may remain.

## 2026-10-03T11:12:51.455Z — user

<external_codex_apps_open_page>{"page_id":null}</external_codex_apps_open_page>

## 2026-10-03T11:12:51.491Z — user

so is there anyway to fix the louder more vibrations when at 1-5 cm per second without changing microstepping?


## 2026-10-03T11:12:57.243Z — assistant

I’ll check which adjustments could reduce the vibration while keeping your current quarter-step mode.


## 2026-10-03T11:15:17.799Z — assistant

Motor manufacturers list reduced drive current, mechanical dampers, and gearing as ways to reduce vibration without changing the step mode. The `a` setting affects startup and speed changes; once the speed settles, it won’t change the step spacing.


## 2026-10-03T11:16:03.684Z — assistant

**Yes—you can often reduce it while keeping quarter stepping.** Try these in order:

1. **Test slightly lower motor current.** Record your VREF, then try about **10% lower**. Adjust with power off and measure again after powering up. Lower current can reduce vibration, but also reduces torque; restore the original setting if skipping worsens. This is worth testing even with a correctly calculated VREF. [Manufacturer guidance](https://faq.orientalmotor.com/is-there-a-way-to-reduce-vibration-during-rotation).

2. **Add mechanical damping.** A shaft damper can reduce motor oscillation. Rubber mounting mainly reduces vibration transmitted into the robot chassis. [Oriental Motor’s explanation](https://www.orientalmotor.com/stepper-motors/technology/stepper-motor-basics.html).

3. **Use gear reduction.** A 10:1 reduction lets the motor turn ten times faster while the wheel still moves slowly, potentially avoiding the noisy speed band.

Your `a1`/`a2` commands can improve starts and speed changes. **They won’t change the steady-speed vibration once the ramp finishes.**

## 2026-10-03T11:29:01.070Z — user

s


