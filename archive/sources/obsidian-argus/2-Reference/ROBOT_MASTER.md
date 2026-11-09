# Hardware Specs(Not Listed in CSV)

RPLidar C1

USB Camera

Orangepi 5 8GB

2200Mah 3s 11.1V 30C Lip Battery

5000mah portable charger

# Slight Background Info

I am building a autonomous vacuum cleaner robot

ROS 2

I have installed ROS 2 on my orangepi

The chassis is also finished. I have 2 acrylic plates separated by metal spacers

The acrylic plates are 30cm by 30 cm by 1cm. The nema is mountained in between the plates, but it is mounted with hot glue and popsicle sticks to fit thye nema in between the acrylic. I have also mounted the san ace right above the top of the acrylic board, but turns out the sunction is very weak, so I am working on changing the san ace to in between the acrylic plates, as well as turning it 90 degrees, so it is facing forwards(relative to the robot, and right behind a bag where all the dust goes), and have 2 N20 motors, add some bristles on it, and brush the dust up. I also have a castor wheel in front

I plan on making thew robot autonomous by having it map out the room using the rplidar c1, also have the usb camera and when it sees an obstacle such as socks or something, it moves away from it.

My orangepi 5 does not have a wifi/bleutooth module

Currentloy my battery is 2200 mah, but planning on upgrading to 5000 mah in the future.

Update 2026-08-25: blade fuse spec is 10 amp (was 7.5). Fuse holders are 12 awg only. No 14 awg, I don't want it.

Update 2026-08-25 (store run): Got the rest from a local store. DaKoang On-Off-On switch (250VAC-10A, 125VAC-15A, 6 screw terminals), 2x 12 awg inline fuse holders, 5x 10 amp blade fuses, 2x Wago 221-412 (2-hole), 4x Wago 221-415 (5-hole), 4x Wago 221-413 (3-hole), 2x 100uf 35v capacitors. At that time, the N20 motors and 0.1uf capacitors had not arrived yet.

Current 2026-09-27: I basically have all the parts now except the newest battery system. The older parts gap is closed. Fuse holders: just the 2x 12 awg inline ones, no 14 awg fuse holder. The new battery adapter is the thing with 14 awg red/black leads.

Update 2026-09-27: I mounted the NEMAs at the bottom of the chassis, below the acrylic. I connected the wiring for one NEMA so far. I decided to switch from the LiPo plan to a power-tool battery because it should be easier to use and safer day to day. I am waiting for the power-tool battery adapter parts. The adapter should go from the tool battery to 14 awg red and black wire. Before powering the robot from it, check voltage, polarity, and fuse placement.

Correction 2026-09-27: I already know the correct Vref. Basically all parts have arrived except the newest battery system.

Sensor update 2026-09-27: I already mounted a camera and the lidar.

