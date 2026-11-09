# Argus Vac.fz

Historical source: local-extra-190


<?xml version="1.0" encoding="UTF-8"?>

<module fritzingVersion="1.0.5.2025-04-02.CD-2185-0-b9add9ea" icon=".png">

    <project_properties>

        <simulator_animation_time_s value="5s"/>

        <simulator_number_of_steps value="400"/>

        <simulator_time_step_mode value="false"/>

        <simulator_time_step_s value="1us"/>

    </project_properties>

    <boards>

        <board moduleId="TwoLayerRectanglePCBModuleID" title="Rectangular PCB - Resizable" instance="PCB1" width="8.46667cm" height="5.64444cm"/>

    </boards>

    <programs pid="243fe0a1d23ed6b13439b6e5883ee30e">

        <program language="Arduino">[REDACTED_HOME_PATH]</program>

    </programs>

    <views>

        <view name="breadboardView" backgroundColor="#ffffff" gridSize="0.1in" showGrid="1" alignToGrid="1" viewFromBelow="0" colorWiresByLength="0"/>

        <view name="schematicView" backgroundColor="#ffffff" gridSize="0.1in" showGrid="1" alignToGrid="1" viewFromBelow="0"/>

        <view name="pcbView" backgroundColor="#333333" gridSize="0.1in" showGrid="1" alignToGrid="1" viewFromBelow="0" autorouteTraceWidth="" autorouteViaHoleSize="" DRC_Keepout="" autorouteViaRingThickness="" GPG_Keepout=""/>

    </views>

    <instances>

        <instance moduleIdRef="TwoLayerRectanglePCBModuleID" modelIndex="5797" path=":/resources/parts/core/rectangle_pcb_two_layers.fzp">

            <property name="layers" value="2"/>

            <property name="width" value="84.66666666666667"/>

            <property name="height" value="56.44444444444444"/>

            <title>PCB1</title>

            <views>

                <pcbView layer="board">

                    <geometry z="1.50245" x="142" y="0"/>

                </pcbView>

            </views>

        </instance>

        <instance moduleIdRef="Arduino_MEGA_2560-Rev3(fix)" modelIndex="5904" path="C:/Program Files/Fritzing/fritzing-parts/core/Arduino_MEGA_2560-Rev3(fix).fzp">

            <title>Arduino mega</title>

            <views>

                <breadboardView layer="breadboardbreadboard">

                    <geometry z="1.50167" x="650.267" y="-735.732">

                        <transform m11="0" m12="1" m13="0" m21="-1" m22="0" m23="0" m31="285.733" m32="-96.7329" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="859.439" y="-850.579" z="5.0026" xOffset="209.172" yOffset="-114.847" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector239" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514714" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector377" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411229" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector265" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411686" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector371" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514768" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector266" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411673" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector343" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411201" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector344" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411268" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector375" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514733" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector261" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411499" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector369" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514771" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector267" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411696" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector243" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515587" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector373" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514749" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector260" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411622" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector264" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411660" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector378" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411251" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector242" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515590" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector238" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514695" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector259" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515044" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector258" layer="breadboardbreadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515041" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.50244" x="720.005" y="108"/>

                    <titleGeometry visible="true" x="1080.3" y="101" z="12.5" xOffset="360.295" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector239" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514714" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector377" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411229" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector265" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411686" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector371" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514768" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector266" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411673" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector343" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411201" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector344" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411268" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector375" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514733" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector261" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411499" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector369" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514771" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector267" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411696" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector243" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515587" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector373" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514749" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector260" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411622" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector264" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411660" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector378" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411251" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector242" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515590" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector238" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514695" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector259" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515044" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector258" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515041" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50244" x="117" y="-243"/>

                    <titleGeometry visible="true" x="243" y="-250" z="6.5" xOffset="126" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector239" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514714" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector377" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411229" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector265" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411686" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector371" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514768" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector266" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411673" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector343" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411201" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector344" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411268" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector375" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514733" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector261" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411499" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector369" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514771" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector267" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411696" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector243" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515587" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector373" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514749" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector260" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411622" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector264" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411660" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector378" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411251" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector242" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515590" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector238" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514695" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector259" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515044" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector258" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515041" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="raspberry-pi-4B_1" modelIndex="6246" path="C:/Program Files/Fritzing/fritzing-parts/core/raspberry-pi-4B_1.fzp">

            <title>OrangePi 5(Raspberry Pi image as substitute)</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50173" x="267.356" y="-574.902"/>

                    <titleGeometry visible="true" x="356.254" y="-336.427" z="5.00272" xOffset="88.898" yOffset="238.475" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.50248" x="599.998" y="99.61"/>

                    <titleGeometry visible="true" x="902.08" y="92.61" z="12.5" xOffset="302.082" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50246" x="-9.44052" y="-252.461"/>

                    <titleGeometry visible="true" x="90.4564" y="-259.461" z="6.50002" xOffset="99.8969" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="7d0bc366bcac9395c747f3a92e2ff843leg" modelIndex="6269" path="C:/Program Files/Fritzing/fritzing-parts/core/stepper_motor_bipolar.fzp">

            <title>Left Wheel Motor</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50187" x="722.776" y="-225.327">

                        <transform m11="0" m12="-1" m13="0" m21="1" m22="0" m23="0" m31="-47.9358" m32="197.818" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="825.718" y="-203.903" z="5.00253" xOffset="102.942" yOffset="21.4241" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="71.2793" y="242.183"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="0.977395" y="41.6619"/>

                                <bezier/>

                                <point x="165.258" y="36.4224"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411615" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="breadboard">

                            <geometry x="88.8551" y="242.183"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="7.34533" y="74.9952"/>

                                <bezier/>

                                <point x="148.826" y="65.0609"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411608" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="80.0672" y="242.183"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="6.8161" y="64.592"/>

                                <bezier/>

                                <point x="155.835" y="56.1701"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411601" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="62.4915" y="242.183"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="1.28508" y="51.071"/>

                                <bezier/>

                                <point x="173.418" y="46.8521"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411594" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.5025" x="1226.7" y="389.7"/>

                    <titleGeometry visible="true" x="1239.3" y="382.7" z="12.5" xOffset="12.6" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411615" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411608" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411601" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411594" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50249" x="467.316" y="-198.579"/>

                    <titleGeometry visible="true" x="531.25" y="-205.579" z="6.50004" xOffset="63.9338" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411615" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411608" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411601" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411594" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="lipoly5000_11.1v_sch_2f81baf3d895ea87e8cd344d8a6e4660_4" modelIndex="6316" path="[REDACTED_HOME_PATH]">

            <title>5000 Mah 11.1V 30C 3s Lipo</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50175" x="2250.34" y="-717.966">

                        <transform m11="-4.44089e-16" m12="-1" m13="0" m21="1" m22="-4.44089e-16" m23="0" m31="-111.883" m32="289.048" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="2257.24" y="-641.433" z="5.00259" xOffset="6.89614" yOffset="76.533" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513668" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513819" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.50252" x="223.2" y="16.2">

                        <transform m11="0" m12="1" m13="0" m21="-1" m22="0" m23="0" m31="17.1" m32="4.5" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="235.8" y="9.2" z="12.5001" xOffset="12.6" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513668" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513819" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50251" x="899.518" y="-149.241"/>

                    <titleGeometry visible="true" x="936.469" y="-156.241" z="6.50007" xOffset="36.9518" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513668" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513819" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="6626" path=":/resources/parts/core/wire.fzp">

            <title>Wire1</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50166" x="1176.12" y="-737.71" x1="0" y1="0" x2="335.792" y2="125.435" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85412190" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411470" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50246" x="798.805" y="-464.305" x1="0" y1="0" x2="406.392" y2="94.8581" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85412190" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411470" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50245" x="798.805" y="-464.305" x1="0" y1="0" x2="406.392" y2="94.8581" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85412190" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411470" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="6629" path=":/resources/parts/core/wire.fzp">

            <title>Wire2</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50172" x="1176.18" y="-667.375" x1="0" y1="0" x2="327.155" y2="163.096" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="6647" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411470" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50247" x="731.905" y="-338.494" x1="0" y1="0" x2="472.293" y2="-19.9701" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="6647" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411470" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50247" x="731.905" y="-338.494" x1="0" y1="0" x2="472.293" y2="-19.9701" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="6647" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411470" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="6647" path=":/resources/parts/core/wire.fzp">

            <title>Wire4</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50171" x="1503.34" y="-504.279" x1="0" y1="0" x2="98.9559" y2="45.1239" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513367" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6629" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50251" x="1053" y="-351" x1="0" y1="0" x2="153" y2="-8.99875" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513367" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6629" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5025" x="1053" y="-351" x1="0" y1="0" x2="153" y2="-8.99875" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513367" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6629" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="MediumElectrolyticCapacitorModuleID" modelIndex="6781" path="C:/Program Files/Fritzing/fritzing-parts/core/capacitor_electrolytic_medium.fzp">

            <property name="capacitance5mm" value="0.1nF"/>

            <property name="capacitance7.5mm" value="10nF"/>

            <property name="capacitance10mm" value="2.2µF"/>

            <property name="capacitance15mm" value="4.7µF"/>

            <property name="capacitance22.5mm" value="10µF"/>

            <property name="capacitance27.5mm" value="22µF"/>

            <property name="capacitance37.5mm" value="100nF"/>

            <property name="capacitance" value="100µF"/>

            <property name="voltageHigh" value="35V"/>

            <property name="voltage" value="35V"/>

            <title>C2</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50181" x="980.359" y="-232.61">

                        <transform m11="1" m12="0" m13="0" m21="0" m22="-1" m23="0" m31="0" m32="53.9109" m33="1"/>

                    </geometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="18.7164" y="53.9109"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="-0.401799" y="28.9138"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85412033" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="9.7164" y="53.9109"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="-0.727797" y="27.9358"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85412010" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.50253" x="300.79" y="71.21">

                        <transform m11="0" m12="1" m13="0" m21="-1" m22="0" m23="0" m31="36.9" m32="0" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="337.69" y="64.21" z="12.5001" xOffset="36.9" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85412033" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85412010" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50252" x="1124.55" y="71.5623"/>

                    <titleGeometry visible="true" x="1143.45" y="57.5623" z="6.50008" xOffset="18.9" yOffset="-14" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                        <displayKey key="capacitance"/>

                        <displayKey key="voltage"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85412033" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85412010" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="pololu0002_a988" modelIndex="85410559" path="C:/Program Files/Fritzing/fritzing-parts/core/pololu0002_a988.fzp">

            <title>Left Motor Driver</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50179" x="940.312" y="-327.973">

                        <transform m11="0" m12="1" m13="0" m21="-1" m22="0" m23="0" m31="63" m32="9" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="994.312" y="-341.973" z="5.00041" xOffset="54" yOffset="-14" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector12" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411601" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector10" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411615" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector6" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411663" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector7" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411689" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector14" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411313" layer="breadboardWire"/>

                                <connect connectorId="connector1" modelIndex="85412010" layer="breadboardWire"/>

                                <connect connectorId="connector0" modelIndex="85411302" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector9" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411185" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector8" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411234" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector15" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85412033" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411646" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector13" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411608" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector5" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411646" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector11" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411594" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.50172" x="427.5" y="31.5"/>

                    <titleGeometry visible="true" x="481.5" y="24.5" z="13.0004" xOffset="54" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector12" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411601" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector10" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411615" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector6" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411663" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector7" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411689" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector14" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411313" layer="copper1trace"/>

                                <connect connectorId="connector1" modelIndex="85412010" layer="copper1trace"/>

                                <connect connectorId="connector0" modelIndex="85411302" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector9" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411185" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector8" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411234" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector15" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85412033" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411646" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector13" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411608" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector5" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411646" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector11" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411594" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50173" x="422.48" y="27.9476"/>

                    <titleGeometry visible="true" x="532.038" y="20.9476" z="7.00039" xOffset="109.558" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector12" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411601" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector10" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411615" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector6" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411663" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector7" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411689" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector14" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411313" layer="schematicTrace"/>

                                <connect connectorId="connector1" modelIndex="85412010" layer="schematicTrace"/>

                                <connect connectorId="connector0" modelIndex="85411302" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector9" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411185" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector8" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411234" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector15" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85412033" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411646" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector13" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411608" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector5" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411646" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector11" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411594" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="pololu0002_a988" modelIndex="85410567" path="C:/Program Files/Fritzing/fritzing-parts/core/pololu0002_a988.fzp">

            <title>Right Motor Driver</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50177" x="1318.31" y="-327.973">

                        <transform m11="0" m12="1" m13="0" m21="-1" m22="0" m23="0" m31="63" m32="9" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="1400.41" y="-343.089" z="5.0004" xOffset="82.1006" yOffset="-15.1158" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector12" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411581" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector10" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411567" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector6" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411676" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector7" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411699" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector14" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411333" layer="breadboardWire"/>

                                <connect connectorId="connector1" modelIndex="85411979" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector9" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411271" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector8" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411254" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector15" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411956" layer="breadboardWire"/>

                                <connect connectorId="connector0" modelIndex="85411330" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411653" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector13" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411574" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector5" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411653" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector11" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411554" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.50173" x="634.5" y="31.5"/>

                    <titleGeometry visible="true" x="688.5" y="24.5" z="13.0004" xOffset="54" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector12" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411581" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector10" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411567" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector6" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411676" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector7" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411699" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector14" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411333" layer="copper1trace"/>

                                <connect connectorId="connector1" modelIndex="85411979" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector9" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411271" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector8" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411254" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector15" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411956" layer="copper1trace"/>

                                <connect connectorId="connector0" modelIndex="85411330" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411653" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector13" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411574" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector5" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411653" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector11" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411554" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50172" x="633.629" y="27.6482"/>

                    <titleGeometry visible="true" x="739.038" y="20.9476" z="7.0004" xOffset="109.558" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector12" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411581" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector10" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411567" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector6" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411676" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector7" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411699" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector14" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411333" layer="schematicTrace"/>

                                <connect connectorId="connector1" modelIndex="85411979" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector9" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411271" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector8" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411254" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector15" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411956" layer="schematicTrace"/>

                                <connect connectorId="connector0" modelIndex="85411330" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411653" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector13" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411574" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector5" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411653" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector11" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411554" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411185" path=":/resources/parts/core/wire.fzp">

            <title>Wire402</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50176" x="944.678" y="-268.723" x1="0" y1="0" x2="0.310823" y2="34.7557" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411194" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector9" modelIndex="85410559" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50177" x="1146.48" y="-399.776" x1="0" y1="0" x2="-309.657" y2="-43.3655" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411194" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector9" modelIndex="85410559" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50176" x="1146.48" y="-399.776" x1="0" y1="0" x2="-309.657" y2="-43.3655" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411194" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector9" modelIndex="85410559" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411188" path=":/resources/parts/core/wire.fzp">

            <title>Wire403</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50174" x="1025.79" y="-440.779" x1="0" y1="0" x2="0" y2="-18.0881" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411208" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411215" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50176" x="836.818" y="-378.093" x1="0" y1="0" x2="0.181538" y2="-62.9071" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411208" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411215" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50177" x="836.818" y="-378.093" x1="0" y1="0" x2="0.181538" y2="-62.9071" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411208" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411215" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411191" path=":/resources/parts/core/wire.fzp">

            <title>Wire404</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50178" x="926.777" y="-324.158" x1="0" y1="0" x2="27.1322" y2="0" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411215" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411222" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50187" x="846.07" y="-233.967" x1="0" y1="0" x2="-9.25157" y2="-144.126" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411215" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411222" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50178" x="846.07" y="-233.967" x1="0" y1="0" x2="-9.25157" y2="-144.126" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411215" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411222" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411194" path=":/resources/parts/core/wire.fzp">

            <title>Wire405</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5018" x="944.989" y="-233.967" x1="0" y1="0" x2="-26.7792" y2="-35.9265" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411222" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411185" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50186" x="944.989" y="-233.967" x1="0" y1="0" x2="-98.9186" y2="0" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411222" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411185" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50179" x="944.989" y="-233.967" x1="0" y1="0" x2="-98.9186" y2="0" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411222" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411185" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411201" path=":/resources/parts/core/wire.fzp">

            <title>Wire408</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50183" x="1025.79" y="-476.955" x1="0" y1="0" x2="-98.79" y2="-0.04383" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector343" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411208" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50185" x="981.042" y="-467.911" x1="0" y1="0" x2="-19.9921" y2="-16.1841" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector343" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411208" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5018" x="981.042" y="-467.911" x1="0" y1="0" x2="-19.9921" y2="-16.1841" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector343" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411208" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411208" path=":/resources/parts/core/wire.fzp">

            <title>Wire411</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50186" x="1025.79" y="-458.867" x1="0" y1="0" x2="0" y2="-18.0881" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411201" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411188" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50184" x="999.13" y="-440.779" x1="0" y1="0" x2="-18.0881" y2="-27.1322" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411201" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411188" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50181" x="999.13" y="-440.779" x1="0" y1="0" x2="-18.0881" y2="-27.1322" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411201" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411188" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411215" path=":/resources/parts/core/wire.fzp">

            <title>Wire414</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50188" x="953.91" y="-324.158" x1="0" y1="0" x2="71.8764" y2="-116.621" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411188" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411191" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50183" x="944.866" y="-333.202" x1="0" y1="0" x2="80.9205" y2="-107.577" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411188" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411191" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50182" x="944.866" y="-333.202" x1="0" y1="0" x2="80.9205" y2="-107.577" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411188" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411191" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411222" path=":/resources/parts/core/wire.fzp">

            <title>Wire417</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50185" x="918.209" y="-269.894" x1="0" y1="0" x2="8.56805" y2="-54.2643" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411191" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411194" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50182" x="918.209" y="-269.894" x1="0" y1="0" x2="8.56805" y2="-54.2643" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411191" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411194" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50183" x="918.209" y="-269.894" x1="0" y1="0" x2="8.56805" y2="-54.2643" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411191" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411194" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411229" path=":/resources/parts/core/wire.fzp">

            <title>Wire420</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50192" x="774" y="-476.999" x1="0" y1="0" x2="-36.065" y2="-0.01307" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411244" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector377" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50181" x="878.829" y="-210.729" x1="0" y1="0" x2="56.9172" y2="-59.6275" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411244" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector377" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50184" x="878.829" y="-210.729" x1="0" y1="0" x2="56.9172" y2="-59.6275" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411244" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector377" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411234" path=":/resources/parts/core/wire.fzp">

            <title>Wire421</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50189" x="926.937" y="-233.767" x1="0" y1="0" x2="8.68652" y2="-34.9558" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector8" modelIndex="85410559" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411237" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5018" x="926.937" y="-233.767" x1="0" y1="0" x2="8.68652" y2="-34.9558" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector8" modelIndex="85410559" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411237" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50185" x="926.937" y="-233.767" x1="0" y1="0" x2="8.68652" y2="-34.9558" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector8" modelIndex="85410559" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411237" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411237" path=":/resources/parts/core/wire.fzp">

            <title>Wire422</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5019" x="729.082" y="-233.767" x1="0" y1="0" x2="197.855" y2="0" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411234" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411244" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50179" x="710.787" y="-233.767" x1="0" y1="0" x2="216.15" y2="0" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411234" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411244" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50186" x="710.787" y="-233.767" x1="0" y1="0" x2="216.15" y2="0" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411234" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411244" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411244" path=":/resources/parts/core/wire.fzp">

            <title>Wire425</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50191" x="737.935" y="-477.012" x1="0" y1="0" x2="-8.85267" y2="243.245" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411237" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411229" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50178" x="737.891" y="-468.212" x1="0" y1="0" x2="-8.80862" y2="234.445" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411237" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411229" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50187" x="737.891" y="-468.212" x1="0" y1="0" x2="-8.80862" y2="234.445" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411237" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411229" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411251" path=":/resources/parts/core/wire.fzp">

            <title>Wire428</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50195" x="774" y="-467.999" x1="0" y1="0" x2="0.121" y2="215.946" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411257" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector378" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50196" x="1299.09" y="-245.1" x1="0" y1="0" x2="15.0652" y2="-23.7567" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411257" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector378" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50188" x="1299.09" y="-245.1" x1="0" y1="0" x2="15.0652" y2="-23.7567" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411257" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector378" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411254" path=":/resources/parts/core/wire.fzp">

            <title>Wire429</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50194" x="1314.15" y="-252.053" x1="0" y1="0" x2="-0.528022" y2="-16.6699" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector8" modelIndex="85410567" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411257" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50195" x="1314.15" y="-252.053" x1="0" y1="0" x2="-0.528022" y2="-16.6699" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector8" modelIndex="85410567" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411257" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50189" x="1314.15" y="-252.053" x1="0" y1="0" x2="-0.528022" y2="-16.6699" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector8" modelIndex="85410567" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411257" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411257" path=":/resources/parts/core/wire.fzp">

            <title>Wire430</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50193" x="774.121" y="-252.053" x1="0" y1="0" x2="540.031" y2="0" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411254" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411251" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50194" x="764.85" y="-252.053" x1="0" y1="0" x2="549.302" y2="0" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411254" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411251" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5019" x="764.85" y="-252.053" x1="0" y1="0" x2="549.302" y2="0" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411254" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411251" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411268" path=":/resources/parts/core/wire.fzp">

            <title>Wire435</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50196" x="927" y="-467.999" x1="0" y1="0" x2="135.1" y2="-0.182059" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411277" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector344" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50193" x="1278.81" y="-220.764" x1="0" y1="0" x2="44.6163" y2="-49.2517" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411277" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector344" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50191" x="1278.81" y="-220.764" x1="0" y1="0" x2="44.6163" y2="-49.2517" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411277" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector344" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411271" path=":/resources/parts/core/wire.fzp">

            <title>Wire436</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50197" x="1322.84" y="-242.782" x1="0" y1="0" x2="-0.165558" y2="-25.9408" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector9" modelIndex="85410567" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411274" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50192" x="1322.84" y="-242.782" x1="0" y1="0" x2="-0.165558" y2="-25.9408" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector9" modelIndex="85410567" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411274" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50192" x="1322.84" y="-242.782" x1="0" y1="0" x2="-0.165558" y2="-25.9408" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector9" modelIndex="85410567" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411274" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411274" path=":/resources/parts/core/wire.fzp">

            <title>Wire437</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50198" x="1062.23" y="-243.134" x1="0" y1="0" x2="260.616" y2="0.352408" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411271" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411288" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50191" x="1062.1" y="-234.091" x1="0" y1="0" x2="260.744" y2="-8.69148" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411271" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411288" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50193" x="1062.1" y="-234.091" x1="0" y1="0" x2="260.744" y2="-8.69148" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411271" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411288" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411277" path=":/resources/parts/core/wire.fzp">

            <title>Wire438</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50199" x="1062.1" y="-468.181" x1="0" y1="0" x2="0" y2="45.1957" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411288" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411268" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5019" x="1062.1" y="-458.91" x1="0" y1="0" x2="0" y2="224.82" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411288" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411268" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50194" x="1062.1" y="-458.91" x1="0" y1="0" x2="0" y2="224.82" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411288" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411268" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411288" path=":/resources/parts/core/wire.fzp">

            <title>Wire443</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.502" x="1062.1" y="-422.985" x1="0" y1="0" x2="0.128391" y2="179.851" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411274" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411277" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50189" x="1062.1" y="-422.985" x1="0" y1="0" x2="0" y2="188.895" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411274" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411277" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50195" x="1062.1" y="-422.985" x1="0" y1="0" x2="0" y2="188.895" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411274" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411277" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411302" path=":/resources/parts/core/wire.fzp">

            <title>Wire448</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50203" x="989.946" y="-268.722" x1="0" y1="0" x2="18.1096" y2="-0.956919" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411323" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85410559" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50188" x="1000.87" y="-266.503" x1="0" y1="0" x2="627.763" y2="-309.44" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411323" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85410559" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50196" x="1000.87" y="-266.503" x1="0" y1="0" x2="627.763" y2="-309.44" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411323" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85410559" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411313" path=":/resources/parts/core/wire.fzp">

            <title>Wire453</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50204" x="989.946" y="-268.723" x1="0" y1="0" x2="0.0382266" y2="-19.2686" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411417" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85410559" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50205" x="1185.78" y="-425.524" x1="0" y1="0" x2="440.431" y2="-160.588" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411417" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85410559" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50197" x="1185.78" y="-425.524" x1="0" y1="0" x2="440.431" y2="-160.588" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411417" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85410559" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411316" path=":/resources/parts/core/wire.fzp">

            <title>Wire454</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50206" x="1025.95" y="-287.991" x1="0" y1="0" x2="179.724" y2="-89.6247" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513415" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411417" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50204" x="1025.86" y="-323.886" x1="0" y1="0" x2="603.135" y2="-261.114" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513415" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411417" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50198" x="1025.86" y="-323.886" x1="0" y1="0" x2="603.135" y2="-261.114" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513415" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411417" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411323" path=":/resources/parts/core/wire.fzp">

            <title>Wire457</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50202" x="1008.06" y="-269.679" x1="0" y1="0" x2="234.038" y2="-90.5201" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513392" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411302" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50203" x="1017.06" y="-269.679" x1="0" y1="0" x2="611.944" y2="-306.32" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513392" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411302" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50199" x="1017.06" y="-269.679" x1="0" y1="0" x2="611.944" y2="-306.32" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513392" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411302" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411330" path=":/resources/parts/core/wire.fzp">

            <title>Wire460</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50211" x="1377" y="-268.723" x1="0" y1="0" x2="18.0082" y2="16.643" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411945" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector15" modelIndex="85410567" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50202" x="1621.76" y="-309.179" x1="0" y1="0" x2="9.7893" y2="-267.574" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411945" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector15" modelIndex="85410567" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.502" x="1621.76" y="-309.179" x1="0" y1="0" x2="9.7893" y2="-267.574" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411945" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector15" modelIndex="85410567" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411333" path=":/resources/parts/core/wire.fzp">

            <title>Wire461</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50214" x="1367.95" y="-268.723" x1="0" y1="0" x2="9.08727" y2="-19.3154" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411726" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85410567" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50201" x="1620.13" y="-585.727" x1="0" y1="0" x2="9.7893" y2="-1.13687e-13" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411726" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85410567" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50201" x="1620.13" y="-585.727" x1="0" y1="0" x2="9.7893" y2="-1.13687e-13" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411726" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85410567" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411336" path=":/resources/parts/core/wire.fzp">

            <title>Wire462</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50215" x="1566.23" y="-557.762" x1="0" y1="0" x2="215.804" y2="-31.3208" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513267" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411353" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.502" x="1611.16" y="-593.884" x1="0" y1="0" x2="17.844" y2="8.88436" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411353" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50202" x="1611.16" y="-593.884" x1="0" y1="0" x2="17.844" y2="8.88436" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513267" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411353" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411342" path=":/resources/parts/core/wire.fzp">

            <title>Wire464</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50208" x="1449.1" y="-431.769" x1="0" y1="0" x2="152.667" y2="-117.008" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513501" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513415" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50199" x="1593.03" y="-584.946" x1="0" y1="0" x2="18.1259" y2="0.0353179" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513501" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513415" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50203" x="1593.03" y="-584.946" x1="0" y1="0" x2="18.1259" y2="0.0353179" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513501" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513415" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411353" path=":/resources/parts/core/wire.fzp">

            <title>Wire469</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50216" x="1476.07" y="-242.893" x1="0" y1="0" x2="90.1563" y2="-314.869" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411336" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411368" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50198" x="1476.08" y="-242.893" x1="0" y1="0" x2="152.81" y2="-342.053" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411336" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411368" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50204" x="1476.08" y="-242.893" x1="0" y1="0" x2="152.81" y2="-342.053" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411336" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411368" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411368" path=":/resources/parts/core/wire.fzp">

            <title>Wire476</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50217" x="1421.96" y="-270.05" x1="0" y1="0" x2="54.1124" y2="27.1564" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411353" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411726" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50197" x="1368.03" y="-242.893" x1="0" y1="0" x2="108.047" y2="0" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411353" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411726" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50205" x="1368.03" y="-242.893" x1="0" y1="0" x2="108.047" y2="0" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411353" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411726" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411379" path=":/resources/parts/core/wire.fzp">

            <title>Wire481</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50213" x="1574.9" y="-252.052" x1="0" y1="0" x2="144.07" y2="-98.7672" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513460" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411386" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50213" x="1574.9" y="-252.053" x1="0" y1="0" x2="54.1037" y2="-323.946" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513460" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411386" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50206" x="1574.9" y="-252.053" x1="0" y1="0" x2="54.1037" y2="-323.946" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513460" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411386" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411386" path=":/resources/parts/core/wire.fzp">

            <title>Wire484</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5021" x="1431.2" y="-216.128" x1="0" y1="0" x2="143.701" y2="-35.9242" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411379" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411945" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50212" x="1467.12" y="-216.128" x1="0" y1="0" x2="107.774" y2="-35.9248" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411379" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411945" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50207" x="1467.12" y="-216.128" x1="0" y1="0" x2="107.774" y2="-35.9248" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411379" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411945" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411417" path=":/resources/parts/core/wire.fzp">

            <title>Wire499</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50209" x="989.984" y="-287.992" x1="0" y1="0" x2="35.9708" y2="0.0006" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411316" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411313" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50211" x="989.984" y="-287.991" x1="0" y1="0" x2="35.971" y2="0" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411316" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411313" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50208" x="989.984" y="-287.991" x1="0" y1="0" x2="35.971" y2="0" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411316" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411313" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="RioRand_LM2596_94ce9810d0922bc731e2f315085d46ab_1" modelIndex="85411470" path="C:/Program Files/Fritzing/fritzing-parts/core/RioRand_LM2596_94ce9810d0922bc731e2f315085d46ab_1.fzp">

            <title>12V -&gt; 5V DC-DC Buck Converter</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50182" x="1011.53" y="-743.43">

                        <transform m11="-1" m12="0" m13="0" m21="0" m22="-1" m23="0" m31="170.118" m32="81.4851" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="1203.67" y="-743.974" z="5.00261" xOffset="192.136" yOffset="-0.544343" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="6626" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514347" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514328" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="6629" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.50174" x="1164.62" y="452.933"/>

                    <titleGeometry visible="true" x="1335.59" y="445.933" z="13.0004" xOffset="170.979" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="6626" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514347" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514328" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="6629" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50174" x="944.55" y="224.55"/>

                    <titleGeometry visible="true" x="999.45" y="217.55" z="7.00043" xOffset="54.9" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="6626" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514347" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514328" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="6629" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411499" path=":/resources/parts/core/wire.fzp">

            <title>Wire520</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50219" x="756" y="-647.999" x1="0" y1="0" x2="-36.1412" y2="-0.130345" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411511" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector261" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5021" x="963.686" y="-816.325" x1="0" y1="0" x2="53.4633" y2="149.607" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411511" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector261" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50209" x="963.686" y="-816.325" x1="0" y1="0" x2="53.4633" y2="149.607" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411511" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector261" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411502" path=":/resources/parts/core/wire.fzp">

            <title>Wire521</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50218" x="972.223" y="-810.036" x1="0" y1="0" x2="107.777" y2="54.036" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85514323" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411505" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50209" x="972.223" y="-810.036" x1="0" y1="0" x2="44.7485" y2="142.644" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411505" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5021" x="972.223" y="-810.036" x1="0" y1="0" x2="44.7485" y2="142.644" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85514323" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411505" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411505" path=":/resources/parts/core/wire.fzp">

            <title>Wire522</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5022" x="729.166" y="-792.065" x1="0" y1="0" x2="243.057" y2="-17.971" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411502" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411508" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50208" x="729.167" y="-792.065" x1="0" y1="0" x2="243.056" y2="-17.9708" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411502" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411508" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50211" x="729.167" y="-792.065" x1="0" y1="0" x2="243.056" y2="-17.9708" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411502" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411508" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411508" path=":/resources/parts/core/wire.fzp">

            <title>Wire523</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50221" x="719.82" y="-656.85" x1="0" y1="0" x2="9.34598" y2="-135.215" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411505" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411511" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50207" x="720.181" y="-656.834" x1="0" y1="0" x2="8.98542" y2="-135.231" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411505" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411511" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50212" x="720.181" y="-656.834" x1="0" y1="0" x2="8.98542" y2="-135.231" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411505" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411511" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411511" path=":/resources/parts/core/wire.fzp">

            <title>Wire524</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50222" x="719.859" y="-648.129" x1="0" y1="0" x2="-0.0383324" y2="-8.72065" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411508" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411499" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50206" x="692.776" y="-656.834" x1="0" y1="0" x2="27.4055" y2="0" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411508" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411499" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50213" x="692.776" y="-656.834" x1="0" y1="0" x2="27.4055" y2="0" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411508" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411499" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="7d0bc366bcac9395c747f3a92e2ff843leg" modelIndex="85411550" path="C:/Program Files/Fritzing/fritzing-parts/core/stepper_motor_bipolar.fzp">

            <title>Right Wheel Motor</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50184" x="1510.74" y="-227.319">

                        <transform m11="0" m12="1" m13="0" m21="-1" m22="0" m23="0" m31="197.818" m32="47.9365" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="1556" y="-205.677" z="5.00254" xOffset="45.2647" yOffset="21.6422" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="71.2793" y="242.183"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="-27.5731" y="132.087"/>

                                <bezier/>

                                <point x="-138.429" y="135.892"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411567" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="breadboard">

                            <geometry x="88.8551" y="242.183"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="2.06697" y="107.907"/>

                                <bezier/>

                                <point x="-165.212" y="108.367"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411574" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="80.0672" y="242.183"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="-4.57444" y="118.942"/>

                                <bezier/>

                                <point x="-153.163" y="116.913"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411581" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="62.4915" y="242.183"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="-24.996" y="122.16"/>

                                <bezier/>

                                <point x="-126.108" y="125.373"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411554" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.50249" x="1267.71" y="353.28"/>

                    <titleGeometry visible="true" x="1280.31" y="346.28" z="12.5" xOffset="12.6" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411567" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411574" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411581" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411554" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50248" x="764.316" y="-153.579"/>

                    <titleGeometry visible="true" x="828.25" y="-160.579" z="6.50004" xOffset="63.9338" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411567" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411574" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411581" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411554" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411554" path=":/resources/parts/core/wire.fzp">

            <title>Wire541</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50223" x="1341" y="-242.999" x1="0" y1="0" x2="-0.218625" y2="-25.7233" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector11" modelIndex="85410567" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411550" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50221" x="1339.09" y="-250.882" x1="0" y1="0" x2="1.67131" y2="-17.4559" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector11" modelIndex="85410567" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411550" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50214" x="1339.09" y="-250.882" x1="0" y1="0" x2="1.67131" y2="-17.4559" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector11" modelIndex="85410567" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411550" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411567" path=":/resources/parts/core/wire.fzp">

            <title>Wire546</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50224" x="1330.48" y="-246.532" x1="0" y1="0" x2="1.24676" y2="-22.1902" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector10" modelIndex="85410567" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411550" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5022" x="1332.34" y="-253.563" x1="0" y1="0" x2="0.469851" y2="-13.3125" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector10" modelIndex="85410567" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411550" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50215" x="1332.34" y="-253.563" x1="0" y1="0" x2="0.469851" y2="-13.3125" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector10" modelIndex="85410567" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411550" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411574" path=":/resources/parts/core/wire.fzp">

            <title>Wire549</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50225" x="1358.01" y="-255.739" x1="0" y1="0" x2="0.882596" y2="-12.9829" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector13" modelIndex="85410567" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85411550" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50219" x="1359.28" y="-262.96" x1="0" y1="0" x2="0.783085" y2="-6.89115" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector13" modelIndex="85410567" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85411550" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50216" x="1359.28" y="-262.96" x1="0" y1="0" x2="0.783085" y2="-6.89115" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector13" modelIndex="85410567" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85411550" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411581" path=":/resources/parts/core/wire.fzp">

            <title>Wire552</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50226" x="1349.46" y="-252.478" x1="0" y1="0" x2="0.374986" y2="-16.2441" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector12" modelIndex="85410567" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85411550" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50218" x="1350.67" y="-263.273" x1="0" y1="0" x2="-0.156617" y2="-5.4816" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector12" modelIndex="85410567" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85411550" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50217" x="1350.67" y="-263.273" x1="0" y1="0" x2="-0.156617" y2="-5.4816" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector12" modelIndex="85410567" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85411550" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411594" path=":/resources/parts/core/wire.fzp">

            <title>Wire557</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50227" x="963.875" y="-263.418" x1="0" y1="0" x2="-1.09028" y2="-5.3039" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector11" modelIndex="85410559" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="6269" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50217" x="964.41" y="-261.979" x1="0" y1="0" x2="-0.694444" y2="-8.68056" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector11" modelIndex="85410559" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="6269" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50218" x="964.41" y="-261.979" x1="0" y1="0" x2="-0.694444" y2="-8.68056" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector11" modelIndex="85410559" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="6269" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411601" path=":/resources/parts/core/wire.fzp">

            <title>Wire560</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50228" x="973.193" y="-263.411" x1="0" y1="0" x2="-1.35467" y2="-5.31117" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector12" modelIndex="85410559" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="6269" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50216" x="972.702" y="-264.995" x1="0" y1="0" x2="-1.29991" y2="-3.15692" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector12" modelIndex="85410559" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="6269" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50219" x="972.702" y="-264.995" x1="0" y1="0" x2="-1.29991" y2="-3.15692" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector12" modelIndex="85410559" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="6269" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411608" path=":/resources/parts/core/wire.fzp">

            <title>Wire563</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50229" x="982.084" y="-265.19" x1="0" y1="0" x2="-1.19186" y2="-3.53231" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector13" modelIndex="85410559" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="6269" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50215" x="980.986" y="-265.493" x1="0" y1="0" x2="-0.234742" y2="-4.46009" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector13" modelIndex="85410559" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="6269" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5022" x="980.986" y="-265.493" x1="0" y1="0" x2="-0.234742" y2="-4.46009" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector13" modelIndex="85410559" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="6269" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411615" path=":/resources/parts/core/wire.fzp">

            <title>Wire566</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5023" x="953.446" y="-264.046" x1="0" y1="0" x2="0.285806" y2="-4.67603" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector10" modelIndex="85410559" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6269" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50214" x="954.225" y="-263.615" x1="0" y1="0" x2="0.938967" y2="-6.33803" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector10" modelIndex="85410559" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6269" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50221" x="954.225" y="-263.615" x1="0" y1="0" x2="0.938967" y2="-6.33803" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector10" modelIndex="85410559" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6269" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411622" path=":/resources/parts/core/wire.fzp">

            <title>Wire569</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50234" x="756" y="-657" x1="0" y1="0" x2="-27.0327" y2="0.0470028" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411631" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector260" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5023" x="997.727" y="-853.977" x1="0" y1="0" x2="20.4545" y2="116.477" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411631" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector260" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50222" x="997.727" y="-853.977" x1="0" y1="0" x2="20.4545" y2="116.477" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411631" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector260" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411625" path=":/resources/parts/core/wire.fzp">

            <title>Wire570</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50231" x="1025.88" y="-891.052" x1="0" y1="0" x2="54.8303" y2="8.69739" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514306" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411628" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50229" x="1007.95" y="-818.75" x1="0" y1="0" x2="8.98045" y2="80.7965" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411628" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50223" x="1007.95" y="-818.75" x1="0" y1="0" x2="8.98045" y2="80.7965" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514306" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411628" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411628" path=":/resources/parts/core/wire.fzp">

            <title>Wire571</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50232" x="738.069" y="-836.931" x1="0" y1="0" x2="287.813" y2="-54.1207" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411625" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411631" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50228" x="738.068" y="-836.932" x1="0" y1="0" x2="269.886" y2="18.1818" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411625" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411631" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50224" x="738.068" y="-836.932" x1="0" y1="0" x2="269.886" y2="18.1818" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411625" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411631" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411631" path=":/resources/parts/core/wire.fzp">

            <title>Wire572</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50233" x="728.967" y="-656.953" x1="0" y1="0" x2="9.10134" y2="-179.978" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411628" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411622" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50227" x="728.958" y="-665.894" x1="0" y1="0" x2="9.11065" y2="-171.037" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411628" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411622" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50225" x="728.958" y="-665.894" x1="0" y1="0" x2="9.11065" y2="-171.037" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411628" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411622" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411646" path=":/resources/parts/core/wire.fzp">

            <title>Wire579</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50235" x="962.785" y="-315" x1="0" y1="0" x2="-9.05376" y2="0" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fa50e6" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector5" modelIndex="85410559" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85410559" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50226" x="962.031" y="-315.115" x1="0" y1="0" x2="-7.98065" y2="0" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector5" modelIndex="85410559" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85410559" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50226" x="962.031" y="-315.115" x1="0" y1="0" x2="-7.98065" y2="0" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector5" modelIndex="85410559" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85410559" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411653" path=":/resources/parts/core/wire.fzp">

            <title>Wire582</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50236" x="1340.78" y="-315" x1="0" y1="0" x2="-9.05376" y2="0" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fa50e6" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector5" modelIndex="85410567" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85410567" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50225" x="1341.4" y="-316.919" x1="0" y1="0" x2="-10.1788" y2="0.550206" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector5" modelIndex="85410567" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85410567" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50227" x="1341.4" y="-316.919" x1="0" y1="0" x2="-10.1788" y2="0.550206" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector5" modelIndex="85410567" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85410567" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411660" path=":/resources/parts/core/wire.fzp">

            <title>Wire585</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50237" x="927" y="-602.999" x1="0" y1="0" x2="62.92" y2="-0.184218" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411663" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector264" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50224" x="929.353" y="-400.498" x1="0" y1="0" x2="15.4229" y2="85.0746" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411663" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector264" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50228" x="929.353" y="-400.498" x1="0" y1="0" x2="15.4229" y2="85.0746" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411663" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector264" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411663" path=":/resources/parts/core/wire.fzp">

            <title>Wire586</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50238" x="989.92" y="-603.183" x1="0" y1="0" x2="-45.243" y2="288.183" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector6" modelIndex="85410559" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411660" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50223" x="981.025" y="-593.928" x1="0" y1="0" x2="-36.3472" y2="278.928" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector6" modelIndex="85410559" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411660" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50229" x="981.025" y="-593.928" x1="0" y1="0" x2="-36.3472" y2="278.928" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector6" modelIndex="85410559" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411660" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411673" path=":/resources/parts/core/wire.fzp">

            <title>Wire589</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50239" x="927" y="-621.001" x1="0" y1="0" x2="45.086" y2="0.142261" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411679" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector266" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50222" x="1021.22" y="-600" x1="0" y1="0" x2="303.448" y2="283.289" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411679" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector266" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5023" x="1021.22" y="-600" x1="0" y1="0" x2="303.448" y2="283.289" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411679" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector266" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411676" path=":/resources/parts/core/wire.fzp">

            <title>Wire590</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5024" x="1044.03" y="-612.202" x1="0" y1="0" x2="278.646" y2="297.202" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector6" modelIndex="85410567" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411679" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5024" x="1044.03" y="-612.202" x1="0" y1="0" x2="278.646" y2="297.202" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector6" modelIndex="85410567" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411679" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50231" x="1044.03" y="-612.202" x1="0" y1="0" x2="278.646" y2="297.202" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector6" modelIndex="85410567" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411679" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411679" path=":/resources/parts/core/wire.fzp">

            <title>Wire591</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50241" x="972.086" y="-620.859" x1="0" y1="0" x2="71.9459" y2="8.6573" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411676" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411673" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50239" x="962.865" y="-621.22" x1="0" y1="0" x2="81.1671" y2="9.01857" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411676" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411673" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50232" x="962.865" y="-621.22" x1="0" y1="0" x2="81.1671" y2="9.01857" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411676" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411673" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411686" path=":/resources/parts/core/wire.fzp">

            <title>Wire594</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50242" x="927" y="-611.999" x1="0" y1="0" x2="44.883" y2="-0.203229" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411689" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector265" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50238" x="920.424" y="-385.146" x1="0" y1="0" x2="14.3236" y2="69.496" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411689" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector265" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50233" x="920.424" y="-385.146" x1="0" y1="0" x2="14.3236" y2="69.496" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411689" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector265" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411689" path=":/resources/parts/core/wire.fzp">

            <title>Wire595</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50243" x="971.883" y="-612.202" x1="0" y1="0" x2="-36.2596" y2="297.202" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector7" modelIndex="85410559" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411686" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50237" x="980.902" y="-594.164" x1="0" y1="0" x2="-45.2781" y2="279.164" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector7" modelIndex="85410559" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411686" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50234" x="980.902" y="-594.164" x1="0" y1="0" x2="-45.2781" y2="279.164" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector7" modelIndex="85410559" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411686" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411696" path=":/resources/parts/core/wire.fzp">

            <title>Wire598</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50244" x="927" y="-630" x1="0" y1="0" x2="62.877" y2="-8.957" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411699" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector267" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50236" x="979.061" y="-636.823" x1="0" y1="0" x2="333.574" y2="319.134" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411699" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector267" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50235" x="979.061" y="-636.823" x1="0" y1="0" x2="333.574" y2="319.134" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411699" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector267" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411699" path=":/resources/parts/core/wire.fzp">

            <title>Wire599</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50245" x="989.877" y="-638.957" x1="0" y1="0" x2="323.746" y2="323.957" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector7" modelIndex="85410567" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411696" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50235" x="999.08" y="-611.963" x1="0" y1="0" x2="314.544" y2="296.963" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector7" modelIndex="85410567" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411696" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50236" x="999.08" y="-611.963" x1="0" y1="0" x2="314.544" y2="296.963" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector7" modelIndex="85410567" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411696" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411726" path=":/resources/parts/core/wire.fzp">

            <title>Wire612</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50246" x="1377.03" y="-288.038" x1="0" y1="0" x2="44.9299" y2="17.9884" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411368" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411333" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50234" x="1376.95" y="-288.022" x1="0" y1="0" x2="45.0124" y2="17.9719" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411368" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411333" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50237" x="1376.95" y="-288.022" x1="0" y1="0" x2="45.0124" y2="17.9719" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411368" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411333" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="MediumElectrolyticCapacitorModuleID" modelIndex="85411922" path="C:/Program Files/Fritzing/fritzing-parts/core/capacitor_electrolytic_medium.fzp">

            <property name="capacitance5mm" value="0.1nF"/>

            <property name="capacitance7.5mm" value="10nF"/>

            <property name="capacitance10mm" value="2.2µF"/>

            <property name="capacitance15mm" value="4.7µF"/>

            <property name="capacitance22.5mm" value="10µF"/>

            <property name="capacitance27.5mm" value="22µF"/>

            <property name="capacitance37.5mm" value="100nF"/>

            <property name="capacitance" value="100µF"/>

            <property name="voltageHigh" value="35V"/>

            <property name="voltage" value="35V"/>

            <title>C3</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50168" x="1358.28" y="-243">

                        <transform m11="1" m12="0" m13="0" m21="0" m22="-1" m23="0" m31="0" m32="53.9109" m33="1"/>

                    </geometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="18.7164" y="53.9109"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="0.371048" y="3.40765"/>

                                <bezier/>

                                <point x="0.166389" y="21.3128"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411956" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="9.7164" y="53.9109"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="-0.332779" y="14.6572"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411979" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.50175" x="251.55" y="107.55">

                        <transform m11="0" m12="1" m13="0" m21="-1" m22="0" m23="0" m31="36.9" m32="0" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="288.45" y="100.55" z="13.0005" xOffset="36.9" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411956" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411979" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50175" x="548.55" y="-36.4377"/>

                    <titleGeometry visible="true" x="567.45" y="-50.4377" z="7.00045" xOffset="18.9" yOffset="-14" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                        <displayKey key="capacitance"/>

                        <displayKey key="voltage"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411956" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411979" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411945" path=":/resources/parts/core/wire.fzp">

            <title>Wire645</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50247" x="1395.01" y="-252.08" x1="0" y1="0" x2="36.1889" y2="35.9517" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411386" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411330" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50233" x="1377.04" y="-261.065" x1="0" y1="0" x2="54.1589" y2="44.9367" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411386" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411330" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50238" x="1377.04" y="-261.065" x1="0" y1="0" x2="54.1589" y2="44.9367" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411386" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411330" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411956" path=":/resources/parts/core/wire.fzp">

            <title>Wire650</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50248" x="1377.16" y="-264.313" x1="0" y1="0" x2="-0.164478" y2="-4.40957" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector15" modelIndex="85410567" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411922" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50232" x="1376.54" y="-264.226" x1="0" y1="0" x2="-0.332779" y2="-3.99334" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector15" modelIndex="85410567" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411922" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50239" x="1376.54" y="-264.226" x1="0" y1="0" x2="-0.332779" y2="-3.99334" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector15" modelIndex="85410567" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411922" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85411979" path=":/resources/parts/core/wire.fzp">

            <title>Wire661</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50249" x="1367.66" y="-257.657" x1="0" y1="0" x2="0.280745" y2="-11.0652" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85410567" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411922" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50231" x="1367.89" y="-257.238" x1="0" y1="0" x2="-0.998336" y2="-8.65225" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85410567" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411922" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5024" x="1367.89" y="-257.238" x1="0" y1="0" x2="-0.998336" y2="-8.65225" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85410567" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411922" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85412010" path=":/resources/parts/core/wire.fzp">

            <title>Wire676</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5025" x="989.348" y="-260.546" x1="0" y1="0" x2="0.598763" y2="-8.17657" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85410559" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="6781" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50243" x="988.753" y="-260.147" x1="0" y1="0" x2="-0.488998" y2="-6.19397" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85410559" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="6781" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50241" x="988.753" y="-260.147" x1="0" y1="0" x2="-0.488998" y2="-6.19397" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85410559" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="6781" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85412033" path=":/resources/parts/core/wire.fzp">

            <title>Wire687</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50251" x="998.674" y="-261.524" x1="0" y1="0" x2="0.32671" y2="-7.19857" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector15" modelIndex="85410559" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6781" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50242" x="998.859" y="-260.473" x1="0" y1="0" x2="1.30399" y2="-5.86797" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector15" modelIndex="85410559" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6781" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50242" x="998.859" y="-260.473" x1="0" y1="0" x2="1.30399" y2="-5.86797" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector15" modelIndex="85410559" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6781" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85412190" path=":/resources/parts/core/wire.fzp">

            <title>Wire754</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50252" x="1511.91" y="-612.275" x1="0" y1="0" x2="270.088" y2="0.275" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513267" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6626" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50241" x="1637.75" y="-692.715" x1="0" y1="0" x2="27.0244" y2="-9.5575" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6626" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50243" x="1637.75" y="-692.715" x1="0" y1="0" x2="27.0244" y2="-9.5575" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513267" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6626" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="wago-221-415_1" modelIndex="85513085" path="[REDACTED_HOME_PATH]">

            <title>12V Positive Wago 1</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50007" x="1776.79" y="-449.913"/>

                    <titleGeometry visible="true" x="1859.82" y="-402.801" z="5.00255" xOffset="83.0285" yOffset="47.1111" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513578" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513460" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513392" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513350" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514192" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="breadboard">

                    <geometry z="3.50016" x="1422.3" y="-71.2298"/>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50015" x="1417.89" y="-75.5419"/>

                    <titleGeometry visible="true" x="1436.06" y="-82.5419" z="7.00083" xOffset="18.1649" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513578" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513460" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513392" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513350" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514192" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="wago-221-415_1" modelIndex="85513267" path="[REDACTED_HOME_PATH]">

            <title>12V Negative Wago 1</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50006" x="1776.79" y="-647.913">

                        <transform m11="1" m12="0" m13="0" m21="0" m22="1" m23="0" m31="1.92e-05" m32="0.000191" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="1851.73" y="-595.406" z="5.00258" xOffset="74.9468" yOffset="52.5073" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85412190" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513501" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411336" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514089" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513842" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="breadboard">

                    <geometry z="3.50015" x="1472.19" y="-117.07"/>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50014" x="1447.21" y="-114.362"/>

                    <titleGeometry visible="true" x="1465.38" y="-121.362" z="7.00083" xOffset="18.1649" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85412190" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513501" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411336" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514089" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513842" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85513350" path=":/resources/parts/core/wire.fzp">

            <title>Wire942</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50005" x="1782" y="-437.567" x1="0" y1="0" x2="-53.8765" y2="-12.1865" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513358" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513085" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50033" x="1699.76" y="-457.126" x1="0" y1="0" x2="44.8052" y2="-36.865" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513358" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50018" x="1699.76" y="-457.126" x1="0" y1="0" x2="44.8052" y2="-36.865" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513358" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513085" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85513353" path=":/resources/parts/core/wire.fzp">

            <title>Wire943</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50004" x="1610.92" y="-476.746" x1="0" y1="0" x2="0.0089" y2="-9.15605" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513623" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513553" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50032" x="1728.12" y="-486.051" x1="0" y1="0" x2="17.8813" y2="-8.94765" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513623" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513553" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5002" x="1728.12" y="-486.051" x1="0" y1="0" x2="17.8813" y2="-8.94765" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513623" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513553" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85513358" path=":/resources/parts/core/wire.fzp">

            <title>Wire945</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50003" x="1728.12" y="-449.753" x1="0" y1="0" x2="-90.3346" y2="9.02267" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513553" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513350" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50031" x="1728.12" y="-449.753" x1="0" y1="0" x2="0" y2="-36.2979" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513553" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513350" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50022" x="1728.12" y="-449.753" x1="0" y1="0" x2="0" y2="-36.2979" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513553" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513350" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85513367" path=":/resources/parts/core/wire.fzp">

            <title>Wire949</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5017" x="1602.29" y="-459.155" x1="0" y1="0" x2="26.9443" y2="36.1272" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513578" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6647" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5003" x="1602.29" y="-459.155" x1="0" y1="0" x2="180.418" y2="35.801" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513578" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6647" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50024" x="1602.29" y="-459.155" x1="0" y1="0" x2="180.418" y2="35.801" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513578" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6647" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85513392" path=":/resources/parts/core/wire.fzp">

            <title>Wire961</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50201" x="1242.1" y="-360.199" x1="0" y1="0" x2="539.933" y2="-30.8837" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513085" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411323" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50029" x="1242.09" y="-360.199" x1="0" y1="0" x2="540.648" y2="-40.2377" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411323" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50025" x="1242.09" y="-360.199" x1="0" y1="0" x2="540.648" y2="-40.2377" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513085" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411323" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85513415" path=":/resources/parts/core/wire.fzp">

            <title>Wire972</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50205" x="1205.68" y="-377.616" x1="0" y1="0" x2="243.423" y2="-54.1533" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411342" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411316" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50028" x="1205.68" y="-377.616" x1="0" y1="0" x2="243.423" y2="-54.1533" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411342" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411316" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50026" x="1205.68" y="-377.616" x1="0" y1="0" x2="243.423" y2="-54.1533" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85411342" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411316" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85513460" path=":/resources/parts/core/wire.fzp">

            <title>Wire994</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50212" x="1718.97" y="-350.82" x1="0" y1="0" x2="62.3182" y2="-17.826" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513085" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411379" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50027" x="1728.17" y="-377.616" x1="0" y1="0" x2="53.8344" y2="-0.38433" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411379" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50027" x="1728.17" y="-377.616" x1="0" y1="0" x2="53.8344" y2="-0.38433" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513085" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411379" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="SparkFun-Passives-FUSE-X20MM" modelIndex="85513496" path="C:/Program Files/Fritzing/fritzing-parts/core/sparkfun-passives-fuse-x20mm.fzp">

            <title>12AWG 7.5AMP Fuse</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50008" x="1647" y="-498.866">

                        <transform m11="-1" m12="0" m13="0" m21="0" m22="-1" m23="0" m31="83.4663" m32="25.7325" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="1652.93" y="-467.932" z="5.00271" xOffset="5.93323" yOffset="30.9339" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513623" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513668" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.50014" x="1068.21" y="-99"/>

                    <titleGeometry visible="true" x="1091.79" y="-106" z="13.0008" xOffset="23.58" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector2" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513623" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513668" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50016" x="1070.56" y="-99.4502"/>

                    <titleGeometry visible="true" x="1143.44" y="-106.45" z="7.00084" xOffset="72.875" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513623" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513668" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85513501" path=":/resources/parts/core/wire.fzp">

            <title>Wire1007</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50207" x="1601.77" y="-548.777" x1="0" y1="0" x2="179.521" y2="-17.8687" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513267" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411342" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50026" x="1601.77" y="-548.777" x1="0" y1="0" x2="173.695" y2="-25.3376" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411342" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50029" x="1601.77" y="-548.777" x1="0" y1="0" x2="173.695" y2="-25.3376" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513267" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411342" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85513553" path=":/resources/parts/core/wire.fzp">

            <title>Wire1032</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50002" x="1637.78" y="-440.731" x1="0" y1="0" x2="-26.8589" y2="-36.0154" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513353" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513358" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50025" x="1656.1" y="-468.2" x1="0" y1="0" x2="-18.3129" y2="-17.7025" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513353" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513358" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50032" x="1656.1" y="-468.2" x1="0" y1="0" x2="-18.3129" y2="-17.7025" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513353" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513358" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85513578" path=":/resources/parts/core/wire.fzp">

            <title>Wire1044</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50169" x="1629.23" y="-423.028" x1="0" y1="0" x2="152.766" y2="9.0278" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513085" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513367" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50043" x="1629.24" y="-423.028" x1="0" y1="0" x2="153.474" y2="-0.326247" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513367" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50033" x="1629.24" y="-423.028" x1="0" y1="0" x2="153.474" y2="-0.326247" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513085" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513367" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85513623" path=":/resources/parts/core/wire.fzp">

            <title>Wire1066</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50001" x="1610.93" y="-485.902" x1="0" y1="0" x2="63.07" y2="-0.09755" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513496" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513353" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50042" x="1637.78" y="-485.902" x1="0" y1="0" x2="27.4694" y2="0" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513496" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513353" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50036" x="1637.78" y="-485.902" x1="0" y1="0" x2="27.4694" y2="0" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513496" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513353" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85513668" path=":/resources/parts/core/wire.fzp">

            <title>Wire1088</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50009" x="2142" y="-513" x1="0" y1="0" x2="-417.832" y2="27" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513496" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6316" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50041" x="1746.44" y="-492.617" x1="0" y1="0" x2="-43.951" y2="7.93559" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513496" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6316" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50037" x="1746.44" y="-492.617" x1="0" y1="0" x2="-43.951" y2="7.93559" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513496" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="6316" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85513819" path=":/resources/parts/core/wire.fzp">

            <title>Wire1160</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50015" x="2142" y="-522.001" x1="0" y1="0" x2="-513.13" y2="17.8013" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513865" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="6316" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5004" x="1636.81" y="-538.229" x1="0" y1="0" x2="136.117" y2="-14.1789" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513865" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="6316" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50041" x="1636.81" y="-538.229" x1="0" y1="0" x2="136.117" y2="-14.1789" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513865" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="6316" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85513842" path=":/resources/parts/core/wire.fzp">

            <title>Wire1171</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50014" x="1656.09" y="-539.931" x1="0" y1="0" x2="125.903" y2="-3.84293" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85513267" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513865" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50039" x="1656.09" y="-539.931" x1="0" y1="0" x2="120.082" y2="-11.3115" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513865" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50042" x="1656.09" y="-539.931" x1="0" y1="0" x2="120.082" y2="-11.3115" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85513267" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513865" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85513865" path=":/resources/parts/core/wire.fzp">

            <title>Wire1182</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50013" x="1628.87" y="-504.2" x1="0" y1="0" x2="27.2234" y2="-35.7307" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513842" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513819" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50038" x="1637.94" y="-521.782" x1="0" y1="0" x2="18.1489" y2="-18.1489" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513842" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513819" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50043" x="1637.94" y="-521.782" x1="0" y1="0" x2="18.1489" y2="-18.1489" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513842" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513819" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="DC Mini Metal Gear Motor_2015fb8e9adee36c637bb22e371b121f_1" modelIndex="85513980" path="[REDACTED_HOME_PATH] Mini Metal Gear Motor_2015fb8e9adee36c637bb22e371b121f_1.fzp">

            <title>Frontish Brush Motor</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.5001" x="1584" y="-1000.8"/>

                    <titleGeometry visible="true" x="1620.23" y="-1019.91" z="5.0027" xOffset="36.2273" yOffset="-19.1136" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector3" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515804" layer="breadboardWire"/>

                                <connect connectorId="connector0" modelIndex="85514657" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515827" layer="breadboardWire"/>

                                <connect connectorId="connector0" modelIndex="85514654" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.50017" x="250.2" y="169.2">

                        <transform m11="0" m12="1" m13="0" m21="-1" m22="0" m23="0" m31="17.1" m32="4.5" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="262.8" y="162.2" z="13.0008" xOffset="12.6" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector3" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515804" layer="copper1trace"/>

                                <connect connectorId="connector0" modelIndex="85514657" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515827" layer="copper1trace"/>

                                <connect connectorId="connector0" modelIndex="85514654" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50017" x="1090.35" y="-99.9063"/>

                    <titleGeometry visible="true" x="1105.65" y="-106.906" z="7.00086" xOffset="15.3" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector3" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515804" layer="schematicTrace"/>

                                <connect connectorId="connector0" modelIndex="85514657" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515827" layer="schematicTrace"/>

                                <connect connectorId="connector0" modelIndex="85514654" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="DC Mini Metal Gear Motor_2015fb8e9adee36c637bb22e371b121f_1" modelIndex="85513983" path="[REDACTED_HOME_PATH] Mini Metal Gear Motor_2015fb8e9adee36c637bb22e371b121f_1.fzp">

            <title>Backish brush Motor</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50011" x="1584" y="-955.8"/>

                    <titleGeometry visible="true" x="1615.67" y="-903.332" z="5.00269" xOffset="31.6728" yOffset="52.4683" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector3" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515782" layer="breadboardWire"/>

                                <connect connectorId="connector0" modelIndex="85514619" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515797" layer="breadboardWire"/>

                                <connect connectorId="connector0" modelIndex="85514616" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.50018" x="286.2" y="169.2">

                        <transform m11="0" m12="1" m13="0" m21="-1" m22="0" m23="0" m31="17.1" m32="4.5" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="298.8" y="162.2" z="13.0008" xOffset="12.6" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector3" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515782" layer="copper1trace"/>

                                <connect connectorId="connector0" modelIndex="85514619" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515797" layer="copper1trace"/>

                                <connect connectorId="connector0" modelIndex="85514616" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50019" x="1072.35" y="89.0937"/>

                    <titleGeometry visible="true" x="1087.65" y="82.0937" z="7.00087" xOffset="15.3" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector3" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515782" layer="schematicTrace"/>

                                <connect connectorId="connector0" modelIndex="85514619" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515797" layer="schematicTrace"/>

                                <connect connectorId="connector0" modelIndex="85514616" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="wago-221-415_1" modelIndex="85513986" path="[REDACTED_HOME_PATH]">

            <title>12V Negative Wago 2</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50012" x="1776.79" y="-782.913"/>

                    <titleGeometry visible="true" x="1855.98" y="-719.072" z="5.00257" xOffset="79.1955" yOffset="63.8409" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector3" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514547" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514874" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514039" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="breadboard">

                    <geometry z="3.50019" x="1257.96" y="103.318"/>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50021" x="1255.89" y="104.458"/>

                    <titleGeometry visible="true" x="1274.06" y="97.4581" z="7.00088" xOffset="18.1649" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector3" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514547" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514874" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects/>

                        </connector>

                        <connector connectorId="connector4" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514039" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="wago-221-415_1" modelIndex="85513989" path="[REDACTED_HOME_PATH]">

            <title>12V Positive Wago 2</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50016" x="1776.79" y="-314.913"/>

                    <titleGeometry visible="true" x="1859.32" y="-264.653" z="5.00256" xOffset="82.5328" yOffset="50.2599" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514255" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514877" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514138" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="breadboard">

                    <geometry z="3.50022" x="687.986" y="280.099"/>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50023" x="688.893" y="284.458"/>

                    <titleGeometry visible="true" x="707.058" y="277.458" z="7.00089" xOffset="18.1649" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514255" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514877" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514138" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514039" path=":/resources/parts/core/wire.fzp">

            <title>Wire1227</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50019" x="1782" y="-678.774" x1="0" y1="0" x2="-27.068" y2="12.6663" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514064" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85513986" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50053" x="1735.06" y="-646.735" x1="0" y1="0" x2="48.679" y2="4.47052" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514064" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50044" x="1735.06" y="-646.735" x1="0" y1="0" x2="48.679" y2="4.47052" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514064" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85513986" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514064" path=":/resources/parts/core/wire.fzp">

            <title>Wire1239</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50018" x="1754.93" y="-666.107" x1="0" y1="0" x2="0.0109414" y2="18.2737" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514089" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514039" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50052" x="1745.99" y="-638.787" x1="0" y1="0" x2="36.7227" y2="-6.13339" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514089" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514039" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50045" x="1745.99" y="-638.787" x1="0" y1="0" x2="36.7227" y2="-6.13339" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514089" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514039" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514089" path=":/resources/parts/core/wire.fzp">

            <title>Wire1251</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50017" x="1754.94" y="-647.834" x1="0" y1="0" x2="27.0571" y2="12.2671" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513267" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514064" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50051" x="1763.87" y="-638.787" x1="0" y1="0" x2="18.8406" y2="-6.13339" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514064" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50046" x="1763.87" y="-638.787" x1="0" y1="0" x2="18.8406" y2="-6.13339" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513267" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514064" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514138" path=":/resources/parts/core/wire.fzp">

            <title>Wire1275</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50022" x="1782" y="-302.567" x1="0" y1="0" x2="-35.8191" y2="-12.4182" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514165" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513989" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5005" x="1742.61" y="-351.431" x1="0" y1="0" x2="36.0087" y2="-3.11614" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514165" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50047" x="1742.61" y="-351.431" x1="0" y1="0" x2="36.0087" y2="-3.11614" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514165" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85513989" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514165" path=":/resources/parts/core/wire.fzp">

            <title>Wire1288</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50021" x="1746.18" y="-314.985" x1="0" y1="0" x2="-0.809575" y2="-8.74629" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514192" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514138" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50049" x="1755.08" y="-342.083" x1="0" y1="0" x2="27.6297" y2="-13.0451" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514192" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514138" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50048" x="1755.08" y="-342.083" x1="0" y1="0" x2="27.6297" y2="-13.0451" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514192" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514138" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514192" path=":/resources/parts/core/wire.fzp">

            <title>Wire1301</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5002" x="1745.37" y="-323.731" x1="0" y1="0" x2="36.6286" y2="-22.0426" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85513085" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514165" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50048" x="1764.08" y="-342.083" x1="0" y1="0" x2="18.6275" y2="-13.0451" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514165" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50049" x="1764.08" y="-342.083" x1="0" y1="0" x2="18.6275" y2="-13.0451" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85513085" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514165" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514255" path=":/resources/parts/core/wire.fzp">

            <title>Wire1327</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50029" x="1782" y="-279" x1="0" y1="0" x2="-45.1841" y2="-0.104478" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514270" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513989" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50047" x="1783.08" y="-854.809" x1="0" y1="0" x2="-204.112" y2="10.857" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514270" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5005" x="1783.08" y="-854.809" x1="0" y1="0" x2="-204.112" y2="10.857" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514270" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85513989" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514258" path=":/resources/parts/core/wire.fzp">

            <title>Wire1328</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50028" x="1367.81" y="-828.201" x1="0" y1="0" x2="-7.17997" y2="-17.5965" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector5" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516206" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50046" x="1592.99" y="-873.48" x1="0" y1="0" x2="-13.4899" y2="31.9796" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector5" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516206" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50051" x="1592.99" y="-873.48" x1="0" y1="0" x2="-13.4899" y2="31.9796" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector5" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516206" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514261" path=":/resources/parts/core/wire.fzp">

            <title>Wire1329</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50027" x="1917.11" y="-836.842" x1="0" y1="0" x2="-341.925" y2="-18.1449" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516206" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517189" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50045" x="2196.04" y="-882.362" x1="0" y1="0" x2="-603.046" y2="8.88284" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516206" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517189" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50052" x="2196.04" y="-882.362" x1="0" y1="0" x2="-603.046" y2="8.88284" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516206" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517189" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514264" path=":/resources/parts/core/wire.fzp">

            <title>Wire1330</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50025" x="1979.78" y="-126.354" x1="0" y1="0" x2="36.0896" y2="-269.678" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517259" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514267" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50044" x="2204.92" y="-152.982" x1="0" y1="0" x2="-8.88284" y2="-729.38" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517259" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514267" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50053" x="2204.92" y="-152.982" x1="0" y1="0" x2="-8.88284" y2="-729.38" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517259" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514267" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514267" path=":/resources/parts/core/wire.fzp">

            <title>Wire1331</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50024" x="1709.73" y="-144.089" x1="0" y1="0" x2="270.051" y2="17.7352" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514264" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514270" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50061" x="1745.97" y="-144.099" x1="0" y1="0" x2="458.947" y2="-8.88284" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514264" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514270" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50054" x="1745.97" y="-144.099" x1="0" y1="0" x2="458.947" y2="-8.88284" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514264" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514270" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514270" path=":/resources/parts/core/wire.fzp">

            <title>Wire1332</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50023" x="1736.82" y="-279.104" x1="0" y1="0" x2="-27.0832" y2="135.015" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514267" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514255" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5006" x="1737.09" y="-297.082" x1="0" y1="0" x2="8.88284" y2="152.982" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514267" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514255" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50055" x="1737.09" y="-297.082" x1="0" y1="0" x2="8.88284" y2="152.982" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514267" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514255" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="wago-221-413_1" modelIndex="85514306" path="[REDACTED_HOME_PATH]">

            <title>5V Negative Wago 1</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50035" x="1075.5" y="-894.7"/>

                    <titleGeometry visible="true" x="1167.4" y="-883.7" z="5.00263" xOffset="91.9048" yOffset="11" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514356" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411625" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="breadboard">

                    <geometry z="3.50034" x="551.39" y="-13.7449"/>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50028" x="553.972" y="-12.5418"/>

                    <titleGeometry visible="true" x="572.137" y="-19.5418" z="7.00093" xOffset="18.1649" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514356" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects/>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411625" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="wago-221-413_1" modelIndex="85514323" path="[REDACTED_HOME_PATH]">

            <title>5V Positive Wago 1</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50036" x="1075.5" y="-813.7"/>

                    <titleGeometry visible="true" x="1166.09" y="-798.753" z="5.00262" xOffset="90.5891" yOffset="14.9474" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514333" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411502" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514402" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="breadboard">

                    <geometry z="3.50035" x="677.036" y="-33.1724"/>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.5003" x="679.972" y="-30.5418"/>

                    <titleGeometry visible="true" x="698.137" y="-37.5418" z="7.00094" xOffset="18.1649" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514333" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85411502" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514402" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514328" path=":/resources/parts/core/wire.fzp">

            <title>Wire1355</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50032" x="1016.97" y="-667.392" x1="0" y1="0" x2="-26.8929" y2="1.40453" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514338" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85411470" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50059" x="1012.82" y="-776.29" x1="0" y1="0" x2="66.7124" y2="-1.13714" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514338" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85411470" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50056" x="1012.82" y="-776.29" x1="0" y1="0" x2="66.7124" y2="-1.13714" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514338" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85411470" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514333" path=":/resources/parts/core/wire.fzp">

            <title>Wire1357</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50031" x="990.073" y="-774.016" x1="0" y1="0" x2="90.6696" y2="-4.42136" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514323" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514338" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50058" x="1026.08" y="-774.016" x1="0" y1="0" x2="54.6601" y2="-4.42136" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514338" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50057" x="1026.08" y="-774.016" x1="0" y1="0" x2="54.6601" y2="-4.42136" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514323" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514338" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514338" path=":/resources/parts/core/wire.fzp">

            <title>Wire1359</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5003" x="990.073" y="-665.987" x1="0" y1="0" x2="0" y2="-108.029" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514333" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514328" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50057" x="990.073" y="-665.987" x1="0" y1="0" x2="0" y2="-108.029" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514333" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514328" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50058" x="990.073" y="-665.987" x1="0" y1="0" x2="0" y2="-108.029" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514333" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514328" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514347" path=":/resources/parts/core/wire.fzp">

            <title>Wire1363</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50034" x="1016.93" y="-737.953" x1="0" y1="0" x2="0.0554753" y2="-125.897" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514356" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85411470" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50056" x="999.928" y="-856.648" x1="0" y1="0" x2="76.5677" y2="-1.89524" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514356" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85411470" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50059" x="999.928" y="-856.648" x1="0" y1="0" x2="76.5677" y2="-1.89524" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514356" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85411470" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514356" path=":/resources/parts/core/wire.fzp">

            <title>Wire1367</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50033" x="1016.99" y="-863.85" x1="0" y1="0" x2="63.7572" y2="4.41299" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514306" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514347" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50055" x="1026.08" y="-863.85" x1="0" y1="0" x2="54.6601" y2="4.41299" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514347" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5006" x="1026.08" y="-863.85" x1="0" y1="0" x2="54.6601" y2="4.41299" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514306" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514347" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514395" path=":/resources/parts/core/wire.fzp">

            <title>Wire1385</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50042" x="1394.27" y="-845.797" x1="0" y1="0" x2="9.82751" y2="26.6691" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514442" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector7" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50054" x="1058.93" y="-803.205" x1="0" y1="0" x2="21.6109" y2="0" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514442" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector7" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50061" x="1058.93" y="-803.205" x1="0" y1="0" x2="21.6109" y2="0" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514442" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector7" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514402" path=":/resources/parts/core/wire.fzp">

            <title>Wire1388</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50041" x="1061.81" y="-819.053" x1="0" y1="0" x2="18.8972" y2="17.6983" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514323" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514409" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50067" x="1053.17" y="-809.688" x1="0" y1="0" x2="27.5416" y2="8.33363" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514409" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50062" x="1053.17" y="-809.688" x1="0" y1="0" x2="27.5416" y2="8.33363" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514323" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514409" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514409" path=":/resources/parts/core/wire.fzp">

            <title>Wire1391</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5004" x="1269.28" y="-819.053" x1="0" y1="0" x2="-207.47" y2="0" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514402" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514433" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50066" x="1269.28" y="-819.053" x1="0" y1="0" x2="-207.465" y2="0" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514402" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514433" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50063" x="1269.28" y="-819.053" x1="0" y1="0" x2="-207.465" y2="0" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514402" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514433" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514433" path=":/resources/parts/core/wire.fzp">

            <title>Wire1402</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50039" x="1385.95" y="-782.838" x1="0" y1="0" x2="-116.671" y2="-36.2154" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514409" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514442" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50065" x="1557.08" y="-773.965" x1="0" y1="0" x2="-287.798" y2="-45.0873" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514409" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514442" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50064" x="1557.08" y="-773.965" x1="0" y1="0" x2="-287.798" y2="-45.0873" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514409" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514442" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514442" path=":/resources/parts/core/wire.fzp">

            <title>Wire1406</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50038" x="1404.1" y="-819.128" x1="0" y1="0" x2="-18.1452" y2="36.2905" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514433" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514395" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50064" x="1557.06" y="-827.925" x1="0" y1="0" x2="0.0170318" y2="53.9601" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514433" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514395" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50065" x="1557.06" y="-827.925" x1="0" y1="0" x2="0.0170318" y2="53.9601" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514433" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514395" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514476" path=":/resources/parts/core/wire.fzp">

            <title>Wire1421</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50046" x="1377.45" y="-845.797" x1="0" y1="0" x2="35.6898" y2="80.7132" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514547" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector6" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50063" x="1571.88" y="-699.612" x1="0" y1="0" x2="212.902" y2="3.70726" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514547" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector6" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50066" x="1571.88" y="-699.612" x1="0" y1="0" x2="212.902" y2="3.70726" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514547" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector6" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514547" path=":/resources/parts/core/wire.fzp">

            <title>Wire1456</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50045" x="1413.14" y="-765.084" x1="0" y1="0" x2="368.148" y2="63.4381" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513986" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514476" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50062" x="1584.06" y="-693.257" x1="0" y1="0" x2="197.943" y2="0.256834" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514476" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50067" x="1584.06" y="-693.257" x1="0" y1="0" x2="197.943" y2="0.256834" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513986" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514476" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514616" path=":/resources/parts/core/wire.fzp">

            <title>Wire1487</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50056" x="1710" y="-921.6" x1="0" y1="0" x2="35.9888" y2="-5.50858" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514631" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513983" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50072" x="1483.98" y="-847.304" x1="0" y1="0" x2="94.3219" y2="30.9095" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514631" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513983" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50068" x="1483.98" y="-847.304" x1="0" y1="0" x2="94.3219" y2="30.9095" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514631" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513983" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514619" path=":/resources/parts/core/wire.fzp">

            <title>Wire1488</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50063" x="1710" y="-945" x1="0" y1="0" x2="53.8943" y2="-0.014122" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514647" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513983" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50071" x="1457.53" y="-831.371" x1="0" y1="0" x2="122.682" y2="26.1297" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514647" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513983" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50069" x="1457.53" y="-831.371" x1="0" y1="0" x2="122.682" y2="26.1297" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514647" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513983" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514625" path=":/resources/parts/core/wire.fzp">

            <title>Wire1490</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50055" x="1575" y="-890.909" x1="0" y1="0" x2="-89.9646" y2="-126.053" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516482" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514628" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5007" x="1539.08" y="-882.146" x1="0" y1="0" x2="-18.1395" y2="54.2801" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516482" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514628" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5007" x="1539.08" y="-882.146" x1="0" y1="0" x2="-18.1395" y2="54.2801" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516482" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514628" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514628" path=":/resources/parts/core/wire.fzp">

            <title>Wire1491</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50051" x="1755.11" y="-864.205" x1="0" y1="0" x2="-180.114" y2="-26.7045" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514625" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514631" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50069" x="1745.99" y="-890.9" x1="0" y1="0" x2="-206.908" y2="8.75382" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514625" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514631" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50071" x="1745.99" y="-890.9" x1="0" y1="0" x2="-206.908" y2="8.75382" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514625" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514631" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514631" path=":/resources/parts/core/wire.fzp">

            <title>Wire1492</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5005" x="1745.99" y="-927.109" x1="0" y1="0" x2="9.12484" y2="62.9044" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514628" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514616" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50068" x="1745.99" y="-917.957" x1="0" y1="0" x2="0" y2="27.0573" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514628" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514616" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50072" x="1745.99" y="-917.957" x1="0" y1="0" x2="0" y2="27.0573" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514628" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514616" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514641" path=":/resources/parts/core/wire.fzp">

            <title>Wire1496</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50062" x="1575" y="-881.818" x1="0" y1="0" x2="-89.9649" y2="-153.169" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516504" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514644" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50079" x="1574.89" y="-890.9" x1="0" y1="0" x2="-44.9628" y2="53.7166" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516504" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514644" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50073" x="1574.89" y="-890.9" x1="0" y1="0" x2="-44.9628" y2="53.7166" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516504" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514644" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514644" path=":/resources/parts/core/wire.fzp">

            <title>Wire1497</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50058" x="1764.2" y="-855.114" x1="0" y1="0" x2="-189.205" y2="-26.7045" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514641" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514647" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50078" x="1763.89" y="-890.9" x1="0" y1="0" x2="-189.003" y2="0" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514641" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514647" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50074" x="1763.89" y="-890.9" x1="0" y1="0" x2="-189.003" y2="0" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514641" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514647" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514647" path=":/resources/parts/core/wire.fzp">

            <title>Wire1498</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50057" x="1763.89" y="-945.014" x1="0" y1="0" x2="0.310245" y2="89.9008" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514644" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514619" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50077" x="1763.89" y="-935.863" x1="0" y1="0" x2="0" y2="44.9628" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514644" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514619" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50075" x="1763.89" y="-935.863" x1="0" y1="0" x2="0" y2="44.9628" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514644" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514619" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514654" path=":/resources/parts/core/wire.fzp">

            <title>Wire1501</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50067" x="1710" y="-966.6" x1="0" y1="0" x2="45.1405" y2="-5.4717" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514672" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513980" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50076" x="1488.94" y="-833.204" x1="0" y1="0" x2="90.7214" y2="36.6069" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514672" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513980" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50076" x="1488.94" y="-833.204" x1="0" y1="0" x2="90.7214" y2="36.6069" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514672" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513980" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514657" path=":/resources/parts/core/wire.fzp">

            <title>Wire1502</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50071" x="1710" y="-990" x1="0" y1="0" x2="63.046" y2="0.0227652" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514688" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513980" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50075" x="1492.13" y="-818.482" x1="0" y1="0" x2="85.5487" y2="30.6384" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514688" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513980" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50077" x="1492.13" y="-818.482" x1="0" y1="0" x2="85.5487" y2="30.6384" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514688" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513980" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514663" path=":/resources/parts/core/wire.fzp">

            <title>Wire1504</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50066" x="1574.89" y="-1026.19" x1="0" y1="0" x2="-95.2711" y2="120.798" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514669" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50074" x="1574.89" y="-1026.19" x1="0" y1="0" x2="-72.02" y2="198.155" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514669" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50078" x="1574.89" y="-1026.19" x1="0" y1="0" x2="-72.02" y2="198.155" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514669" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514669" path=":/resources/parts/core/wire.fzp">

            <title>Wire1505</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50065" x="1755.14" y="-1026.19" x1="0" y1="0" x2="-180.25" y2="-0.0035" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514663" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514672" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50073" x="1755.14" y="-1026.19" x1="0" y1="0" x2="-180.249" y2="0" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514663" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514672" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50079" x="1755.14" y="-1026.19" x1="0" y1="0" x2="-180.249" y2="0" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514663" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514672" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514672" path=":/resources/parts/core/wire.fzp">

            <title>Wire1506</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50064" x="1755.14" y="-972.072" x1="0" y1="0" x2="0" y2="-54.1145" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514669" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514654" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50088" x="1755.14" y="-972.072" x1="0" y1="0" x2="0" y2="-54.1145" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514669" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514654" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5008" x="1755.14" y="-972.072" x1="0" y1="0" x2="0" y2="-54.1145" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514669" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514654" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514682" path=":/resources/parts/core/wire.fzp">

            <title>Wire1510</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5007" x="1566.13" y="-1044.1" x1="0" y1="0" x2="-86.5141" y2="155.526" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514685" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50087" x="1566.14" y="-1044.09" x1="0" y1="0" x2="-81.1718" y2="225.212" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514685" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50081" x="1566.14" y="-1044.09" x1="0" y1="0" x2="-81.1718" y2="225.212" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514685" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514685" path=":/resources/parts/core/wire.fzp">

            <title>Wire1511</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50069" x="1763.9" y="-1052.85" x1="0" y1="0" x2="-197.765" y2="8.74912" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514682" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514688" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50086" x="1763.89" y="-1052.85" x1="0" y1="0" x2="-197.757" y2="8.75382" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514682" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514688" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50082" x="1763.89" y="-1052.85" x1="0" y1="0" x2="-197.757" y2="8.75382" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514682" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514688" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514688" path=":/resources/parts/core/wire.fzp">

            <title>Wire1512</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50068" x="1773.05" y="-989.977" x1="0" y1="0" x2="-9.15172" y2="-62.8683" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514685" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514657" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50085" x="1773.05" y="-1007.88" x1="0" y1="0" x2="-9.15172" y2="-44.9628" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514685" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514657" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50083" x="1773.05" y="-1007.88" x1="0" y1="0" x2="-9.15172" y2="-44.9628" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514685" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514657" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514695" path=":/resources/parts/core/wire.fzp">

            <title>Wire1515</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50077" x="927" y="-707.4" x1="0" y1="0" x2="27.1189" y2="-3.63497" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#33ffc5" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514707" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector238" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50084" x="1779.12" y="-847.65" x1="0" y1="0" x2="-146.686" y2="5.60772" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514707" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector238" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50084" x="1779.12" y="-847.65" x1="0" y1="0" x2="-146.686" y2="5.60772" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514707" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector238" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514698" path=":/resources/parts/core/wire.fzp">

            <title>Wire1516</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50076" x="1817.62" y="-828.063" x1="0" y1="0" x2="-395.685" y2="-62.8575" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#33ffc5" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516377" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514701" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50083" x="1817.62" y="-828.063" x1="0" y1="0" x2="-184.122" y2="-13.4371" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516377" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514701" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50085" x="1817.62" y="-828.063" x1="0" y1="0" x2="-184.122" y2="-13.4371" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516377" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514701" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514701" path=":/resources/parts/core/wire.fzp">

            <title>Wire1517</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50074" x="1808.91" y="-1089.3" x1="0" y1="0" x2="8.706" y2="261.241" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#33ffc5" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514698" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514704" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50082" x="1808.91" y="-1089.31" x1="0" y1="0" x2="8.70812" y2="261.244" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514698" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514704" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50086" x="1808.91" y="-1089.31" x1="0" y1="0" x2="8.70812" y2="261.244" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514698" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514704" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514704" path=":/resources/parts/core/wire.fzp">

            <title>Wire1518</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50073" x="953.791" y="-1025.99" x1="0" y1="0" x2="855.123" y2="-63.3136" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#33ffc5" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514701" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514707" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50081" x="917.929" y="-1017.06" x1="0" y1="0" x2="890.985" y2="-72.2491" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514701" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514707" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50087" x="917.929" y="-1017.06" x1="0" y1="0" x2="890.985" y2="-72.2491" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514701" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514707" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514707" path=":/resources/parts/core/wire.fzp">

            <title>Wire1519</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50072" x="954.119" y="-711.035" x1="0" y1="0" x2="-0.328251" y2="-314.958" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#33ffc5" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514704" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514695" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5008" x="945.01" y="-711.035" x1="0" y1="0" x2="0.0136553" y2="-306.022" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514704" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514695" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50088" x="945.01" y="-711.035" x1="0" y1="0" x2="0.0136553" y2="-306.022" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514704" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514695" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514714" path=":/resources/parts/core/wire.fzp">

            <title>Wire1522</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50083" x="927" y="-698.4" x1="0" y1="0" x2="36.0177" y2="-3.68739" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#8c3b00" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514726" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector239" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50098" x="1723.01" y="-786.048" x1="0" y1="0" x2="-90.4752" y2="-3.25711" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514726" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector239" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50089" x="1723.01" y="-786.048" x1="0" y1="0" x2="-90.4752" y2="-3.25711" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514726" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector239" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514717" path=":/resources/parts/core/wire.fzp">

            <title>Wire1523</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50082" x="1809.1" y="-818.928" x1="0" y1="0" x2="-351.108" y2="-27.0896" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#8c3b00" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516432" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514720" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50097" x="1835.92" y="-791.839" x1="0" y1="0" x2="-202.422" y2="4.33868" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516432" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514720" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5009" x="1835.92" y="-791.839" x1="0" y1="0" x2="-202.422" y2="4.33868" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516432" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514720" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514720" path=":/resources/parts/core/wire.fzp">

            <title>Wire1524</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5008" x="1844.89" y="-1079.68" x1="0" y1="0" x2="-35.7881" y2="260.757" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#8c3b00" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514717" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514723" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50096" x="1826.87" y="-1098.01" x1="0" y1="0" x2="9.04752" y2="306.168" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514717" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514723" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50091" x="1826.87" y="-1098.01" x1="0" y1="0" x2="9.04752" y2="306.168" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514717" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514723" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514723" path=":/resources/parts/core/wire.fzp">

            <title>Wire1525</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50079" x="962.633" y="-1016.67" x1="0" y1="0" x2="882.257" y2="-63.0096" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#8c3b00" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514720" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514726" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50095" x="918.142" y="-1035.04" x1="0" y1="0" x2="908.733" y2="-81.0658" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514720" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514726" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50092" x="918.142" y="-1035.04" x1="0" y1="0" x2="908.733" y2="-81.0658" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514720" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514726" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514726" path=":/resources/parts/core/wire.fzp">

            <title>Wire1526</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50078" x="963.018" y="-702.087" x1="0" y1="0" x2="-0.384854" y2="-314.588" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#8c3b00" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514723" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514714" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50094" x="953.97" y="-693.04" x1="0" y1="0" x2="-35.8282" y2="-341.996" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514723" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514714" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50093" x="953.97" y="-693.04" x1="0" y1="0" x2="-35.8282" y2="-341.996" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514723" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514714" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514733" path=":/resources/parts/core/wire.fzp">

            <title>Wire1529</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50088" x="783" y="-476.999" x1="0" y1="0" x2="8.49811" y2="-584.712" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#ef6100" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514742" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector375" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50093" x="1761.36" y="-823.753" x1="0" y1="0" x2="-127.804" y2="-0.284642" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514742" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector375" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50094" x="1761.36" y="-823.753" x1="0" y1="0" x2="-127.804" y2="-0.284642" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514742" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector375" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514736" path=":/resources/parts/core/wire.fzp">

            <title>Wire1530</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50087" x="1863.21" y="-819.098" x1="0" y1="0" x2="-432.09" y2="-62.9779" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#ef6100" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516388" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514739" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50092" x="1863.21" y="-819.098" x1="0" y1="0" x2="-229.713" y2="-4.40159" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516388" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514739" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50095" x="1863.21" y="-819.098" x1="0" y1="0" x2="-229.713" y2="-4.40159" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516388" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514739" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514739" path=":/resources/parts/core/wire.fzp">

            <title>Wire1531</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50085" x="1872.17" y="-1124.89" x1="0" y1="0" x2="-8.958" y2="305.789" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#ef6100" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514736" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514742" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50091" x="1872.16" y="-1124.89" x1="0" y1="0" x2="-8.95123" y2="305.789" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514736" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514742" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50096" x="1872.16" y="-1124.89" x1="0" y1="0" x2="-8.95123" y2="305.789" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514736" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514742" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514742" path=":/resources/parts/core/wire.fzp">

            <title>Wire1532</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50084" x="791.498" y="-1061.71" x1="0" y1="0" x2="1080.67" y2="-63.1765" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#ef6100" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514739" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514733" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5009" x="746.767" y="-1062" x1="0" y1="0" x2="1125.4" y2="-62.8918" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514739" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514733" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50097" x="746.767" y="-1062" x1="0" y1="0" x2="1125.4" y2="-62.8918" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514739" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514733" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514749" path=":/resources/parts/core/wire.fzp">

            <title>Wire1535</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50093" x="792" y="-476.999" x1="0" y1="0" x2="8.97435" y2="-567.093" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#a37911" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514758" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector373" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50089" x="1903.56" y="-822.859" x1="0" y1="0" x2="-270.97" y2="-11.1412" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514758" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector373" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50098" x="1903.56" y="-822.859" x1="0" y1="0" x2="-270.97" y2="-11.1412" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514758" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector373" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514752" path=":/resources/parts/core/wire.fzp">

            <title>Wire1536</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50092" x="1853.82" y="-828.032" x1="0" y1="0" x2="-413.856" y2="-44.8592" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#a37911" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516399" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514755" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50107" x="1853.82" y="-828.032" x1="0" y1="0" x2="-220.32" y2="-4.4684" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516399" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514755" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50099" x="1853.82" y="-828.032" x1="0" y1="0" x2="-220.32" y2="-4.4684" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516399" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514755" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514755" path=":/resources/parts/core/wire.fzp">

            <title>Wire1537</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5009" x="1862.97" y="-1116.11" x1="0" y1="0" x2="-9.154" y2="288.078" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#a37911" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514752" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514758" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50106" x="1862.97" y="-1106.96" x1="0" y1="0" x2="-9.15172" y2="278.928" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514752" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514758" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.501" x="1862.97" y="-1106.96" x1="0" y1="0" x2="-9.15172" y2="278.928" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514752" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514758" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514758" path=":/resources/parts/core/wire.fzp">

            <title>Wire1538</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50089" x="800.974" y="-1044.09" x1="0" y1="0" x2="1062" y2="-72.02" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#a37911" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514755" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514749" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50105" x="810.126" y="-1062" x1="0" y1="0" x2="1052.85" y2="-54.1145" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514755" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514749" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50101" x="810.126" y="-1062" x1="0" y1="0" x2="1052.85" y2="-54.1145" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514755" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514749" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514768" path=":/resources/parts/core/wire.fzp">

            <title>Wire1541</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50099" x="801" y="-476.999" x1="0" y1="0" x2="8.88859" y2="-72.0999" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#a37911" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514795" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector371" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50104" x="1779.66" y="-805.695" x1="0" y1="0" x2="-146.459" y2="9.69466" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514795" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector371" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50102" x="1779.66" y="-805.695" x1="0" y1="0" x2="-146.459" y2="9.69466" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514795" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector371" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514771" path=":/resources/parts/core/wire.fzp">

            <title>Wire1542</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50107" x="810" y="-476.999" x1="0" y1="0" x2="18.0316" y2="-152.878" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#ef6100" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514806" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector369" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50103" x="1655.36" y="-807.08" x1="0" y1="0" x2="-22.5055" y2="0.692475" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514806" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector369" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50103" x="1655.36" y="-807.08" x1="0" y1="0" x2="-22.5055" y2="0.692475" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514806" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector369" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514774" path=":/resources/parts/core/wire.fzp">

            <title>Wire1543</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50106" x="1890.11" y="-791.926" x1="0" y1="0" x2="-450.142" y2="-36.0618" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#ef6100" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516410" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514783" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50102" x="1872.11" y="-809.85" x1="0" y1="0" x2="-238.607" y2="4.35002" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516410" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514783" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50104" x="1872.11" y="-809.85" x1="0" y1="0" x2="-238.607" y2="4.35002" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516410" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514783" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514777" path=":/resources/parts/core/wire.fzp">

            <title>Wire1544</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50098" x="1871.99" y="-810.046" x1="0" y1="0" x2="-422.838" y2="-26.7869" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#a37911" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516421" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514786" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50101" x="1881.11" y="-800.848" x1="0" y1="0" x2="-247.61" y2="4.34784" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516421" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514786" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50105" x="1881.11" y="-800.848" x1="0" y1="0" x2="-247.61" y2="4.34784" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516421" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514786" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514780" path=":/resources/parts/core/wire.fzp">

            <title>Wire1545</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50104" x="1872.11" y="-1142.93" x1="0" y1="0" x2="9.00118" y2="8.99828" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#ef6100" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514783" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514789" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.501" x="1881.11" y="-1133.93" x1="0" y1="0" x2="-9.00218" y2="324.079" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514783" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514789" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50106" x="1881.11" y="-1133.93" x1="0" y1="0" x2="-9.00218" y2="324.079" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514783" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514789" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514783" path=":/resources/parts/core/wire.fzp">

            <title>Wire1546</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50103" x="1881.11" y="-1133.93" x1="0" y1="0" x2="8.99433" y2="342.002" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#ef6100" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514774" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514780" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50099" x="1881.11" y="-1133.93" x1="0" y1="0" x2="-9.00218" y2="324.079" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514774" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514780" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50107" x="1881.11" y="-1133.93" x1="0" y1="0" x2="-9.00218" y2="324.079" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514774" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514780" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514786" path=":/resources/parts/core/wire.fzp">

            <title>Wire1547</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50096" x="1890.11" y="-1160.94" x1="0" y1="0" x2="-18.1199" y2="350.892" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#a37911" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514777" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514792" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50117" x="1890.11" y="-1151.93" x1="0" y1="0" x2="-9.00218" y2="351.085" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514777" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514792" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50108" x="1890.11" y="-1151.93" x1="0" y1="0" x2="-9.00218" y2="351.085" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514777" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514792" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514789" path=":/resources/parts/core/wire.fzp">

            <title>Wire1548</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50102" x="755.821" y="-1089" x1="0" y1="0" x2="1116.29" y2="-53.9261" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#ef6100" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514780" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514813" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50116" x="773.757" y="-1079.87" x1="0" y1="0" x2="1098.35" y2="-63.06" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514780" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514813" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50109" x="773.757" y="-1079.87" x1="0" y1="0" x2="1098.35" y2="-63.06" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514780" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514813" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514792" path=":/resources/parts/core/wire.fzp">

            <title>Wire1549</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50095" x="746.748" y="-1097.88" x1="0" y1="0" x2="1143.36" y2="-63.0597" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#a37911" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514786" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514795" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50115" x="746.747" y="-1097.88" x1="0" y1="0" x2="1143.36" y2="-63.0577" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514786" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514795" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5011" x="746.747" y="-1097.88" x1="0" y1="0" x2="1143.36" y2="-63.0577" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514786" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514795" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514795" path=":/resources/parts/core/wire.fzp">

            <title>Wire1550</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50094" x="809.889" y="-549.099" x1="0" y1="0" x2="-63.1414" y2="-548.779" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#a37911" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514792" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514768" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50114" x="836.781" y="-549.203" x1="0" y1="0" x2="-90.0334" y2="-548.674" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514792" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514768" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50111" x="836.781" y="-549.203" x1="0" y1="0" x2="-90.0334" y2="-548.674" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514792" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514768" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514806" path=":/resources/parts/core/wire.fzp">

            <title>Wire1555</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50101" x="828.032" y="-629.877" x1="0" y1="0" x2="-63.113" y2="-351.099" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#ef6100" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514813" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514771" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50113" x="828.032" y="-629.877" x1="0" y1="0" x2="-54.2744" y2="-449.994" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514813" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514771" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50112" x="828.032" y="-629.877" x1="0" y1="0" x2="-54.2744" y2="-449.994" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514813" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514771" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514813" path=":/resources/parts/core/wire.fzp">

            <title>Wire1558</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.501" x="764.919" y="-980.976" x1="0" y1="0" x2="-9.09715" y2="-108.029" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#ef6100" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514789" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514806" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50112" x="764.919" y="-980.976" x1="0" y1="0" x2="8.83861" y2="-98.8947" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514789" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514806" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50113" x="764.919" y="-980.976" x1="0" y1="0" x2="8.83861" y2="-98.8947" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514789" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514806" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="1000FADF10011leg" modelIndex="85514850" path="C:/Program Files/Fritzing/fritzing-parts/core/dc_motor.fzp">

            <property name="voltage (max)" value="6V"/>

            <property name="voltage (min)" value="3V"/>

            <title>San Ace 40 Axial Fan</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50037" x="1989.68" y="-1245.83">

                        <transform m11="0" m12="-1" m13="0" m21="1" m22="0" m23="0" m31="40.2575" m32="109.908" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="2107.56" y="-1223.67" z="5.00267" xOffset="117.881" yOffset="22.1582" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="2.5" y="41.3206"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="-22.3331" y="16.883"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514858" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="2.5" y="30.7157"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="-19.9676" y="49.9753"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514865" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.5002" x="151.2" y="52.2">

                        <transform m11="0" m12="1" m13="0" m21="-1" m22="0" m23="0" m31="17.1" m32="4.5" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="163.8" y="45.2" z="13.0009" xOffset="12.6" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514858" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514865" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50031" x="3358.35" y="8.74002"/>

                    <titleGeometry visible="true" x="3373.65" y="1.74002" z="7.00095" xOffset="15.3" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514858" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514865" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="drv-1012_1" modelIndex="85514855" path="[REDACTED_HOME_PATH]">

            <title>San Ace 40 Motor Driver</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50043" x="1972.93" y="-1103.26"/>

                    <titleGeometry visible="true" x="2107.49" y="-915.952" z="5.00268" xOffset="134.561" yOffset="187.308" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector10" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514880" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector6" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515217" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector7" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515593" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector9" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514858" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515599" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515145" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector8" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514865" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515459" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515243" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector11" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514982" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.50021" x="1744.02" y="147.375"/>

                    <titleGeometry visible="true" x="1920.87" y="140.375" z="13.0009" xOffset="176.85" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector6" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515217" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector7" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515593" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515599" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515145" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515459" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515243" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50034" x="1745.59" y="143.55"/>

                    <titleGeometry visible="true" x="1836.49" y="136.55" z="7.00096" xOffset="90.9" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector10" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514880" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector6" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515217" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector7" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515593" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector9" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514858" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector3" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515599" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515145" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector8" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514865" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515459" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515243" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector11" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514982" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514858" path=":/resources/parts/core/wire.fzp">

            <title>Wire1561</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50108" x="2088.14" y="-1116.09" x1="0" y1="0" x2="0.358601" y2="18.0875" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#ef6100" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector9" modelIndex="85514855" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514850" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50111" x="2086.92" y="-1113.63" x1="0" y1="0" x2="3.37094" y2="14.7095" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514850" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50114" x="2086.92" y="-1113.63" x1="0" y1="0" x2="3.37094" y2="14.7095" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector9" modelIndex="85514855" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514850" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514865" path=":/resources/parts/core/wire.fzp">

            <title>Wire1564</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50109" x="2110.63" y="-1118.45" x1="0" y1="0" x2="-4.62493" y2="20.453" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#ef6100" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector8" modelIndex="85514855" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514850" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5011" x="2108.98" y="-1117.31" x1="0" y1="0" x2="-0.612897" y2="17.1611" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514850" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50115" x="2108.98" y="-1117.31" x1="0" y1="0" x2="-0.612897" y2="17.1611" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector8" modelIndex="85514855" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514850" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514874" path=":/resources/parts/core/wire.fzp">

            <title>Wire1568</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50116" x="1782.03" y="-724.083" x1="0" y1="0" x2="-35.9405" y2="4.29081" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514892" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513986" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50109" x="2186.59" y="-1133.08" x1="0" y1="0" x2="-114.313" y2="32.242" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514892" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50116" x="2186.59" y="-1133.08" x1="0" y1="0" x2="-114.313" y2="32.242" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514892" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513986" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514877" path=":/resources/parts/core/wire.fzp">

            <title>Wire1569</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50122" x="1782.03" y="-256.083" x1="0" y1="0" x2="-36.2594" y2="3.84401" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514994" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513989" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50108" x="2187.01" y="-1156.94" x1="0" y1="0" x2="-135.249" y2="54.4346" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514994" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50117" x="2187.01" y="-1156.94" x1="0" y1="0" x2="-135.249" y2="54.4346" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514994" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513989" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514880" path=":/resources/parts/core/wire.fzp">

            <title>Wire1570</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50115" x="2223.56" y="-1142.57" x1="0" y1="0" x2="-152.096" y2="44.9851" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector10" modelIndex="85514855" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514883" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50127" x="2223.56" y="-1142.57" x1="0" y1="0" x2="-152.096" y2="44.9851" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514883" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50118" x="2223.56" y="-1142.57" x1="0" y1="0" x2="-152.096" y2="44.9851" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector10" modelIndex="85514855" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514883" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514883" path=":/resources/parts/core/wire.fzp">

            <title>Wire1571</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50114" x="2303.49" y="-1116.37" x1="0" y1="0" x2="-79.9278" y2="-26.2058" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514880" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514886" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50126" x="2303.49" y="-1116.37" x1="0" y1="0" x2="-79.9278" y2="-26.2058" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514880" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514886" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50119" x="2303.49" y="-1116.37" x1="0" y1="0" x2="-79.9278" y2="-26.2058" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514880" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514886" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514886" path=":/resources/parts/core/wire.fzp">

            <title>Wire1572</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50113" x="2286.46" y="-837.276" x1="0" y1="0" x2="17.0338" y2="-279.092" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514883" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514937" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50125" x="2286.46" y="-837.276" x1="0" y1="0" x2="17.0338" y2="-279.092" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514883" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514937" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5012" x="2286.46" y="-837.276" x1="0" y1="0" x2="17.0338" y2="-279.092" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514883" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514937" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514889" path=":/resources/parts/core/wire.fzp">

            <title>Wire1573</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50112" x="1763.65" y="-783.554" x1="0" y1="0" x2="189.292" y2="0.534093" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514937" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514892" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50124" x="1763.65" y="-783.554" x1="0" y1="0" x2="522.806" y2="-53.7219" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514937" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514892" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50121" x="1763.65" y="-783.554" x1="0" y1="0" x2="522.806" y2="-53.7219" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514937" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514892" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514892" path=":/resources/parts/core/wire.fzp">

            <title>Wire1574</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50111" x="1746.09" y="-719.792" x1="0" y1="0" x2="17.5591" y2="-63.7619" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514889" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514874" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50123" x="1746.09" y="-719.792" x1="0" y1="0" x2="17.5591" y2="-63.7619" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514889" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514874" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50122" x="1746.09" y="-719.792" x1="0" y1="0" x2="17.5591" y2="-63.7619" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514889" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514874" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514937" path=":/resources/parts/core/wire.fzp">

            <title>Wire1596</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5011" x="1952.94" y="-783.02" x1="0" y1="0" x2="333.514" y2="-54.256" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514886" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514889" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50122" x="1952.94" y="-783.02" x1="0" y1="0" x2="333.514" y2="-54.256" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514886" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514889" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50123" x="1952.94" y="-783.02" x1="0" y1="0" x2="333.514" y2="-54.256" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514886" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514889" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514982" path=":/resources/parts/core/wire.fzp">

            <title>Wire1618</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50121" x="2231.57" y="-1160.69" x1="0" y1="0" x2="-177.603" y2="63.1026" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector11" modelIndex="85514855" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514985" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50121" x="2231.57" y="-1160.69" x1="0" y1="0" x2="-177.603" y2="63.1026" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514985" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50124" x="2231.57" y="-1160.69" x1="0" y1="0" x2="-177.603" y2="63.1026" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector11" modelIndex="85514855" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514985" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514985" path=":/resources/parts/core/wire.fzp">

            <title>Wire1619</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5012" x="2322.37" y="-1125.16" x1="0" y1="0" x2="-90.8" y2="-35.53" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514982" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517084" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5012" x="2322.37" y="-1125.16" x1="0" y1="0" x2="-90.8024" y2="-35.5314" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514982" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517084" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50125" x="2322.37" y="-1125.16" x1="0" y1="0" x2="-90.8024" y2="-35.5314" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514982" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517084" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514988" path=":/resources/parts/core/wire.fzp">

            <title>Wire1620</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50119" x="2033.94" y="-108.303" x1="0" y1="0" x2="18.4459" y2="-296.459" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517224" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514991" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50119" x="2295.56" y="-36.0395" x1="0" y1="0" x2="26.8122" y2="-1089.12" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517224" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514991" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50126" x="2295.56" y="-36.0395" x1="0" y1="0" x2="26.8122" y2="-1089.12" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517224" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514991" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514991" path=":/resources/parts/core/wire.fzp">

            <title>Wire1621</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50118" x="1737.73" y="-36.0395" x1="0" y1="0" x2="296.205" y2="-72.2637" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514988" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514994" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50118" x="1737.73" y="-36.0395" x1="0" y1="0" x2="557.828" y2="-5.68434e-14" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514988" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514994" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50127" x="1737.73" y="-36.0395" x1="0" y1="0" x2="557.828" y2="-5.68434e-14" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514988" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514994" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85514994" path=":/resources/parts/core/wire.fzp">

            <title>Wire1622</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50117" x="1745.77" y="-252.239" x1="0" y1="0" x2="-8.04114" y2="216.199" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514991" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514877" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50134" x="1745.99" y="-278.928" x1="0" y1="0" x2="-8.25934" y2="242.889" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514991" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514877" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50128" x="1745.99" y="-278.928" x1="0" y1="0" x2="-8.25934" y2="242.889" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514991" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514877" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515041" path=":/resources/parts/core/wire.fzp">

            <title>Wire1645</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50126" x="756" y="-675" x1="0" y1="0" x2="-81.0552" y2="-8.99233" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515064" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector258" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50133" x="1959.69" y="-1066.16" x1="0" y1="0" x2="122.322" y2="123.408" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515064" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector258" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50129" x="1959.69" y="-1066.16" x1="0" y1="0" x2="122.322" y2="123.408" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515064" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector258" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515044" path=":/resources/parts/core/wire.fzp">

            <title>Wire1646</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50129" x="756" y="-666" x1="0" y1="0" x2="-125.504" y2="-0.524769" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515082" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector259" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50132" x="1897.08" y="-998.484" x1="0" y1="0" x2="183.846" y2="63.3326" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515082" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector259" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5013" x="1897.08" y="-998.484" x1="0" y1="0" x2="183.846" y2="63.3326" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515082" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector259" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515056" path=":/resources/parts/core/wire.fzp">

            <title>Wire1650</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50125" x="1827.12" y="-1322.84" x1="0" y1="0" x2="90.5907" y2="-9.51201" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515148" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515061" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50131" x="1953.41" y="-1232.85" x1="0" y1="0" x2="17.2652" y2="234.404" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515061" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50131" x="1953.41" y="-1232.85" x1="0" y1="0" x2="17.2652" y2="234.404" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515148" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515061" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515061" path=":/resources/parts/core/wire.fzp">

            <title>Wire1651</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50124" x="611.964" y="-1287.01" x1="0" y1="0" x2="1215.16" y2="-35.8296" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515056" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515064" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5013" x="657.067" y="-1215.18" x1="0" y1="0" x2="1296.35" y2="-17.6673" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515056" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515064" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50132" x="657.067" y="-1215.18" x1="0" y1="0" x2="1296.35" y2="-17.6673" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515056" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515064" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515064" path=":/resources/parts/core/wire.fzp">

            <title>Wire1652</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50123" x="674.945" y="-683.992" x1="0" y1="0" x2="-62.9804" y2="-603.02" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515061" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515041" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50129" x="674.945" y="-683.992" x1="0" y1="0" x2="-17.8777" y2="-531.186" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515061" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515041" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50133" x="674.945" y="-683.992" x1="0" y1="0" x2="-17.8777" y2="-531.186" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515061" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515041" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515079" path=":/resources/parts/core/wire.fzp">

            <title>Wire1659</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50128" x="602.888" y="-1296.03" x1="0" y1="0" x2="1314.82" y2="-126.325" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515151" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515082" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50128" x="702.316" y="-1170.09" x1="0" y1="0" x2="1242.16" y2="-27.5161" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515082" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50134" x="702.316" y="-1170.09" x1="0" y1="0" x2="1242.16" y2="-27.5161" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515151" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515082" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515082" path=":/resources/parts/core/wire.fzp">

            <title>Wire1660</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50127" x="630.496" y="-666.525" x1="0" y1="0" x2="-27.6083" y2="-629.504" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515079" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515044" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50141" x="701.926" y="-666.061" x1="0" y1="0" x2="0.389758" y2="-504.029" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515079" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515044" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50135" x="701.926" y="-666.061" x1="0" y1="0" x2="0.389758" y2="-504.029" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515079" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515044" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515137" path=":/resources/parts/core/wire.fzp">

            <title>Wire1687</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50133" x="1917" y="-1287" x1="0" y1="0" x2="-27.1083" y2="17.9157" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515229" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85515148" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5014" x="2102.36" y="-1036.66" x1="0" y1="0" x2="-1.99249" y2="93.0778" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515229" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50136" x="2102.36" y="-1036.66" x1="0" y1="0" x2="-1.99249" y2="93.0778" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515229" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85515148" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515140" path=":/resources/parts/core/wire.fzp">

            <title>Wire1688</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5014" x="1917" y="-1377" x1="0" y1="0" x2="-54.2544" y2="17.7419" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515534" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85515151" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50139" x="2100.09" y="-895.483" x1="0" y1="0" x2="0" y2="-37.2881" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515534" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50137" x="2100.09" y="-895.483" x1="0" y1="0" x2="0" y2="-37.2881" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515534" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85515151" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515145" path=":/resources/parts/core/wire.fzp">

            <title>Wire1689</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50139" x="2096.9" y="-917.929" x1="0" y1="0" x2="3.07426" y2="-16.0021" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85514855" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515522" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50138" x="2115.17" y="-908.874" x1="0" y1="0" x2="-15.1961" y2="-25.057" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85514855" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515522" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50138" x="2115.17" y="-908.874" x1="0" y1="0" x2="-15.1961" y2="-25.057" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85514855" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515522" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="wago-221-413_1" modelIndex="85515148" path="[REDACTED_HOME_PATH]">

            <title>5V Positive Wago 2</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50044" x="1912.5" y="-1344.7"/>

                    <titleGeometry visible="true" x="1988.33" y="-1319.19" z="5.00266" xOffset="75.8309" yOffset="25.512" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515240" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515137" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515056" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="breadboard">

                    <geometry z="3.50036" x="441.995" y="-142.816"/>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50035" x="445.972" y="-138.542"/>

                    <titleGeometry visible="true" x="464.137" y="-145.542" z="7.00097" xOffset="18.1649" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515240" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515137" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515056" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="wago-221-413_1" modelIndex="85515151" path="[REDACTED_HOME_PATH]">

            <title>5V Negative Wago 2</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50047" x="1912.5" y="-1434.7"/>

                    <titleGeometry visible="true" x="1986.23" y="-1410.82" z="5.00265" xOffset="73.7257" yOffset="23.8826" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515456" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515140" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515079" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="breadboard">

                    <geometry z="3.50037" x="630.995" y="-160.816"/>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50038" x="634.972" y="-156.542"/>

                    <titleGeometry visible="true" x="653.137" y="-163.542" z="7.00098" xOffset="18.1649" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515456" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515140" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515079" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515217" path=":/resources/parts/core/wire.fzp">

            <title>Wire1721</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50132" x="2007.09" y="-1043.84" x1="0" y1="0" x2="92.9121" y2="100.873" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector6" modelIndex="85514855" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515226" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50137" x="2007.09" y="-1043.84" x1="0" y1="0" x2="92.9121" y2="100.873" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector6" modelIndex="85514855" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515226" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50139" x="2007.09" y="-1043.84" x1="0" y1="0" x2="92.9121" y2="100.873" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector6" modelIndex="85514855" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515226" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515226" path=":/resources/parts/core/wire.fzp">

            <title>Wire1725</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50131" x="2007.09" y="-1269.08" x1="0" y1="0" x2="0" y2="225.249" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515217" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515229" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50136" x="1925.91" y="-1242.23" x1="0" y1="0" x2="81.1872" y2="198.39" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515217" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515229" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5014" x="1925.91" y="-1242.23" x1="0" y1="0" x2="81.1872" y2="198.39" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515217" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515229" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515229" path=":/resources/parts/core/wire.fzp">

            <title>Wire1726</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5013" x="1889.89" y="-1269.08" x1="0" y1="0" x2="117.203" y2="0" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515226" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515137" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50135" x="1889.89" y="-1269.08" x1="0" y1="0" x2="36.0154" y2="26.8589" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515226" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515137" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50141" x="1889.89" y="-1269.08" x1="0" y1="0" x2="36.0154" y2="26.8589" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515226" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515137" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515240" path=":/resources/parts/core/wire.fzp">

            <title>Wire1731</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50145" x="1917.74" y="-1309.44" x1="0" y1="0" x2="-37.0075" y2="13.494" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515251" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515148" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50151" x="1961.92" y="-1073.75" x1="0" y1="0" x2="119.644" y2="130.632" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515251" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50142" x="1961.92" y="-1073.75" x1="0" y1="0" x2="119.644" y2="130.632" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515251" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515148" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515243" path=":/resources/parts/core/wire.fzp">

            <title>Wire1732</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50144" x="1989" y="-1044" x1="0" y1="0" x2="93.0064" y2="101.038" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85514855" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515245" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5015" x="1989" y="-1044" x1="0" y1="0" x2="93.0064" y2="101.038" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85514855" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515245" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50143" x="1989" y="-1044" x1="0" y1="0" x2="93.0064" y2="101.038" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector4" modelIndex="85514855" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515245" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515245" path=":/resources/parts/core/wire.fzp">

            <title>Wire1733</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50143" x="1997.94" y="-1250.77" x1="0" y1="0" x2="-8.93784" y2="206.771" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515243" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515248" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50149" x="1997.94" y="-1250.77" x1="0" y1="0" x2="-8.93784" y2="206.771" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515243" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515248" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50144" x="1997.94" y="-1250.77" x1="0" y1="0" x2="-8.93784" y2="206.771" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515243" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515248" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515248" path=":/resources/parts/core/wire.fzp">

            <title>Wire1734</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50142" x="1863.03" y="-1259.93" x1="0" y1="0" x2="134.905" y2="9.15645" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515245" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515251" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50148" x="1863.03" y="-1259.93" x1="0" y1="0" x2="134.905" y2="9.15645" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515245" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515251" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50145" x="1863.03" y="-1259.93" x1="0" y1="0" x2="134.905" y2="9.15645" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515245" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515251" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515251" path=":/resources/parts/core/wire.fzp">

            <title>Wire1735</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50141" x="1880.74" y="-1295.94" x1="0" y1="0" x2="-17.7025" y2="36.0154" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515248" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515240" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50147" x="1880.74" y="-1295.94" x1="0" y1="0" x2="-17.7025" y2="36.0154" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515248" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515240" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50146" x="1880.74" y="-1295.94" x1="0" y1="0" x2="-17.7025" y2="36.0154" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515248" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515240" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515456" path=":/resources/parts/core/wire.fzp">

            <title>Wire1836</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50151" x="1917.74" y="-1399.44" x1="0" y1="0" x2="-81.9131" y2="13.2631" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515471" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515151" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50146" x="2066.99" y="-892.978" x1="0" y1="0" x2="16.6246" y2="-42.7489" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515471" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50147" x="2066.99" y="-892.978" x1="0" y1="0" x2="16.6246" y2="-42.7489" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515471" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515151" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515459" path=":/resources/parts/core/wire.fzp">

            <title>Wire1837</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5015" x="2078.87" y="-900.103" x1="0" y1="0" x2="3.10485" y2="-33.8283" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514855" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515462" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50145" x="2078.87" y="-900.103" x1="0" y1="0" x2="3.10485" y2="-33.8283" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514855" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515462" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50148" x="2078.87" y="-900.103" x1="0" y1="0" x2="3.10485" y2="-33.8283" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514855" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515462" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515462" path=":/resources/parts/core/wire.fzp">

            <title>Wire1838</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50149" x="1944.29" y="-908.811" x1="0" y1="0" x2="134.58" y2="8.70812" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515459" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515465" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50144" x="1944.29" y="-891.395" x1="0" y1="0" x2="134.58" y2="-8.70812" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515459" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515465" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50149" x="1944.29" y="-891.395" x1="0" y1="0" x2="134.58" y2="-8.70812" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515459" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515465" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515465" path=":/resources/parts/core/wire.fzp">

            <title>Wire1839</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50148" x="1944.29" y="-1205.68" x1="0" y1="0" x2="0" y2="296.868" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515462" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515468" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50143" x="1944.29" y="-1205.68" x1="0" y1="0" x2="0" y2="314.284" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515462" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515468" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5015" x="1944.29" y="-1205.68" x1="0" y1="0" x2="0" y2="314.284" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515462" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515468" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515468" path=":/resources/parts/core/wire.fzp">

            <title>Wire1840</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50147" x="1800.21" y="-1205.68" x1="0" y1="0" x2="144.08" y2="0" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515465" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515471" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50142" x="1800.21" y="-1205.68" x1="0" y1="0" x2="144.08" y2="0" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515465" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515471" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50151" x="1800.21" y="-1205.68" x1="0" y1="0" x2="144.08" y2="0" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515465" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515471" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515471" path=":/resources/parts/core/wire.fzp">

            <title>Wire1841</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50146" x="1835.83" y="-1386.17" x1="0" y1="0" x2="-35.6241" y2="180.496" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515468" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515456" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50161" x="1835.83" y="-1386.17" x1="0" y1="0" x2="-35.6241" y2="180.496" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515468" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515456" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50152" x="1835.83" y="-1386.17" x1="0" y1="0" x2="-35.6241" y2="180.496" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515468" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515456" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515522" path=":/resources/parts/core/wire.fzp">

            <title>Wire1866</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50138" x="2097.07" y="-891.395" x1="0" y1="0" x2="-0.177305" y2="-26.5343" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515145" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515525" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5016" x="2097.07" y="-891.395" x1="0" y1="0" x2="-0.177305" y2="-26.5343" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515145" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515525" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50153" x="2097.07" y="-891.395" x1="0" y1="0" x2="-0.177305" y2="-26.5343" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515145" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515525" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515525" path=":/resources/parts/core/wire.fzp">

            <title>Wire1867</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50137" x="1917.37" y="-891.395" x1="0" y1="0" x2="179.704" y2="0" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515522" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515528" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50159" x="1917.37" y="-881.895" x1="0" y1="0" x2="179.704" y2="-9.49977" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515522" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515528" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50154" x="1917.37" y="-881.895" x1="0" y1="0" x2="179.704" y2="-9.49977" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515522" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515528" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515528" path=":/resources/parts/core/wire.fzp">

            <title>Wire1868</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50136" x="1926.08" y="-1178.76" x1="0" y1="0" x2="-8.70812" y2="287.368" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515525" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515531" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50158" x="1926.08" y="-1178.76" x1="0" y1="0" x2="-8.70812" y2="296.868" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515525" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515531" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50155" x="1926.08" y="-1178.76" x1="0" y1="0" x2="-8.70812" y2="296.868" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515525" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515531" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515531" path=":/resources/parts/core/wire.fzp">

            <title>Wire1869</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50135" x="1808.91" y="-1178.76" x1="0" y1="0" x2="117.164" y2="0" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515528" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515534" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50157" x="1817.62" y="-1178.76" x1="0" y1="0" x2="108.456" y2="0" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515528" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515534" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50156" x="1817.62" y="-1178.76" x1="0" y1="0" x2="108.456" y2="0" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515528" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515534" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515534" path=":/resources/parts/core/wire.fzp">

            <title>Wire1870</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50134" x="1862.75" y="-1359.26" x1="0" y1="0" x2="-53.832" y2="180.496" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515531" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515140" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50156" x="1862.75" y="-1359.26" x1="0" y1="0" x2="-35.6241" y2="162.288" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515531" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515140" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50157" x="1862.75" y="-1359.26" x1="0" y1="0" x2="-35.6241" y2="162.288" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515531" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515140" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515587" path=":/resources/parts/core/wire.fzp">

            <title>Wire1896</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50156" x="927" y="-662.4" x1="0" y1="0" x2="-333.25" y2="41.3772" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515611" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector243" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50155" x="2193.55" y="-973.055" x1="0" y1="0" x2="-83.112" y2="29.6015" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515611" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector243" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50158" x="2193.55" y="-973.055" x1="0" y1="0" x2="-83.112" y2="29.6015" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515611" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector243" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515590" path=":/resources/parts/core/wire.fzp">

            <title>Wire1897</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50161" x="927" y="-671.4" x1="0" y1="0" x2="-341.773" y2="86.1727" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515618" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector242" modelIndex="5904" layer="breadboardbreadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50154" x="2294.5" y="-900.569" x1="0" y1="0" x2="-185.199" y2="-33.7761" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515618" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector242" modelIndex="5904" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50159" x="2294.5" y="-900.569" x1="0" y1="0" x2="-185.199" y2="-33.7761" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515618" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector242" modelIndex="5904" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515593" path=":/resources/parts/core/wire.fzp">

            <title>Wire1898</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50155" x="2186.44" y="-1044.07" x1="0" y1="0" x2="-77.43" y2="101.106" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector7" modelIndex="85514855" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515596" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50153" x="2186.44" y="-1044.07" x1="0" y1="0" x2="-77.4343" y2="101.106" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector7" modelIndex="85514855" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515596" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5016" x="2186.44" y="-1044.07" x1="0" y1="0" x2="-77.4343" y2="101.106" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector7" modelIndex="85514855" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515596" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515596" path=":/resources/parts/core/wire.fzp">

            <title>Wire1899</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50154" x="2277.06" y="-1511.93" x1="0" y1="0" x2="-90.6242" y2="467.857" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515593" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515605" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50152" x="2106.21" y="-1484.75" x1="0" y1="0" x2="80.226" y2="440.678" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515593" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515605" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50161" x="2106.21" y="-1484.75" x1="0" y1="0" x2="80.226" y2="440.678" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515593" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515605" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515599" path=":/resources/parts/core/wire.fzp">

            <title>Wire1900</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5016" x="2213.56" y="-1035.03" x1="0" y1="0" x2="-104.586" y2="101.098" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85514855" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515602" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50171" x="2213.56" y="-1035.03" x1="0" y1="0" x2="-104.589" y2="101.097" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85514855" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515602" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50162" x="2213.56" y="-1035.03" x1="0" y1="0" x2="-104.589" y2="101.097" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85514855" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515602" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515602" path=":/resources/parts/core/wire.fzp">

            <title>Wire1901</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50159" x="2349.24" y="-1538.84" x1="0" y1="0" x2="-135.675" y2="503.808" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515599" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515608" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5017" x="2142.37" y="-1511.86" x1="0" y1="0" x2="71.1864" y2="476.836" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515599" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515608" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50163" x="2142.37" y="-1511.86" x1="0" y1="0" x2="71.1864" y2="476.836" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515599" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515608" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515605" path=":/resources/parts/core/wire.fzp">

            <title>Wire1902</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50153" x="558.192" y="-1332.2" x1="0" y1="0" x2="1718.87" y2="-179.723" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515596" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515611" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50169" x="558.192" y="-1296.05" x1="0" y1="0" x2="1548.02" y2="-188.701" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515596" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515611" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50164" x="558.192" y="-1296.05" x1="0" y1="0" x2="1548.02" y2="-188.701" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515596" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515611" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515608" path=":/resources/parts/core/wire.fzp">

            <title>Wire1903</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50158" x="548.736" y="-1340.79" x1="0" y1="0" x2="1800.5" y2="-198.044" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515602" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515618" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50168" x="522.034" y="-1404.52" x1="0" y1="0" x2="1620.34" y2="-107.345" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515602" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515618" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50165" x="522.034" y="-1404.52" x1="0" y1="0" x2="1620.34" y2="-107.345" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515602" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515618" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515611" path=":/resources/parts/core/wire.fzp">

            <title>Wire1904</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50152" x="593.75" y="-621.023" x1="0" y1="0" x2="-35.5579" y2="-711.181" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515605" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515587" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50167" x="593.75" y="-621.023" x1="0" y1="0" x2="-35.5579" y2="-711.181" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515605" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515587" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50166" x="593.75" y="-621.023" x1="0" y1="0" x2="-35.5579" y2="-711.181" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515605" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515587" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515618" path=":/resources/parts/core/wire.fzp">

            <title>Wire1907</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50157" x="585.227" y="-585.227" x1="0" y1="0" x2="-36.4908" y2="-755.567" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515608" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515590" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50166" x="585.227" y="-585.227" x1="0" y1="0" x2="-63.1934" y2="-819.293" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515608" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515590" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50167" x="585.227" y="-585.227" x1="0" y1="0" x2="-63.1934" y2="-819.293" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515608" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515590" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="SmallElectrolyticCapacitorModuleID" modelIndex="85515777" path="C:/Program Files/Fritzing/fritzing-parts/core/capacitor_electrolytic_small.fzp">

            <property name="capacitance5mm" value="0.1nF"/>

            <property name="capacitance7.5mm" value="10nF"/>

            <property name="capacitance10mm" value="2.2µF"/>

            <property name="capacitance15mm" value="4.7µF"/>

            <property name="capacitance22.5mm" value="10µF"/>

            <property name="capacitance27.5mm" value="22µF"/>

            <property name="capacitance37.5mm" value="100nF"/>

            <property name="capacitance" value="0.1µF"/>

            <property name="voltageHigh" value="35V"/>

            <property name="voltage" value="50V"/>

            <title>C4</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50049" x="1648.82" y="-953.177">

                        <transform m11="0" m12="1" m13="0" m21="1" m22="0" m23="0" m31="-12.861" m32="12.861" m33="1"/>

                    </geometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="13.401" y="43.4394"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="0" y="12.6"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515797" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="4.401" y="43.4394"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="-4.98753" y="20.8294"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515782" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.50024" x="152.55" y="76.05">

                        <transform m11="0" m12="1" m13="0" m21="-1" m22="0" m23="0" m31="18.9" m32="0" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="171.45" y="69.05" z="13.0009" xOffset="18.9" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515797" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515782" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.5004" x="314.55" y="-81.4377"/>

                    <titleGeometry visible="true" x="333.45" y="-95.4377" z="7.00099" xOffset="18.9" yOffset="-14" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                        <displayKey key="capacitance"/>

                        <displayKey key="voltage"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515797" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515782" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="SmallElectrolyticCapacitorModuleID" modelIndex="85515780" path="C:/Program Files/Fritzing/fritzing-parts/core/capacitor_electrolytic_small.fzp">

            <property name="capacitance5mm" value="0.1nF"/>

            <property name="capacitance7.5mm" value="10nF"/>

            <property name="capacitance10mm" value="2.2µF"/>

            <property name="capacitance15mm" value="4.7µF"/>

            <property name="capacitance22.5mm" value="10µF"/>

            <property name="capacitance27.5mm" value="22µF"/>

            <property name="capacitance37.5mm" value="100nF"/>

            <property name="capacitance" value="0.1µF"/>

            <property name="voltageHigh" value="35V"/>

            <property name="voltage" value="50V"/>

            <title>C5</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.50048" x="1648.82" y="-998.177">

                        <transform m11="0" m12="1" m13="0" m21="1" m22="0" m23="0" m31="-12.861" m32="12.861" m33="1"/>

                    </geometry>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="13.401" y="43.4394"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="0" y="12.6"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515827" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="4.401" y="43.4394"/>

                            <leg>

                                <point x="0" y="0"/>

                                <bezier/>

                                <point x="-4.48878" y="16.3406"/>

                                <bezier/>

                            </leg>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515804" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper0">

                    <geometry z="5.50023" x="185.68" y="54.24">

                        <transform m11="0" m12="1" m13="0" m21="-1" m22="0" m23="0" m31="18.9" m32="0" m33="1"/>

                    </geometry>

                    <titleGeometry visible="true" x="204.58" y="47.24" z="13.0009" xOffset="18.9" yOffset="-7" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515827" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper0">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515804" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematic">

                    <geometry z="2.50039" x="362.83" y="-124.558"/>

                    <titleGeometry visible="true" x="381.73" y="-138.558" z="7.00099" xOffset="18.9" yOffset="-14" textColor="#000000" fontSize="5">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                        <displayKey key="capacitance"/>

                        <displayKey key="voltage"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector1" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515827" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematic">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515804" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515782" path=":/resources/parts/core/wire.fzp">

            <title>Wire1910</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50162" x="1700.23" y="-940.903" x1="0" y1="0" x2="9.77222" y2="-4.09779" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513983" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515777" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50165" x="1698.75" y="-940.898" x1="0" y1="0" x2="8.72818" y2="-3.2419" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513983" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515777" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50168" x="1698.75" y="-940.898" x1="0" y1="0" x2="8.72818" y2="-3.2419" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513983" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515777" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515797" path=":/resources/parts/core/wire.fzp">

            <title>Wire1917</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50163" x="1692" y="-926.915" x1="0" y1="0" x2="18.0016" y2="5.31468" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513983" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515777" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50164" x="1690.27" y="-925.686" x1="0" y1="0" x2="18.9526" y2="4.48878" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513983" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515777" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50169" x="1690.27" y="-925.686" x1="0" y1="0" x2="18.9526" y2="4.48878" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513983" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515777" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515804" path=":/resources/parts/core/wire.fzp">

            <title>Wire1920</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50164" x="1695.74" y="-985.404" x1="0" y1="0" x2="14.261" y2="-4.59654" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513980" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515780" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50163" x="1694.26" y="-985.536" x1="0" y1="0" x2="15.212" y2="-3.99002" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513980" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515780" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5017" x="1694.26" y="-985.536" x1="0" y1="0" x2="15.212" y2="-3.99002" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector3" modelIndex="85513980" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85515780" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85515827" path=":/resources/parts/core/wire.fzp">

            <title>Wire1931</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50165" x="1692" y="-971.915" x1="0" y1="0" x2="18.0016" y2="5.31468" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513980" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515780" layer="breadboard"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50162" x="1691.02" y="-970.823" x1="0" y1="0" x2="17.7057" y2="3.99002" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513980" layer="copper0"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515780" layer="copper0"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50171" x="1691.02" y="-970.823" x1="0" y1="0" x2="17.7057" y2="3.99002" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector2" modelIndex="85513980" layer="schematic"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85515780" layer="schematic"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="L298N motor driver_ed29594eba4fbd330bd92441a17764ea_15" modelIndex="85516153" path="[REDACTED_HOME_PATH] motor driver_ed29594eba4fbd330bd92441a17764ea_15.fzp">

            <title>L298N1( Brush Motors Driver)</title>

            <views>

                <breadboardView layer="breadboard">

                    <geometry z="2.5" x="1329.15" y="-994.672"/>

                    <titleGeometry visible="true" x="1180.41" y="-965.734" z="5.00264" xOffset="-148.741" yOffset="28.9383" textColor="#000000" fontSize="9">

                        <displayKey key=""/>

                        <displayKey key="mn"/>

                        <displayKey key="mpn"/>

                        <displayKey key="part number"/>

                    </titleGeometry>

                    <connectors>

                        <connector connectorId="connector12" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516432" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516515" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector6" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514476" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector7" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514395" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector14" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516399" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514682" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector16" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516421" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516493" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector15" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516410" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514663" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector13" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516388" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector5" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514258" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector11" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516377" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="breadboard">

                    <geometry z="3.50001" x="1319.23" y="-346.455"/>

                    <connectors>

                        <connector connectorId="connector12" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516432" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516515" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector6" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514476" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector7" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514395" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector14" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516399" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514682" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector16" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516421" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516493" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector15" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516410" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514663" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector13" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516388" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector5" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514258" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector11" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516377" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="breadboard">

                    <geometry z="3.50001" x="1256.23" y="-1064.42"/>

                    <connectors>

                        <connector connectorId="connector12" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516432" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector1" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516515" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector6" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514476" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector7" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514395" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector14" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516399" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector2" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514682" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector16" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516421" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516493" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector15" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516410" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector4" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514663" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector13" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516388" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector5" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514258" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector11" layer="breadboard">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516377" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85516206" path=":/resources/parts/core/wire.fzp">

            <title>Wire2065</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50026" x="1575.18" y="-854.987" x1="0" y1="0" x2="-207.37" y2="26.786" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514258" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514261" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5" x="1575.18" y="-854.987" x1="0" y1="0" x2="-207.374" y2="26.7858" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514258" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514261" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5" x="1575.18" y="-854.987" x1="0" y1="0" x2="-207.374" y2="26.7858" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514258" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514261" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85516377" path=":/resources/parts/core/wire.fzp">

            <title>Wire2150</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50075" x="1421.93" y="-890.921" x1="0" y1="0" x2="-8.93492" y2="35.9205" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#33ffc5" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector11" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514698" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50011" x="1431.12" y="-882.076" x1="0" y1="0" x2="-18.1197" y2="27.076" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector11" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514698" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50002" x="1431.12" y="-882.076" x1="0" y1="0" x2="-18.1197" y2="27.076" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector11" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514698" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85516388" path=":/resources/parts/core/wire.fzp">

            <title>Wire2155</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50086" x="1431.12" y="-882.076" x1="0" y1="0" x2="-9.1197" y2="27.076" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#ef6100" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector13" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514736" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.5001" x="1431.12" y="-872.891" x1="0" y1="0" x2="-9.1197" y2="17.8912" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector13" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514736" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50003" x="1431.12" y="-872.891" x1="0" y1="0" x2="-9.1197" y2="17.8912" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector13" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514736" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85516399" path=":/resources/parts/core/wire.fzp">

            <title>Wire2160</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50091" x="1439.96" y="-872.891" x1="0" y1="0" x2="-8.96426" y2="17.8912" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#a37911" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514752" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50009" x="1439.96" y="-864.047" x1="0" y1="0" x2="-8.96426" y2="9.04665" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514752" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50004" x="1439.96" y="-864.047" x1="0" y1="0" x2="-8.96426" y2="9.04665" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector14" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514752" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85516410" path=":/resources/parts/core/wire.fzp">

            <title>Wire2165</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50105" x="1439.96" y="-827.988" x1="0" y1="0" x2="0.0357699" y2="-27.012" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#ef6100" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector15" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514774" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50008" x="1439.96" y="-836.833" x1="0" y1="0" x2="0.0357699" y2="-18.1674" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector15" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514774" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50005" x="1439.96" y="-836.833" x1="0" y1="0" x2="0.0357699" y2="-18.1674" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector15" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514774" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85516421" path=":/resources/parts/core/wire.fzp">

            <title>Wire2170</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50097" x="1449.15" y="-836.833" x1="0" y1="0" x2="-0.149024" y2="-18.1674" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#a37911" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector16" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514777" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50007" x="1449.15" y="-836.833" x1="0" y1="0" x2="-0.149024" y2="-18.1674" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector16" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514777" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50006" x="1449.15" y="-836.833" x1="0" y1="0" x2="-0.149024" y2="-18.1674" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector16" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514777" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85516432" path=":/resources/parts/core/wire.fzp">

            <title>Wire2175</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50081" x="1457.99" y="-846.017" x1="0" y1="0" x2="0.00640812" y2="-8.98267" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#8c3b00" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector12" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514717" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50006" x="1457.99" y="-846.017" x1="0" y1="0" x2="0.00640812" y2="-8.98267" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector12" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514717" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50007" x="1457.99" y="-846.017" x1="0" y1="0" x2="0.00640812" y2="-8.98267" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector12" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514717" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85516471" path=":/resources/parts/core/wire.fzp">

            <title>Wire2194</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50054" x="1160.8" y="-972.159" x1="0" y1="0" x2="0" y2="27.2727" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516493" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516482" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50005" x="1323.1" y="-1007.95" x1="0" y1="0" x2="7.39756" y2="105.858" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516493" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516482" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50008" x="1323.1" y="-1007.95" x1="0" y1="0" x2="7.39756" y2="105.858" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516493" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516482" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85516482" path=":/resources/parts/core/wire.fzp">

            <title>Wire2199</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50053" x="1485.04" y="-1016.96" x1="0" y1="0" x2="-324.24" y2="44.8029" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516471" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514625" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50004" x="1485.03" y="-1016.96" x1="0" y1="0" x2="-161.935" y2="9.01253" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516471" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514625" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50009" x="1485.03" y="-1016.96" x1="0" y1="0" x2="-161.935" y2="9.01253" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516471" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514625" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85516493" path=":/resources/parts/core/wire.fzp">

            <title>Wire2204</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50052" x="1160.8" y="-944.886" x1="0" y1="0" x2="169.7" y2="42.7946" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#fff800" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516471" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50003" x="1305.07" y="-927.128" x1="0" y1="0" x2="25.4226" y2="25.0362" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516471" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.5001" x="1305.07" y="-927.128" x1="0" y1="0" x2="25.4226" y2="25.0362" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516471" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85516504" path=":/resources/parts/core/wire.fzp">

            <title>Wire2209</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50061" x="1485.04" y="-1034.99" x1="0" y1="0" x2="-332.762" y2="45.2143" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516526" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514641" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50002" x="1485.03" y="-1034.99" x1="0" y1="0" x2="-154.537" y2="149.717" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516526" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514641" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50011" x="1485.03" y="-1034.99" x1="0" y1="0" x2="-154.537" y2="149.717" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516526" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514641" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85516515" path=":/resources/parts/core/wire.fzp">

            <title>Wire2214</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.5006" x="1152.27" y="-935.795" x1="0" y1="0" x2="178.223" y2="50.5251" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516526" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50013" x="1260.01" y="-962.887" x1="0" y1="0" x2="70.4853" y2="77.6171" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516526" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50012" x="1260.01" y="-962.887" x1="0" y1="0" x2="70.4853" y2="77.6171" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516153" layer="breadboard"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516526" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85516526" path=":/resources/parts/core/wire.fzp">

            <title>Wire2219</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50059" x="1152.27" y="-989.773" x1="0" y1="0" x2="0" y2="53.9773" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#25cc35" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516515" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516504" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <pcbView layer="copper1trace">

                    <geometry z="9.50012" x="1314.08" y="-1016.96" x1="0" y1="0" x2="-54.0752" y2="54.0752" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516515" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516504" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

                <schematicView layer="schematicTrace">

                    <geometry z="5.50013" x="1314.08" y="-1016.96" x1="0" y1="0" x2="-54.0752" y2="54.0752" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85516515" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85516504" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85517084" path=":/resources/parts/core/wire.fzp">

            <title>Wire2497</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50119" x="2303.92" y="-837.255" x1="0" y1="0" x2="18.4484" y2="-287.905" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514985" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517119" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <schematicView layer="schematicTrace">

                    <geometry z="6.00256" x="2303.92" y="-837.255" x1="0" y1="0" x2="18.4484" y2="-287.905" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514985" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517119" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

                <pcbView layer="copper1trace">

                    <geometry z="10.0026" x="2303.92" y="-837.255" x1="0" y1="0" x2="18.4484" y2="-287.905" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514985" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517119" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85517119" path=":/resources/parts/core/wire.fzp">

            <title>Wire2514</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50119" x="1971.02" y="-764.773" x1="0" y1="0" x2="332.899" y2="-72.4822" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517084" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517154" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <schematicView layer="schematicTrace">

                    <geometry z="6.00257" x="1943.14" y="-764.706" x1="0" y1="0" x2="360.784" y2="-72.549" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517084" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517154" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

                <pcbView layer="copper1trace">

                    <geometry z="10.0026" x="1943.14" y="-764.706" x1="0" y1="0" x2="360.784" y2="-72.549" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517084" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517154" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85517154" path=":/resources/parts/core/wire.fzp">

            <title>Wire2531</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50119" x="1989.2" y="-728.977" x1="0" y1="0" x2="-18.1818" y2="-35.7955" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517119" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517224" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <schematicView layer="schematicTrace">

                    <geometry z="6.00258" x="1961.93" y="-728.977" x1="0" y1="0" x2="-18.7946" y2="-35.7286" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517119" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517224" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

                <pcbView layer="copper1trace">

                    <geometry z="10.0026" x="1961.93" y="-728.977" x1="0" y1="0" x2="-18.7946" y2="-35.7286" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517119" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517224" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85517189" path=":/resources/parts/core/wire.fzp">

            <title>Wire2548</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50025" x="1971.02" y="-719.886" x1="0" y1="0" x2="-53.9175" y2="-116.956" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514261" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517259" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <schematicView layer="schematicTrace">

                    <geometry z="6.00259" x="1952.84" y="-719.886" x1="0" y1="0" x2="-35.7356" y2="-116.956" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514261" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517259" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

                <pcbView layer="copper1trace">

                    <geometry z="10.0026" x="1952.84" y="-719.886" x1="0" y1="0" x2="-35.7356" y2="-116.956" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85514261" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85517259" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85517224" path=":/resources/parts/core/wire.fzp">

            <title>Wire2565</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50119" x="2052.38" y="-404.762" x1="0" y1="0" x2="-63.1764" y2="-324.215" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517154" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514988" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <schematicView layer="schematicTrace">

                    <geometry z="6.0026" x="2052.38" y="-404.762" x1="0" y1="0" x2="-63.1764" y2="-324.215" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517154" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514988" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

                <pcbView layer="copper1trace">

                    <geometry z="10.0026" x="2052.38" y="-404.762" x1="0" y1="0" x2="-63.1764" y2="-324.215" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517154" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514988" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

            </views>

        </instance>

        <instance moduleIdRef="WireModuleID" modelIndex="85517259" path=":/resources/parts/core/wire.fzp">

            <title>Wire2582</title>

            <views>

                <breadboardView layer="breadboardWire">

                    <geometry z="3.50025" x="2015.87" y="-396.032" x1="0" y1="0" x2="-44.8503" y2="-323.855" wireFlags="64"/>

                    <wireExtras mils="22.2222" color="#cc1414" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517189" layer="breadboardWire"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="breadboardWire">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514264" layer="breadboardWire"/>

                            </connects>

                        </connector>

                    </connectors>

                </breadboardView>

                <schematicView layer="schematicTrace">

                    <geometry z="6.00261" x="2015.87" y="-396.032" x1="0" y1="0" x2="-44.8503" y2="-323.855" wireFlags="64"/>

                    <wireExtras mils="9.7222" color="#404040" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517189" layer="schematicTrace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="schematicTrace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514264" layer="schematicTrace"/>

                            </connects>

                        </connector>

                    </connectors>

                </schematicView>

                <pcbView layer="copper1trace">

                    <geometry z="10.0026" x="2015.87" y="-396.032" x1="0" y1="0" x2="-44.8503" y2="-323.855" wireFlags="64"/>

                    <wireExtras mils="11.1111" color="#f2c600" opacity="1" banded="0"/>

                    <connectors>

                        <connector connectorId="connector1" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector0" modelIndex="85517189" layer="copper1trace"/>

                            </connects>

                        </connector>

                        <connector connectorId="connector0" layer="copper1trace">

                            <geometry x="0" y="0"/>

                            <connects>

                                <connect connectorId="connector1" modelIndex="85514264" layer="copper1trace"/>

                            </connects>

                        </connector>

                    </connectors>

                </pcbView>

            </views>

        </instance>

    </instances>

</module>

