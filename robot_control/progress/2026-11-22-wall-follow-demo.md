# First powered right-wall trial — 22 November 2026

At 23:30 Taipei time, Argus completed the eight-second phone-started trial
beside a row of cardboard boxes. The video shows a slow forward crawl and a
stop. No box contact is visible in the recorded pass.

The Pi logged the initial stationary scan check, then 14 `Following right
wall` reports with 12% left and 9% right wheel commands. The run ended with
`END Duration limit reached`. The controller subsequently reported stopped,
zero wheel outputs and no pending Start. The bridge restart count was zero.

The controller’s right-side clearance estimate increased from roughly 0.20 m
to 0.25 m, measured beyond its inflated footprint. The trial validates a
bounded powered wall pass and normal timer stop. It leaves physical wall-gap
control, loaded cornering and operation outside this short run to be verified.

## Box-wall fit update and repeat

The wall fitter now selects the dominant face and leaves stray returns in
the obstacle checks. A follow-up run stopped on an obstacle inside the swept
footprint. The next run kept its right-side clearance estimate between about
19.8 and 20.4 cm from the modeled body while tracking, began a forward left
curve near the end, and finished at the eight-second limit. The Pi read back
stopped and zero wheel outputs afterward. The measured starting wheel-to-box
gap was approximately 15 cm. The measured final wheel-to-box gap was about
20 cm. The follow-up clip shows a slow forward pass and a brief change of
heading near the end.

The trial log now reports the fitted wall gap and heading along with wheel
commands. Gap is estimated for the configured body radius.
