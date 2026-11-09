import fs from 'node:fs';
import init from 'replicad-opencascadejs';
import * as r from 'replicad';
const oc=await init({wasmBinary:fs.readFileSync(new URL('./node_modules/replicad-opencascadejs/dist/replicad_single.wasm',import.meta.url))});
r.setOC(oc);
const model=await r.importSTEP(new Blob([fs.readFileSync('[REDACTED_HOME_PATH]
console.log('SOLIDS',model.solids.length);
for(const [i,s] of model.solids.entries()) console.log(i,s.boundingBox.bounds,r.measureVolume(s),s.faces.length);
const s=model.solids.find(s=>{const [a,b]=s.boundingBox.bounds;return Math.abs((a[0]+b[0])/2)<.01&&Math.abs((a[1]+b[1])/2)<.01&&b[2]>14&&b[2]<15;});
if(!s)throw Error('shaft not found');
fs.writeFileSync('../original_output.step',Buffer.from(await s.blobSTEP().arrayBuffer()));
fs.writeFileSync('../original_mesh.json',JSON.stringify(s.mesh({tolerance:.03,angularTolerance:.08})));
console.log('ORIGINAL',s.boundingBox.bounds);
