import * as r from 'replicad';
import {dims} from './hex_external.mjs';
export function buildWideBase(original,uniform=false){
 const baseTopZ=-1.5, lowerLength=10, lowerRadius=6.5, bodyRadius=uniform?6.5:6;
 const zTip=baseTopZ+40,zHex=zTip-dims.hexLength;
 const zFlange=zHex-dims.flangeHeight,zFlare=zFlange-dims.flareHeight;
 const lowerBox=()=>r.makeBox([-50,-50,-50],[50,50,baseTopZ]);
 const base=original.clone().intersect(lowerBox()).cut(r.makeCylinder(dims.boreRadius,60,[0,0,-5]));
 // Retain the mounting plate. Replace the protruding shaft, with a 13 mm
 // lower section spanning 10 mm from the plate top to its upper transition.
 let profile=r.draw([0,baseTopZ]).lineTo([7.5,baseTopZ])
  .cubicBezierCurveTo([lowerRadius,baseTopZ+1.5],[6.9,baseTopZ],[lowerRadius,baseTopZ+.7]);
 if(!uniform)profile=profile.lineTo([lowerRadius,baseTopZ+lowerLength])
  .cubicBezierCurveTo([bodyRadius,baseTopZ+lowerLength+2],[lowerRadius,baseTopZ+lowerLength+2/3],[bodyRadius,baseTopZ+lowerLength+4/3]);
 const upper=profile
  .lineTo([bodyRadius,zFlare])
  .cubicBezierCurveTo([dims.flangeRadius,zFlange],[bodyRadius,zFlare+1],[dims.flangeRadius,zFlange-1])
  .lineTo([0,zFlange]).close().sketchOnPlane('XZ').revolve([0,0,1],{origin:[0,0,0]});
 const flange=r.makeCylinder(dims.flangeRadius,dims.flangeHeight,[0,0,zFlange]);
 let hex=r.drawPolysides(dims.hexAcrossFlats/Math.sqrt(3),6).sketchOnPlane('XY',zHex).extrude(dims.hexLength);
 hex=hex.chamfer(.3,e=>e.inPlane('XY',zTip));
 const part=base.clone().fuse(upper).fuse(flange).fuse(hex)
  .cut(r.makeCylinder(dims.boreRadius,dims.zJoin+4.3,[0,0,-4.3])).simplify();
 return {part,base,lowerBox,zHex,zTip};
}
