# Motor speed troubleshooting

Chat ID: `6ab52933-9c18-83ee-9b6a-9de48ba6eaa9`

Export scope: all pages exposed by the chat read tool. Tool outputs may be truncated; some ChatGPT answers are returned only as reference placeholders. This is not a guaranteed complete transcript. Raw responses are retained beside this text.

## 2026-09-24T22:59:22.129477+08:00

### Justin

Will this work

[User attached 1 image; image contents were not included]

### Assistant

I would **not use that listing** for TurboVac.

It is a generic 18650 lithium-ion pack, not the safer LiFePO₄ option. The claimed “12 V 32,000 mAh / 24 cells / ≤10 A” at NT$545 including a charger is also a major red flag—capacity and safety specs are not trustworthy enough for a high-current robot.

Voltage-wise, it could run 12 V-class electronics, but I would not rely on it for two steppers after your current battery issue.

Ask a parent/mentor to help choose a **reputable sealed 12.8 V LiFePO₄ pack with an integrated BMS and matched charger**, with verified continuous-current documentation. For now, a quality 12 V wall adapter is the safer choice for bench testing.

## 2026-09-24T23:04:39.459521+08:00

### Justin

What abt these

[User attached 1 image; image contents were not included]

### Assistant

No—skip this one too.

The listing explicitly says **聚合物鋰電池**: lithium-polymer/LiPo chemistry, just in a blue case with an LED indicator. It is not the safer LiFePO₄ option, and the claimed **12 V 25 Ah** capacity with a bundled 3 A charger still has no visible safety certification or trustworthy BMS details.

The case and battery-level LEDs do not solve the underlying safety issue. Don’t use a generic marketplace LiPo pack as the replacement for the questionable 3S pack.

For now, stick to a good 12 V wall adapter for bench testing, and have a parent/mentor choose any eventual onboard battery from a reputable supplier with clear protection and charger documentation.

## 2026-09-24T23:07:30.484398+08:00

### Justin

What abt these? Also what if I go back to lipos? How can I ensure that it never stops working? This is the second battery I broke already

[User attached 1 image; image contents were not included]

### Assistant

These look like **LiFePO₄ / lithium-iron** starter batteries, which are a better chemistry direction than generic LiPo packs. But the image includes many different models—some may be **6 V**, and they are designed for vehicle starting, so I can’t say a particular one will suit TurboVac from this screenshot alone.

For a parent/mentor to consider one, the exact model needs documented:

- **12.8 V nominal** output
- Built-in BMS/protection
- Verified continuous-current rating
- Manufacturer-approved charger

Don’t choose based only on “large capacity” or the listing title.

And for going back to LiPos: there is no way to guarantee one will “never stop working.” Since this is the **second pack** that has failed or acted abnormal, pause LiPo use for this project until an experienced adult checks the charger, wiring, and motor power setup. A safer plan is a reputable protected LiFePO₄ pack, or a wall adapter while you are still testing the drivetrain.

## 2026-09-24T23:09:34.033498+08:00

### Justin

To be fair the first time it stopped working was because I accidentally cut both red and balck at the same time. This time I don’t know why

### Assistant

Ah—then the first failure has a clear cause: cutting the red and black leads together created a short circuit. That does **not** mean you’ve randomly ruined two batteries the same way.

For the current pack, a charger detecting only two cells could be a failed balance lead, an internal cell fault, or a charger issue. It may not be something you did wrong.

Still keep this one disconnected and have an experienced adult/RC hobbyist check the pack and charger together. For future projects, don’t cut or modify lithium-battery leads yourself; use a pre-made protected power solution or have an adult handle any battery wiring.

## 2026-09-24T23:15:00.121836+08:00

### Justin

How much will this help? Btw Remeber that 3.7 volt thing? I’m just curious if it’s because I used the battery so much thst it got to below 12v, which caused the battery to start turning the motor only periodically, and eventually the battery stopped working at all

[User attached 1 image; image contents were not included]

### Assistant

That device would help with **diagnosis**, not prevention. It can show the total pack voltage and each cell’s voltage, which lets an adult/mentor spot an imbalanced or failed cell before it becomes a bigger issue. Do **not** use it to test the current suspect pack yourself.

About the 3.7 V point:

- **3.7 V per cell = 11.1 V total for a 3S pack**, which is normal nominal voltage.
- Going **below 12 V total** by itself would not ruin a 3S LiPo.
- A weak/discharged pack can sag under motor load and make the motor behave poorly.
- But it does **not** explain why the balance charger now detects only two cells.

The “runs briefly every ~20 seconds” symptom still sounds more like the A4988 driver repeatedly overheating/protecting itself than the battery simply being below 12 V. The missing third cell is a separate battery/balance-lead fault that needs adult inspection.
