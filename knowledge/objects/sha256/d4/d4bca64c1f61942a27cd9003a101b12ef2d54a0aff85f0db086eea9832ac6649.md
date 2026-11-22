# Argus Vac context refresh — 22 November 2026

This is a review of dated records, not a new live robot test. Sources: the
14 November Argus chat and [local roaming progress](../../workspace/robot_control/progress/2026-11-14-lidar-roaming.md),
[GitHub main at 802b216d](https://github.com/minesoil/Argus.vac-manual/commit/802b216d15838611eade87c17f269bf1993e2ae6),
the [19 November schedule](https://docs.google.com/document/d/1_jxdNUTrJjb9dQszOOyR57c2Cohulxxr9PGxCfO5UOY/edit),
the [21 November side-brush chat](https://chatgpt.com/c/6affe83a-5870-83ec-be22-4664b686133a),
and the [22 November automation chat](https://chatgpt.com/c/6b028cf5-6a84-83e8-b9b8-92677e34a50a).

## Navigation status retained from 14 November

The C1 scan front is raw 7.5° for the current mount, calibrated with an upright
front target. The 30 cm robot uses an estimated 15 cm body radius from the
drive-wheel midpoint and an estimated C1 origin 8 cm forward. The ESP32 phone
page showed a live 72-bin scan with robot-forward at the top, a clearer arrow,
and smoother display according to Justin. This is a relative live scan, not an
accumulated room map. The final phone status-label firmware was hash-verified
after flashing, but its new label was not confirmed visually.

The corrected-heading phone trial turned away from the marker bag and moved
forward without contact according to Justin. A separate supervised 60-second
floor run at 12% with a 0.25 m requested wall gap completed with Stop/zero;
Justin confirmed no contact and switched motor power OFF afterward. The logs
show forward motion, moving curves and pivots. They do not measure the actual
closest body gap, stopping distance, room coverage or outdoor performance.

Two **private** Pi profiles were then separated: the normal systemd profile
limits phone Start to 20 seconds and 12%; a manually launched bridge used an
indoor-only profile with no software duration cap, the same wheel limits and
the same geometry. In the subsequent phone attempt, the controller briefly
ran then stopped with the reason `Control session ended or another operator
took over`; final reported wheel outputs were zero. The record does not show
whether Justin tapped Stop, left/locked the page or lost heartbeat, or whether
there was contact. A full minute of no-time-limit phone roaming was **not**
verified. The user's last motor-power confirmation was OFF before this attempt;
he was instructed to turn it ON for the attempt, and no later OFF confirmation
is recorded. This is historical state, not a claim about power on 22 November.
The manual Pi bridge's persistence and systemd restart after reboot were not
validated. The outdoor showcase's outcome was not recorded.

## Newer project context

- On 21 November, Justin said he had printed the side-brush parts and fitted
  the N20 motors, but had not yet used them in real operation. Printing and
  fitting do not establish electrical or cleaning performance.
- The 19 November schedule targets a functional, presentable Argus prototype
  by 31 December 2026 and allocates roughly four hours per week before
  6 December, then roughly 7.5 hours per week through 31 December. These are
  plans, not work completed.
- On 22 November, Justin said he wants to focus his next 2–3 hours of Argus
  work on automation. No new physical navigation result follows from that
  preference.

## Source reconciliation

At the start of this review, GitHub main had no commits after 802b216d. It omitted the
later 7.5° correction, 60-second run, and final phone status and still contains
90° advice in its roaming guide. The
[14 November convention sheet](https://drive.google.com/file/d/1RwiIDJJyBqMxaipAJ7x2Lmd80DObdKsy/view)
was built from that older commit, so treat it as a historical snapshot. The
[Argus Drive folder](https://drive.google.com/drive/folders/1QJp4BG7FYXhRmEM8DHH-u1eUcUxIfKBT)
has older handbook/dashboard/portfolio/master records, with no newer physical
navigation test found. Gmail could not be checked because its connection
requires reauthentication. A newer assistant summary claiming phone/camera
work was never flashed conflicts with the 14 November physical tests and is
not used as evidence.

After this reconciliation, the reviewed local source, calibrated example,
and memory were published to GitHub main as
[4c0f62e](https://github.com/minesoil/Argus.vac-manual/commit/4c0f62e580ef305597f95a68f2700bc6e81922dc).
That publication changes the repository record; it does not validate a new
physical run. The older convention sheet remains a historical snapshot.

Remaining checks: determine why the no-time-limit phone session ended; verify
the phone Stop/heartbeat and Pi service after reboot; measure loaded stopping
and wall clearance; inspect low-object/drop-off sensing before any open-area
run. Floor tape is not detected by the current C1 controller.
