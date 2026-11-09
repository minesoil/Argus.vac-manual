import fs from 'node:fs';
import init from 'replicad-opencascadejs';
import * as r from 'replicad';
const oc=await init({wasmBinary:fs.readFileSync(new URL('./node_modules/replicad-opencascadejs/dist/replicad_single.wasm',import.meta.url))});r.setOC(oc);
const assembly=await r.importSTEP(new Blob([fs.readFileSync('[REDACTED_HOME_PATH]
const lid=assembly.solids.find(s=>{const[a,b]=s.boundingBox.bounds;return Math.abs(a[2]+3.8)<.001&&Math.abs(b[2]-.2)<.001&&Math.abs(b[0]-21)<.001;});
if(!lid)throw new Error('Original lid not identified');
const original=await r.importSTEP(new Blob([fs.readFileSync('../original_output.step')]));
const exported=await r.importSTEP(new Blob([fs.readFileSync('../../outputs/shaft_pair_direct_hex_M3_40mm_13mm_base.step')]));
const part=exported.solids.find(s=>Math.abs(s.boundingBox.center[0])<.001).clone().translateZ(-4.2);
const originalOverlap=r.measureVolume(original.clone().intersect(lid.clone()));
const newOverlap=part.clone().intersect(lid.clone());
const volume=r.measureVolume(newOverlap);
const report={original_output_lid_overlap_mm3:originalOverlap,new_13mm_base_lid_overlap_mm3:volume,new_overlap_bounds:volume>1e-6?newOverlap.boundingBox.bounds:null,fits_original_lid:volume<1e-6};
fs.writeFileSync('../widebase_housing_check.json',JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
