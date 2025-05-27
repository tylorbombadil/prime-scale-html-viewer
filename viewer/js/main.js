import { drawScale } from './draw.js';
import { loadScale } from './utils.js';

loadScale('../../output/scale_20250526_082847.json').then(scale => {
  drawScale(scale);
});
