# A4988 Stepper Motor Driver Carrier.fzpz

Historical source: local-extra-202


## part.0223_0eb44bbb4c4f50c21567b8c79110a3c3_5.fzp

<?xml version='1.0' encoding='UTF-8'?>
<module referenceFile="A4988_Stepper_Motor_Driver_Carrier__3435bf9bd5708b982b93aaee2713f798.fzp" moduleId="0223_0eb44bbb4c4f50c21567b8c79110a3c3_5" fritzingVersion="0.7.7b.08.14.6293">
 <author>Király László</author>
 <title>A4988 Stepper Motor Driver Carrier</title>
 <label>MD09B</label>
 <date>Sun Sep 13 2015</date>
 <tags>
  <tag>Motor Driver</tag>
  <tag>Pololu</tag>
  <tag>MD09B</tag>
  <tag>Stepper</tag>
  <tag>1182</tag>
  <tag>1201</tag>
 </tags>
 <properties>
  <property name="family">Stepper Motor Driver</property>
  <property name="part number"></property>
  <property name="layer"></property>
  <property name="variant">variant 4</property>
 </properties>
 <description>The Pololu stepper motor driver carrier for the A4988 motor driver integrated circuits.
http://www.pololu.com/catalog/product/1182</description>
 <views>
  <breadboardView>
   <layers image="breadboard/0223_4ed19ade2e699853070a13a613764d44_1_breadboard.svg">
    <layer layerId="breadboard"/>
   </layers>
  </breadboardView>
  <iconView>
   <layers image="icon/0223_4ed19ade2e699853070a13a613764d44_1_icon.svg">
    <layer layerId="icon"/>
   </layers>
  </iconView>
  <schematicView>
   <layers image="schematic/0223_4ed19ade2e699853070a13a613764d44_1_schematic.svg">
    <layer layerId="schematic"/>
   </layers>
  </schematicView>
  <pcbView>
   <layers image="pcb/0223_4ed19ade2e699853070a13a613764d44_1_pcb.svg">
    <layer layerId="copper1"/>
    <layer layerId="copper0"/>
   </layers>
  </pcbView>
 </views>
 <connectors>
  <connector type="pad" name="Enable" id="connector130">
   <description>This input turns on or off all of the FET outputs. When set to a logic high, the outputs are disabled. When set to a logic low, the internal control enables the outputs as required. The translator inputs STEP, DIR, and MSx, as well as the internal sequencing logic, all remain active, independent of the ENABLE input state.</description>
   <views>
    <breadboardView>
     <p svgId="connector130" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector130" layer="schematic" terminalId="connector130terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector130" layer="copper0"/>
     <p svgId="connector130" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
  <connector type="pad" name="GROUND" id="connector141">
   <description>Stepper ground.</description>
   <views>
    <breadboardView>
     <p svgId="connector141" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector141" layer="schematic" terminalId="connector141terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector141" layer="copper0"/>
     <p svgId="connector141" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
  <connector type="pad" name="MS1" id="connector131">
   <description>Microstep Resolution Switch 1.</description>
   <views>
    <breadboardView>
     <p svgId="connector131" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector131" layer="schematic" terminalId="connector131terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector131" layer="copper0"/>
     <p svgId="connector131" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
  <connector type="pad" name="OUT 2B" id="connector142">
   <description>Power connections to the stepper.</description>
   <views>
    <breadboardView>
     <p svgId="connector142" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector142" layer="schematic" terminalId="connector142terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector142" layer="copper0"/>
     <p svgId="connector142" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
  <connector type="pad" name="MS2" id="connector132">
   <description>Microstep Resolution Switch 2.</description>
   <views>
    <breadboardView>
     <p svgId="connector132" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector132" layer="schematic" terminalId="connector132terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector132" layer="copper0"/>
     <p svgId="connector132" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
  <connector type="pad" name="OUT 2A" id="connector143">
   <description>Power connections to the stepper.</description>
   <views>
    <breadboardView>
     <p svgId="connector143" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector143" layer="schematic" terminalId="connector143terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector143" layer="copper0"/>
     <p svgId="connector143" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
  <connector type="pad" name="MS3" id="connector133">
   <description>Microstep Resolution Switch 3.</description>
   <views>
    <breadboardView>
     <p svgId="connector133" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector133" layer="schematic" terminalId="connector133terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector133" layer="copper0"/>
     <p svgId="connector133" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
  <connector type="pad" name="OUT 1A" id="connector144">
   <description>Power connections to the stepper.</description>
   <views>
    <breadboardView>
     <p svgId="connector144" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector144" layer="schematic" terminalId="connector144terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector144" layer="copper0"/>
     <p svgId="connector144" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
  <connector type="pad" name="RESET" id="connector134">
   <description>Reset chip.</description>
   <views>
    <breadboardView>
     <p svgId="connector134" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector134" layer="schematic" terminalId="connector134terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector134" layer="copper0"/>
     <p svgId="connector134" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
  <connector type="pad" name="OUT 1B" id="connector145">
   <description>Power connections to the stepper.</description>
   <views>
    <breadboardView>
     <p svgId="connector145" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector145" layer="schematic" terminalId="connector145terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector145" layer="copper0"/>
     <p svgId="connector145" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
  <connector type="pad" name="SLEEP" id="connector135">
   <description>Sleep pin</description>
   <views>
    <breadboardView>
     <p svgId="connector135" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector135" layer="schematic" terminalId="connector135terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector135" layer="copper0"/>
     <p svgId="connector135" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
  <connector type="pad" name="VDD" id="connector146">
   <description>Logic Voltage</description>
   <views>
    <breadboardView>
     <p svgId="connector146" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector146" layer="schematic" terminalId="connector146terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector146" layer="copper0"/>
     <p svgId="connector146" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
  <connector type="pad" name="STEP" id="connector136">
   <description>Stepping impulse.</description>
   <views>
    <breadboardView>
     <p svgId="connector136" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector136" layer="schematic" terminalId="connector136terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector136" layer="copper0"/>
     <p svgId="connector136" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
  <connector type="pad" name="GROUND" id="connector147">
   <description>Logic ground</description>
   <views>
    <breadboardView>
     <p svgId="connector147" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector147" layer="schematic" terminalId="connector147terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector147" layer="copper0"/>
     <p svgId="connector147" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
  <connector type="pad" name="DIR" id="connector137">
   <description>This determines the direction of rotation of the motor. Changes to this input do not take effect  until the next STEP rising edge.</description>
   <views>
    <breadboardView>
     <p svgId="connector137" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector137" layer="schematic" terminalId="connector137terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector137" layer="copper0"/>
     <p svgId="connector137" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
  <connector type="pad" name="VMOT" id="connector140">
   <description>Stepper voltage.</description>
   <views>
    <breadboardView>
     <p svgId="connector140" layer="breadboard"/>
    </breadboardView>
    <schematicView>
     <p svgId="connector140" layer="schematic" terminalId="connector140terminal"/>
    </schematicView>
    <pcbView>
     <p svgId="connector140" layer="copper0"/>
     <p svgId="connector140" layer="copper1"/>
    </pcbView>
   </views>
  </connector>
 </connectors>
</module>


## svg.breadboard.0223_4ed19ade2e699853070a13a613764d44_1_breadboard.svg

<?xml version='1.0' encoding='UTF-8' standalone='no'?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->
<svg xmlns="http://www.w3.org/2000/svg" height="72" width="54"  gorn="0" version="1.1" id="svg3039">
    <desc >
        <referenceFile >A4988 icon.svg</referenceFile>
    </desc>
    <metadata  id="metadata3045">
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <cc:Work xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:cc="http://creativecommons.org/ns#" rdf:about="">
                <dc:format xmlns:dc="http://purl.org/dc/elements/1.1/">image/svg+xml</dc:format>
                <dc:type xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
                <dc:title xmlns:dc="http://purl.org/dc/elements/1.1/"/>
            </cc:Work>
        </rdf:RDF>
    </metadata>
    <defs  id="defs3043"/>
    <g transform="translate(0,-79.004003)" >
        <g >
            <g >
                <g >
                    <g >
                        <g >
                            <g >
                                <g  gorn="0.3.0.0.0.0.0.0.0" style="display:inline" id="layer1">
                                    <rect height="72" width="54"  x="0" y="79" gorn="0.3.0.0.0.0.0.0.0.0" style="fill:#008000" id="rect3134"/>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>
    <g transform="translate(0,-79.004003)" >
        <g >
            <g >
                <g >
                    <g >
                        <g >
                            <g >
                                <g  gorn="0.4.0.0.0.0.0.0.0" style="display:none" id="layer2">
                                    <image height="151" width="114"  x="-0.07853318" y="-0.39528903" href="data:image/png;base64,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 " id="image3131"/>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>
    <g transform="translate(0,-79.004003)" >
        <g >
            <g >
                <g >
                    <g >
                        <g >
                            <g >
                                <g  gorn="0.5.0.0.0.0.0.0.0" id="layer3">
                                    <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,79.393922)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0" style="fill:#000000" id="connector130"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,88.435052)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.1.0.0.0.0.0.0.0" style="fill:#000000" id="connector131"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,97.476182)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.2.0.0.0.0.0.0.0" style="fill:#000000" id="connector132"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,106.51731)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.3.0.0.0.0.0.0.0" style="fill:#000000" id="connector133"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,115.55844)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.4.0.0.0.0.0.0.0" style="fill:#000000" id="connector134"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,124.59957)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.5.0.0.0.0.0.0.0" style="fill:#000000" id="connector135"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,133.6407)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.6.0.0.0.0.0.0.0" style="fill:#000000" id="connector136"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,142.68183)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.7.0.0.0.0.0.0.0" style="fill:#000000" id="connector137"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,142.68183)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.8.0.0.0.0.0.0.0" style="fill:#000000" id="connector147"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,133.6407)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.9.0.0.0.0.0.0.0" style="fill:#000000" id="connector146"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,124.59957)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.10.0.0.0.0.0.0.0" style="fill:#000000" id="connector145"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,115.55844)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.11.0.0.0.0.0.0.0" style="fill:#000000" id="connector144"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,106.51731)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.12.0.0.0.0.0.0.0" style="fill:#000000" id="connector143"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,97.476182)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.13.0.0.0.0.0.0.0" style="fill:#000000" id="connector142"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,88.435052)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.14.0.0.0.0.0.0.0" style="fill:#000000" id="connector141"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,79.393922)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.15.0.0.0.0.0.0.0" style="fill:#000000" id="connector140"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g fill="#000000" xmlns:xml="http://www.w3.org/XML/1998/namespace"  font-size="10" stroke="none" gorn="0.5.0.0.0.0.0.0.0.16" fill-opacity="1" style="font-style:normal;font-weight:normal;line-height:100%;letter-spacing:0px;word-spacing:0px;font-family:Droid Sans" xml:space="preserve" id="text3151"/>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>
    <g transform="translate(0,-79.004003)" >
        <g >
            <g >
                <g >
                    <g >
                        <g >
                            <g >
                                <g  gorn="0.6.0.0.0.0.0.0.0" id="layer5">
                                    <rect height="0.95169789" width="2.3684211"  x="9.9473686" y="105.06897" gorn="0.6.0.0.0.0.0.0.0.0" style="fill:#808080" id="rect3299"/>
                                    <rect height="0.95169789" width="2.3684211"  x="9.9473686" y="106.9809" gorn="0.6.0.0.0.0.0.0.0.1" style="fill:#808080" id="rect3299-1"/>
                                    <rect height="0.95169789" width="2.3684211"  x="9.9473686" y="108.64114" gorn="0.6.0.0.0.0.0.0.0.2" style="fill:#808080" id="rect3299-16"/>
                                    <rect height="0.95169789" width="2.3684211"  x="9.9473686" y="110.39671" gorn="0.6.0.0.0.0.0.0.0.3" style="fill:#808080" id="rect3299-14"/>
                                    <rect height="0.95169789" width="2.3684211"  x="9.9473686" y="112.34039" gorn="0.6.0.0.0.0.0.0.0.4" style="fill:#808080" id="rect3299-9"/>
                                    <rect height="0.95169789" width="2.3684211"  x="9.9473686" y="114.28406" gorn="0.6.0.0.0.0.0.0.0.5" style="fill:#808080" id="rect3299-6"/>
                                    <rect height="0.95169789" width="2.3684211"  x="9.9473686" y="115.91424" gorn="0.6.0.0.0.0.0.0.0.6" style="fill:#808080" id="rect3299-4"/>
                                    <rect height="0.95169789" width="2.3684211"  x="29.368422" y="115.91424" gorn="0.6.0.0.0.0.0.0.0.7" style="fill:#808080" id="rect3299-44"/>
                                    <rect height="0.95169789" width="2.3684211"  x="29.368422" y="114.03326" gorn="0.6.0.0.0.0.0.0.0.8" style="fill:#808080" id="rect3299-10"/>
                                    <rect height="0.95169789" width="2.3684211"  x="29.368422" y="112.15229" gorn="0.6.0.0.0.0.0.0.0.9" style="fill:#808080" id="rect3299-3"/>
                                    <rect height="0.95169789" width="2.3684211"  x="29.368422" y="110.27132" gorn="0.6.0.0.0.0.0.0.0.10" style="fill:#808080" id="rect3299-7"/>
                                    <rect height="0.95169789" width="2.3684211"  x="29.368422" y="108.39034" gorn="0.6.0.0.0.0.0.0.0.11" style="fill:#808080" id="rect3299-43"/>
                                    <rect height="0.95169789" width="2.3684211"  x="29.368422" y="106.50936" gorn="0.6.0.0.0.0.0.0.0.12" style="fill:#808080" id="rect3299-48"/>
                                    <rect height="0.95169789" width="2.3684211"  x="29.368422" y="104.62839" gorn="0.6.0.0.0.0.0.0.0.13" style="fill:#808080" id="rect3299-12"/>
                                    <g transform="matrix(0,0.47584896,-0.47368421,0,45.187654,75.134064)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <g  gorn="0.6.0.0.0.0.0.0.0.14.0.0.0.0.0.0.0" id="g3498">
                                                                    <rect height="2" width="5"  x="53.499126" y="38.99173" gorn="0.6.0.0.0.0.0.0.0.14.0.0.0.0.0.0.0.0" style="fill:#808080" id="rect3299-92"/>
                                                                    <rect height="2" width="5"  x="53.499126" y="43.009682" gorn="0.6.0.0.0.0.0.0.0.14.0.0.0.0.0.0.0.1" style="fill:#808080" id="rect3299-1-2"/>
                                                                    <rect height="2" width="5"  x="53.499126" y="46.498672" gorn="0.6.0.0.0.0.0.0.0.14.0.0.0.0.0.0.0.2" style="fill:#808080" id="rect3299-16-3"/>
                                                                    <rect height="2" width="5"  x="53.499126" y="50.188023" gorn="0.6.0.0.0.0.0.0.0.14.0.0.0.0.0.0.0.3" style="fill:#808080" id="rect3299-14-1"/>
                                                                    <rect height="2" width="5"  x="53.499126" y="54.272671" gorn="0.6.0.0.0.0.0.0.0.14.0.0.0.0.0.0.0.4" style="fill:#808080" id="rect3299-9-3"/>
                                                                    <rect height="2" width="5"  x="53.499126" y="58.357311" gorn="0.6.0.0.0.0.0.0.0.14.0.0.0.0.0.0.0.5" style="fill:#808080" id="rect3299-6-2"/>
                                                                    <rect height="2" width="5"  x="53.499126" y="61.783138" gorn="0.6.0.0.0.0.0.0.0.14.0.0.0.0.0.0.0.6" style="fill:#808080" id="rect3299-4-1"/>
                                                                </g>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="matrix(0,0.47584896,-0.47368421,0,45.250069,93.881101)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <g  gorn="0.6.0.0.0.0.0.0.0.15.0.0.0.0.0.0.0" id="g3498-2">
                                                                    <rect height="2" width="5"  x="53.499126" y="38.99173" gorn="0.6.0.0.0.0.0.0.0.15.0.0.0.0.0.0.0.0" style="fill:#808080" id="rect3299-92-3"/>
                                                                    <rect height="2" width="5"  x="53.499126" y="43.009682" gorn="0.6.0.0.0.0.0.0.0.15.0.0.0.0.0.0.0.1" style="fill:#808080" id="rect3299-1-2-5"/>
                                                                    <rect height="2" width="5"  x="53.499126" y="46.498672" gorn="0.6.0.0.0.0.0.0.0.15.0.0.0.0.0.0.0.2" style="fill:#808080" id="rect3299-16-3-9"/>
                                                                    <rect height="2" width="5"  x="53.499126" y="50.188023" gorn="0.6.0.0.0.0.0.0.0.15.0.0.0.0.0.0.0.3" style="fill:#808080" id="rect3299-14-1-0"/>
                                                                    <rect height="2" width="5"  x="53.499126" y="54.272671" gorn="0.6.0.0.0.0.0.0.0.15.0.0.0.0.0.0.0.4" style="fill:#808080" id="rect3299-9-3-1"/>
                                                                    <rect height="2" width="5"  x="53.499126" y="58.357311" gorn="0.6.0.0.0.0.0.0.0.15.0.0.0.0.0.0.0.5" style="fill:#808080" id="rect3299-6-2-3"/>
                                                                    <rect height="2" width="5"  x="53.499126" y="61.783138" gorn="0.6.0.0.0.0.0.0.0.15.0.0.0.0.0.0.0.6" style="fill:#808080" id="rect3299-4-1-6"/>
                                                                </g>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>
    <g transform="translate(0,-79.004003)" >
        <g >
            <g >
                <g >
                    <g >
                        <g >
                            <g >
                                <g  gorn="0.7.0.0.0.0.0.0.0" style="display:inline" id="layer4">
                                    <rect height="18.088671" width="17.123714"  x="12.533853" y="102.05419" gorn="0.7.0.0.0.0.0.0.0.0" style="fill:#000000" id="rect3278"/>
                                    <rect height="11.349753" width="12.004253"  x="25.420771" y="136.28079" gorn="0.7.0.0.0.0.0.0.0.1" style="fill:#000000" id="rect3546"/>
                                    <rect height="5.8522167" width="12.004253"  x="30.716764" y="83.078819" gorn="0.7.0.0.0.0.0.0.0.2" style="fill:#803300" id="rect3548"/>
                                    <rect height="5.8963547" width="1.6622884"  x="29.127184" y="83.243279" gorn="0.7.0.0.0.0.0.0.0.3" style="fill:#808080" id="rect3552"/>
                                    <rect height="5.8963547" width="1.6622884"  x="41.713341" y="82.968079" gorn="0.7.0.0.0.0.0.0.0.4" style="fill:#808080;display:inline" id="rect3552-7"/>
                                    <g transform="matrix(0.44101633,0,0,0.41021461,5.4542653,90.256166)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <path d="m 69.691357,126.03037 c 0,5.96896 -4.838795,10.80775 -10.807751,10.80775 -5.968956,0 -10.807751,-4.83879 -10.807751,-10.80775 0,-5.96895 4.838795,-10.80775 10.807751,-10.80775 5.968956,0 10.807751,4.8388 10.807751,10.80775 z"  gorn="0.7.0.0.0.0.0.0.0.5.0.0.0.0.0.0.0" style="fill:#b3b3b3" id="path3591"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>
    <g transform="translate(0,-79.004003)" >
        <g >
            <g >
                <g >
                    <g >
                        <g >
                            <g >
                                <g  gorn="0.8.0.0.0.0.0.0.0" style="display:inline" id="layer6">
                                    <g  gorn="0.8.0.0.0.0.0.0.0.0" style="fill:#ffffff" id="g3253">
                                        <g transform="translate(0.6904297,1.863209)" >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <g >
                                                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;display:inline;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3163">
                                                                        <path d="M 9.588,82.928 C 9.5879979,83.042667 9.511998,83.1 9.36,83.1 l -1.468,0 0,-2.668 1.468,0 c 0.151998,3e-6 0.2279979,0.056 0.228,0.168 -2.1e-6,0.114669 -0.076002,0.172002 -0.228,0.172 l -1.128,0 0,0.828 0.456,0 c 0.1519987,1e-6 0.2279986,0.056 0.228,0.168 -1.4e-6,0.114668 -0.076001,0.172001 -0.228,0.172 l -0.456,0 0,0.82 1.128,0 c 0.151998,0 0.2279979,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3094"/>
                                                                        <path d="m 12.064563,83.1 -0.452001,0 -0.904,-2.056 0,1.828 c 0,0.152 -0.056,0.228 -0.167999,0.228 -0.114668,0 -0.172001,-0.076 -0.172001,-0.228 l 0,-2.44 0.452,0 0.904,2.08 0,-1.852 c -1e-6,-0.151997 0.056,-0.227997 0.168001,-0.228 0.114664,3e-6 0.171997,0.076 0.172,0.228 l 0,2.44"  gorn="0.8.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3096"/>
                                                                        <path d="m 14.537125,82.936 c -2e-6,0.04533 -0.01733,0.08533 -0.052,0.12 -0.032,0.032 -0.07067,0.048 -0.116,0.048 -0.08267,0 -0.141335,-0.06 -0.176,-0.18 l -0.12,-0.4 -0.76,0 -0.116,0.4 c -0.03467,0.12 -0.09467,0.18 -0.18,0.18 -0.04533,0 -0.08533,-0.016 -0.12,-0.048 -0.032,-0.03467 -0.048,-0.07467 -0.048,-0.12 0,-0.02667 0.0067,-0.06267 0.02,-0.108 l 0.664,-2.26 c 0.02667,-0.088 0.08133,-0.131997 0.164,-0.132 0.08267,3e-6 0.137332,0.044 0.164,0.132 l 0.656,2.26 c 0.01333,0.04533 0.02,0.08133 0.02,0.108 m -0.56,-0.752 -0.284,-0.964 -0.28,0.964 0.564,0"  gorn="0.8.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3098"/>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                        <g transform="translate(0.71972661,1.6112559)" >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <g >
                                                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3171">
                                                                        <path d="m 9.588,92.372 c -2.1e-6,0.152 -0.057335,0.228 -0.172,0.228 -0.1120018,0 -0.1680017,-0.076 -0.168,-0.228 l 0,-1.968 -0.34,0.484 0,0.032 c -1.4e-6,0.152002 -0.056001,0.228001 -0.168,0.228 -0.1146678,10e-7 -0.1720011,-0.076 -0.172,-0.228 l 0,-0.032 -0.336,-0.484 0,1.968 c -7e-7,0.152 -0.056001,0.228 -0.168,0.228 -0.1146671,0 -0.1720004,-0.076 -0.172,-0.228 l 0,-2.44 0.432,0 0.416,0.604 0.416,-0.604 0.432,0 0,2.44"  gorn="0.8.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3101"/>
                                                                        <path d="m 12.064563,92.216 c -3e-6,0.106667 -0.03867,0.197334 -0.116,0.272 -0.07467,0.07467 -0.166669,0.112 -0.276,0.112 l -0.84,0 c -0.122668,0 -0.230668,-0.04267 -0.324,-0.128 -0.09067,-0.08533 -0.136001,-0.184 -0.136,-0.296 -10e-7,-0.130666 0.05867,-0.195999 0.175999,-0.196 0.09333,10e-7 0.148,0.064 0.164001,0.192 0.008,0.05867 0.044,0.088 0.107999,0.088 l 0.828001,0 c 0.048,0 0.072,-0.01333 0.072,-0.04 -2e-6,-0.01333 -0.012,-0.036 -0.036,-0.068 l -1.228,-1.584 c -0.05867,-0.07466 -0.088,-0.157331 -0.088,-0.248 0,-0.114664 0.03867,-0.207998 0.116,-0.28 0.08,-0.072 0.182666,-0.107997 0.308001,-0.108 l 0.812,0 c 0.119998,3e-6 0.225331,0.04534 0.315999,0.136 0.09333,0.088 0.139998,0.189336 0.140001,0.304 -3e-6,0.130669 -0.056,0.196002 -0.168,0.196 -0.101336,2e-6 -0.158669,-0.064 -0.172,-0.192 -0.008,-0.06933 -0.04934,-0.103998 -0.124,-0.104 l -0.812,0 c -0.048,2e-6 -0.072,0.016 -0.072,0.048 -10e-7,0.016 0.0093,0.036 0.028,0.06 l 1.228001,1.584 c 0.064,0.08267 0.096,0.166667 0.096,0.252"  gorn="0.8.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3103"/>
                                                                        <path d="m 14.545125,92.416 c -2e-6,0.122667 -0.05334,0.184 -0.16,0.184 l -1.308,0 c -0.152,0 -0.228,-0.05733 -0.228,-0.172 0,-0.112 0.076,-0.168 0.228,-0.168 l 0.448,0 0,-1.988 -0.448,0 c -0.152,2e-6 -0.228,-0.05733 -0.228,-0.172 0,-0.111997 0.076,-0.167997 0.228,-0.168 l 0.788,0 0,2.328 0.34,0 0,-0.644 c -2e-6,-0.149332 0.05733,-0.223999 0.172,-0.224 0.111998,10e-7 0.167998,0.07467 0.168,0.224 l 0,0.8"  gorn="0.8.0.0.0.0.0.0.0.0.1.0.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3105"/>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                        <g transform="translate(0.4697266,10.361256)" >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <g >
                                                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.2.0.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3171-7">
                                                                        <path d="m 9.588,92.372 c -2.1e-6,0.152 -0.057335,0.228 -0.172,0.228 -0.1120018,0 -0.1680017,-0.076 -0.168,-0.228 l 0,-1.968 -0.34,0.484 0,0.032 c -1.4e-6,0.152002 -0.056001,0.228001 -0.168,0.228 -0.1146678,10e-7 -0.1720011,-0.076 -0.172,-0.228 l 0,-0.032 -0.336,-0.484 0,1.968 c -7e-7,0.152 -0.056001,0.228 -0.168,0.228 -0.1146671,0 -0.1720004,-0.076 -0.172,-0.228 l 0,-2.44 0.432,0 0.416,0.604 0.416,-0.604 0.432,0 0,2.44"  gorn="0.8.0.0.0.0.0.0.0.0.2.0.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3108"/>
                                                                        <path d="m 12.064563,92.216 c -3e-6,0.106667 -0.03867,0.197334 -0.116,0.272 -0.07467,0.07467 -0.166669,0.112 -0.276,0.112 l -0.84,0 c -0.122668,0 -0.230668,-0.04267 -0.324,-0.128 -0.09067,-0.08533 -0.136001,-0.184 -0.136,-0.296 -10e-7,-0.130666 0.05867,-0.195999 0.175999,-0.196 0.09333,10e-7 0.148,0.064 0.164001,0.192 0.008,0.05867 0.044,0.088 0.107999,0.088 l 0.828001,0 c 0.048,0 0.072,-0.01333 0.072,-0.04 -2e-6,-0.01333 -0.012,-0.036 -0.036,-0.068 l -1.228,-1.584 c -0.05867,-0.07466 -0.088,-0.157331 -0.088,-0.248 0,-0.114664 0.03867,-0.207998 0.116,-0.28 0.08,-0.072 0.182666,-0.107997 0.308001,-0.108 l 0.812,0 c 0.119998,3e-6 0.225331,0.04534 0.315999,0.136 0.09333,0.088 0.139998,0.189336 0.140001,0.304 -3e-6,0.130669 -0.056,0.196002 -0.168,0.196 -0.101336,2e-6 -0.158669,-0.064 -0.172,-0.192 -0.008,-0.06933 -0.04934,-0.103998 -0.124,-0.104 l -0.812,0 c -0.048,2e-6 -0.072,0.016 -0.072,0.048 -10e-7,0.016 0.0093,0.036 0.028,0.06 l 1.228001,1.584 c 0.064,0.08267 0.096,0.166667 0.096,0.252"  gorn="0.8.0.0.0.0.0.0.0.0.2.0.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3110"/>
                                                                        <path d="m 14.541125,92.428 c -2e-6,0.114667 -0.076,0.172 -0.228,0.172 l -1.468,0 0,-1.16 c 0,-0.09866 0.032,-0.179999 0.096,-0.244 0.06667,-0.06667 0.149333,-0.1 0.248,-0.1 l 1.008,0 0,-0.824 -1.124,0 c -0.152,2e-6 -0.228,-0.05733 -0.228,-0.172 0,-0.111997 0.076,-0.167997 0.228,-0.168 l 1.124,0 c 0.09867,3e-6 0.179998,0.03467 0.244,0.104 0.06667,0.06667 0.1,0.150669 0.1,0.252 l 0,0.808 c -2e-6,0.09867 -0.03333,0.181335 -0.1,0.248 -0.064,0.064 -0.145335,0.096 -0.244,0.096 l -1.008,0 0,0.82 1.124,0 c 0.151998,0 0.227998,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.0.2.0.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3112"/>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                        <g transform="translate(0.2197266,19.361256)" >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <g >
                                                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.3.0.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3171-6">
                                                                        <path d="m 9.588,92.372 c -2.1e-6,0.152 -0.057335,0.228 -0.172,0.228 -0.1120018,0 -0.1680017,-0.076 -0.168,-0.228 l 0,-1.968 -0.34,0.484 0,0.032 c -1.4e-6,0.152002 -0.056001,0.228001 -0.168,0.228 -0.1146678,10e-7 -0.1720011,-0.076 -0.172,-0.228 l 0,-0.032 -0.336,-0.484 0,1.968 c -7e-7,0.152 -0.056001,0.228 -0.168,0.228 -0.1146671,0 -0.1720004,-0.076 -0.172,-0.228 l 0,-2.44 0.432,0 0.416,0.604 0.416,-0.604 0.432,0 0,2.44"  gorn="0.8.0.0.0.0.0.0.0.0.3.0.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3115"/>
                                                                        <path d="m 12.064563,92.216 c -3e-6,0.106667 -0.03867,0.197334 -0.116,0.272 -0.07467,0.07467 -0.166669,0.112 -0.276,0.112 l -0.84,0 c -0.122668,0 -0.230668,-0.04267 -0.324,-0.128 -0.09067,-0.08533 -0.136001,-0.184 -0.136,-0.296 -10e-7,-0.130666 0.05867,-0.195999 0.175999,-0.196 0.09333,10e-7 0.148,0.064 0.164001,0.192 0.008,0.05867 0.044,0.088 0.107999,0.088 l 0.828001,0 c 0.048,0 0.072,-0.01333 0.072,-0.04 -2e-6,-0.01333 -0.012,-0.036 -0.036,-0.068 l -1.228,-1.584 c -0.05867,-0.07466 -0.088,-0.157331 -0.088,-0.248 0,-0.114664 0.03867,-0.207998 0.116,-0.28 0.08,-0.072 0.182666,-0.107997 0.308001,-0.108 l 0.812,0 c 0.119998,3e-6 0.225331,0.04534 0.315999,0.136 0.09333,0.088 0.139998,0.189336 0.140001,0.304 -3e-6,0.130669 -0.056,0.196002 -0.168,0.196 -0.101336,2e-6 -0.158669,-0.064 -0.172,-0.192 -0.008,-0.06933 -0.04934,-0.103998 -0.124,-0.104 l -0.812,0 c -0.048,2e-6 -0.072,0.016 -0.072,0.048 -10e-7,0.016 0.0093,0.036 0.028,0.06 l 1.228001,1.584 c 0.064,0.08267 0.096,0.166667 0.096,0.252"  gorn="0.8.0.0.0.0.0.0.0.0.3.0.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3117"/>
                                                                        <path d="m 14.537125,92.26 c -2e-6,0.096 -0.03333,0.177333 -0.1,0.244 -0.06667,0.064 -0.148002,0.096 -0.244,0.096 l -1.124,0 c -0.152,0 -0.228,-0.05733 -0.228,-0.172 0,-0.112 0.076,-0.168 0.228,-0.168 l 1.124,0 0,-0.616 c -2e-6,-0.135999 -0.06133,-0.203999 -0.184,-0.204 l -0.6,0 c -0.152001,10e-7 -0.228001,-0.056 -0.228,-0.168 -10e-7,-0.114665 0.076,-0.171999 0.228,-0.172 l 0.604,0 c 0.114665,1e-6 0.171998,-0.07066 0.172,-0.212 l 0,-0.616 -1.116,0 c -0.152,2e-6 -0.228,-0.05733 -0.228,-0.172 0,-0.111997 0.076,-0.167997 0.228,-0.168 l 1.124,0 c 0.09066,3e-6 0.169331,0.02934 0.236,0.088 0.06666,0.05867 0.1,0.128002 0.1,0.208 l 0,0.744 c -2e-6,0.114668 -0.04267,0.213335 -0.128,0.296 0.09066,0.09867 0.135998,0.214668 0.136,0.348 l 0,0.644"  gorn="0.8.0.0.0.0.0.0.0.0.3.0.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3119"/>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                        <g transform="translate(0.2197266,28.611256)" >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <g >
                                                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.4.0.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3171-0">
                                                                        <path d="m 9.592,92.436 c -2.1e-6,0.04267 -0.017335,0.08133 -0.052,0.116 -0.034669,0.032 -0.074669,0.048 -0.12,0.048 -0.061335,0 -0.1186685,-0.03867 -0.172,-0.116 l -0.932,-1.332 -0.08,0 0,1.22 c -7e-7,0.152 -0.056001,0.228 -0.168,0.228 -0.1146671,0 -0.1720004,-0.06267 -0.172,-0.188 l 0,-2.48 1.192,0 c 0.1413316,3e-6 0.2599982,0.052 0.356,0.156 0.098665,0.104002 0.1479979,0.230669 0.148,0.38 l 0,0.152 c -2.1e-6,0.157335 -0.050669,0.285335 -0.152,0.384 -0.098668,0.09867 -0.2266684,0.148001 -0.384,0.148 l -0.324,0 0.796,1.14 c 0.042665,0.06133 0.063998,0.109334 0.064,0.144 m -0.34,-1.816 0,-0.132 c -1.8e-6,-0.143998 -0.070668,-0.215998 -0.212,-0.216 l -0.804,0 0,0.54 0.804,0 c 0.1413317,2e-6 0.2119982,-0.064 0.212,-0.192"  gorn="0.8.0.0.0.0.0.0.0.0.4.0.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3122"/>
                                                                        <path d="m 12.064563,92.428 c -3e-6,0.114667 -0.076,0.172 -0.228001,0.172 l -1.468,0 0,-2.668 1.468,0 c 0.151998,3e-6 0.227998,0.056 0.228001,0.168 -3e-6,0.114669 -0.076,0.172002 -0.228001,0.172 l -1.128,0 0,0.828 0.456001,0 c 0.151998,1e-6 0.227998,0.056 0.228,0.168 -2e-6,0.114668 -0.076,0.172001 -0.228,0.172 l -0.456001,0 0,0.82 1.128,0 c 0.151998,0 0.227998,0.056 0.228001,0.168"  gorn="0.8.0.0.0.0.0.0.0.0.4.0.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3124"/>
                                                                        <path d="m 14.541125,92.216 c -2e-6,0.106667 -0.03867,0.197334 -0.116,0.272 -0.07467,0.07467 -0.166668,0.112 -0.276,0.112 l -0.84,0 c -0.122667,0 -0.230667,-0.04267 -0.324,-0.128 -0.09067,-0.08533 -0.136,-0.184 -0.136,-0.296 0,-0.130666 0.05867,-0.195999 0.176,-0.196 0.09333,10e-7 0.147999,0.064 0.164,0.192 0.008,0.05867 0.044,0.088 0.108,0.088 l 0.828,0 c 0.048,0 0.072,-0.01333 0.072,-0.04 -2e-6,-0.01333 -0.012,-0.036 -0.036,-0.068 l -1.228,-1.584 c -0.05867,-0.07466 -0.088,-0.157331 -0.088,-0.248 0,-0.114664 0.03867,-0.207998 0.116,-0.28 0.08,-0.072 0.182666,-0.107997 0.308,-0.108 l 0.812,0 c 0.119998,3e-6 0.225331,0.04534 0.316,0.136 0.09333,0.088 0.139998,0.189336 0.14,0.304 -2e-6,0.130669 -0.056,0.196002 -0.168,0.196 -0.101335,2e-6 -0.158668,-0.064 -0.172,-0.192 -0.008,-0.06933 -0.04933,-0.103998 -0.124,-0.104 l -0.812,0 c -0.048,2e-6 -0.072,0.016 -0.072,0.048 -1e-6,0.016 0.0093,0.036 0.028,0.06 l 1.228,1.584 c 0.064,0.08267 0.096,0.166667 0.096,0.252"  gorn="0.8.0.0.0.0.0.0.0.0.4.0.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3126"/>
                                                                        <path d="m 17.017687,92.428 c -2e-6,0.114667 -0.076,0.172 -0.228,0.172 l -1.468,0 0,-2.668 1.468,0 c 0.151998,3e-6 0.227998,0.056 0.228,0.168 -2e-6,0.114669 -0.076,0.172002 -0.228,0.172 l -1.128,0 0,0.828 0.456,0 c 0.151999,1e-6 0.227999,0.056 0.228,0.168 -1e-6,0.114668 -0.076,0.172001 -0.228,0.172 l -0.456,0 0,0.82 1.128,0 c 0.151998,0 0.227998,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.0.4.0.0.0.0.0.0.0.3" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3128"/>
                                                                        <path d="m 19.49425,90.376 c -2e-6,0.125335 -0.056,0.188002 -0.168,0.188 -0.114668,2e-6 -0.172002,-0.076 -0.172,-0.228 l 0,-0.064 -0.34,0 0,2.136 c -1e-6,0.125333 -0.056,0.188 -0.168,0.188 -0.114668,0 -0.172001,-0.076 -0.172,-0.228 l 0,-2.096 -0.336,0 0,0.068 c -1e-6,0.149335 -0.056,0.224002 -0.168,0.224 -0.114667,2e-6 -0.172,-0.07466 -0.172,-0.224 l 0,-0.408 1.696,0 0,0.444"  gorn="0.8.0.0.0.0.0.0.0.0.4.0.0.0.0.0.0.0.4" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3130"/>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                        <g transform="translate(0.21972658,37.611256)" >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <g >
                                                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.5.0.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3171-71">
                                                                        <path d="m 9.588,92.216 c -2.1e-6,0.106667 -0.038669,0.197334 -0.116,0.272 -0.074669,0.07467 -0.1666685,0.112 -0.276,0.112 l -0.84,0 c -0.1226674,0 -0.2306673,-0.04267 -0.324,-0.128 -0.090667,-0.08533 -0.1360004,-0.184 -0.136,-0.296 -4e-7,-0.130666 0.058666,-0.195999 0.176,-0.196 0.093333,10e-7 0.1479993,0.064 0.164,0.192 0.008,0.05867 0.043999,0.088 0.108,0.088 l 0.828,0 c 0.047998,0 0.071998,-0.01333 0.072,-0.04 -1.7e-6,-0.01333 -0.012002,-0.036 -0.036,-0.068 L 7.98,90.568 c -0.058667,-0.07466 -0.088,-0.157331 -0.088,-0.248 -4e-7,-0.114664 0.038666,-0.207998 0.116,-0.28 0.079999,-0.072 0.182666,-0.107997 0.308,-0.108 l 0.812,0 c 0.1199983,3e-6 0.2253315,0.04534 0.316,0.136 0.093331,0.088 0.1399979,0.189336 0.14,0.304 -2.1e-6,0.130669 -0.056002,0.196002 -0.168,0.196 -0.1013351,2e-6 -0.1586684,-0.064 -0.172,-0.192 -0.008,-0.06933 -0.049335,-0.103998 -0.124,-0.104 l -0.812,0 c -0.048001,2e-6 -0.072001,0.016 -0.072,0.048 -7e-7,0.016 0.00933,0.036 0.028,0.06 l 1.228,1.584 c 0.063998,0.08267 0.095998,0.166667 0.096,0.252"  gorn="0.8.0.0.0.0.0.0.0.0.5.0.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3133"/>
                                                                        <path d="m 12.060563,92.428 c -3e-6,0.114667 -0.076,0.172 -0.228,0.172 l -1.46,0 0,-2.436 c -10e-7,-0.151997 0.056,-0.227997 0.168,-0.228 0.114665,3e-6 0.171999,0.076 0.172,0.228 l 0,2.096 1.12,0 c 0.151997,0 0.227997,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.0.5.0.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3135"/>
                                                                        <path d="m 14.541125,92.428 c -2e-6,0.114667 -0.076,0.172 -0.228,0.172 l -1.468,0 0,-2.668 1.468,0 c 0.151998,3e-6 0.227998,0.056 0.228,0.168 -2e-6,0.114669 -0.076,0.172002 -0.228,0.172 l -1.128,0 0,0.828 0.456,0 c 0.151999,1e-6 0.227999,0.056 0.228,0.168 -1e-6,0.114668 -0.076,0.172001 -0.228,0.172 l -0.456,0 0,0.82 1.128,0 c 0.151998,0 0.227998,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.0.5.0.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3137"/>
                                                                        <path d="m 17.017687,92.428 c -2e-6,0.114667 -0.076,0.172 -0.228,0.172 l -1.468,0 0,-2.668 1.468,0 c 0.151998,3e-6 0.227998,0.056 0.228,0.168 -2e-6,0.114669 -0.076,0.172002 -0.228,0.172 l -1.128,0 0,0.828 0.456,0 c 0.151999,1e-6 0.227999,0.056 0.228,0.168 -1e-6,0.114668 -0.076,0.172001 -0.228,0.172 l -0.456,0 0,0.82 1.128,0 c 0.151998,0 0.227998,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.0.5.0.0.0.0.0.0.0.3" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3139"/>
                                                                        <path d="m 19.49825,91.028 c -2e-6,0.176001 -0.04933,0.313335 -0.148,0.412 -0.09867,0.09867 -0.236002,0.148001 -0.412,0.148 l -0.8,0 0,0.784 c -1e-6,0.149333 -0.056,0.224 -0.168,0.224 -0.05067,0 -0.092,-0.016 -0.124,-0.048 -0.032,-0.03467 -0.048,-0.07867 -0.048,-0.132 l 0,-2.484 1.184,0 c 0.154665,3e-6 0.278665,0.04934 0.372,0.148 0.096,0.09867 0.143998,0.230669 0.144,0.396 l 0,0.552 m -0.34,0 0,-0.552 c -2e-6,-0.135998 -0.06933,-0.203998 -0.208,-0.204 l -0.812,0 0,0.976 0.824,0 c 0.130665,10e-7 0.195998,-0.07333 0.196,-0.22"  gorn="0.8.0.0.0.0.0.0.0.0.5.0.0.0.0.0.0.0.4" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3141"/>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                        <g transform="translate(0.31640627,46.611256)" >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <g >
                                                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.6.0.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3171-71-9">
                                                                        <path d="m 9.588,92.216 c -2.1e-6,0.106667 -0.038669,0.197334 -0.116,0.272 -0.074669,0.07467 -0.1666685,0.112 -0.276,0.112 l -0.84,0 c -0.1226674,0 -0.2306673,-0.04267 -0.324,-0.128 -0.090667,-0.08533 -0.1360004,-0.184 -0.136,-0.296 -4e-7,-0.130666 0.058666,-0.195999 0.176,-0.196 0.093333,10e-7 0.1479993,0.064 0.164,0.192 0.008,0.05867 0.043999,0.088 0.108,0.088 l 0.828,0 c 0.047998,0 0.071998,-0.01333 0.072,-0.04 -1.7e-6,-0.01333 -0.012002,-0.036 -0.036,-0.068 L 7.98,90.568 c -0.058667,-0.07466 -0.088,-0.157331 -0.088,-0.248 -4e-7,-0.114664 0.038666,-0.207998 0.116,-0.28 0.079999,-0.072 0.182666,-0.107997 0.308,-0.108 l 0.812,0 c 0.1199983,3e-6 0.2253315,0.04534 0.316,0.136 0.093331,0.088 0.1399979,0.189336 0.14,0.304 -2.1e-6,0.130669 -0.056002,0.196002 -0.168,0.196 -0.1013351,2e-6 -0.1586684,-0.064 -0.172,-0.192 -0.008,-0.06933 -0.049335,-0.103998 -0.124,-0.104 l -0.812,0 c -0.048001,2e-6 -0.072001,0.016 -0.072,0.048 -7e-7,0.016 0.00933,0.036 0.028,0.06 l 1.228,1.584 c 0.063998,0.08267 0.095998,0.166667 0.096,0.252"  gorn="0.8.0.0.0.0.0.0.0.0.6.0.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3144"/>
                                                                        <path d="m 12.064563,90.376 c -3e-6,0.125335 -0.056,0.188002 -0.168,0.188 -0.114669,2e-6 -0.172002,-0.076 -0.172001,-0.228 l 0,-0.064 -0.34,0 0,2.136 c -1e-6,0.125333 -0.056,0.188 -0.167999,0.188 -0.114668,0 -0.172002,-0.076 -0.172,-0.228 l 0,-2.096 -0.336001,0 0,0.068 c 0,0.149335 -0.056,0.224002 -0.167999,0.224 -0.114668,2e-6 -0.172001,-0.07466 -0.172001,-0.224 l 0,-0.408 1.696001,0 0,0.444"  gorn="0.8.0.0.0.0.0.0.0.0.6.0.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3146"/>
                                                                        <path d="m 14.541125,92.428 c -2e-6,0.114667 -0.076,0.172 -0.228,0.172 l -1.468,0 0,-2.668 1.468,0 c 0.151998,3e-6 0.227998,0.056 0.228,0.168 -2e-6,0.114669 -0.076,0.172002 -0.228,0.172 l -1.128,0 0,0.828 0.456,0 c 0.151999,1e-6 0.227999,0.056 0.228,0.168 -1e-6,0.114668 -0.076,0.172001 -0.228,0.172 l -0.456,0 0,0.82 1.128,0 c 0.151998,0 0.227998,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.0.6.0.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3148"/>
                                                                        <path d="m 17.021687,91.028 c -2e-6,0.176001 -0.04933,0.313335 -0.148,0.412 -0.09867,0.09867 -0.236001,0.148001 -0.412,0.148 l -0.8,0 0,0.784 c 0,0.149333 -0.056,0.224 -0.167999,0.224 -0.05067,0 -0.092,-0.016 -0.124,-0.048 -0.032,-0.03467 -0.048,-0.07867 -0.048,-0.132 l 0,-2.484 1.184,0 c 0.154665,3e-6 0.278665,0.04934 0.372,0.148 0.096,0.09867 0.143998,0.230669 0.144,0.396 l 0,0.552 m -0.34,0 0,-0.552 c -1e-6,-0.135998 -0.06933,-0.203998 -0.208,-0.204 l -0.812,0 0,0.976 0.824,0 c 0.130665,10e-7 0.195999,-0.07333 0.196,-0.22"  gorn="0.8.0.0.0.0.0.0.0.0.6.0.0.0.0.0.0.0.3" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3150"/>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                        <g transform="translate(0.3164063,55.111256)" >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g >
                                                                <g >
                                                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.7.0.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3171-71-4">
                                                                        <path d="m 9.584,91.256 c -2.1e-6,0.133335 -0.026669,0.253334 -0.08,0.36 l -0.348,0.7 C 9.0626651,92.505333 8.9013319,92.6 8.672,92.6 l -0.556,0 c -0.1520005,0 -0.2280004,-0.05733 -0.228,-0.172 -4e-7,-0.112 0.075999,-0.168 0.228,-0.168 l 0.112,0 0,-1.988 -0.112,0 c -0.1520005,2e-6 -0.2280004,-0.05733 -0.228,-0.172 -4e-7,-0.111997 0.075999,-0.167997 0.228,-0.168 l 0.588,0 c 0.2079986,3e-6 0.3613318,0.100003 0.46,0.3 L 9.5,90.916 c 0.055998,0.114668 0.083998,0.228001 0.084,0.34 m -0.34,0.012 c -1.7e-6,-0.064 -0.022668,-0.141332 -0.068,-0.232 L 8.852,90.38 c -0.034668,-0.072 -0.093335,-0.107998 -0.176,-0.108 l -0.108,0 0,1.988 0.116,0 c 0.082665,0 0.141332,-0.036 0.176,-0.108 l 0.336,-0.688 c 0.031998,-0.06667 0.047998,-0.131999 0.048,-0.196"  gorn="0.8.0.0.0.0.0.0.0.0.7.0.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3153"/>
                                                                        <path d="m 12.064563,92.428 c -3e-6,0.114667 -0.076,0.172 -0.228001,0.172 l -1.231999,0 c -0.152001,0 -0.228001,-0.05733 -0.228,-0.172 -1e-6,-0.112 0.076,-0.168 0.228,-0.168 l 0.443999,0 0,-1.988 -0.452,0 c -0.152,2e-6 -0.228,-0.05733 -0.228,-0.172 0,-0.111997 0.076,-0.167997 0.228,-0.168 l 1.24,0 c 0.151998,3e-6 0.227998,0.056 0.228001,0.168 -3e-6,0.114669 -0.076,0.172002 -0.228001,0.172 l -0.448,0 0,1.988 0.448,0 c 0.151998,0 0.227998,0.056 0.228001,0.168"  gorn="0.8.0.0.0.0.0.0.0.0.7.0.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3155"/>
                                                                        <path d="m 14.545125,92.436 c -2e-6,0.04267 -0.01734,0.08133 -0.052,0.116 -0.03467,0.032 -0.07467,0.048 -0.12,0.048 -0.06133,0 -0.118668,-0.03867 -0.172,-0.116 l -0.932,-1.332 -0.08,0 0,1.22 c -1e-6,0.152 -0.056,0.228 -0.168,0.228 -0.114667,0 -0.172,-0.06267 -0.172,-0.188 l 0,-2.48 1.192,0 c 0.141332,3e-6 0.259998,0.052 0.356,0.156 0.09866,0.104002 0.147998,0.230669 0.148,0.38 l 0,0.152 c -2e-6,0.157335 -0.05067,0.285335 -0.152,0.384 -0.09867,0.09867 -0.226668,0.148001 -0.384,0.148 l -0.324,0 0.796,1.14 c 0.04266,0.06133 0.064,0.109334 0.064,0.144 m -0.34,-1.816 0,-0.132 c -2e-6,-0.143998 -0.07067,-0.215998 -0.212,-0.216 l -0.804,0 0,0.54 0.804,0 c 0.141332,2e-6 0.211998,-0.064 0.212,-0.192"  gorn="0.8.0.0.0.0.0.0.0.0.7.0.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3157"/>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                        <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.8" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3409">
                                            <path d="m 37.338,82.778 c -2e-6,0.05867 -0.01067,0.116002 -0.032,0.172 l -0.652,1.688 c -0.02934,0.07467 -0.08267,0.112 -0.16,0.112 -0.08,0 -0.134668,-0.03733 -0.164,-0.112 L 35.674,82.95 c -0.008,-0.016 -0.012,-0.028 -0.012,-0.036 -0.01333,-0.032 -0.02,-0.07733 -0.02,-0.136 l 0,-0.468 c 0,-0.151997 0.05733,-0.227997 0.172,-0.228 0.111999,3e-6 0.167999,0.076 0.168,0.228 l 0,0.492 0.508,1.308 0.508,-1.308 0,-0.496 c -2e-6,-0.149331 0.05733,-0.223997 0.172,-0.224 0.111998,3e-6 0.167998,0.07467 0.168,0.224 l 0,0.472"  gorn="0.8.0.0.0.0.0.0.0.0.8.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3160"/>
                                            <path d="m 39.814562,84.522 c -2e-6,0.152 -0.05734,0.228 -0.172,0.228 -0.112001,0 -0.168001,-0.076 -0.168,-0.228 l 0,-1.968 -0.34,0.484 0,0.032 c -1e-6,0.152002 -0.056,0.228001 -0.167999,0.228 -0.114668,10e-7 -0.172002,-0.076 -0.172001,-0.228 l 0,-0.032 -0.336,-0.484 0,1.968 c 0,0.152 -0.056,0.228 -0.168,0.228 -0.114667,0 -0.172,-0.076 -0.171999,-0.228 l 0,-2.44 0.431999,0 0.416001,0.604 0.415999,-0.604 0.432,0 0,2.44"  gorn="0.8.0.0.0.0.0.0.0.0.8.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3162"/>
                                            <path d="m 42.291125,83.418 c -2e-6,0.122668 -0.032,0.248001 -0.096,0.376 l -0.352,0.708 c -0.03467,0.072 -0.08933,0.132 -0.164,0.18 -0.07467,0.04533 -0.152001,0.068 -0.232,0.068 -0.184001,0 -0.320001,-0.08667 -0.408,-0.26 l -0.356,-0.708 c -0.05867,-0.117332 -0.088,-0.239999 -0.088,-0.368 0,-0.119999 0.02533,-0.230665 0.076,-0.332 l 0.368,-0.744 c 0.08533,-0.170664 0.222666,-0.255997 0.412,-0.256 0.07733,3e-6 0.151999,0.02267 0.224,0.068 0.07466,0.04534 0.129332,0.102669 0.164,0.172 l 0.38,0.76 c 0.048,0.096 0.072,0.208001 0.072,0.336 m -0.34,-0.004 c -2e-6,-0.06933 -0.02134,-0.146665 -0.064,-0.232 l -0.348,-0.696 c -0.01867,-0.04 -0.05067,-0.06 -0.096,-0.06 -0.048,2e-6 -0.08133,0.02 -0.1,0.06 l -0.34,0.684 c -0.04533,0.09067 -0.068,0.173335 -0.068,0.248 -10e-7,0.06667 0.02267,0.146668 0.068,0.24 l 0.332,0.668 c 0.02667,0.05333 0.064,0.08 0.112,0.08 0.04,0 0.072,-0.02267 0.096,-0.068 l 0.364,-0.724 c 0.02933,-0.05867 0.044,-0.125332 0.044,-0.2"  gorn="0.8.0.0.0.0.0.0.0.0.8.2" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3164"/>
                                            <path d="m 44.767687,82.526 c -2e-6,0.125335 -0.056,0.188002 -0.167999,0.188 -0.114669,2e-6 -0.172002,-0.076 -0.172001,-0.228 l 0,-0.064 -0.34,0 0,2.136 c -1e-6,0.125333 -0.056,0.188 -0.167999,0.188 -0.114668,0 -0.172002,-0.076 -0.172001,-0.228 l 0,-2.096 -0.336,0 0,0.068 c 0,0.149335 -0.056,0.224002 -0.168,0.224 -0.114667,2e-6 -0.172,-0.07466 -0.171999,-0.224 l 0,-0.408 1.695999,0 0,0.444"  gorn="0.8.0.0.0.0.0.0.0.0.8.3" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3166"/>
                                        </g>
                                        <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.9" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3409-8">
                                            <path d="m 39.680867,93.710055 c -2e-6,0.133333 -0.05067,0.249333 -0.152,0.348 -0.101335,0.09867 -0.220002,0.148 -0.356,0.148 l -0.676,0 c -0.146667,0 -0.269334,-0.04933 -0.368,-0.148 -0.096,-0.09867 -0.144,-0.221333 -0.144,-0.368 l 0,-0.94 c 0,-0.151999 0.052,-0.294665 0.156,-0.428 l 0.452,-0.584 c 0.103999,-0.133331 0.242666,-0.199998 0.416,-0.2 l 0.44,0 c 0.151998,2e-6 0.227998,0.056 0.228,0.168 -2e-6,0.114669 -0.076,0.172002 -0.228,0.172 l -0.396,0 c -0.06667,2e-6 -0.110668,0.0053 -0.132,0.016 -0.01867,0.008 -0.048,0.03867 -0.088,0.092 l -0.424,0.548 c -0.056,0.072 -0.084,0.158668 -0.084,0.26 l 0,0.868 c -10e-7,0.136 0.06667,0.204 0.2,0.204 l 0.628,0 c 0.125332,0 0.187998,-0.068 0.188,-0.204 l 0,-0.324 -0.284,0 c -0.152001,10e-7 -0.228001,-0.056 -0.228,-0.168 -1e-6,-0.114666 0.076,-0.171999 0.228,-0.172 l 0.624,0 0,0.712"  gorn="0.8.0.0.0.0.0.0.0.0.9.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3169"/>
                                            <path d="m 42.15343,94.206055 -0.452,0 -0.904,-2.056 0,1.828 c -10e-7,0.152 -0.056,0.228 -0.168,0.228 -0.114667,0 -0.172001,-0.076 -0.172,-0.228 l 0,-2.44 0.452,0 0.904,2.08 0,-1.852 c -2e-6,-0.151998 0.056,-0.227998 0.168,-0.228 0.114664,2e-6 0.171998,0.076 0.172,0.228 l 0,2.44"  gorn="0.8.0.0.0.0.0.0.0.0.9.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3171"/>
                                            <path d="m 44.625992,92.862055 c -2e-6,0.133334 -0.02667,0.253334 -0.08,0.36 l -0.348,0.7 c -0.09333,0.189333 -0.254668,0.284 -0.484,0.284 l -0.556,0 c -0.152,0 -0.228,-0.05733 -0.228,-0.172 0,-0.112 0.076,-0.168 0.228,-0.168 l 0.112,0 0,-1.988 -0.112,0 c -0.152,2e-6 -0.228,-0.05733 -0.228,-0.172 0,-0.111998 0.076,-0.167998 0.228,-0.168 l 0.588,0 c 0.207999,2e-6 0.361332,0.100002 0.46,0.3 l 0.336,0.684 c 0.056,0.114668 0.084,0.228001 0.084,0.34 m -0.34,0.012 c -2e-6,-0.064 -0.02267,-0.141332 -0.068,-0.232 l -0.324,-0.656 c -0.03467,-0.072 -0.09333,-0.107998 -0.176,-0.108 l -0.108,0 0,1.988 0.116,0 c 0.08267,0 0.141332,-0.036 0.176,-0.108 l 0.336,-0.688 c 0.032,-0.06667 0.048,-0.131999 0.048,-0.196"  gorn="0.8.0.0.0.0.0.0.0.0.9.2" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3173"/>
                                        </g>
                                        <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.10" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3409-3">
                                            <path d="m 43.176867,102.53405 c -2e-6,0.11466 -0.076,0.172 -0.228,0.172 l -1.468,0 0,-1.16 c 0,-0.0987 0.032,-0.18 0.096,-0.244 0.06667,-0.0667 0.149333,-0.1 0.248,-0.1 l 1.008,0 0,-0.824 -1.124,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.112 0.076,-0.168 0.228,-0.168 l 1.124,0 c 0.09866,0 0.179998,0.0347 0.244,0.104 0.06667,0.0667 0.1,0.15067 0.1,0.252 l 0,0.808 c -2e-6,0.0987 -0.03334,0.18133 -0.1,0.248 -0.064,0.064 -0.145335,0.096 -0.244,0.096 l -1.008,0 0,0.82 1.124,0 c 0.151998,0 0.227998,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.0.10.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3176"/>
                                            <path d="m 45.65743,101.99405 c -2e-6,0.208 -0.06534,0.37866 -0.196,0.512 -0.130669,0.13333 -0.297335,0.2 -0.5,0.2 l -1,0 0,-2.668 1.016,0 c 0.205331,0 0.369331,0.0693 0.492,0.208 0.125331,0.13867 0.187998,0.32133 0.188,0.548 -2e-6,0.25333 -0.076,0.448 -0.228,0.584 0.088,0.0853 0.147998,0.17066 0.18,0.256 0.032,0.0853 0.048,0.20533 0.048,0.36 m -0.34,-1.212 c -2e-6,-0.26933 -0.124002,-0.404 -0.372,-0.404 l -0.644,0 0,0.828 0.648,0 c 0.245331,0 0.367998,-0.14133 0.368,-0.424 m 0,1.172 c -2e-6,-0.272 -0.125335,-0.408 -0.376,-0.408 l -0.64,0 0,0.82 0.648,0 c 0.245331,0 0.367998,-0.13734 0.368,-0.412"  gorn="0.8.0.0.0.0.0.0.0.0.10.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3178"/>
                                        </g>
                                        <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.11" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3409-3-2">
                                            <path d="m 42.937609,111.81238 c -2e-6,0.11467 -0.076,0.172 -0.228,0.172 l -1.468,0 0,-1.16 c 0,-0.0987 0.032,-0.18 0.096,-0.244 0.06667,-0.0667 0.149333,-0.1 0.248,-0.1 l 1.008,0 0,-0.824 -1.124,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.11199 0.076,-0.16799 0.228,-0.168 l 1.124,0 c 0.09866,1e-5 0.179998,0.0347 0.244,0.104 0.06667,0.0667 0.1,0.15067 0.1,0.252 l 0,0.808 c -2e-6,0.0987 -0.03334,0.18134 -0.1,0.248 -0.064,0.064 -0.145335,0.096 -0.244,0.096 l -1.008,0 0,0.82 1.124,0 c 0.151998,0 0.227998,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.0.11.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3181"/>
                                            <path d="m 45.410172,111.82038 c -2e-6,0.0453 -0.01734,0.0853 -0.052,0.12 -0.032,0.032 -0.07067,0.048 -0.116,0.048 -0.08267,0 -0.141335,-0.06 -0.176,-0.18 l -0.12,-0.4 -0.76,0 -0.116,0.4 c -0.03467,0.12 -0.09467,0.18 -0.18,0.18 -0.04533,0 -0.08533,-0.016 -0.12,-0.048 -0.032,-0.0347 -0.048,-0.0747 -0.048,-0.12 -10e-7,-0.0267 0.0067,-0.0627 0.02,-0.108 l 0.664,-2.26 c 0.02667,-0.088 0.08133,-0.13199 0.164,-0.132 0.08266,1e-5 0.137332,0.044 0.164,0.132 l 0.656,2.26 c 0.01333,0.0453 0.02,0.0813 0.02,0.108 m -0.56,-0.752 -0.284,-0.964 -0.28,0.964 0.564,0"  gorn="0.8.0.0.0.0.0.0.0.0.11.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3183"/>
                                        </g>
                                        <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.12" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3409-3-7">
                                            <path d="m 43.191609,121.30038 c -2e-6,0.12267 -0.05333,0.184 -0.16,0.184 l -1.308,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.112 0.076,-0.168 0.228,-0.168 l 0.448,0 0,-1.988 -0.448,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.11199 0.076,-0.16799 0.228,-0.168 l 0.788,0 0,2.328 0.34,0 0,-0.644 c -1e-6,-0.14933 0.05733,-0.224 0.172,-0.224 0.111998,0 0.167998,0.0747 0.168,0.224 l 0,0.8"  gorn="0.8.0.0.0.0.0.0.0.0.12.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3186"/>
                                            <path d="m 45.660172,121.32038 c -2e-6,0.0453 -0.01734,0.0853 -0.052,0.12 -0.032,0.032 -0.07067,0.048 -0.116,0.048 -0.08267,0 -0.141335,-0.06 -0.176,-0.18 l -0.12,-0.4 -0.76,0 -0.116,0.4 c -0.03467,0.12 -0.09467,0.18 -0.18,0.18 -0.04533,0 -0.08533,-0.016 -0.12,-0.048 -0.032,-0.0347 -0.048,-0.0747 -0.048,-0.12 -10e-7,-0.0267 0.0067,-0.0627 0.02,-0.108 l 0.664,-2.26 c 0.02667,-0.088 0.08133,-0.13199 0.164,-0.132 0.08266,1e-5 0.137332,0.044 0.164,0.132 l 0.656,2.26 c 0.01333,0.0453 0.02,0.0813 0.02,0.108 m -0.56,-0.752 -0.284,-0.964 -0.28,0.964 0.564,0"  gorn="0.8.0.0.0.0.0.0.0.0.12.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3188"/>
                                        </g>
                                        <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.13" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3409-3-0">
                                            <path d="m 42.941609,130.55037 c -2e-6,0.12267 -0.05333,0.184 -0.16,0.184 l -1.308,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.11199 0.076,-0.16799 0.228,-0.168 l 0.448,0 0,-1.988 -0.448,0 c -0.152,1e-5 -0.228,-0.0573 -0.228,-0.172 0,-0.11199 0.076,-0.16799 0.228,-0.168 l 0.788,0 0,2.328 0.34,0 0,-0.644 c -1e-6,-0.14933 0.05733,-0.22399 0.172,-0.224 0.111998,1e-5 0.167998,0.0747 0.168,0.224 l 0,0.8"  gorn="0.8.0.0.0.0.0.0.0.0.13.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3191"/>
                                            <path d="m 45.418172,130.02237 c -2e-6,0.20801 -0.06533,0.37867 -0.196,0.512 -0.130669,0.13334 -0.297335,0.2 -0.5,0.2 l -1,0 0,-2.668 1.016,0 c 0.205332,1e-5 0.369331,0.0693 0.492,0.208 0.125331,0.13867 0.187998,0.32134 0.188,0.548 -2e-6,0.25334 -0.076,0.44801 -0.228,0.584 0.088,0.0853 0.147998,0.17067 0.18,0.256 0.032,0.0853 0.048,0.20534 0.048,0.36 m -0.34,-1.212 c -2e-6,-0.26933 -0.124002,-0.40399 -0.372,-0.404 l -0.644,0 0,0.828 0.648,0 c 0.245332,10e-6 0.367998,-0.14133 0.368,-0.424 m 0,1.172 c -2e-6,-0.27199 -0.125335,-0.40799 -0.376,-0.408 l -0.64,0 0,0.82 0.648,0 c 0.245332,1e-5 0.367998,-0.13733 0.368,-0.412"  gorn="0.8.0.0.0.0.0.0.0.0.13.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3193"/>
                                        </g>
                                        <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.14" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3409-3-5">
                                            <path d="m 40.437609,137.26237 c -2e-6,0.0587 -0.01067,0.11601 -0.032,0.172 l -0.652,1.688 c -0.02933,0.0747 -0.08267,0.112 -0.16,0.112 -0.08,0 -0.134667,-0.0373 -0.164,-0.112 l -0.656,-1.688 c -0.008,-0.016 -0.012,-0.028 -0.012,-0.036 -0.01333,-0.032 -0.02,-0.0773 -0.02,-0.136 l 0,-0.468 c 0,-0.15199 0.05733,-0.22799 0.172,-0.228 0.112,1e-5 0.168,0.076 0.168,0.228 l 0,0.492 0.508,1.30801 0.508,-1.30801 0,-0.496 c -10e-7,-0.14933 0.05733,-0.22399 0.172,-0.224 0.111998,1e-5 0.167998,0.0747 0.168,0.224 l 0,0.472"  gorn="0.8.0.0.0.0.0.0.0.0.14.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3196"/>
                                            <path d="m 42.910172,137.89037 c -2e-6,0.13334 -0.02667,0.25334 -0.08,0.36 l -0.348,0.7 c -0.09333,0.18934 -0.254668,0.284 -0.484,0.284 l -0.556,0 c -0.152001,0 -0.228001,-0.0573 -0.228,-0.172 -10e-7,-0.11199 0.076,-0.16799 0.228,-0.168 l 0.112,0 0,-1.988 -0.112,0 c -0.152001,1e-5 -0.228001,-0.0573 -0.228,-0.172 -10e-7,-0.11199 0.076,-0.16799 0.228,-0.168 l 0.588,0 c 0.207998,1e-5 0.361332,0.10001 0.46,0.3 l 0.336,0.684 c 0.056,0.11467 0.084,0.22801 0.084,0.34 m -0.34,0.012 c -2e-6,-0.064 -0.02267,-0.14133 -0.068,-0.232 l -0.324,-0.656 c -0.03467,-0.072 -0.09334,-0.10799 -0.176,-0.108 l -0.108,0 0,1.988 0.116,0 c 0.08267,1e-5 0.141332,-0.036 0.176,-0.108 l 0.336,-0.688 c 0.032,-0.0667 0.048,-0.13199 0.048,-0.196"  gorn="0.8.0.0.0.0.0.0.0.0.14.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3198"/>
                                            <path d="m 45.386734,137.89037 c -2e-6,0.13334 -0.02667,0.25334 -0.08,0.36 l -0.348,0.7 c -0.09334,0.18934 -0.254668,0.284 -0.484,0.284 l -0.556,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.11199 0.076,-0.16799 0.228,-0.168 l 0.112,0 0,-1.988 -0.112,0 c -0.152,1e-5 -0.228,-0.0573 -0.228,-0.172 0,-0.11199 0.076,-0.16799 0.228,-0.168 l 0.588,0 c 0.207999,1e-5 0.361332,0.10001 0.46,0.3 l 0.336,0.684 c 0.056,0.11467 0.084,0.22801 0.084,0.34 m -0.34,0.012 c -10e-7,-0.064 -0.02267,-0.14133 -0.068,-0.232 l -0.324,-0.656 c -0.03467,-0.072 -0.09333,-0.10799 -0.176,-0.108 l -0.108,0 0,1.988 0.116,0 c 0.08267,1e-5 0.141332,-0.036 0.176,-0.108 l 0.336,-0.688 c 0.032,-0.0667 0.048,-0.13199 0.048,-0.196"  gorn="0.8.0.0.0.0.0.0.0.0.14.2" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3200"/>
                                        </g>
                                        <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.15" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3491">
                                            <path d="m 39.592,148.004 c -2e-6,0.13333 -0.05067,0.24933 -0.152,0.348 -0.101335,0.0987 -0.220002,0.148 -0.356,0.148 l -0.676,0 c -0.146667,0 -0.269334,-0.0493 -0.368,-0.148 -0.096,-0.0987 -0.144,-0.22133 -0.144,-0.368 l 0,-0.94 c 0,-0.152 0.052,-0.29466 0.156,-0.428 l 0.452,-0.584 c 0.103999,-0.13333 0.242665,-0.2 0.416,-0.2 l 0.44,0 c 0.151998,0 0.227998,0.056 0.228,0.168 -2e-6,0.11467 -0.076,0.172 -0.228,0.172 l -0.396,0 c -0.06667,0 -0.110668,0.005 -0.132,0.016 -0.01867,0.008 -0.048,0.0387 -0.088,0.092 l -0.424,0.548 c -0.056,0.072 -0.084,0.15867 -0.084,0.26 l 0,0.868 c -10e-7,0.136 0.06667,0.204 0.2,0.204 l 0.628,0 c 0.125332,0 0.187998,-0.068 0.188,-0.204 l 0,-0.324 -0.284,0 c -0.152001,0 -0.228001,-0.056 -0.228,-0.168 -1e-6,-0.11467 0.076,-0.172 0.228,-0.172 l 0.624,0 0,0.712"  gorn="0.8.0.0.0.0.0.0.0.0.15.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3203"/>
                                            <path d="m 42.064562,148.5 -0.451999,0 -0.904001,-2.056 0,1.828 c 0,0.152 -0.056,0.228 -0.168,0.228 -0.114667,0 -0.172,-0.076 -0.171999,-0.228 l 0,-2.44 0.451999,0 0.904,2.08 0,-1.852 c -10e-7,-0.152 0.056,-0.228 0.168,-0.228 0.114665,0 0.171998,0.076 0.172,0.228 l 0,2.44"  gorn="0.8.0.0.0.0.0.0.0.0.15.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3205"/>
                                            <path d="m 44.537125,147.156 c -2e-6,0.13333 -0.02667,0.25333 -0.08,0.36 l -0.348,0.7 c -0.09333,0.18933 -0.254668,0.284 -0.484,0.284 l -0.556,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.112 0.076,-0.168 0.228,-0.168 l 0.112,0 0,-1.988 -0.112,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.112 0.076,-0.168 0.228,-0.168 l 0.588,0 c 0.207999,0 0.361332,0.1 0.46,0.3 l 0.336,0.684 c 0.056,0.11467 0.084,0.228 0.084,0.34 m -0.34,0.012 c -2e-6,-0.064 -0.02267,-0.14133 -0.068,-0.232 l -0.324,-0.656 c -0.03467,-0.072 -0.09333,-0.108 -0.176,-0.108 l -0.108,0 0,1.988 0.116,0 c 0.08267,0 0.141332,-0.036 0.176,-0.108 l 0.336,-0.688 c 0.032,-0.0667 0.048,-0.132 0.048,-0.196"  gorn="0.8.0.0.0.0.0.0.0.0.15.2" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3207"/>
                                        </g>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>
</svg>


## svg.icon.0223_4ed19ade2e699853070a13a613764d44_1_icon.svg

<?xml version='1.0' encoding='UTF-8' standalone='no'?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->
<svg xmlns="http://www.w3.org/2000/svg" height="72" width="54"  gorn="0" version="1.1" id="svg3039">
    <desc >
        <referenceFile >A4988 icon.svg</referenceFile>
    </desc>
    <metadata  id="metadata3045">
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <cc:Work xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:cc="http://creativecommons.org/ns#" rdf:about="">
                <dc:format xmlns:dc="http://purl.org/dc/elements/1.1/">image/svg+xml</dc:format>
                <dc:type xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
                <dc:title xmlns:dc="http://purl.org/dc/elements/1.1/"/>
            </cc:Work>
        </rdf:RDF>
    </metadata>
    <defs  id="defs3043"/>
    <g transform="translate(0,-79.004003)" >
        <g >
            <g >
                <g >
                    <g >
                        <g >
                            <g  gorn="0.3.0.0.0.0.0.0" style="display:inline" id="layer1">
                                <rect height="72" width="54"  x="0" y="79" gorn="0.3.0.0.0.0.0.0.0" style="fill:#008000" id="rect3134"/>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>
    <g transform="translate(0,-79.004003)" >
        <g >
            <g >
                <g >
                    <g >
                        <g >
                            <g  gorn="0.4.0.0.0.0.0.0" style="display:none" id="layer2">
                                <image height="151" width="114"  x="-0.07853318" y="-0.39528903" href="data:image/png;base64,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 " id="image3131"/>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>
    <g transform="translate(0,-79.004003)" >
        <g >
            <g >
                <g >
                    <g >
                        <g >
                            <g  gorn="0.5.0.0.0.0.0.0" id="layer3">
                                <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,79.393922)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.0.0.0.0.0.0.0" style="fill:#000000" id="path3143"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,88.435052)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.1.0.0.0.0.0.0" style="fill:#000000" id="path3143-9"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,97.476182)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.2.0.0.0.0.0.0" style="fill:#000000" id="path3143-6"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,106.51731)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.3.0.0.0.0.0.0" style="fill:#000000" id="path3143-7"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,115.55844)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.4.0.0.0.0.0.0" style="fill:#000000" id="path3143-8"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,124.59957)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.5.0.0.0.0.0.0" style="fill:#000000" id="path3143-97"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,133.6407)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.6.0.0.0.0.0.0" style="fill:#000000" id="path3143-5"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0.47368421,0,0,0.47584896,0.07349049,142.68183)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.7.0.0.0.0.0.0" style="fill:#000000" id="path3143-52"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,142.68183)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.8.0.0.0.0.0.0" style="fill:#000000" id="path3143-4"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,133.6407)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.9.0.0.0.0.0.0" style="fill:#000000" id="path3143-94"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,124.59957)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.10.0.0.0.0.0.0" style="fill:#000000" id="path3143-47"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,115.55844)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.11.0.0.0.0.0.0" style="fill:#000000" id="path3143-95"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,106.51731)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.12.0.0.0.0.0.0" style="fill:#000000" id="path3143-56"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,97.476182)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.13.0.0.0.0.0.0" style="fill:#000000" id="path3143-1"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,88.435052)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.14.0.0.0.0.0.0" style="fill:#000000" id="path3143-59"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0.47368421,0,0,0.47584896,45.073491,79.393922)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 13.789199,9.0085154 c 0,2.4699126 -2.00226,4.4721726 -4.4721729,4.4721726 -2.4699128,0 -4.4721727,-2.00226 -4.4721727,-4.4721726 0,-2.4699128 2.0022599,-4.4721728 4.4721727,-4.4721728 2.4699129,0 4.4721729,2.00226 4.4721729,4.4721728 z"  gorn="0.5.0.0.0.0.0.0.15.0.0.0.0.0.0" style="fill:#000000" id="path3143-13"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g fill="#000000" xmlns:xml="http://www.w3.org/XML/1998/namespace"  font-size="10" stroke="none" gorn="0.5.0.0.0.0.0.0.16" fill-opacity="1" style="font-style:normal;font-weight:normal;line-height:100%;letter-spacing:0px;word-spacing:0px;font-family:Droid Sans" xml:space="preserve" id="text3151"/>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>
    <g transform="translate(0,-79.004003)" >
        <g >
            <g >
                <g >
                    <g >
                        <g >
                            <g  gorn="0.6.0.0.0.0.0.0" id="layer5">
                                <rect height="0.95169789" width="2.3684211"  x="9.9473686" y="105.06897" gorn="0.6.0.0.0.0.0.0.0" style="fill:#808080" id="rect3299"/>
                                <rect height="0.95169789" width="2.3684211"  x="9.9473686" y="106.9809" gorn="0.6.0.0.0.0.0.0.1" style="fill:#808080" id="rect3299-1"/>
                                <rect height="0.95169789" width="2.3684211"  x="9.9473686" y="108.64114" gorn="0.6.0.0.0.0.0.0.2" style="fill:#808080" id="rect3299-16"/>
                                <rect height="0.95169789" width="2.3684211"  x="9.9473686" y="110.39671" gorn="0.6.0.0.0.0.0.0.3" style="fill:#808080" id="rect3299-14"/>
                                <rect height="0.95169789" width="2.3684211"  x="9.9473686" y="112.34039" gorn="0.6.0.0.0.0.0.0.4" style="fill:#808080" id="rect3299-9"/>
                                <rect height="0.95169789" width="2.3684211"  x="9.9473686" y="114.28406" gorn="0.6.0.0.0.0.0.0.5" style="fill:#808080" id="rect3299-6"/>
                                <rect height="0.95169789" width="2.3684211"  x="9.9473686" y="115.91424" gorn="0.6.0.0.0.0.0.0.6" style="fill:#808080" id="rect3299-4"/>
                                <rect height="0.95169789" width="2.3684211"  x="29.368422" y="115.91424" gorn="0.6.0.0.0.0.0.0.7" style="fill:#808080" id="rect3299-44"/>
                                <rect height="0.95169789" width="2.3684211"  x="29.368422" y="114.03326" gorn="0.6.0.0.0.0.0.0.8" style="fill:#808080" id="rect3299-10"/>
                                <rect height="0.95169789" width="2.3684211"  x="29.368422" y="112.15229" gorn="0.6.0.0.0.0.0.0.9" style="fill:#808080" id="rect3299-3"/>
                                <rect height="0.95169789" width="2.3684211"  x="29.368422" y="110.27132" gorn="0.6.0.0.0.0.0.0.10" style="fill:#808080" id="rect3299-7"/>
                                <rect height="0.95169789" width="2.3684211"  x="29.368422" y="108.39034" gorn="0.6.0.0.0.0.0.0.11" style="fill:#808080" id="rect3299-43"/>
                                <rect height="0.95169789" width="2.3684211"  x="29.368422" y="106.50936" gorn="0.6.0.0.0.0.0.0.12" style="fill:#808080" id="rect3299-48"/>
                                <rect height="0.95169789" width="2.3684211"  x="29.368422" y="104.62839" gorn="0.6.0.0.0.0.0.0.13" style="fill:#808080" id="rect3299-12"/>
                                <g transform="matrix(0,0.47584896,-0.47368421,0,45.187654,75.134064)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g  gorn="0.6.0.0.0.0.0.0.14.0.0.0.0.0.0" id="g3498">
                                                            <rect height="2" width="5"  x="53.499126" y="38.99173" gorn="0.6.0.0.0.0.0.0.14.0.0.0.0.0.0.0" style="fill:#808080" id="rect3299-92"/>
                                                            <rect height="2" width="5"  x="53.499126" y="43.009682" gorn="0.6.0.0.0.0.0.0.14.0.0.0.0.0.0.1" style="fill:#808080" id="rect3299-1-2"/>
                                                            <rect height="2" width="5"  x="53.499126" y="46.498672" gorn="0.6.0.0.0.0.0.0.14.0.0.0.0.0.0.2" style="fill:#808080" id="rect3299-16-3"/>
                                                            <rect height="2" width="5"  x="53.499126" y="50.188023" gorn="0.6.0.0.0.0.0.0.14.0.0.0.0.0.0.3" style="fill:#808080" id="rect3299-14-1"/>
                                                            <rect height="2" width="5"  x="53.499126" y="54.272671" gorn="0.6.0.0.0.0.0.0.14.0.0.0.0.0.0.4" style="fill:#808080" id="rect3299-9-3"/>
                                                            <rect height="2" width="5"  x="53.499126" y="58.357311" gorn="0.6.0.0.0.0.0.0.14.0.0.0.0.0.0.5" style="fill:#808080" id="rect3299-6-2"/>
                                                            <rect height="2" width="5"  x="53.499126" y="61.783138" gorn="0.6.0.0.0.0.0.0.14.0.0.0.0.0.0.6" style="fill:#808080" id="rect3299-4-1"/>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                                <g transform="matrix(0,0.47584896,-0.47368421,0,45.250069,93.881101)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g  gorn="0.6.0.0.0.0.0.0.15.0.0.0.0.0.0" id="g3498-2">
                                                            <rect height="2" width="5"  x="53.499126" y="38.99173" gorn="0.6.0.0.0.0.0.0.15.0.0.0.0.0.0.0" style="fill:#808080" id="rect3299-92-3"/>
                                                            <rect height="2" width="5"  x="53.499126" y="43.009682" gorn="0.6.0.0.0.0.0.0.15.0.0.0.0.0.0.1" style="fill:#808080" id="rect3299-1-2-5"/>
                                                            <rect height="2" width="5"  x="53.499126" y="46.498672" gorn="0.6.0.0.0.0.0.0.15.0.0.0.0.0.0.2" style="fill:#808080" id="rect3299-16-3-9"/>
                                                            <rect height="2" width="5"  x="53.499126" y="50.188023" gorn="0.6.0.0.0.0.0.0.15.0.0.0.0.0.0.3" style="fill:#808080" id="rect3299-14-1-0"/>
                                                            <rect height="2" width="5"  x="53.499126" y="54.272671" gorn="0.6.0.0.0.0.0.0.15.0.0.0.0.0.0.4" style="fill:#808080" id="rect3299-9-3-1"/>
                                                            <rect height="2" width="5"  x="53.499126" y="58.357311" gorn="0.6.0.0.0.0.0.0.15.0.0.0.0.0.0.5" style="fill:#808080" id="rect3299-6-2-3"/>
                                                            <rect height="2" width="5"  x="53.499126" y="61.783138" gorn="0.6.0.0.0.0.0.0.15.0.0.0.0.0.0.6" style="fill:#808080" id="rect3299-4-1-6"/>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>
    <g transform="translate(0,-79.004003)" >
        <g >
            <g >
                <g >
                    <g >
                        <g >
                            <g  gorn="0.7.0.0.0.0.0.0" style="display:inline" id="layer4">
                                <rect height="18.088671" width="17.123714"  x="12.533853" y="102.05419" gorn="0.7.0.0.0.0.0.0.0" style="fill:#000000" id="rect3278"/>
                                <rect height="11.349753" width="12.004253"  x="25.420771" y="136.28079" gorn="0.7.0.0.0.0.0.0.1" style="fill:#000000" id="rect3546"/>
                                <rect height="5.8522167" width="12.004253"  x="30.716764" y="83.078819" gorn="0.7.0.0.0.0.0.0.2" style="fill:#803300" id="rect3548"/>
                                <rect height="5.8963547" width="1.6622884"  x="29.127184" y="83.243279" gorn="0.7.0.0.0.0.0.0.3" style="fill:#808080" id="rect3552"/>
                                <rect height="5.8963547" width="1.6622884"  x="41.713341" y="82.968079" gorn="0.7.0.0.0.0.0.0.4" style="fill:#808080;display:inline" id="rect3552-7"/>
                                <g transform="matrix(0.44101633,0,0,0.41021461,5.4542653,90.256166)" >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <path d="m 69.691357,126.03037 c 0,5.96896 -4.838795,10.80775 -10.807751,10.80775 -5.968956,0 -10.807751,-4.83879 -10.807751,-10.80775 0,-5.96895 4.838795,-10.80775 10.807751,-10.80775 5.968956,0 10.807751,4.8388 10.807751,10.80775 z"  gorn="0.7.0.0.0.0.0.0.5.0.0.0.0.0.0" style="fill:#b3b3b3" id="path3591"/>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>
    <g transform="translate(0,-79.004003)" >
        <g >
            <g >
                <g >
                    <g >
                        <g >
                            <g  gorn="0.8.0.0.0.0.0.0" style="display:inline" id="layer6">
                                <g  gorn="0.8.0.0.0.0.0.0.0" style="fill:#ffffff" id="g3253">
                                    <g transform="translate(0.6904297,1.863209)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.0.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;display:inline;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3163">
                                                                <path d="M 9.588,82.928 C 9.5879979,83.042667 9.511998,83.1 9.36,83.1 l -1.468,0 0,-2.668 1.468,0 c 0.151998,3e-6 0.2279979,0.056 0.228,0.168 -2.1e-6,0.114669 -0.076002,0.172002 -0.228,0.172 l -1.128,0 0,0.828 0.456,0 c 0.1519987,1e-6 0.2279986,0.056 0.228,0.168 -1.4e-6,0.114668 -0.076001,0.172001 -0.228,0.172 l -0.456,0 0,0.82 1.128,0 c 0.151998,0 0.2279979,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3094"/>
                                                                <path d="m 12.064563,83.1 -0.452001,0 -0.904,-2.056 0,1.828 c 0,0.152 -0.056,0.228 -0.167999,0.228 -0.114668,0 -0.172001,-0.076 -0.172001,-0.228 l 0,-2.44 0.452,0 0.904,2.08 0,-1.852 c -1e-6,-0.151997 0.056,-0.227997 0.168001,-0.228 0.114664,3e-6 0.171997,0.076 0.172,0.228 l 0,2.44"  gorn="0.8.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3096"/>
                                                                <path d="m 14.537125,82.936 c -2e-6,0.04533 -0.01733,0.08533 -0.052,0.12 -0.032,0.032 -0.07067,0.048 -0.116,0.048 -0.08267,0 -0.141335,-0.06 -0.176,-0.18 l -0.12,-0.4 -0.76,0 -0.116,0.4 c -0.03467,0.12 -0.09467,0.18 -0.18,0.18 -0.04533,0 -0.08533,-0.016 -0.12,-0.048 -0.032,-0.03467 -0.048,-0.07467 -0.048,-0.12 0,-0.02667 0.0067,-0.06267 0.02,-0.108 l 0.664,-2.26 c 0.02667,-0.088 0.08133,-0.131997 0.164,-0.132 0.08267,3e-6 0.137332,0.044 0.164,0.132 l 0.656,2.26 c 0.01333,0.04533 0.02,0.08133 0.02,0.108 m -0.56,-0.752 -0.284,-0.964 -0.28,0.964 0.564,0"  gorn="0.8.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3098"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="translate(0.71972661,1.6112559)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.1.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3171">
                                                                <path d="m 9.588,92.372 c -2.1e-6,0.152 -0.057335,0.228 -0.172,0.228 -0.1120018,0 -0.1680017,-0.076 -0.168,-0.228 l 0,-1.968 -0.34,0.484 0,0.032 c -1.4e-6,0.152002 -0.056001,0.228001 -0.168,0.228 -0.1146678,10e-7 -0.1720011,-0.076 -0.172,-0.228 l 0,-0.032 -0.336,-0.484 0,1.968 c -7e-7,0.152 -0.056001,0.228 -0.168,0.228 -0.1146671,0 -0.1720004,-0.076 -0.172,-0.228 l 0,-2.44 0.432,0 0.416,0.604 0.416,-0.604 0.432,0 0,2.44"  gorn="0.8.0.0.0.0.0.0.0.1.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3101"/>
                                                                <path d="m 12.064563,92.216 c -3e-6,0.106667 -0.03867,0.197334 -0.116,0.272 -0.07467,0.07467 -0.166669,0.112 -0.276,0.112 l -0.84,0 c -0.122668,0 -0.230668,-0.04267 -0.324,-0.128 -0.09067,-0.08533 -0.136001,-0.184 -0.136,-0.296 -10e-7,-0.130666 0.05867,-0.195999 0.175999,-0.196 0.09333,10e-7 0.148,0.064 0.164001,0.192 0.008,0.05867 0.044,0.088 0.107999,0.088 l 0.828001,0 c 0.048,0 0.072,-0.01333 0.072,-0.04 -2e-6,-0.01333 -0.012,-0.036 -0.036,-0.068 l -1.228,-1.584 c -0.05867,-0.07466 -0.088,-0.157331 -0.088,-0.248 0,-0.114664 0.03867,-0.207998 0.116,-0.28 0.08,-0.072 0.182666,-0.107997 0.308001,-0.108 l 0.812,0 c 0.119998,3e-6 0.225331,0.04534 0.315999,0.136 0.09333,0.088 0.139998,0.189336 0.140001,0.304 -3e-6,0.130669 -0.056,0.196002 -0.168,0.196 -0.101336,2e-6 -0.158669,-0.064 -0.172,-0.192 -0.008,-0.06933 -0.04934,-0.103998 -0.124,-0.104 l -0.812,0 c -0.048,2e-6 -0.072,0.016 -0.072,0.048 -10e-7,0.016 0.0093,0.036 0.028,0.06 l 1.228001,1.584 c 0.064,0.08267 0.096,0.166667 0.096,0.252"  gorn="0.8.0.0.0.0.0.0.0.1.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3103"/>
                                                                <path d="m 14.545125,92.416 c -2e-6,0.122667 -0.05334,0.184 -0.16,0.184 l -1.308,0 c -0.152,0 -0.228,-0.05733 -0.228,-0.172 0,-0.112 0.076,-0.168 0.228,-0.168 l 0.448,0 0,-1.988 -0.448,0 c -0.152,2e-6 -0.228,-0.05733 -0.228,-0.172 0,-0.111997 0.076,-0.167997 0.228,-0.168 l 0.788,0 0,2.328 0.34,0 0,-0.644 c -2e-6,-0.149332 0.05733,-0.223999 0.172,-0.224 0.111998,10e-7 0.167998,0.07467 0.168,0.224 l 0,0.8"  gorn="0.8.0.0.0.0.0.0.0.1.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3105"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="translate(0.4697266,10.361256)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.2.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3171-7">
                                                                <path d="m 9.588,92.372 c -2.1e-6,0.152 -0.057335,0.228 -0.172,0.228 -0.1120018,0 -0.1680017,-0.076 -0.168,-0.228 l 0,-1.968 -0.34,0.484 0,0.032 c -1.4e-6,0.152002 -0.056001,0.228001 -0.168,0.228 -0.1146678,10e-7 -0.1720011,-0.076 -0.172,-0.228 l 0,-0.032 -0.336,-0.484 0,1.968 c -7e-7,0.152 -0.056001,0.228 -0.168,0.228 -0.1146671,0 -0.1720004,-0.076 -0.172,-0.228 l 0,-2.44 0.432,0 0.416,0.604 0.416,-0.604 0.432,0 0,2.44"  gorn="0.8.0.0.0.0.0.0.0.2.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3108"/>
                                                                <path d="m 12.064563,92.216 c -3e-6,0.106667 -0.03867,0.197334 -0.116,0.272 -0.07467,0.07467 -0.166669,0.112 -0.276,0.112 l -0.84,0 c -0.122668,0 -0.230668,-0.04267 -0.324,-0.128 -0.09067,-0.08533 -0.136001,-0.184 -0.136,-0.296 -10e-7,-0.130666 0.05867,-0.195999 0.175999,-0.196 0.09333,10e-7 0.148,0.064 0.164001,0.192 0.008,0.05867 0.044,0.088 0.107999,0.088 l 0.828001,0 c 0.048,0 0.072,-0.01333 0.072,-0.04 -2e-6,-0.01333 -0.012,-0.036 -0.036,-0.068 l -1.228,-1.584 c -0.05867,-0.07466 -0.088,-0.157331 -0.088,-0.248 0,-0.114664 0.03867,-0.207998 0.116,-0.28 0.08,-0.072 0.182666,-0.107997 0.308001,-0.108 l 0.812,0 c 0.119998,3e-6 0.225331,0.04534 0.315999,0.136 0.09333,0.088 0.139998,0.189336 0.140001,0.304 -3e-6,0.130669 -0.056,0.196002 -0.168,0.196 -0.101336,2e-6 -0.158669,-0.064 -0.172,-0.192 -0.008,-0.06933 -0.04934,-0.103998 -0.124,-0.104 l -0.812,0 c -0.048,2e-6 -0.072,0.016 -0.072,0.048 -10e-7,0.016 0.0093,0.036 0.028,0.06 l 1.228001,1.584 c 0.064,0.08267 0.096,0.166667 0.096,0.252"  gorn="0.8.0.0.0.0.0.0.0.2.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3110"/>
                                                                <path d="m 14.541125,92.428 c -2e-6,0.114667 -0.076,0.172 -0.228,0.172 l -1.468,0 0,-1.16 c 0,-0.09866 0.032,-0.179999 0.096,-0.244 0.06667,-0.06667 0.149333,-0.1 0.248,-0.1 l 1.008,0 0,-0.824 -1.124,0 c -0.152,2e-6 -0.228,-0.05733 -0.228,-0.172 0,-0.111997 0.076,-0.167997 0.228,-0.168 l 1.124,0 c 0.09867,3e-6 0.179998,0.03467 0.244,0.104 0.06667,0.06667 0.1,0.150669 0.1,0.252 l 0,0.808 c -2e-6,0.09867 -0.03333,0.181335 -0.1,0.248 -0.064,0.064 -0.145335,0.096 -0.244,0.096 l -1.008,0 0,0.82 1.124,0 c 0.151998,0 0.227998,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.2.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3112"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="translate(0.2197266,19.361256)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.3.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3171-6">
                                                                <path d="m 9.588,92.372 c -2.1e-6,0.152 -0.057335,0.228 -0.172,0.228 -0.1120018,0 -0.1680017,-0.076 -0.168,-0.228 l 0,-1.968 -0.34,0.484 0,0.032 c -1.4e-6,0.152002 -0.056001,0.228001 -0.168,0.228 -0.1146678,10e-7 -0.1720011,-0.076 -0.172,-0.228 l 0,-0.032 -0.336,-0.484 0,1.968 c -7e-7,0.152 -0.056001,0.228 -0.168,0.228 -0.1146671,0 -0.1720004,-0.076 -0.172,-0.228 l 0,-2.44 0.432,0 0.416,0.604 0.416,-0.604 0.432,0 0,2.44"  gorn="0.8.0.0.0.0.0.0.0.3.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3115"/>
                                                                <path d="m 12.064563,92.216 c -3e-6,0.106667 -0.03867,0.197334 -0.116,0.272 -0.07467,0.07467 -0.166669,0.112 -0.276,0.112 l -0.84,0 c -0.122668,0 -0.230668,-0.04267 -0.324,-0.128 -0.09067,-0.08533 -0.136001,-0.184 -0.136,-0.296 -10e-7,-0.130666 0.05867,-0.195999 0.175999,-0.196 0.09333,10e-7 0.148,0.064 0.164001,0.192 0.008,0.05867 0.044,0.088 0.107999,0.088 l 0.828001,0 c 0.048,0 0.072,-0.01333 0.072,-0.04 -2e-6,-0.01333 -0.012,-0.036 -0.036,-0.068 l -1.228,-1.584 c -0.05867,-0.07466 -0.088,-0.157331 -0.088,-0.248 0,-0.114664 0.03867,-0.207998 0.116,-0.28 0.08,-0.072 0.182666,-0.107997 0.308001,-0.108 l 0.812,0 c 0.119998,3e-6 0.225331,0.04534 0.315999,0.136 0.09333,0.088 0.139998,0.189336 0.140001,0.304 -3e-6,0.130669 -0.056,0.196002 -0.168,0.196 -0.101336,2e-6 -0.158669,-0.064 -0.172,-0.192 -0.008,-0.06933 -0.04934,-0.103998 -0.124,-0.104 l -0.812,0 c -0.048,2e-6 -0.072,0.016 -0.072,0.048 -10e-7,0.016 0.0093,0.036 0.028,0.06 l 1.228001,1.584 c 0.064,0.08267 0.096,0.166667 0.096,0.252"  gorn="0.8.0.0.0.0.0.0.0.3.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3117"/>
                                                                <path d="m 14.537125,92.26 c -2e-6,0.096 -0.03333,0.177333 -0.1,0.244 -0.06667,0.064 -0.148002,0.096 -0.244,0.096 l -1.124,0 c -0.152,0 -0.228,-0.05733 -0.228,-0.172 0,-0.112 0.076,-0.168 0.228,-0.168 l 1.124,0 0,-0.616 c -2e-6,-0.135999 -0.06133,-0.203999 -0.184,-0.204 l -0.6,0 c -0.152001,10e-7 -0.228001,-0.056 -0.228,-0.168 -10e-7,-0.114665 0.076,-0.171999 0.228,-0.172 l 0.604,0 c 0.114665,1e-6 0.171998,-0.07066 0.172,-0.212 l 0,-0.616 -1.116,0 c -0.152,2e-6 -0.228,-0.05733 -0.228,-0.172 0,-0.111997 0.076,-0.167997 0.228,-0.168 l 1.124,0 c 0.09066,3e-6 0.169331,0.02934 0.236,0.088 0.06666,0.05867 0.1,0.128002 0.1,0.208 l 0,0.744 c -2e-6,0.114668 -0.04267,0.213335 -0.128,0.296 0.09066,0.09867 0.135998,0.214668 0.136,0.348 l 0,0.644"  gorn="0.8.0.0.0.0.0.0.0.3.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3119"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="translate(0.2197266,28.611256)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.4.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3171-0">
                                                                <path d="m 9.592,92.436 c -2.1e-6,0.04267 -0.017335,0.08133 -0.052,0.116 -0.034669,0.032 -0.074669,0.048 -0.12,0.048 -0.061335,0 -0.1186685,-0.03867 -0.172,-0.116 l -0.932,-1.332 -0.08,0 0,1.22 c -7e-7,0.152 -0.056001,0.228 -0.168,0.228 -0.1146671,0 -0.1720004,-0.06267 -0.172,-0.188 l 0,-2.48 1.192,0 c 0.1413316,3e-6 0.2599982,0.052 0.356,0.156 0.098665,0.104002 0.1479979,0.230669 0.148,0.38 l 0,0.152 c -2.1e-6,0.157335 -0.050669,0.285335 -0.152,0.384 -0.098668,0.09867 -0.2266684,0.148001 -0.384,0.148 l -0.324,0 0.796,1.14 c 0.042665,0.06133 0.063998,0.109334 0.064,0.144 m -0.34,-1.816 0,-0.132 c -1.8e-6,-0.143998 -0.070668,-0.215998 -0.212,-0.216 l -0.804,0 0,0.54 0.804,0 c 0.1413317,2e-6 0.2119982,-0.064 0.212,-0.192"  gorn="0.8.0.0.0.0.0.0.0.4.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3122"/>
                                                                <path d="m 12.064563,92.428 c -3e-6,0.114667 -0.076,0.172 -0.228001,0.172 l -1.468,0 0,-2.668 1.468,0 c 0.151998,3e-6 0.227998,0.056 0.228001,0.168 -3e-6,0.114669 -0.076,0.172002 -0.228001,0.172 l -1.128,0 0,0.828 0.456001,0 c 0.151998,1e-6 0.227998,0.056 0.228,0.168 -2e-6,0.114668 -0.076,0.172001 -0.228,0.172 l -0.456001,0 0,0.82 1.128,0 c 0.151998,0 0.227998,0.056 0.228001,0.168"  gorn="0.8.0.0.0.0.0.0.0.4.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3124"/>
                                                                <path d="m 14.541125,92.216 c -2e-6,0.106667 -0.03867,0.197334 -0.116,0.272 -0.07467,0.07467 -0.166668,0.112 -0.276,0.112 l -0.84,0 c -0.122667,0 -0.230667,-0.04267 -0.324,-0.128 -0.09067,-0.08533 -0.136,-0.184 -0.136,-0.296 0,-0.130666 0.05867,-0.195999 0.176,-0.196 0.09333,10e-7 0.147999,0.064 0.164,0.192 0.008,0.05867 0.044,0.088 0.108,0.088 l 0.828,0 c 0.048,0 0.072,-0.01333 0.072,-0.04 -2e-6,-0.01333 -0.012,-0.036 -0.036,-0.068 l -1.228,-1.584 c -0.05867,-0.07466 -0.088,-0.157331 -0.088,-0.248 0,-0.114664 0.03867,-0.207998 0.116,-0.28 0.08,-0.072 0.182666,-0.107997 0.308,-0.108 l 0.812,0 c 0.119998,3e-6 0.225331,0.04534 0.316,0.136 0.09333,0.088 0.139998,0.189336 0.14,0.304 -2e-6,0.130669 -0.056,0.196002 -0.168,0.196 -0.101335,2e-6 -0.158668,-0.064 -0.172,-0.192 -0.008,-0.06933 -0.04933,-0.103998 -0.124,-0.104 l -0.812,0 c -0.048,2e-6 -0.072,0.016 -0.072,0.048 -1e-6,0.016 0.0093,0.036 0.028,0.06 l 1.228,1.584 c 0.064,0.08267 0.096,0.166667 0.096,0.252"  gorn="0.8.0.0.0.0.0.0.0.4.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3126"/>
                                                                <path d="m 17.017687,92.428 c -2e-6,0.114667 -0.076,0.172 -0.228,0.172 l -1.468,0 0,-2.668 1.468,0 c 0.151998,3e-6 0.227998,0.056 0.228,0.168 -2e-6,0.114669 -0.076,0.172002 -0.228,0.172 l -1.128,0 0,0.828 0.456,0 c 0.151999,1e-6 0.227999,0.056 0.228,0.168 -1e-6,0.114668 -0.076,0.172001 -0.228,0.172 l -0.456,0 0,0.82 1.128,0 c 0.151998,0 0.227998,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.4.0.0.0.0.0.0.3" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3128"/>
                                                                <path d="m 19.49425,90.376 c -2e-6,0.125335 -0.056,0.188002 -0.168,0.188 -0.114668,2e-6 -0.172002,-0.076 -0.172,-0.228 l 0,-0.064 -0.34,0 0,2.136 c -1e-6,0.125333 -0.056,0.188 -0.168,0.188 -0.114668,0 -0.172001,-0.076 -0.172,-0.228 l 0,-2.096 -0.336,0 0,0.068 c -1e-6,0.149335 -0.056,0.224002 -0.168,0.224 -0.114667,2e-6 -0.172,-0.07466 -0.172,-0.224 l 0,-0.408 1.696,0 0,0.444"  gorn="0.8.0.0.0.0.0.0.0.4.0.0.0.0.0.0.4" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3130"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="translate(0.21972658,37.611256)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.5.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3171-71">
                                                                <path d="m 9.588,92.216 c -2.1e-6,0.106667 -0.038669,0.197334 -0.116,0.272 -0.074669,0.07467 -0.1666685,0.112 -0.276,0.112 l -0.84,0 c -0.1226674,0 -0.2306673,-0.04267 -0.324,-0.128 -0.090667,-0.08533 -0.1360004,-0.184 -0.136,-0.296 -4e-7,-0.130666 0.058666,-0.195999 0.176,-0.196 0.093333,10e-7 0.1479993,0.064 0.164,0.192 0.008,0.05867 0.043999,0.088 0.108,0.088 l 0.828,0 c 0.047998,0 0.071998,-0.01333 0.072,-0.04 -1.7e-6,-0.01333 -0.012002,-0.036 -0.036,-0.068 L 7.98,90.568 c -0.058667,-0.07466 -0.088,-0.157331 -0.088,-0.248 -4e-7,-0.114664 0.038666,-0.207998 0.116,-0.28 0.079999,-0.072 0.182666,-0.107997 0.308,-0.108 l 0.812,0 c 0.1199983,3e-6 0.2253315,0.04534 0.316,0.136 0.093331,0.088 0.1399979,0.189336 0.14,0.304 -2.1e-6,0.130669 -0.056002,0.196002 -0.168,0.196 -0.1013351,2e-6 -0.1586684,-0.064 -0.172,-0.192 -0.008,-0.06933 -0.049335,-0.103998 -0.124,-0.104 l -0.812,0 c -0.048001,2e-6 -0.072001,0.016 -0.072,0.048 -7e-7,0.016 0.00933,0.036 0.028,0.06 l 1.228,1.584 c 0.063998,0.08267 0.095998,0.166667 0.096,0.252"  gorn="0.8.0.0.0.0.0.0.0.5.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3133"/>
                                                                <path d="m 12.060563,92.428 c -3e-6,0.114667 -0.076,0.172 -0.228,0.172 l -1.46,0 0,-2.436 c -10e-7,-0.151997 0.056,-0.227997 0.168,-0.228 0.114665,3e-6 0.171999,0.076 0.172,0.228 l 0,2.096 1.12,0 c 0.151997,0 0.227997,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.5.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3135"/>
                                                                <path d="m 14.541125,92.428 c -2e-6,0.114667 -0.076,0.172 -0.228,0.172 l -1.468,0 0,-2.668 1.468,0 c 0.151998,3e-6 0.227998,0.056 0.228,0.168 -2e-6,0.114669 -0.076,0.172002 -0.228,0.172 l -1.128,0 0,0.828 0.456,0 c 0.151999,1e-6 0.227999,0.056 0.228,0.168 -1e-6,0.114668 -0.076,0.172001 -0.228,0.172 l -0.456,0 0,0.82 1.128,0 c 0.151998,0 0.227998,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.5.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3137"/>
                                                                <path d="m 17.017687,92.428 c -2e-6,0.114667 -0.076,0.172 -0.228,0.172 l -1.468,0 0,-2.668 1.468,0 c 0.151998,3e-6 0.227998,0.056 0.228,0.168 -2e-6,0.114669 -0.076,0.172002 -0.228,0.172 l -1.128,0 0,0.828 0.456,0 c 0.151999,1e-6 0.227999,0.056 0.228,0.168 -1e-6,0.114668 -0.076,0.172001 -0.228,0.172 l -0.456,0 0,0.82 1.128,0 c 0.151998,0 0.227998,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.5.0.0.0.0.0.0.3" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3139"/>
                                                                <path d="m 19.49825,91.028 c -2e-6,0.176001 -0.04933,0.313335 -0.148,0.412 -0.09867,0.09867 -0.236002,0.148001 -0.412,0.148 l -0.8,0 0,0.784 c -1e-6,0.149333 -0.056,0.224 -0.168,0.224 -0.05067,0 -0.092,-0.016 -0.124,-0.048 -0.032,-0.03467 -0.048,-0.07867 -0.048,-0.132 l 0,-2.484 1.184,0 c 0.154665,3e-6 0.278665,0.04934 0.372,0.148 0.096,0.09867 0.143998,0.230669 0.144,0.396 l 0,0.552 m -0.34,0 0,-0.552 c -2e-6,-0.135998 -0.06933,-0.203998 -0.208,-0.204 l -0.812,0 0,0.976 0.824,0 c 0.130665,10e-7 0.195998,-0.07333 0.196,-0.22"  gorn="0.8.0.0.0.0.0.0.0.5.0.0.0.0.0.0.4" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3141"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="translate(0.31640627,46.611256)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.6.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3171-71-9">
                                                                <path d="m 9.588,92.216 c -2.1e-6,0.106667 -0.038669,0.197334 -0.116,0.272 -0.074669,0.07467 -0.1666685,0.112 -0.276,0.112 l -0.84,0 c -0.1226674,0 -0.2306673,-0.04267 -0.324,-0.128 -0.090667,-0.08533 -0.1360004,-0.184 -0.136,-0.296 -4e-7,-0.130666 0.058666,-0.195999 0.176,-0.196 0.093333,10e-7 0.1479993,0.064 0.164,0.192 0.008,0.05867 0.043999,0.088 0.108,0.088 l 0.828,0 c 0.047998,0 0.071998,-0.01333 0.072,-0.04 -1.7e-6,-0.01333 -0.012002,-0.036 -0.036,-0.068 L 7.98,90.568 c -0.058667,-0.07466 -0.088,-0.157331 -0.088,-0.248 -4e-7,-0.114664 0.038666,-0.207998 0.116,-0.28 0.079999,-0.072 0.182666,-0.107997 0.308,-0.108 l 0.812,0 c 0.1199983,3e-6 0.2253315,0.04534 0.316,0.136 0.093331,0.088 0.1399979,0.189336 0.14,0.304 -2.1e-6,0.130669 -0.056002,0.196002 -0.168,0.196 -0.1013351,2e-6 -0.1586684,-0.064 -0.172,-0.192 -0.008,-0.06933 -0.049335,-0.103998 -0.124,-0.104 l -0.812,0 c -0.048001,2e-6 -0.072001,0.016 -0.072,0.048 -7e-7,0.016 0.00933,0.036 0.028,0.06 l 1.228,1.584 c 0.063998,0.08267 0.095998,0.166667 0.096,0.252"  gorn="0.8.0.0.0.0.0.0.0.6.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3144"/>
                                                                <path d="m 12.064563,90.376 c -3e-6,0.125335 -0.056,0.188002 -0.168,0.188 -0.114669,2e-6 -0.172002,-0.076 -0.172001,-0.228 l 0,-0.064 -0.34,0 0,2.136 c -1e-6,0.125333 -0.056,0.188 -0.167999,0.188 -0.114668,0 -0.172002,-0.076 -0.172,-0.228 l 0,-2.096 -0.336001,0 0,0.068 c 0,0.149335 -0.056,0.224002 -0.167999,0.224 -0.114668,2e-6 -0.172001,-0.07466 -0.172001,-0.224 l 0,-0.408 1.696001,0 0,0.444"  gorn="0.8.0.0.0.0.0.0.0.6.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3146"/>
                                                                <path d="m 14.541125,92.428 c -2e-6,0.114667 -0.076,0.172 -0.228,0.172 l -1.468,0 0,-2.668 1.468,0 c 0.151998,3e-6 0.227998,0.056 0.228,0.168 -2e-6,0.114669 -0.076,0.172002 -0.228,0.172 l -1.128,0 0,0.828 0.456,0 c 0.151999,1e-6 0.227999,0.056 0.228,0.168 -1e-6,0.114668 -0.076,0.172001 -0.228,0.172 l -0.456,0 0,0.82 1.128,0 c 0.151998,0 0.227998,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.6.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3148"/>
                                                                <path d="m 17.021687,91.028 c -2e-6,0.176001 -0.04933,0.313335 -0.148,0.412 -0.09867,0.09867 -0.236001,0.148001 -0.412,0.148 l -0.8,0 0,0.784 c 0,0.149333 -0.056,0.224 -0.167999,0.224 -0.05067,0 -0.092,-0.016 -0.124,-0.048 -0.032,-0.03467 -0.048,-0.07867 -0.048,-0.132 l 0,-2.484 1.184,0 c 0.154665,3e-6 0.278665,0.04934 0.372,0.148 0.096,0.09867 0.143998,0.230669 0.144,0.396 l 0,0.552 m -0.34,0 0,-0.552 c -1e-6,-0.135998 -0.06933,-0.203998 -0.208,-0.204 l -0.812,0 0,0.976 0.824,0 c 0.130665,10e-7 0.195999,-0.07333 0.196,-0.22"  gorn="0.8.0.0.0.0.0.0.0.6.0.0.0.0.0.0.3" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3150"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g transform="translate(0.3164063,55.111256)" >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g >
                                                            <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.7.0.0.0.0.0.0" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="flowRoot3171-71-4">
                                                                <path d="m 9.584,91.256 c -2.1e-6,0.133335 -0.026669,0.253334 -0.08,0.36 l -0.348,0.7 C 9.0626651,92.505333 8.9013319,92.6 8.672,92.6 l -0.556,0 c -0.1520005,0 -0.2280004,-0.05733 -0.228,-0.172 -4e-7,-0.112 0.075999,-0.168 0.228,-0.168 l 0.112,0 0,-1.988 -0.112,0 c -0.1520005,2e-6 -0.2280004,-0.05733 -0.228,-0.172 -4e-7,-0.111997 0.075999,-0.167997 0.228,-0.168 l 0.588,0 c 0.2079986,3e-6 0.3613318,0.100003 0.46,0.3 L 9.5,90.916 c 0.055998,0.114668 0.083998,0.228001 0.084,0.34 m -0.34,0.012 c -1.7e-6,-0.064 -0.022668,-0.141332 -0.068,-0.232 L 8.852,90.38 c -0.034668,-0.072 -0.093335,-0.107998 -0.176,-0.108 l -0.108,0 0,1.988 0.116,0 c 0.082665,0 0.141332,-0.036 0.176,-0.108 l 0.336,-0.688 c 0.031998,-0.06667 0.047998,-0.131999 0.048,-0.196"  gorn="0.8.0.0.0.0.0.0.0.7.0.0.0.0.0.0.0" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3153"/>
                                                                <path d="m 12.064563,92.428 c -3e-6,0.114667 -0.076,0.172 -0.228001,0.172 l -1.231999,0 c -0.152001,0 -0.228001,-0.05733 -0.228,-0.172 -1e-6,-0.112 0.076,-0.168 0.228,-0.168 l 0.443999,0 0,-1.988 -0.452,0 c -0.152,2e-6 -0.228,-0.05733 -0.228,-0.172 0,-0.111997 0.076,-0.167997 0.228,-0.168 l 1.24,0 c 0.151998,3e-6 0.227998,0.056 0.228001,0.168 -3e-6,0.114669 -0.076,0.172002 -0.228001,0.172 l -0.448,0 0,1.988 0.448,0 c 0.151998,0 0.227998,0.056 0.228001,0.168"  gorn="0.8.0.0.0.0.0.0.0.7.0.0.0.0.0.0.1" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3155"/>
                                                                <path d="m 14.545125,92.436 c -2e-6,0.04267 -0.01734,0.08133 -0.052,0.116 -0.03467,0.032 -0.07467,0.048 -0.12,0.048 -0.06133,0 -0.118668,-0.03867 -0.172,-0.116 l -0.932,-1.332 -0.08,0 0,1.22 c -1e-6,0.152 -0.056,0.228 -0.168,0.228 -0.114667,0 -0.172,-0.06267 -0.172,-0.188 l 0,-2.48 1.192,0 c 0.141332,3e-6 0.259998,0.052 0.356,0.156 0.09866,0.104002 0.147998,0.230669 0.148,0.38 l 0,0.152 c -2e-6,0.157335 -0.05067,0.285335 -0.152,0.384 -0.09867,0.09867 -0.226668,0.148001 -0.384,0.148 l -0.324,0 0.796,1.14 c 0.04266,0.06133 0.064,0.109334 0.064,0.144 m -0.34,-1.816 0,-0.132 c -2e-6,-0.143998 -0.07067,-0.215998 -0.212,-0.216 l -0.804,0 0,0.54 0.804,0 c 0.141332,2e-6 0.211998,-0.064 0.212,-0.192"  gorn="0.8.0.0.0.0.0.0.0.7.0.0.0.0.0.0.2" style="font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3157"/>
                                                            </g>
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.8" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3409">
                                        <path d="m 37.338,82.778 c -2e-6,0.05867 -0.01067,0.116002 -0.032,0.172 l -0.652,1.688 c -0.02934,0.07467 -0.08267,0.112 -0.16,0.112 -0.08,0 -0.134668,-0.03733 -0.164,-0.112 L 35.674,82.95 c -0.008,-0.016 -0.012,-0.028 -0.012,-0.036 -0.01333,-0.032 -0.02,-0.07733 -0.02,-0.136 l 0,-0.468 c 0,-0.151997 0.05733,-0.227997 0.172,-0.228 0.111999,3e-6 0.167999,0.076 0.168,0.228 l 0,0.492 0.508,1.308 0.508,-1.308 0,-0.496 c -2e-6,-0.149331 0.05733,-0.223997 0.172,-0.224 0.111998,3e-6 0.167998,0.07467 0.168,0.224 l 0,0.472"  gorn="0.8.0.0.0.0.0.0.0.8.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3160"/>
                                        <path d="m 39.814562,84.522 c -2e-6,0.152 -0.05734,0.228 -0.172,0.228 -0.112001,0 -0.168001,-0.076 -0.168,-0.228 l 0,-1.968 -0.34,0.484 0,0.032 c -1e-6,0.152002 -0.056,0.228001 -0.167999,0.228 -0.114668,10e-7 -0.172002,-0.076 -0.172001,-0.228 l 0,-0.032 -0.336,-0.484 0,1.968 c 0,0.152 -0.056,0.228 -0.168,0.228 -0.114667,0 -0.172,-0.076 -0.171999,-0.228 l 0,-2.44 0.431999,0 0.416001,0.604 0.415999,-0.604 0.432,0 0,2.44"  gorn="0.8.0.0.0.0.0.0.0.8.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3162"/>
                                        <path d="m 42.291125,83.418 c -2e-6,0.122668 -0.032,0.248001 -0.096,0.376 l -0.352,0.708 c -0.03467,0.072 -0.08933,0.132 -0.164,0.18 -0.07467,0.04533 -0.152001,0.068 -0.232,0.068 -0.184001,0 -0.320001,-0.08667 -0.408,-0.26 l -0.356,-0.708 c -0.05867,-0.117332 -0.088,-0.239999 -0.088,-0.368 0,-0.119999 0.02533,-0.230665 0.076,-0.332 l 0.368,-0.744 c 0.08533,-0.170664 0.222666,-0.255997 0.412,-0.256 0.07733,3e-6 0.151999,0.02267 0.224,0.068 0.07466,0.04534 0.129332,0.102669 0.164,0.172 l 0.38,0.76 c 0.048,0.096 0.072,0.208001 0.072,0.336 m -0.34,-0.004 c -2e-6,-0.06933 -0.02134,-0.146665 -0.064,-0.232 l -0.348,-0.696 c -0.01867,-0.04 -0.05067,-0.06 -0.096,-0.06 -0.048,2e-6 -0.08133,0.02 -0.1,0.06 l -0.34,0.684 c -0.04533,0.09067 -0.068,0.173335 -0.068,0.248 -10e-7,0.06667 0.02267,0.146668 0.068,0.24 l 0.332,0.668 c 0.02667,0.05333 0.064,0.08 0.112,0.08 0.04,0 0.072,-0.02267 0.096,-0.068 l 0.364,-0.724 c 0.02933,-0.05867 0.044,-0.125332 0.044,-0.2"  gorn="0.8.0.0.0.0.0.0.0.8.2" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3164"/>
                                        <path d="m 44.767687,82.526 c -2e-6,0.125335 -0.056,0.188002 -0.167999,0.188 -0.114669,2e-6 -0.172002,-0.076 -0.172001,-0.228 l 0,-0.064 -0.34,0 0,2.136 c -1e-6,0.125333 -0.056,0.188 -0.167999,0.188 -0.114668,0 -0.172002,-0.076 -0.172001,-0.228 l 0,-2.096 -0.336,0 0,0.068 c 0,0.149335 -0.056,0.224002 -0.168,0.224 -0.114667,2e-6 -0.172,-0.07466 -0.171999,-0.224 l 0,-0.408 1.695999,0 0,0.444"  gorn="0.8.0.0.0.0.0.0.0.8.3" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3166"/>
                                    </g>
                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.9" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3409-8">
                                        <path d="m 39.680867,93.710055 c -2e-6,0.133333 -0.05067,0.249333 -0.152,0.348 -0.101335,0.09867 -0.220002,0.148 -0.356,0.148 l -0.676,0 c -0.146667,0 -0.269334,-0.04933 -0.368,-0.148 -0.096,-0.09867 -0.144,-0.221333 -0.144,-0.368 l 0,-0.94 c 0,-0.151999 0.052,-0.294665 0.156,-0.428 l 0.452,-0.584 c 0.103999,-0.133331 0.242666,-0.199998 0.416,-0.2 l 0.44,0 c 0.151998,2e-6 0.227998,0.056 0.228,0.168 -2e-6,0.114669 -0.076,0.172002 -0.228,0.172 l -0.396,0 c -0.06667,2e-6 -0.110668,0.0053 -0.132,0.016 -0.01867,0.008 -0.048,0.03867 -0.088,0.092 l -0.424,0.548 c -0.056,0.072 -0.084,0.158668 -0.084,0.26 l 0,0.868 c -10e-7,0.136 0.06667,0.204 0.2,0.204 l 0.628,0 c 0.125332,0 0.187998,-0.068 0.188,-0.204 l 0,-0.324 -0.284,0 c -0.152001,10e-7 -0.228001,-0.056 -0.228,-0.168 -1e-6,-0.114666 0.076,-0.171999 0.228,-0.172 l 0.624,0 0,0.712"  gorn="0.8.0.0.0.0.0.0.0.9.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3169"/>
                                        <path d="m 42.15343,94.206055 -0.452,0 -0.904,-2.056 0,1.828 c -10e-7,0.152 -0.056,0.228 -0.168,0.228 -0.114667,0 -0.172001,-0.076 -0.172,-0.228 l 0,-2.44 0.452,0 0.904,2.08 0,-1.852 c -2e-6,-0.151998 0.056,-0.227998 0.168,-0.228 0.114664,2e-6 0.171998,0.076 0.172,0.228 l 0,2.44"  gorn="0.8.0.0.0.0.0.0.0.9.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3171"/>
                                        <path d="m 44.625992,92.862055 c -2e-6,0.133334 -0.02667,0.253334 -0.08,0.36 l -0.348,0.7 c -0.09333,0.189333 -0.254668,0.284 -0.484,0.284 l -0.556,0 c -0.152,0 -0.228,-0.05733 -0.228,-0.172 0,-0.112 0.076,-0.168 0.228,-0.168 l 0.112,0 0,-1.988 -0.112,0 c -0.152,2e-6 -0.228,-0.05733 -0.228,-0.172 0,-0.111998 0.076,-0.167998 0.228,-0.168 l 0.588,0 c 0.207999,2e-6 0.361332,0.100002 0.46,0.3 l 0.336,0.684 c 0.056,0.114668 0.084,0.228001 0.084,0.34 m -0.34,0.012 c -2e-6,-0.064 -0.02267,-0.141332 -0.068,-0.232 l -0.324,-0.656 c -0.03467,-0.072 -0.09333,-0.107998 -0.176,-0.108 l -0.108,0 0,1.988 0.116,0 c 0.08267,0 0.141332,-0.036 0.176,-0.108 l 0.336,-0.688 c 0.032,-0.06667 0.048,-0.131999 0.048,-0.196"  gorn="0.8.0.0.0.0.0.0.0.9.2" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3173"/>
                                    </g>
                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.10" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3409-3">
                                        <path d="m 43.176867,102.53405 c -2e-6,0.11466 -0.076,0.172 -0.228,0.172 l -1.468,0 0,-1.16 c 0,-0.0987 0.032,-0.18 0.096,-0.244 0.06667,-0.0667 0.149333,-0.1 0.248,-0.1 l 1.008,0 0,-0.824 -1.124,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.112 0.076,-0.168 0.228,-0.168 l 1.124,0 c 0.09866,0 0.179998,0.0347 0.244,0.104 0.06667,0.0667 0.1,0.15067 0.1,0.252 l 0,0.808 c -2e-6,0.0987 -0.03334,0.18133 -0.1,0.248 -0.064,0.064 -0.145335,0.096 -0.244,0.096 l -1.008,0 0,0.82 1.124,0 c 0.151998,0 0.227998,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.10.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3176"/>
                                        <path d="m 45.65743,101.99405 c -2e-6,0.208 -0.06534,0.37866 -0.196,0.512 -0.130669,0.13333 -0.297335,0.2 -0.5,0.2 l -1,0 0,-2.668 1.016,0 c 0.205331,0 0.369331,0.0693 0.492,0.208 0.125331,0.13867 0.187998,0.32133 0.188,0.548 -2e-6,0.25333 -0.076,0.448 -0.228,0.584 0.088,0.0853 0.147998,0.17066 0.18,0.256 0.032,0.0853 0.048,0.20533 0.048,0.36 m -0.34,-1.212 c -2e-6,-0.26933 -0.124002,-0.404 -0.372,-0.404 l -0.644,0 0,0.828 0.648,0 c 0.245331,0 0.367998,-0.14133 0.368,-0.424 m 0,1.172 c -2e-6,-0.272 -0.125335,-0.408 -0.376,-0.408 l -0.64,0 0,0.82 0.648,0 c 0.245331,0 0.367998,-0.13734 0.368,-0.412"  gorn="0.8.0.0.0.0.0.0.0.10.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3178"/>
                                    </g>
                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.11" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3409-3-2">
                                        <path d="m 42.937609,111.81238 c -2e-6,0.11467 -0.076,0.172 -0.228,0.172 l -1.468,0 0,-1.16 c 0,-0.0987 0.032,-0.18 0.096,-0.244 0.06667,-0.0667 0.149333,-0.1 0.248,-0.1 l 1.008,0 0,-0.824 -1.124,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.11199 0.076,-0.16799 0.228,-0.168 l 1.124,0 c 0.09866,1e-5 0.179998,0.0347 0.244,0.104 0.06667,0.0667 0.1,0.15067 0.1,0.252 l 0,0.808 c -2e-6,0.0987 -0.03334,0.18134 -0.1,0.248 -0.064,0.064 -0.145335,0.096 -0.244,0.096 l -1.008,0 0,0.82 1.124,0 c 0.151998,0 0.227998,0.056 0.228,0.168"  gorn="0.8.0.0.0.0.0.0.0.11.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3181"/>
                                        <path d="m 45.410172,111.82038 c -2e-6,0.0453 -0.01734,0.0853 -0.052,0.12 -0.032,0.032 -0.07067,0.048 -0.116,0.048 -0.08267,0 -0.141335,-0.06 -0.176,-0.18 l -0.12,-0.4 -0.76,0 -0.116,0.4 c -0.03467,0.12 -0.09467,0.18 -0.18,0.18 -0.04533,0 -0.08533,-0.016 -0.12,-0.048 -0.032,-0.0347 -0.048,-0.0747 -0.048,-0.12 -10e-7,-0.0267 0.0067,-0.0627 0.02,-0.108 l 0.664,-2.26 c 0.02667,-0.088 0.08133,-0.13199 0.164,-0.132 0.08266,1e-5 0.137332,0.044 0.164,0.132 l 0.656,2.26 c 0.01333,0.0453 0.02,0.0813 0.02,0.108 m -0.56,-0.752 -0.284,-0.964 -0.28,0.964 0.564,0"  gorn="0.8.0.0.0.0.0.0.0.11.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3183"/>
                                    </g>
                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.12" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3409-3-7">
                                        <path d="m 43.191609,121.30038 c -2e-6,0.12267 -0.05333,0.184 -0.16,0.184 l -1.308,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.112 0.076,-0.168 0.228,-0.168 l 0.448,0 0,-1.988 -0.448,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.11199 0.076,-0.16799 0.228,-0.168 l 0.788,0 0,2.328 0.34,0 0,-0.644 c -1e-6,-0.14933 0.05733,-0.224 0.172,-0.224 0.111998,0 0.167998,0.0747 0.168,0.224 l 0,0.8"  gorn="0.8.0.0.0.0.0.0.0.12.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3186"/>
                                        <path d="m 45.660172,121.32038 c -2e-6,0.0453 -0.01734,0.0853 -0.052,0.12 -0.032,0.032 -0.07067,0.048 -0.116,0.048 -0.08267,0 -0.141335,-0.06 -0.176,-0.18 l -0.12,-0.4 -0.76,0 -0.116,0.4 c -0.03467,0.12 -0.09467,0.18 -0.18,0.18 -0.04533,0 -0.08533,-0.016 -0.12,-0.048 -0.032,-0.0347 -0.048,-0.0747 -0.048,-0.12 -10e-7,-0.0267 0.0067,-0.0627 0.02,-0.108 l 0.664,-2.26 c 0.02667,-0.088 0.08133,-0.13199 0.164,-0.132 0.08266,1e-5 0.137332,0.044 0.164,0.132 l 0.656,2.26 c 0.01333,0.0453 0.02,0.0813 0.02,0.108 m -0.56,-0.752 -0.284,-0.964 -0.28,0.964 0.564,0"  gorn="0.8.0.0.0.0.0.0.0.12.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3188"/>
                                    </g>
                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.13" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3409-3-0">
                                        <path d="m 42.941609,130.55037 c -2e-6,0.12267 -0.05333,0.184 -0.16,0.184 l -1.308,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.11199 0.076,-0.16799 0.228,-0.168 l 0.448,0 0,-1.988 -0.448,0 c -0.152,1e-5 -0.228,-0.0573 -0.228,-0.172 0,-0.11199 0.076,-0.16799 0.228,-0.168 l 0.788,0 0,2.328 0.34,0 0,-0.644 c -1e-6,-0.14933 0.05733,-0.22399 0.172,-0.224 0.111998,1e-5 0.167998,0.0747 0.168,0.224 l 0,0.8"  gorn="0.8.0.0.0.0.0.0.0.13.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3191"/>
                                        <path d="m 45.418172,130.02237 c -2e-6,0.20801 -0.06533,0.37867 -0.196,0.512 -0.130669,0.13334 -0.297335,0.2 -0.5,0.2 l -1,0 0,-2.668 1.016,0 c 0.205332,1e-5 0.369331,0.0693 0.492,0.208 0.125331,0.13867 0.187998,0.32134 0.188,0.548 -2e-6,0.25334 -0.076,0.44801 -0.228,0.584 0.088,0.0853 0.147998,0.17067 0.18,0.256 0.032,0.0853 0.048,0.20534 0.048,0.36 m -0.34,-1.212 c -2e-6,-0.26933 -0.124002,-0.40399 -0.372,-0.404 l -0.644,0 0,0.828 0.648,0 c 0.245332,10e-6 0.367998,-0.14133 0.368,-0.424 m 0,1.172 c -2e-6,-0.27199 -0.125335,-0.40799 -0.376,-0.408 l -0.64,0 0,0.82 0.648,0 c 0.245332,1e-5 0.367998,-0.13733 0.368,-0.412"  gorn="0.8.0.0.0.0.0.0.0.13.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3193"/>
                                    </g>
                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.14" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3409-3-5">
                                        <path d="m 40.437609,137.26237 c -2e-6,0.0587 -0.01067,0.11601 -0.032,0.172 l -0.652,1.688 c -0.02933,0.0747 -0.08267,0.112 -0.16,0.112 -0.08,0 -0.134667,-0.0373 -0.164,-0.112 l -0.656,-1.688 c -0.008,-0.016 -0.012,-0.028 -0.012,-0.036 -0.01333,-0.032 -0.02,-0.0773 -0.02,-0.136 l 0,-0.468 c 0,-0.15199 0.05733,-0.22799 0.172,-0.228 0.112,1e-5 0.168,0.076 0.168,0.228 l 0,0.492 0.508,1.30801 0.508,-1.30801 0,-0.496 c -10e-7,-0.14933 0.05733,-0.22399 0.172,-0.224 0.111998,1e-5 0.167998,0.0747 0.168,0.224 l 0,0.472"  gorn="0.8.0.0.0.0.0.0.0.14.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3196"/>
                                        <path d="m 42.910172,137.89037 c -2e-6,0.13334 -0.02667,0.25334 -0.08,0.36 l -0.348,0.7 c -0.09333,0.18934 -0.254668,0.284 -0.484,0.284 l -0.556,0 c -0.152001,0 -0.228001,-0.0573 -0.228,-0.172 -10e-7,-0.11199 0.076,-0.16799 0.228,-0.168 l 0.112,0 0,-1.988 -0.112,0 c -0.152001,1e-5 -0.228001,-0.0573 -0.228,-0.172 -10e-7,-0.11199 0.076,-0.16799 0.228,-0.168 l 0.588,0 c 0.207998,1e-5 0.361332,0.10001 0.46,0.3 l 0.336,0.684 c 0.056,0.11467 0.084,0.22801 0.084,0.34 m -0.34,0.012 c -2e-6,-0.064 -0.02267,-0.14133 -0.068,-0.232 l -0.324,-0.656 c -0.03467,-0.072 -0.09334,-0.10799 -0.176,-0.108 l -0.108,0 0,1.988 0.116,0 c 0.08267,1e-5 0.141332,-0.036 0.176,-0.108 l 0.336,-0.688 c 0.032,-0.0667 0.048,-0.13199 0.048,-0.196"  gorn="0.8.0.0.0.0.0.0.0.14.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3198"/>
                                        <path d="m 45.386734,137.89037 c -2e-6,0.13334 -0.02667,0.25334 -0.08,0.36 l -0.348,0.7 c -0.09334,0.18934 -0.254668,0.284 -0.484,0.284 l -0.556,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.11199 0.076,-0.16799 0.228,-0.168 l 0.112,0 0,-1.988 -0.112,0 c -0.152,1e-5 -0.228,-0.0573 -0.228,-0.172 0,-0.11199 0.076,-0.16799 0.228,-0.168 l 0.588,0 c 0.207999,1e-5 0.361332,0.10001 0.46,0.3 l 0.336,0.684 c 0.056,0.11467 0.084,0.22801 0.084,0.34 m -0.34,0.012 c -10e-7,-0.064 -0.02267,-0.14133 -0.068,-0.232 l -0.324,-0.656 c -0.03467,-0.072 -0.09333,-0.10799 -0.176,-0.108 l -0.108,0 0,1.988 0.116,0 c 0.08267,1e-5 0.141332,-0.036 0.176,-0.108 l 0.336,-0.688 c 0.032,-0.0667 0.048,-0.13199 0.048,-0.196"  gorn="0.8.0.0.0.0.0.0.0.14.2" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3200"/>
                                    </g>
                                    <g fill="#ffffff"  font-size="4" stroke="none" gorn="0.8.0.0.0.0.0.0.0.15" fill-opacity="1" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:50%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;font-family:Droid Sans;-inkscape-font-specification:Droid Sans" id="text3491">
                                        <path d="m 39.592,148.004 c -2e-6,0.13333 -0.05067,0.24933 -0.152,0.348 -0.101335,0.0987 -0.220002,0.148 -0.356,0.148 l -0.676,0 c -0.146667,0 -0.269334,-0.0493 -0.368,-0.148 -0.096,-0.0987 -0.144,-0.22133 -0.144,-0.368 l 0,-0.94 c 0,-0.152 0.052,-0.29466 0.156,-0.428 l 0.452,-0.584 c 0.103999,-0.13333 0.242665,-0.2 0.416,-0.2 l 0.44,0 c 0.151998,0 0.227998,0.056 0.228,0.168 -2e-6,0.11467 -0.076,0.172 -0.228,0.172 l -0.396,0 c -0.06667,0 -0.110668,0.005 -0.132,0.016 -0.01867,0.008 -0.048,0.0387 -0.088,0.092 l -0.424,0.548 c -0.056,0.072 -0.084,0.15867 -0.084,0.26 l 0,0.868 c -10e-7,0.136 0.06667,0.204 0.2,0.204 l 0.628,0 c 0.125332,0 0.187998,-0.068 0.188,-0.204 l 0,-0.324 -0.284,0 c -0.152001,0 -0.228001,-0.056 -0.228,-0.168 -1e-6,-0.11467 0.076,-0.172 0.228,-0.172 l 0.624,0 0,0.712"  gorn="0.8.0.0.0.0.0.0.0.15.0" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3203"/>
                                        <path d="m 42.064562,148.5 -0.451999,0 -0.904001,-2.056 0,1.828 c 0,0.152 -0.056,0.228 -0.168,0.228 -0.114667,0 -0.172,-0.076 -0.171999,-0.228 l 0,-2.44 0.451999,0 0.904,2.08 0,-1.852 c -10e-7,-0.152 0.056,-0.228 0.168,-0.228 0.114665,0 0.171998,0.076 0.172,0.228 l 0,2.44"  gorn="0.8.0.0.0.0.0.0.0.15.1" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3205"/>
                                        <path d="m 44.537125,147.156 c -2e-6,0.13333 -0.02667,0.25333 -0.08,0.36 l -0.348,0.7 c -0.09333,0.18933 -0.254668,0.284 -0.484,0.284 l -0.556,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.112 0.076,-0.168 0.228,-0.168 l 0.112,0 0,-1.988 -0.112,0 c -0.152,0 -0.228,-0.0573 -0.228,-0.172 0,-0.112 0.076,-0.168 0.228,-0.168 l 0.588,0 c 0.207999,0 0.361332,0.1 0.46,0.3 l 0.336,0.684 c 0.056,0.11467 0.084,0.228 0.084,0.34 m -0.34,0.012 c -2e-6,-0.064 -0.02267,-0.14133 -0.068,-0.232 l -0.324,-0.656 c -0.03467,-0.072 -0.09333,-0.108 -0.176,-0.108 l -0.108,0 0,1.988 0.116,0 c 0.08267,0 0.141332,-0.036 0.176,-0.108 l 0.336,-0.688 c 0.032,-0.0667 0.048,-0.132 0.048,-0.196"  gorn="0.8.0.0.0.0.0.0.0.15.2" style="line-height:50%;font-family:Droid Sans;-inkscape-font-specification:Droid Sans;fill:#ffffff" id="path3207"/>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>
</svg>


## svg.pcb.0223_4ed19ade2e699853070a13a613764d44_1_pcb.svg

<?xml version='1.0' encoding='utf-8'?>
<!-- Generator: Adobe Illustrator 13.0.2, SVG Export Plug-In . SVG Version: 6.00 Build 14948)  -->
<svg xmlns="http://www.w3.org/2000/svg" height="0.804639in" width="0.611111in" xmlns:xml="http://www.w3.org/XML/1998/namespace" viewBox="0 0 44 57.934"  x="0px" y="0px" gorn="0" version="1.2" xml:space="preserve" baseProfile="tiny" id="Layer_3">
    <desc >
        <referenceFile >A4988 Stepper Motor Driver Carrier_pcb.svg</referenceFile>
    </desc>
    <g  gorn="0.1" id="copper0">
        <g  gorn="0.1.0" id="copper1">
            <circle r="1.6" fill="none" cx="3.17" cy="3.7"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.0" id="connector130"/>
            <circle r="1.6" fill="none" cx="3.17" cy="10.85"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.1" id="connector131"/>
            <circle r="1.6" fill="none" cx="3.17" cy="18"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.2" id="connector132"/>
            <circle r="1.6" fill="none" cx="3.17" cy="25.15"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.3" id="connector133"/>
            <circle r="1.6" fill="none" cx="3.17" cy="32.3"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.4" id="connector134"/>
            <circle r="1.6" fill="none" cx="3.17" cy="39.45"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.5" id="connector135"/>
            <circle r="1.6" fill="none" cx="3.17" cy="46.6"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.6" id="connector136"/>
            <circle r="1.6" fill="none" cx="3.17" cy="53.75"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.7" id="connector137"/>
            <circle r="1.6" fill="none" cx="39.1" cy="3.7"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.8" id="connector140"/>
            <circle r="1.6" fill="none" cx="39.1" cy="10.85"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.9" id="connector141"/>
            <circle r="1.6" fill="none" cx="39.1" cy="18"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.10" id="connector142"/>
            <circle r="1.6" fill="none" cx="39.1" cy="25.15"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.11" id="connector143"/>
            <circle r="1.6" fill="none" cx="39.1" cy="32.3"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.12" id="connector144"/>
            <circle r="1.6" fill="none" cx="39.1" cy="39.45"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.13" id="connector145"/>
            <circle r="1.6" fill="none" cx="39.1" cy="46.6"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.14" id="connector146"/>
            <circle r="1.6" fill="none" cx="39.1" cy="53.75"  stroke-width="0.2" stroke="#000000" gorn="0.1.0.15" id="connector147"/>
        </g>
    </g>
</svg>


## svg.schematic.0223_4ed19ade2e699853070a13a613764d44_1_schematic.svg

<?xml version='1.0' encoding='utf-8'?>
<!DOCTYPE svg>
<!-- Generator: Adobe Illustrator 12.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 51448)  -->
<svg xmlns="http://www.w3.org/2000/svg" height="87.9" width="88.1" xmlns:xml="http://www.w3.org/XML/1998/namespace" viewBox="0 0 88.1 87.9"  enable-background="new 0 14.5 88.1 87.9" gorn="0" version="1.1" overflow="visible" xml:space="preserve" id="Layer_1">
    <desc >
        <referenceFile >A4988 S M D C Schematic.svg</referenceFile>
    </desc>
    <g transform="translate(0,-14.5)" >
        <g >
            <g >
                <g >
                    <g transform="translate(0,-79.004003)" >
                        <g >
                            <g >
                                <g >
                                    <g >
                                        <g >
                                            <g  gorn="0.1.0.0.0.0.0.0.0.0.0.0" id="layer1">
                                                <rect height="72" width="54" fill="#FFFFFF"  x="17.753" y="102.048" stroke-width="1" stroke="#000000" gorn="0.1.0.0.0.0.0.0.0.0.0.0.0" id="rect3134"/>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                    <g transform="translate(0,-79.004003)" >
                        <g >
                            <g >
                                <g >
                                    <g >
                                        <g >
                                            <g >
                                                <g >
                                                    <g >
                                                        <g transform="translate(0.6904297,1.863209)" >
                                                            <g >
                                                                <g >
                                                                    <g >
                                                                        <g >
                                                                            <g >
                                                                                <g >
                                                                                    <path fill="#8C8C8C" d="M22.656,106.328c0,0.115-0.099,0.172-0.295,0.172h-1.897v-2.668h1.897c0.196,0,0.295,0.056,0.295,0.168c0,0.115-0.099,0.172-0.295,0.172h-1.458V105h0.59c0.196,0,0.294,0.056,0.294,0.168c0,0.115-0.098,0.172-0.294,0.172h-0.59v0.82h1.458C22.557,106.16,22.656,106.216,22.656,106.328" />
                                                                                    <path fill="#8C8C8C" d="M25.858,106.5h-0.585l-1.168-2.056v1.828c0,0.152-0.072,0.228-0.217,0.228c-0.148,0-0.222-0.076-0.222-0.228v-2.44h0.583l1.169,2.08v-1.852c0-0.152,0.072-0.228,0.217-0.228c0.148,0,0.222,0.076,0.222,0.228V106.5" />
                                                                                    <path fill="#8C8C8C" d="M29.055,106.336c0,0.045-0.022,0.085-0.067,0.12c-0.041,0.032-0.091,0.048-0.15,0.048c-0.107,0-0.183-0.06-0.228-0.18l-0.155-0.4h-0.983l-0.15,0.4c-0.045,0.12-0.123,0.18-0.232,0.18c-0.059,0-0.11-0.016-0.155-0.048c-0.042-0.035-0.062-0.075-0.062-0.12c0-0.026,0.009-0.063,0.025-0.108l0.858-2.26c0.035-0.088,0.105-0.132,0.213-0.132c0.107,0,0.177,0.044,0.212,0.132l0.848,2.26C29.045,106.273,29.055,106.309,29.055,106.336 M28.331,105.584l-0.368-0.964l-0.361,0.964H28.331" />
                                                                                </g>
                                                                            </g>
                                                                        </g>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                        <g transform="translate(0.71972661,1.6112559)" >
                                                            <g >
                                                                <g >
                                                                    <g >
                                                                        <g >
                                                                            <g >
                                                                                <g >
                                                                                    <path fill="#8C8C8C" d="M22.665,115.772c0,0.152-0.074,0.228-0.223,0.228c-0.145,0-0.217-0.076-0.217-0.228v-1.968l-0.44,0.484v0.032c0,0.152-0.072,0.228-0.217,0.228c-0.149,0-0.223-0.076-0.223-0.228v-0.032l-0.434-0.484v1.968c0,0.152-0.073,0.228-0.217,0.228c-0.149,0-0.222-0.076-0.222-0.228v-2.44h0.558l0.538,0.604l0.538-0.604h0.559V115.772" />
                                                                                    <path fill="#8C8C8C" d="M25.867,115.616c0,0.106-0.051,0.197-0.15,0.272C25.62,115.963,25.5,116,25.36,116h-1.085c-0.159,0-0.297-0.042-0.419-0.128c-0.117-0.085-0.176-0.184-0.176-0.296c0-0.131,0.077-0.196,0.228-0.196c0.122,0,0.191,0.064,0.212,0.192c0.01,0.059,0.057,0.088,0.14,0.088h1.071c0.062,0,0.093-0.013,0.093-0.04c0-0.013-0.015-0.036-0.046-0.068l-1.588-1.584c-0.077-0.075-0.114-0.157-0.114-0.248c0-0.115,0.05-0.208,0.15-0.28c0.103-0.072,0.236-0.108,0.398-0.108h1.05c0.155,0,0.292,0.045,0.409,0.136c0.12,0.088,0.181,0.189,0.181,0.304c0,0.13-0.072,0.196-0.217,0.196c-0.132,0-0.206-0.064-0.223-0.192c-0.01-0.069-0.063-0.104-0.16-0.104h-1.05c-0.062,0-0.093,0.016-0.093,0.048c0,0.016,0.011,0.036,0.036,0.06l1.588,1.584C25.825,115.446,25.867,115.53,25.867,115.616" />
                                                                                    <path fill="#8C8C8C" d="M29.074,115.816c0,0.123-0.069,0.184-0.207,0.184h-1.691c-0.197,0-0.294-0.057-0.294-0.172c0-0.112,0.098-0.168,0.294-0.168h0.579v-1.988h-0.579c-0.197,0-0.294-0.058-0.294-0.172c0-0.112,0.098-0.168,0.294-0.168h1.019v2.328h0.44v-0.644c0-0.149,0.074-0.224,0.222-0.224c0.145,0,0.218,0.075,0.218,0.224V115.816" />
                                                                                </g>
                                                                            </g>
                                                                        </g>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                        <g transform="translate(0.4697266,10.361256)" >
                                                            <g >
                                                                <g >
                                                                    <g >
                                                                        <g >
                                                                            <g >
                                                                                <g >
                                                                                    <path fill="#8C8C8C" d="M22.591,115.772c0,0.152-0.074,0.228-0.222,0.228c-0.145,0-0.217-0.076-0.217-0.228v-1.968l-0.44,0.484v0.032c0,0.152-0.072,0.228-0.218,0.228c-0.148,0-0.222-0.076-0.222-0.228v-0.032l-0.434-0.484v1.968c0,0.152-0.073,0.228-0.217,0.228c-0.149,0-0.223-0.076-0.223-0.228v-2.44h0.559l0.538,0.604l0.539-0.604h0.558V115.772" />
                                                                                    <path fill="#8C8C8C" d="M25.793,115.616c0,0.106-0.05,0.197-0.15,0.272c-0.097,0.075-0.216,0.112-0.357,0.112h-1.086c-0.159,0-0.297-0.042-0.419-0.128c-0.118-0.085-0.175-0.184-0.175-0.296c0-0.131,0.076-0.196,0.227-0.196c0.122,0,0.191,0.064,0.212,0.192c0.011,0.059,0.057,0.088,0.14,0.088h1.071c0.062,0,0.092-0.013,0.092-0.04c0-0.013-0.015-0.036-0.046-0.068l-1.588-1.584c-0.076-0.075-0.113-0.157-0.113-0.248c0-0.115,0.049-0.208,0.149-0.28c0.104-0.072,0.237-0.108,0.398-0.108h1.05c0.155,0,0.292,0.045,0.408,0.136c0.12,0.088,0.181,0.189,0.181,0.304c0,0.13-0.072,0.196-0.217,0.196c-0.132,0-0.206-0.064-0.223-0.192c-0.01-0.069-0.063-0.104-0.16-0.104h-1.049c-0.062,0-0.093,0.016-0.093,0.048c0,0.016,0.012,0.036,0.036,0.06l1.587,1.584C25.752,115.446,25.793,115.53,25.793,115.616" />
                                                                                    <path fill="#8C8C8C" d="M28.995,115.828c0,0.115-0.098,0.172-0.295,0.172h-1.898v-1.16c0-0.099,0.042-0.18,0.125-0.244c0.086-0.067,0.192-0.1,0.321-0.1h1.303v-0.824h-1.453c-0.197,0-0.295-0.058-0.295-0.172c0-0.112,0.099-0.168,0.295-0.168h1.453c0.128,0,0.233,0.035,0.316,0.104c0.086,0.067,0.129,0.151,0.129,0.252v0.808c0,0.099-0.043,0.182-0.129,0.248c-0.083,0.064-0.188,0.096-0.316,0.096h-1.303v0.82H28.7C28.897,115.66,28.995,115.716,28.995,115.828" />
                                                                                </g>
                                                                            </g>
                                                                        </g>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                        <g transform="translate(0.2197266,19.361256)" >
                                                            <g >
                                                                <g >
                                                                    <g >
                                                                        <g >
                                                                            <g >
                                                                                <g >
                                                                                    <path fill="#8C8C8C" d="M22.518,115.772c0,0.152-0.074,0.228-0.222,0.228c-0.146,0-0.218-0.076-0.218-0.228v-1.968l-0.44,0.484v0.032c0,0.152-0.072,0.228-0.217,0.228c-0.148,0-0.223-0.076-0.223-0.228v-0.032l-0.434-0.484v1.968c0,0.152-0.073,0.228-0.217,0.228c-0.149,0-0.222-0.076-0.222-0.228v-2.44h0.558l0.538,0.604l0.538-0.604h0.559V115.772" />
                                                                                    <path fill="#8C8C8C" d="M25.721,115.616c0,0.106-0.051,0.197-0.15,0.272c-0.097,0.075-0.216,0.112-0.356,0.112h-1.086c-0.16,0-0.298-0.042-0.42-0.128c-0.117-0.085-0.175-0.184-0.175-0.296c0-0.131,0.077-0.196,0.228-0.196c0.122,0,0.191,0.064,0.212,0.192c0.01,0.059,0.057,0.088,0.14,0.088h1.071c0.062,0,0.093-0.013,0.093-0.04c0-0.013-0.015-0.036-0.046-0.068l-1.588-1.584c-0.077-0.075-0.114-0.157-0.114-0.248c0-0.115,0.05-0.208,0.15-0.28c0.103-0.072,0.236-0.108,0.398-0.108h1.049c0.155,0,0.292,0.045,0.409,0.136c0.12,0.088,0.181,0.189,0.181,0.304c0,0.13-0.073,0.196-0.217,0.196c-0.132,0-0.206-0.064-0.223-0.192c-0.01-0.069-0.063-0.104-0.16-0.104h-1.05c-0.062,0-0.093,0.016-0.093,0.048c0,0.016,0.011,0.036,0.036,0.06l1.588,1.584C25.679,115.446,25.721,115.53,25.721,115.616" />
                                                                                    <path fill="#8C8C8C" d="M28.917,115.66c0,0.096-0.043,0.177-0.129,0.244c-0.085,0.064-0.191,0.096-0.315,0.096h-1.454c-0.196,0-0.295-0.057-0.295-0.172c0-0.112,0.099-0.168,0.295-0.168h1.454v-0.616c0-0.136-0.081-0.204-0.238-0.204h-0.776c-0.196,0-0.295-0.056-0.295-0.168c0-0.115,0.099-0.172,0.295-0.172h0.781c0.149,0,0.223-0.07,0.223-0.212v-0.616h-1.443c-0.196,0-0.295-0.058-0.295-0.172c0-0.112,0.099-0.168,0.295-0.168h1.454c0.116,0,0.218,0.029,0.305,0.088c0.086,0.059,0.129,0.128,0.129,0.208v0.744c0,0.115-0.055,0.213-0.165,0.296c0.116,0.099,0.176,0.215,0.176,0.348V115.66" />
                                                                                </g>
                                                                            </g>
                                                                        </g>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                        <g transform="translate(0.2197266,28.611256)" >
                                                            <g >
                                                                <g >
                                                                    <g >
                                                                        <g >
                                                                            <g >
                                                                                <g >
                                                                                    <path fill="#8C8C8C" d="M22.523,115.836c0,0.043-0.022,0.082-0.067,0.116C22.41,115.984,22.358,116,22.301,116c-0.079,0-0.154-0.039-0.223-0.115l-1.205-1.332H20.77v1.222c0,0.149-0.073,0.229-0.217,0.229c-0.149,0-0.223-0.063-0.223-0.188v-2.479h1.541c0.184,0,0.336,0.053,0.46,0.155c0.128,0.104,0.191,0.229,0.191,0.38v0.15c0,0.158-0.064,0.287-0.197,0.386c-0.128,0.099-0.293,0.147-0.497,0.147h-0.418l1.029,1.141C22.496,115.754,22.523,115.8,22.523,115.836 M22.083,114.019v-0.131c0-0.146-0.092-0.217-0.274-0.217h-1.04v0.539h1.04C21.991,114.213,22.083,114.148,22.083,114.019" />
                                                                                    <path fill="#8C8C8C" d="M25.721,115.828c0,0.115-0.099,0.172-0.295,0.172h-1.898v-2.668h1.898c0.196,0,0.295,0.057,0.295,0.168c0,0.115-0.099,0.172-0.295,0.172h-1.458v0.828h0.589c0.197,0,0.295,0.057,0.295,0.168c0,0.115-0.099,0.172-0.295,0.172h-0.589v0.82h1.458C25.622,115.66,25.721,115.716,25.721,115.828" />
                                                                                    <path fill="#8C8C8C" d="M28.922,115.616c0,0.106-0.05,0.197-0.15,0.272c-0.096,0.074-0.216,0.111-0.356,0.111h-1.086c-0.159,0-0.297-0.043-0.419-0.129c-0.117-0.085-0.175-0.184-0.175-0.296c0-0.131,0.076-0.194,0.228-0.194c0.122,0,0.191,0.063,0.212,0.19c0.01,0.06,0.057,0.088,0.139,0.088h1.071c0.062,0,0.093-0.014,0.093-0.04c0-0.013-0.016-0.035-0.046-0.066l-1.588-1.584c-0.077-0.076-0.114-0.158-0.114-0.248c0-0.114,0.05-0.209,0.15-0.279c0.104-0.072,0.237-0.107,0.398-0.107h1.05c0.155,0,0.292,0.045,0.408,0.137c0.12,0.088,0.182,0.188,0.182,0.305c0,0.13-0.073,0.195-0.217,0.195c-0.132,0-0.206-0.063-0.223-0.191c-0.01-0.068-0.063-0.104-0.161-0.104h-1.05c-0.062,0-0.093,0.017-0.093,0.049c0,0.016,0.011,0.035,0.036,0.06l1.588,1.584C28.88,115.447,28.922,115.531,28.922,115.616" />
                                                                                    <path fill="#8C8C8C" d="M32.125,115.828c0,0.115-0.099,0.172-0.294,0.172h-1.898v-2.668h1.898c0.196,0,0.294,0.057,0.294,0.168c0,0.115-0.099,0.172-0.294,0.172h-1.458v0.828h0.589c0.197,0,0.294,0.057,0.294,0.168c0,0.115-0.098,0.172-0.294,0.172h-0.589v0.82h1.458C32.026,115.66,32.125,115.716,32.125,115.828" />
                                                                                    <path fill="#8C8C8C" d="M35.326,113.776c0,0.125-0.073,0.188-0.218,0.188c-0.148,0-0.222-0.076-0.222-0.229v-0.063h-0.439v2.137c0,0.125-0.073,0.189-0.217,0.189c-0.149,0-0.222-0.076-0.222-0.23v-2.096h-0.435v0.067c0,0.149-0.072,0.226-0.217,0.226c-0.148,0-0.222-0.076-0.222-0.226v-0.407h2.193V113.776" />
                                                                                </g>
                                                                            </g>
                                                                        </g>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                        <g transform="translate(0.21972658,37.611256)" >
                                                            <g >
                                                                <g >
                                                                    <g >
                                                                        <g >
                                                                            <g >
                                                                                <g >
                                                                                    <path fill="#8C8C8C" d="M22.518,115.616c0,0.106-0.051,0.197-0.15,0.272c-0.097,0.074-0.216,0.111-0.357,0.111h-1.085c-0.16,0-0.298-0.043-0.42-0.13c-0.117-0.085-0.175-0.185-0.175-0.296c0-0.131,0.077-0.193,0.228-0.193c0.122,0,0.191,0.063,0.212,0.189c0.011,0.061,0.057,0.088,0.14,0.088h1.071c0.062,0,0.093-0.014,0.093-0.04c0-0.013-0.016-0.034-0.046-0.065l-1.588-1.584c-0.077-0.076-0.114-0.158-0.114-0.248c0-0.115,0.05-0.209,0.15-0.28c0.103-0.072,0.236-0.108,0.398-0.108h1.05c0.155,0,0.292,0.045,0.409,0.137c0.121,0.088,0.181,0.189,0.181,0.306c0,0.13-0.073,0.194-0.217,0.194c-0.132,0-0.206-0.063-0.223-0.19c-0.01-0.067-0.064-0.104-0.16-0.104h-1.05c-0.062,0-0.093,0.018-0.093,0.049c0,0.017,0.012,0.035,0.036,0.061l1.588,1.584C22.476,115.447,22.518,115.531,22.518,115.616" />
                                                                                    <path fill="#8C8C8C" d="M25.715,115.828c0,0.115-0.099,0.172-0.294,0.172h-1.888v-2.436c0-0.152,0.072-0.229,0.218-0.229c0.148,0,0.222,0.074,0.222,0.229v2.096h1.449C25.616,115.66,25.715,115.716,25.715,115.828" />
                                                                                    <path fill="#8C8C8C" d="M28.922,115.828c0,0.115-0.099,0.172-0.294,0.172h-1.898v-2.668h1.898c0.196,0,0.294,0.057,0.294,0.168c0,0.115-0.099,0.172-0.294,0.172h-1.458v0.828h0.589c0.196,0,0.295,0.057,0.295,0.168c0,0.115-0.099,0.172-0.295,0.172h-0.589v0.82h1.458C28.823,115.66,28.922,115.716,28.922,115.828" />
                                                                                    <path fill="#8C8C8C" d="M32.125,115.828c0,0.115-0.099,0.172-0.294,0.172h-1.898v-2.668h1.898c0.196,0,0.294,0.057,0.294,0.168c0,0.115-0.099,0.172-0.294,0.172h-1.458v0.828h0.589c0.197,0,0.294,0.057,0.294,0.168c0,0.115-0.098,0.172-0.294,0.172h-0.589v0.82h1.458C32.026,115.66,32.125,115.716,32.125,115.828" />
                                                                                    <path fill="#8C8C8C" d="M35.331,114.427c0,0.176-0.063,0.313-0.191,0.412s-0.305,0.146-0.533,0.146h-1.035v0.784c0,0.147-0.072,0.224-0.217,0.224c-0.065,0-0.119-0.016-0.16-0.048c-0.041-0.032-0.062-0.079-0.062-0.132v-2.482h1.53c0.199,0,0.36,0.049,0.481,0.146c0.124,0.099,0.186,0.229,0.186,0.396V114.427 M34.891,114.427v-0.553c0-0.137-0.089-0.203-0.269-0.203h-1.05v0.977h1.066C34.807,114.648,34.891,114.574,34.891,114.427" />
                                                                                </g>
                                                                            </g>
                                                                        </g>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                        <g transform="translate(0.31640627,46.611256)" >
                                                            <g >
                                                                <g >
                                                                    <g >
                                                                        <g >
                                                                            <g >
                                                                                <g >
                                                                                    <path fill="#8C8C8C" d="M22.546,115.616c0,0.106-0.05,0.197-0.15,0.272C22.299,115.963,22.18,116,22.04,116h-1.086c-0.159,0-0.297-0.043-0.419-0.13c-0.118-0.085-0.176-0.185-0.176-0.296c0-0.131,0.077-0.193,0.228-0.193c0.122,0,0.191,0.063,0.212,0.189c0.011,0.061,0.057,0.088,0.14,0.088h1.07c0.062,0,0.093-0.014,0.093-0.04c0-0.013-0.016-0.034-0.047-0.065l-1.587-1.584c-0.077-0.076-0.114-0.158-0.114-0.248c0-0.115,0.05-0.209,0.15-0.28c0.103-0.072,0.236-0.108,0.398-0.108h1.05c0.155,0,0.292,0.045,0.408,0.137c0.121,0.088,0.181,0.189,0.181,0.306c0,0.13-0.073,0.194-0.217,0.194c-0.132,0-0.206-0.063-0.223-0.19c-0.011-0.067-0.064-0.104-0.161-0.104h-1.049c-0.063,0-0.094,0.018-0.094,0.049c0,0.017,0.012,0.035,0.036,0.061l1.588,1.584C22.504,115.447,22.546,115.531,22.546,115.616" />
                                                                                    <path fill="#8C8C8C" d="M25.749,113.776c0,0.125-0.073,0.188-0.217,0.188c-0.149,0-0.223-0.076-0.223-0.229v-0.063H24.87v2.137c0,0.125-0.072,0.189-0.218,0.189c-0.148,0-0.222-0.076-0.222-0.23v-2.096h-0.435v0.067c0,0.149-0.073,0.226-0.217,0.226c-0.149,0-0.223-0.076-0.223-0.226v-0.407h2.192V113.776" />
                                                                                    <path fill="#8C8C8C" d="M28.95,115.828c0,0.115-0.098,0.172-0.294,0.172h-1.899v-2.668h1.899c0.196,0,0.294,0.057,0.294,0.168c0,0.115-0.098,0.172-0.294,0.172h-1.458v0.828h0.589c0.196,0,0.295,0.057,0.295,0.168c0,0.115-0.099,0.172-0.295,0.172h-0.589v0.82h1.458C28.852,115.66,28.95,115.716,28.95,115.828" />
                                                                                    <path fill="#8C8C8C" d="M32.158,114.427c0,0.176-0.063,0.313-0.191,0.412c-0.128,0.1-0.306,0.146-0.533,0.146H30.4v0.784c0,0.147-0.073,0.224-0.217,0.224c-0.066,0-0.119-0.016-0.16-0.048c-0.042-0.032-0.063-0.079-0.063-0.132v-2.482h1.531c0.199,0,0.359,0.049,0.481,0.146c0.124,0.099,0.186,0.229,0.186,0.396V114.427 M31.719,114.427v-0.553c0-0.137-0.09-0.203-0.269-0.203H30.4v0.977h1.065C31.633,114.648,31.719,114.574,31.719,114.427" />
                                                                                </g>
                                                                            </g>
                                                                        </g>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                        <g transform="translate(0.3164063,55.111256)" >
                                                            <g >
                                                                <g >
                                                                    <g >
                                                                        <g >
                                                                            <g >
                                                                                <g >
                                                                                    <path fill="#8C8C8C" d="M22.541,114.656c0,0.133-0.035,0.254-0.103,0.359l-0.451,0.701c-0.12,0.188-0.328,0.283-0.625,0.283h-0.719c-0.196,0-0.295-0.059-0.295-0.174c0-0.109,0.099-0.168,0.295-0.168h0.146v-1.986h-0.146c-0.196,0-0.295-0.059-0.295-0.172c0-0.111,0.099-0.168,0.295-0.168h0.761c0.269,0,0.467,0.1,0.595,0.301l0.434,0.684C22.504,114.429,22.541,114.545,22.541,114.656 M22.102,114.668c0-0.063-0.03-0.141-0.088-0.232l-0.418-0.653c-0.045-0.071-0.12-0.106-0.228-0.106h-0.139v1.986h0.15c0.107,0,0.182-0.035,0.228-0.105l0.435-0.688C22.081,114.797,22.102,114.732,22.102,114.668" />
                                                                                    <path fill="#8C8C8C" d="M25.749,115.828c0,0.115-0.098,0.172-0.294,0.172h-1.593c-0.197,0-0.295-0.057-0.295-0.172c0-0.111,0.098-0.168,0.295-0.168h0.574v-1.988H23.85c-0.196,0-0.294-0.057-0.294-0.172c0-0.111,0.098-0.168,0.294-0.168h1.604c0.196,0,0.294,0.057,0.294,0.168c0,0.115-0.098,0.172-0.294,0.172h-0.58v1.988h0.58C25.65,115.66,25.749,115.716,25.749,115.828" />
                                                                                    <path fill="#8C8C8C" d="M28.955,115.836c0,0.043-0.022,0.082-0.067,0.116c-0.044,0.032-0.097,0.048-0.154,0.048c-0.079,0-0.154-0.039-0.223-0.115l-1.205-1.332h-0.104v1.222c0,0.149-0.073,0.229-0.217,0.229c-0.149,0-0.223-0.063-0.223-0.188v-2.479h1.541c0.184,0,0.336,0.053,0.46,0.155c0.128,0.104,0.191,0.229,0.191,0.38v0.15c0,0.158-0.064,0.287-0.196,0.386c-0.128,0.099-0.293,0.147-0.497,0.147h-0.418l1.029,1.141C28.928,115.754,28.955,115.8,28.955,115.836 M28.516,114.019v-0.131c0-0.146-0.092-0.217-0.274-0.217h-1.04v0.539h1.04C28.423,114.213,28.516,114.148,28.516,114.019" />
                                                                                </g>
                                                                            </g>
                                                                        </g>
                                                                    </g>
                                                                </g>
                                                            </g>
                                                        </g>
                                                        <g >
                                                            <path fill="#8C8C8C" d="M58.333,106.178c0,0.059-0.015,0.116-0.04,0.172l-0.844,1.688c-0.035,0.075-0.106,0.112-0.204,0.112c-0.104,0-0.178-0.038-0.212-0.112l-0.849-1.688c-0.011-0.016-0.016-0.028-0.016-0.036c-0.021-0.032-0.028-0.078-0.028-0.136v-0.468c0-0.152,0.073-0.228,0.224-0.228c0.143,0,0.216,0.076,0.216,0.228v0.492l0.657,1.308l0.659-1.308v-0.496c0-0.149,0.073-0.224,0.223-0.224c0.144,0,0.218,0.075,0.218,0.224L58.333,106.178" />
                                                            <path fill="#8C8C8C" d="M61.535,107.922c0,0.152-0.073,0.228-0.222,0.228c-0.145,0-0.218-0.076-0.218-0.228v-1.968l-0.439,0.484v0.032c0,0.152-0.072,0.228-0.217,0.228c-0.148,0-0.222-0.076-0.222-0.228v-0.032l-0.436-0.484v1.968c0,0.152-0.073,0.228-0.216,0.228c-0.15,0-0.224-0.076-0.224-0.228v-2.44h0.559l0.538,0.604l0.537-0.604h0.559V107.922" />
                                                            <path fill="#8C8C8C" d="M64.737,106.818c0,0.123-0.04,0.248-0.123,0.376l-0.457,0.708c-0.044,0.072-0.117,0.132-0.213,0.18c-0.096,0.045-0.193,0.068-0.298,0.068c-0.24,0-0.414-0.087-0.527-0.26l-0.46-0.708c-0.076-0.117-0.114-0.24-0.114-0.368c0-0.12,0.033-0.231,0.098-0.332l0.477-0.744c0.111-0.171,0.287-0.256,0.532-0.256c0.1,0,0.197,0.022,0.291,0.068c0.096,0.045,0.167,0.103,0.212,0.172l0.49,0.76C64.707,106.578,64.737,106.69,64.737,106.818 M64.297,106.814c0-0.069-0.027-0.147-0.083-0.232l-0.45-0.696c-0.024-0.04-0.065-0.06-0.123-0.06c-0.063,0-0.106,0.02-0.131,0.06l-0.441,0.684c-0.058,0.091-0.085,0.173-0.085,0.248c0,0.066,0.027,0.146,0.085,0.24l0.43,0.668c0.032,0.054,0.082,0.08,0.143,0.08c0.054,0,0.094-0.022,0.127-0.068l0.47-0.724C64.28,106.955,64.297,106.888,64.297,106.814" />
                                                            <path fill="#8C8C8C" d="M67.939,105.926c0,0.125-0.072,0.188-0.217,0.188c-0.149,0-0.223-0.076-0.223-0.228v-0.064H67.06v2.136c0,0.125-0.073,0.188-0.217,0.188c-0.148,0-0.222-0.076-0.222-0.228v-2.096h-0.436v0.068c0,0.149-0.073,0.224-0.216,0.224c-0.15,0-0.224-0.075-0.224-0.224v-0.408h2.192V105.926" />
                                                        </g>
                                                        <g >
                                                            <path fill="#8C8C8C" d="M61.362,117.11c0,0.133-0.064,0.25-0.195,0.348c-0.13,0.098-0.285,0.148-0.459,0.148h-0.873c-0.188,0-0.35-0.049-0.477-0.148c-0.126-0.099-0.189-0.222-0.189-0.368v-0.94c0-0.152,0.071-0.295,0.202-0.428l0.585-0.584c0.135-0.133,0.313-0.2,0.538-0.2h0.569c0.196,0,0.294,0.056,0.294,0.168c0,0.115-0.098,0.172-0.294,0.172H60.55c-0.086,0-0.141,0.005-0.171,0.016c-0.023,0.008-0.062,0.039-0.113,0.092l-0.55,0.548c-0.07,0.072-0.108,0.158-0.108,0.26v0.868c0,0.136,0.087,0.204,0.261,0.204h0.811c0.162,0,0.242-0.068,0.242-0.204v-0.324h-0.368c-0.195,0-0.294-0.056-0.294-0.168c0-0.115,0.097-0.172,0.294-0.172h0.808L61.362,117.11" />
                                                            <path fill="#8C8C8C" d="M64.558,117.606h-0.584l-1.169-2.056v1.828c0,0.152-0.073,0.228-0.217,0.228c-0.146,0-0.223-0.076-0.223-0.228v-2.44h0.586l1.167,2.08v-1.852c0-0.152,0.073-0.228,0.218-0.228c0.146,0,0.222,0.076,0.222,0.228V117.606" />
                                                            <path fill="#8C8C8C" d="M67.755,116.262c0,0.133-0.033,0.253-0.103,0.36l-0.451,0.7c-0.121,0.189-0.328,0.284-0.625,0.284h-0.719c-0.196,0-0.297-0.058-0.297-0.172c0-0.112,0.1-0.168,0.297-0.168h0.145v-1.988h-0.145c-0.196,0-0.297-0.057-0.297-0.172c0-0.112,0.1-0.168,0.297-0.168h0.76c0.271,0,0.468,0.1,0.596,0.3l0.434,0.684C67.719,116.037,67.755,116.15,67.755,116.262 M67.316,116.274c0-0.064-0.028-0.142-0.087-0.232l-0.419-0.656c-0.046-0.072-0.121-0.108-0.229-0.108h-0.14v1.988h0.151c0.105,0,0.182-0.036,0.227-0.108l0.436-0.688C67.295,116.403,67.316,116.338,67.316,116.274" />
                                                        </g>
                                                        <g >
                                                            <path fill="#8C8C8C" d="M65.882,125.934c0,0.114-0.098,0.172-0.294,0.172h-1.899v-1.16c0-0.099,0.039-0.18,0.124-0.244c0.086-0.066,0.194-0.1,0.32-0.1h1.305v-0.824h-1.454c-0.196,0-0.295-0.057-0.295-0.172c0-0.112,0.097-0.168,0.295-0.168h1.454c0.128,0,0.232,0.035,0.314,0.104c0.085,0.066,0.13,0.15,0.13,0.252v0.808c0,0.099-0.041,0.181-0.13,0.248c-0.082,0.063-0.189,0.096-0.314,0.096h-1.305v0.82h1.455C65.785,125.766,65.882,125.822,65.882,125.934" />
                                                            <path fill="#8C8C8C" d="M69.087,125.394c0,0.208-0.083,0.378-0.252,0.512c-0.168,0.134-0.384,0.2-0.646,0.2h-1.292v-2.668h1.315c0.265,0,0.476,0.069,0.634,0.208c0.163,0.139,0.241,0.321,0.241,0.548c0,0.253-0.094,0.448-0.294,0.584c0.115,0.085,0.191,0.171,0.234,0.256C69.071,125.119,69.087,125.239,69.087,125.394 M68.649,124.182c0-0.269-0.159-0.404-0.48-0.404h-0.834v0.828h0.838C68.492,124.606,68.649,124.464,68.649,124.182 M68.649,125.354c0-0.272-0.162-0.408-0.484-0.408h-0.83v0.82h0.838C68.492,125.766,68.649,125.629,68.649,125.354" />
                                                        </g>
                                                        <g >
                                                            <path fill="#8C8C8C" d="M65.573,135.213c0,0.114-0.098,0.172-0.295,0.172H63.38v-1.16c0-0.099,0.041-0.18,0.124-0.244c0.086-0.066,0.192-0.1,0.321-0.1h1.303v-0.824h-1.453c-0.196,0-0.295-0.057-0.295-0.172c0-0.112,0.097-0.168,0.295-0.168h1.453c0.129,0,0.232,0.035,0.315,0.104c0.087,0.066,0.129,0.15,0.129,0.252v0.808c0,0.099-0.042,0.181-0.129,0.248c-0.083,0.063-0.188,0.096-0.315,0.096h-1.303v0.82h1.452C65.475,135.044,65.573,135.1,65.573,135.213" />
                                                            <path fill="#8C8C8C" d="M68.77,135.22c0,0.045-0.023,0.085-0.068,0.12c-0.04,0.032-0.091,0.048-0.149,0.048c-0.104,0-0.182-0.06-0.228-0.18l-0.156-0.4h-0.982l-0.148,0.4c-0.046,0.12-0.124,0.18-0.231,0.18c-0.063,0-0.115-0.016-0.157-0.048c-0.041-0.035-0.063-0.075-0.063-0.12c0-0.027,0.01-0.063,0.027-0.108l0.857-2.26c0.032-0.088,0.104-0.132,0.213-0.132c0.106,0,0.177,0.044,0.213,0.132l0.848,2.26C68.76,135.158,68.77,135.193,68.77,135.22 M68.045,134.468l-0.366-0.964l-0.359,0.964H68.045" />
                                                        </g>
                                                        <g >
                                                            <path fill="#8C8C8C" d="M65.901,144.701c0,0.122-0.067,0.184-0.206,0.184h-1.69c-0.196,0-0.295-0.057-0.295-0.172c0-0.11,0.099-0.168,0.295-0.168h0.578v-1.988h-0.578c-0.196,0-0.295-0.057-0.295-0.172c0-0.11,0.099-0.168,0.295-0.168h1.018v2.328h0.439V143.9c0-0.148,0.078-0.225,0.223-0.225s0.217,0.076,0.217,0.225V144.701" />
                                                            <path fill="#8C8C8C" d="M69.093,144.72c0,0.045-0.022,0.086-0.067,0.119c-0.041,0.033-0.092,0.049-0.15,0.049c-0.105,0-0.181-0.061-0.227-0.18l-0.157-0.4h-0.982l-0.148,0.4c-0.046,0.119-0.123,0.18-0.232,0.18c-0.062,0-0.113-0.016-0.156-0.049c-0.041-0.033-0.063-0.074-0.063-0.119c0-0.027,0.01-0.063,0.028-0.107l0.858-2.261c0.031-0.089,0.104-0.132,0.212-0.132c0.105,0,0.177,0.043,0.212,0.132l0.849,2.261C69.083,144.658,69.093,144.693,69.093,144.72 M68.369,143.968l-0.366-0.965l-0.359,0.965H68.369" />
                                                        </g>
                                                        <g >
                                                            <path fill="#8C8C8C" d="M65.579,153.951c0,0.122-0.069,0.184-0.208,0.184h-1.689c-0.196,0-0.295-0.057-0.295-0.172c0-0.11,0.099-0.168,0.295-0.168h0.578v-1.988h-0.578c-0.196,0-0.295-0.057-0.295-0.172c0-0.11,0.099-0.168,0.295-0.168h1.018v2.328h0.439v-0.645c0-0.148,0.077-0.225,0.223-0.225s0.218,0.076,0.218,0.225V153.951" />
                                                            <path fill="#8C8C8C" d="M68.78,153.422c0,0.209-0.083,0.379-0.253,0.512c-0.168,0.136-0.385,0.201-0.646,0.201h-1.293v-2.668h1.313c0.266,0,0.478,0.068,0.637,0.207c0.162,0.141,0.244,0.322,0.244,0.549c0,0.255-0.1,0.447-0.297,0.584c0.115,0.087,0.192,0.172,0.235,0.257C68.76,153.148,68.78,153.267,68.78,153.422 M68.34,152.211c0-0.27-0.159-0.404-0.48-0.404h-0.832v0.828h0.835C68.182,152.634,68.34,152.493,68.34,152.211 M68.34,153.382c0-0.272-0.162-0.408-0.487-0.408h-0.825v0.82h0.835C68.182,153.795,68.34,153.657,68.34,153.382" />
                                                        </g>
                                                        <g >
                                                            <path fill="#8C8C8C" d="M62.34,160.662c0,0.059-0.013,0.117-0.04,0.172l-0.841,1.688c-0.036,0.075-0.107,0.112-0.208,0.112s-0.174-0.037-0.212-0.112l-0.846-1.688c-0.01-0.016-0.018-0.027-0.018-0.035c-0.018-0.03-0.028-0.078-0.028-0.137v-0.467c0-0.152,0.076-0.229,0.226-0.229c0.142,0,0.217,0.076,0.217,0.229v0.491l0.657,1.308l0.659-1.308v-0.496c0-0.149,0.073-0.224,0.222-0.224c0.144,0,0.218,0.074,0.218,0.224v0.472" />
                                                            <path fill="#8C8C8C" d="M65.537,161.291c0,0.133-0.034,0.254-0.103,0.359l-0.45,0.699c-0.123,0.189-0.33,0.285-0.626,0.285h-0.719c-0.196,0-0.297-0.06-0.297-0.172c0-0.113,0.098-0.168,0.297-0.168h0.144v-1.988h-0.144c-0.196,0-0.297-0.057-0.297-0.172c0-0.112,0.098-0.168,0.297-0.168h0.759c0.271,0,0.468,0.1,0.597,0.299l0.435,0.686C65.502,161.065,65.537,161.177,65.537,161.291 M65.099,161.302c0-0.064-0.031-0.144-0.089-0.232l-0.42-0.656c-0.042-0.07-0.12-0.107-0.227-0.107h-0.14v1.988h0.149c0.106,0,0.185-0.035,0.227-0.106l0.436-0.688C65.078,161.431,65.099,161.367,65.099,161.302" />
                                                            <path fill="#8C8C8C" d="M68.739,161.291c0,0.133-0.034,0.254-0.103,0.359l-0.45,0.699c-0.12,0.189-0.329,0.285-0.626,0.285h-0.718c-0.196,0-0.294-0.06-0.294-0.172c0-0.113,0.096-0.168,0.294-0.168h0.145v-1.988h-0.145c-0.196,0-0.294-0.057-0.294-0.172c0-0.112,0.096-0.168,0.294-0.168h0.759c0.271,0,0.467,0.1,0.596,0.299l0.435,0.686C68.705,161.065,68.739,161.177,68.739,161.291 M68.3,161.302c0-0.064-0.03-0.144-0.088-0.232l-0.42-0.656c-0.041-0.07-0.119-0.107-0.227-0.107h-0.137v1.988h0.146c0.108,0,0.186-0.035,0.23-0.106l0.434-0.688C68.28,161.431,68.3,161.367,68.3,161.302" />
                                                        </g>
                                                        <g >
                                                            <path fill="#8C8C8C" d="M61.248,171.404c0,0.133-0.065,0.249-0.198,0.348c-0.13,0.102-0.281,0.148-0.456,0.148h-0.877c-0.188,0-0.349-0.049-0.473-0.148c-0.128-0.099-0.188-0.221-0.188-0.367v-0.938c0-0.149,0.067-0.295,0.201-0.431l0.585-0.584c0.133-0.133,0.313-0.197,0.537-0.197h0.568c0.194,0,0.295,0.057,0.295,0.168c0,0.113-0.098,0.172-0.295,0.172h-0.513c-0.086,0-0.142,0.006-0.17,0.018c-0.024,0.008-0.063,0.039-0.116,0.092l-0.548,0.549c-0.074,0.072-0.107,0.158-0.107,0.26v0.868c0,0.136,0.084,0.204,0.257,0.204h0.813c0.162,0,0.243-0.068,0.243-0.204v-0.323h-0.367c-0.193,0-0.297-0.057-0.297-0.169c0-0.114,0.099-0.172,0.297-0.172h0.807L61.248,171.404" />
                                                            <path fill="#8C8C8C" d="M64.444,171.9h-0.583l-1.166-2.057v1.828c0,0.15-0.077,0.229-0.218,0.229c-0.148,0-0.222-0.076-0.222-0.229v-2.439h0.58l1.169,2.08v-1.852c0-0.152,0.073-0.229,0.218-0.229c0.148,0,0.222,0.075,0.222,0.229V171.9" />
                                                            <path fill="#8C8C8C" d="M67.641,170.556c0,0.133-0.035,0.253-0.104,0.359l-0.45,0.698c-0.121,0.188-0.33,0.284-0.626,0.284h-0.719c-0.196,0-0.296-0.059-0.296-0.172c0-0.112,0.097-0.17,0.296-0.17h0.143v-1.986h-0.143c-0.196,0-0.296-0.059-0.296-0.172c0-0.111,0.097-0.168,0.296-0.168h0.76c0.27,0,0.468,0.102,0.597,0.3l0.434,0.687C67.606,170.332,67.641,170.444,67.641,170.556 M67.202,170.568c0-0.064-0.029-0.143-0.089-0.232l-0.418-0.656c-0.043-0.069-0.121-0.105-0.228-0.105h-0.139v1.988h0.148c0.107,0,0.185-0.036,0.228-0.107l0.435-0.689C67.182,170.697,67.202,170.632,67.202,170.568" />
                                                        </g>
                                                    </g>
                                                </g>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                    <g  gorn="0.1.0.0.0.2" id="schematic">
                        <line stroke-linecap="round" fill="none" y1="27.674" y2="27.674" x1="72" x2="78.997"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.2.0" stroke-linejoin="round" id="connector0pin"/>
                        <line stroke-linecap="round" fill="none" y1="27.674" y2="27.674" x1="81.76" x2="76.456"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.2.1" stroke-linejoin="round" id="connector140"/>
                        <g transform="matrix(0.7927 0 0 1 79.0044 26.1382)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.1539">8</text>
                                </g>
                            </g>
                        </g>
                        <line stroke-linecap="round" fill="none" y1="36.758" y2="36.758" x1="72" x2="78.997"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.2.3" stroke-linejoin="round" id="connector1pin"/>
                        <line stroke-linecap="round" fill="none" y1="36.758" y2="36.758" x1="81.76" x2="76.456"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.2.4" stroke-linejoin="round" id="connector141"/>
                        <g transform="matrix(0.7927 0 0 1 79.0044 35.2222)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.1539">7</text>
                                </g>
                            </g>
                        </g>
                        <line stroke-linecap="round" fill="none" y1="45.841" y2="45.841" x1="72" x2="78.997"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.2.6" stroke-linejoin="round" id="connector2pin"/>
                        <line stroke-linecap="round" fill="none" y1="45.841" y2="45.841" x1="81.76" x2="76.456"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.2.7" stroke-linejoin="round" id="connector142"/>
                        <g transform="matrix(0.7927 0 0 1 79.0044 44.3052)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.1539">6</text>
                                </g>
                            </g>
                        </g>
                        <line stroke-linecap="round" fill="none" y1="54.925" y2="54.925" x1="72" x2="78.997"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.2.9" stroke-linejoin="round" id="connector3pin"/>
                        <line stroke-linecap="round" fill="none" y1="54.925" y2="54.925" x1="81.76" x2="76.456"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.2.10" stroke-linejoin="round" id="connector143"/>
                        <g transform="matrix(0.7927 0 0 1 79.0044 53.3872)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.1539">5</text>
                                </g>
                            </g>
                        </g>
                        <line stroke-linecap="round" fill="none" y1="64.007" y2="64.007" x1="72" x2="78.997"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.2.12" stroke-linejoin="round" id="connector4pin"/>
                        <line stroke-linecap="round" fill="none" y1="64.007" y2="64.007" x1="81.76" x2="76.456"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.2.13" stroke-linejoin="round" id="connector144"/>
                        <g transform="matrix(0.7927 0 0 1 79.0044 62.4702)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.1539">4</text>
                                </g>
                            </g>
                        </g>
                        <line stroke-linecap="round" fill="none" y1="73.091" y2="73.091" x1="72" x2="78.997"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.2.15" stroke-linejoin="round" id="connector5pin"/>
                        <line stroke-linecap="round" fill="none" y1="73.091" y2="73.091" x1="81.76" x2="76.456"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.2.16" stroke-linejoin="round" id="connector145"/>
                        <g transform="matrix(0.7927 0 0 1 79.0044 71.5542)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.1539">3</text>
                                </g>
                            </g>
                        </g>
                        <line stroke-linecap="round" fill="none" y1="82.173" y2="82.173" x1="72" x2="78.997"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.2.18" stroke-linejoin="round" id="connector6pin"/>
                        <line stroke-linecap="round" fill="none" y1="82.173" y2="82.173" x1="81.76" x2="76.456"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.2.19" stroke-linejoin="round" id="connector146"/>
                        <g transform="matrix(0.7927 0 0 1 79.0044 80.6392)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.1539">2</text>
                                </g>
                            </g>
                        </g>
                        <line stroke-linecap="round" fill="none" y1="91.257" y2="91.257" x1="72" x2="78.997"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.2.21" stroke-linejoin="round" id="connector7pin"/>
                        <line stroke-linecap="round" fill="none" y1="91.257" y2="91.257" x1="81.76" x2="76.456"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.2.22" stroke-linejoin="round" id="connector147"/>
                        <g transform="matrix(0.7927 0 0 1 79.0044 89.7222)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.1539">1</text>
                                </g>
                            </g>
                        </g>
                    </g>
                    <g  gorn="0.1.0.0.0.3" id="schematic_1_">
                        <line stroke-linecap="round" fill="none" y1="91.459" y2="91.459" x1="17.36" x2="10.364"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.3.0" stroke-linejoin="round" id="connector0pin_1_"/>
                        <line stroke-linecap="round" fill="none" y1="91.459" y2="91.459" x1="7.6" x2="12.906"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.3.1" stroke-linejoin="round" id="connector137"/>
                        <g transform="matrix(0.7926 -0.007 0.0089 1 9.2231 89.6841)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.154">8</text>
                                </g>
                            </g>
                        </g>
                        <line stroke-linecap="round" fill="none" y1="82.375" y2="82.375" x1="17.36" x2="10.364"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.3.3" stroke-linejoin="round" id="connector1pin_1_"/>
                        <line stroke-linecap="round" fill="none" y1="82.375" y2="82.375" x1="7.6" x2="12.906"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.3.4" stroke-linejoin="round" id="connector136"/>
                        <g transform="matrix(0.7927 0.0043 -0.0055 1 9.2114 80.5894)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.1539">7</text>
                                </g>
                            </g>
                        </g>
                        <line stroke-linecap="round" fill="none" y1="73.293" y2="73.293" x1="17.36" x2="10.364"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.3.6" stroke-linejoin="round" id="connector2pin_1_"/>
                        <line stroke-linecap="round" fill="none" y1="73.293" y2="73.293" x1="7.6" x2="12.906"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.3.7" stroke-linejoin="round" id="connector135"/>
                        <g transform="matrix(0.7927 0.0022 -0.0028 1 9.2759 71.5415)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.1539">6</text>
                                </g>
                            </g>
                        </g>
                        <line stroke-linecap="round" fill="none" y1="64.209" y2="64.209" x1="17.36" x2="10.364"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.3.9" stroke-linejoin="round" id="connector3pin_1_"/>
                        <line stroke-linecap="round" fill="none" y1="64.209" y2="64.209" x1="7.6" x2="12.906"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.3.10" stroke-linejoin="round" id="connector134"/>
                        <g transform="matrix(0.7927 -0.0033 0.0042 1 9.2192 62.4322)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.1539">5</text>
                                </g>
                            </g>
                        </g>
                        <line stroke-linecap="round" fill="none" y1="55.126" y2="55.126" x1="17.36" x2="10.364"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.3.12" stroke-linejoin="round" id="connector4pin_1_"/>
                        <line stroke-linecap="round" fill="none" y1="55.126" y2="55.126" x1="7.6" x2="12.906"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.3.13" stroke-linejoin="round" id="connector133"/>
                        <g transform="matrix(0.7926 -0.0062 0.0079 1 9.2222 53.3506)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.154">4</text>
                                </g>
                            </g>
                        </g>
                        <line stroke-linecap="round" fill="none" y1="46.042" y2="46.042" x1="17.36" x2="10.364"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.3.15" stroke-linejoin="round" id="connector5pin_1_"/>
                        <line stroke-linecap="round" fill="none" y1="46.042" y2="46.042" x1="7.6" x2="12.906"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.3.16" stroke-linejoin="round" id="connector132"/>
                        <g transform="matrix(0.7927 -0.0013 0.0016 1 9.2402 44.2735)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.1539">3</text>
                                </g>
                            </g>
                        </g>
                        <line stroke-linecap="round" fill="none" y1="36.959" y2="36.959" x1="17.36" x2="10.364"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.3.18" stroke-linejoin="round" id="connector6pin_1_"/>
                        <line stroke-linecap="round" fill="none" y1="36.959" y2="36.959" x1="7.6" x2="12.906"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.3.19" stroke-linejoin="round" id="connector131"/>
                        <g transform="matrix(0.7926 0.0068 -0.0085 1 9.209 35.1714)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.154">2</text>
                                </g>
                            </g>
                        </g>
                        <line stroke-linecap="round" fill="none" y1="27.876" y2="27.876" x1="17.36" x2="10.364"  stroke-width="0.7" stroke="#000000" gorn="0.1.0.0.0.3.21" stroke-linejoin="round" id="connector7pin_1_"/>
                        <line stroke-linecap="round" fill="none" y1="27.876" y2="27.876" x1="7.6" x2="12.906"  stroke-width="0.7" stroke="#FF0000" gorn="0.1.0.0.0.3.22" stroke-linejoin="round" id="connector130"/>
                        <g transform="matrix(0.7927 7.956983e-004 -0.001 1 9.4731 25.5987)" >
                            <g >
                                <g >
                                    <text fill="#8C8C8C" font-family="Droid Sans"  font-size="3.1539">1</text>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>
</svg>
