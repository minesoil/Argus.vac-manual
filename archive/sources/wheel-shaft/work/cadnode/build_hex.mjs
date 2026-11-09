import fs from 'node:fs';
import assert from 'node:assert/strict';
import init from 'replicad-opencascadejs';
import * as r from 'replicad';
import {buildExternal,dims} from './hex_external.mjs';
import {buildWideBase} from './hex_widebase.mjs';
const oc=await init({wasmBinary:fs.readFileSync(new URL('./node_modules/replicad-opencascadejs/dist/replicad_single.wasm',import.meta.url))});r.setOC(oc);
const original=await r.importSTEP(new Blob([fs.readFileSync('../original_output.step')]));
const targetLength=process.argv.includes('--40mm')?40:process.argv.includes('--35mm')?35:null;
const reinforced=process.argv.includes('--reinforced');
const wideBase=process.argv.includes('--widebase');
const uniform=process.argv.includes('--uniform13');
if(uniform)assert(wideBase);
if(reinforced)assert.equal(targetLength,40);
if(wideBase)assert.equal(targetLength,40);
const variant=(targetLength?'_'+targetLength+'mm':'')+(uniform?'_uniform13':wideBase?'_13mm_base':reinforced?'_reinforced':'');
const baseTopZ=-1.5;
const shaftExtension=variant?targetLength+baseTopZ-(dims.zJoin+dims.flareHeight+dims.flangeHeight+dims.hexLength):0;
const {part:external,base,lowerBox,zHex,zTip}=wideBase?buildWideBase(original,uniform):buildExternal(original,shaftExtension,reinforced);
if(variant)assert(Math.abs((zTip-baseTopZ)-targetLength)<1e-9);
const coverThickness=1.5,nutPocketAcrossFlats=5.7,nutPocketHeight=2.6,screwClearanceDiameter=3.2,screwHoleDepth=8.3;
const zPocketTop=zTip-coverThickness,zPocketBottom=zPocketTop-nutPocketHeight;
function nutHex(af,h,z){
 const rr=af/Math.sqrt(3);
 let d=r.draw([rr,0]);
 for(let i=1;i<6;i++)d=d.lineTo([rr*Math.cos(i*Math.PI/3),rr*Math.sin(i*Math.PI/3)]);
 return d.close().sketchOnPlane('XY',z).extrude(h);
}
const pocket=nutHex(nutPocketAcrossFlats,nutPocketHeight,zPocketBottom);
const entry=r.makeBox([0,-nutPocketAcrossFlats/2,zPocketBottom],[12,nutPocketAcrossFlats/2,zPocketTop]);
const screwHole=r.makeCylinder(screwClearanceDiameter/2,screwHoleDepth+.1,[0,0,zTip-screwHoleDepth]);
const part=external.clone().cut(pocket).cut(entry).cut(screwHole).simplify();
const isValid=s=>{const a=new oc.BRepCheck_Analyzer(s.wrapped,true,false);const valid=a.IsValid();a.delete();return valid;};
assert(isValid(part));assert.equal(part.solids.length,1);
assert(Math.abs(r.measureVolume(base.clone().cut(part.clone())))<1e-6);
assert(Math.abs(r.measureVolume(part.clone().intersect(lowerBox()).cut(base.clone())))<1e-6);
if(reinforced||wideBase){
 const middleZ=dims.zJoin+8;
 const middle=part.clone().intersect(r.makeBox([-20,-20,middleZ],[20,20,middleZ+1]));
 const radius=uniform?6.5:6;
 assert(Math.abs(r.measureVolume(middle)-Math.PI*radius*radius)<1e-5);
 assert(Math.abs(middle.boundingBox.width-radius*2)<1e-5);
}
if(wideBase){
 const lower=part.clone().intersect(r.makeBox([-20,-20,baseTopZ+5],[20,20,baseTopZ+6]));
 assert(Math.abs(lower.boundingBox.width-13)<1e-5);
 assert(Math.abs(r.measureVolume(lower)-Math.PI*(6.5**2-dims.boreRadius**2))<1e-5);
}
const outsideSocket=r.makeCylinder(12,6,[0,0,zHex]).cut(r.drawPolysides(12/Math.sqrt(3),6).sketchOnPlane('XY',zHex).extrude(6));
assert(Math.abs(r.measureVolume(part.clone().intersect(outsideSocket)))<1e-6);
// Verify the complete 5.5 AF x 2.4 mm metal-nut envelope can slide into place.
const nutEnvelope=nutHex(5.5,2.4,zPocketTop-2.4);
for(const x of [0,1,2,3,4,5,6,8,10])assert(Math.abs(r.measureVolume(part.clone().intersect(nutEnvelope.clone().translateX(x))))<1e-6);
assert(zTip-screwHoleDepth-dims.zJoin>1.4);
// A 30-degree turn cannot occur with the nut centered in the pocket.
assert(r.measureVolume(part.clone().intersect(nutEnvelope.clone().rotate(30,[0,0,0],[0,0,1])))>.01);
const one=part.clone().translateZ(4.2),two=one.clone().translateX(40);
const pair=r.makeCompound([one.clone(),two.clone()]);assert.equal(pair.solids.length,2);assert(isValid(pair));
const output='../../outputs',name='shaft_pair_direct_hex_M3'+variant;fs.mkdirSync(output,{recursive:true});
const step=r.exportSTEP([{shape:one,name:'Direct wheel hex 1 - captive M3 nut'},{shape:two,name:'Direct wheel hex 2 - captive M3 nut'}],{unit:'MM',modelUnit:'MM'});
fs.writeFileSync(`${output}/${name}.step`,Buffer.from(await step.arrayBuffer()));
fs.writeFileSync(`${output}/${name}.stl`,Buffer.from(await pair.blobSTL({tolerance:.01,angularTolerance:.05,binary:true}).arrayBuffer()));
const checked=await r.importSTEP(step);assert.equal(checked.solids.length,2);assert(isValid(checked));assert(Math.abs(r.measureVolume(checked)-r.measureVolume(pair))<1e-4);
fs.writeFileSync('../pair_mesh_hex'+variant+'.json',JSON.stringify(pair.mesh({tolerance:.02,angularTolerance:.06})));
fs.writeFileSync('../detail_mesh_hex'+variant+'.json',JSON.stringify(one.mesh({tolerance:.02,angularTolerance:.06})));
const report={units:'mm',hex_across_flats:dims.hexAcrossFlats,hex_length:dims.hexLength,nominal_wheel_socket:{across_flats:12,depth:6},clearance_across_flats:.2,clearance_at_recess_floor:.2,flared_support_height:dims.flareHeight,support_flange_diameter:dims.flangeRadius*2,support_flange_thickness:dims.flangeHeight,nut_required:'Standard M3 hex nut, 5.5 mm AF x 2.4 mm thick, not a nyloc nut',nut_pocket_across_flats:nutPocketAcrossFlats,nut_pocket_height:nutPocketHeight,nut_top_cover:coverThickness,nut_loading_direction:'+X from side before wheel installation',screw_clearance_diameter:screwClearanceDiameter,screw_hole_depth:screwHoleDepth,minimum_web_between_top_and_bottom_bores:zTip-screwHoleDepth-dims.zJoin,bottom_bore_diameter:dims.boreRadius*2,bottom_bore_depth:dims.zJoin+4.2,nominal_screw: 'M3 x 8',minimum_screw_projection_through_wheel_for_full_nut_engagement:6-dims.hexLength+coverThickness+2.4,maximum_wheel_web_thickness_for_full_nut_engagement_with_8mm_screw:8-(6-dims.hexLength+coverThickness+2.4),actual_8mm_screw_engagement_confirmed:false,copies:2,gap:40-one.boundingBox.width,overall_height:zTip+4.2,cad_valid:true,step_reimport_valid:true,nominal_socket_clearance_verified:true,nut_insertion_clearance_verified:true,nut_rotation_prevented:true,gearbox_interface_preserved_except_requested_bore_widening:true,physical_fit_tested:false,load_tested:false};
Object.assign(report,{shaft_extension_added:shaftExtension,base_top_to_hex_tip:zTip-baseTopZ,dimension_datum:'Top flat face of the mounting base, where the shaft rises',base_top_z_in_export:baseTopZ+4.2});
if(reinforced)Object.assign(report,{reinforced_exposed_diameter:12,previous_exposed_diameter:7.999992,lower_transition_height:4,transitions:'Tangent cubic profiles, lower 8-to-12 mm and upper 12-to-14.4 mm',original_8mm_bearing_seat_preserved:true,strength_gain_quantified:false});
if(wideBase)Object.assign(report,{lower_section_diameter:13,lower_section_height_from_base_top:10,root_blend_height:1.5,upper_transition_height:2,main_body_diameter:12,original_8mm_bearing_seat_preserved:false,gearbox_interface_preserved_except_requested_bore_widening:false,mounting_plate_and_underside_holes_preserved:true,gearbox_housing_fit_verified:false,strength_gain_quantified:false});
if(uniform)Object.assign(report,{main_body_diameter:13,upper_transition_height:0,lower_section_height_from_base_top:null,uniform_shaft_diameter:13,transitions:'Smooth root and flange blends; no intermediate diameter step'});
if(variant){
 for(const s of checked.solids)assert(Math.abs(s.boundingBox.bounds[1][2]-(baseTopZ+4.2)-targetLength)<1e-5);
}
fs.writeFileSync('../validation_hex'+variant+'.json',JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
