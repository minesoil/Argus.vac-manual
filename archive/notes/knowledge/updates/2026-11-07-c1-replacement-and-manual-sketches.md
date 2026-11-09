# C1 replacement update and manual control sketches

On November 7 Justin reported a C1 fault and said he is ordering a replacement
adapter. He is unsure which component failed. No bench result establishes an
adapter or scanner-head diagnosis. At this check the laptop Ethernet interfaces
were disconnected, so a new camera inference run on the Pi was unavailable.

A read-only search of Justin's local Arduino sketchbook found several candidates.
Two sketches dated October 25, 2026 are particularly relevant:

- `[REDACTED_HOME_PATH]`
  periodically sends `M:left,right` wheel percentages to the Mega. It continues
  sending zero percentages when the browser command is over 350 ms old.
- `[REDACTED_HOME_PATH]`
  reads USB and Serial1 into the same wheel targets, recognizes S/X stop and
  calls stopNow if the command age exceeds 900 ms. A subsequent drive command
  replaces the previous targets; this sketch has no selected command owner.

This resolves the earlier source-location gap. Multiple ESP32 sketches exist
and the flashed pair remains unconfirmed. No firmware was flashed or motors
driven. Preserve the original sketches in place and keep credentials out of
the archive.
