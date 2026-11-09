# FRC _ Science Fair _ Vacuum Robot.pdf

Historical source: local-extra-007


## Page 1
FRC | Science Fair | Vacuum Robot
段佑霖

## Page 2
Brief Overview of Events
FRC Magnolia Regional 
(Mississippi)
3/18 - 3/21
Created the ﬁrst version of 
my Pit Collect website and 
put it to use.
FRC Championship
(Houston)
4/29 - 5/1
Started using API keys to 
grab standard information 
about teams, as well as 
more information and input 
sections
Mini Autopilot Panel
6/6
Vacuum Robot & 
Science Fair
7/1 - Present
Built a mini autopilot to 
control the autopilot in my 
ﬂight simulator.
Built a mini autopilot to 
control the autopilot in my 
ﬂight simulator.

## Page 3
FRC


## Page 4
2026 Robot


## Page 5
● Created a type of scouting website called Pit 
Collect, which our team used to analyze the 
hardware and basic strategy of other teams
○ Can be used to ﬁgure out how to play against 
them
○ Determine how to cooperate with them when 
they are on the same side as us
○ Helped to build an advanced knowledge and 
understanding of HTML, JS, and CSS through 
the help of vibe coding and my own code.
● Helped solder part of the wiring for the robot
○ Massively developed my soldering skills
○ Paved the way for future projects
● Worked on object detection models for the 
2026 robot
○ Helped to map out game pieces and compile 
into an object detection model for our robot
○ Taught me the basics of object detection and 
object detection software, such as Roboﬂow
Contributions


## Page 6
FRC Magnolia Regional
3/18 - 3/21


## Page 7
Results
● 12th out of 46 teams
● Match record of 6-3-0.
● Got into the semiﬁnals of the playoff matches
● Won the Impact Award
○ took us to the FRC Championship in Houston
● My Pit Collect Website was used to track the 
data of over 40 teams.
Final Score: 
188:288


## Page 8
Struggles/Problems
● To transfer data from the device the 
scouting was done on to the device 
used to compile all the results, we 
decided to use a qr code to transfer all 
the values
● In the early stages of development, the 
QR code was too large, resulting in the 
scanner not being able to pick up the 
QR code
Solution:
● When I was soldering wires, I 
sometimes used to accidentally burn 
the plastic/insulation of the wire and 
wire connectors, rendering the wires 
useless.
● The solder would not melt properly, and 
so I would keep the soldering iron on 
the component for a long time.
QR Code too large Burned Wires
Solution:

## Page 9
QR Code Fix
To solve the issue of my QR code being too large, I 
utilized 4 main methods:
1. Setting Visual Dimension Limits
a. Set the QR code size to 256 by 256 px
i. Ensures the image size will not change
2. LZ-string Compression
a. Before any of the qr codes are generated, all 
the TSV(tab separated values) are compressed 
into Base64 format
i. E.g. A -> 000000, B -> 000001…
3. Character Sanitization
a. Newlines and tabs are deleted from text inputs 
to save space
Doesn’t this make the 
ﬁle size larger?
It does, but LZ string 
compression looks 
for recurring patterns 
and creates a 
dictionary for where 
the values should go
Back:

## Page 10
Soldering Skills Improvement
Since I kept the soldering iron on the component for 
too long, it caused the plastic surrounding the metal 
contacts to melt. This results in the component 
becoming unusable, which wastes time and 
resources.
1. Plug a spare connector in
a. By plugging in a spare connector, it acts as a 
heat sink. The extra metal contacts mean that 
more heat is required to raise the temperature 
of the component, allowing me to keep the 
soldering iron on for longer.
2. Pre-tin both the connector and the wire
a. I used to only pre-tin the wire, which meant that 
there will be poor heat transfer
b. By tinning the connector too, the metal heats 
up way quicker
Heat shrink wrap
XT-60 Connectors
Back:

## Page 11
FRC Houston 
Championships
4/29 - 5/1


## Page 12
Results
● 9 divisions in total
● 49th out of 75 teams in the Daly Division
● My Pit collect website was used to scout over 
70 international teams
● Win loss record of 4-6-0
● Added major features to my Pit Collect 
website
○ API key grabbing from the Blue Alliance to 
display basic information about a team.
○ Allowed for teams to draw out multiple 
autonomous strategies


## Page 13
Struggles/Problems
1. Robot wiring failures during match
a. During a lot of the matches, our robot could 
not move due to electrical wiring mistakes and 
zeroing issues due to human error
b. Time constraints
2. Autonomous path drawing is laggy
a. To lower the QR code size, I decided to lower 
the amount of points(x,y) that will be plotted 
when you drew on the ﬁeld. 
b. This made the line drawing inaccurate and 
laggy, which meant we were compromising our 
data for ﬁle size
c. = lossy compression
1. Although I was not in the ﬁxing team, this 
experience has taught me that even under 
pressure, you cannot skip steps in the 
standard procedure, and must follow the 
checklist as intended.
2. To ﬁx the 


## Page 14
Johnson Space Center


## Page 15
Saturn V Rocket
When I visited the Johnson Space Center in Houston, the 
thing that stood out to me the most was the Saturn V 
Rocket. When I ﬁrst approached it, I was in awe of its 
massive size and complex engineering. 


## Page 16
Flight Simulator Autopilot


## Page 17
Autonomous Vacuum Cleaner

## Page 18
Science Fair