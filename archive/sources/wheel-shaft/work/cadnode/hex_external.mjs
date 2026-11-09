import * as r from 'replicad';
// Shared outer geometry; screw retention is added after its hardware is confirmed.
export const dims={zJoin:11.166664,boreRadius:2.8,flareHeight:3,flangeHeight:1,flangeRadius:7.2,hexAcrossFlats:11.8,hexLength:5.8};
export function buildExternal(original,shaftExtension=0,reinforced=false){
 const {zJoin,boreRadius,flareHeight,flangeHeight,flangeRadius,hexAcrossFlats,hexLength}=dims;
 const lowerBox=()=>r.makeBox([-50,-50,-50],[50,50,zJoin]);
 const originalBase=original.clone().intersect(lowerBox());
 const base=originalBase.clone().cut(r.makeCylinder(boreRadius,zJoin+4.3,[0,0,-4.3]));
 const zFlare=zJoin+shaftExtension;
 let stem;
 if(reinforced){
  if(shaftExtension<4)throw new Error('Reinforced transition requires at least 4 mm extension');
  // Revolved cubic curves meet both cylinders tangentially. The bearing-fit
  // geometry at and below zJoin remains untouched.
  const upper=r.draw([0,zJoin]).lineTo([3.999996,zJoin])
   .cubicBezierCurveTo([6,zJoin+4],[3.999996,zJoin+4/3],[6,zJoin+8/3])
   .lineTo([6,zFlare])
   .cubicBezierCurveTo([flangeRadius,zFlare+flareHeight],[6,zFlare+flareHeight/3],[flangeRadius,zFlare+2*flareHeight/3])
   .lineTo([0,zFlare+flareHeight]).close().sketchOnPlane('XZ').revolve([0,0,1],{origin:[0,0,0]});
  stem=base.clone().fuse(upper);
 }else{
  stem=shaftExtension>0?base.clone().fuse(r.makeCylinder(3.999996,shaftExtension,[0,0,zJoin])):base.clone();
  const flare=r.drawCircle(3.999996).sketchOnPlane('XY',zFlare).loftWith(r.drawCircle(flangeRadius).sketchOnPlane('XY',zFlare+flareHeight));
  stem=stem.fuse(flare);
 }
 const flange=r.makeCylinder(flangeRadius,flangeHeight,[0,0,zFlare+flareHeight]);
 const zHex=zFlare+flareHeight+flangeHeight,zTip=zHex+hexLength;
 let hex=r.drawPolysides(hexAcrossFlats/Math.sqrt(3),6).sketchOnPlane('XY',zHex).extrude(hexLength);
 hex=hex.chamfer(.3,e=>e.inPlane('XY',zTip));
 const part=stem.fuse(flange).fuse(hex).simplify();
 return {part,base,lowerBox,zHex,zTip};
}
