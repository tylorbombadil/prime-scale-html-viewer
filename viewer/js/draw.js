import { drawNotes } from './modules/draw_notes.js';
import { drawSegments } from './modules/draw_segments.js';
import { drawPrimes } from './modules/draw_primes.js';

export function drawScale(scale) {
  const canvas = document.getElementById('line-readout');
  const ctx = canvas.getContext('2d');

  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // draw base line
  ctx.beginPath();
  ctx.moveTo(0, canvas.height / 2);
  ctx.lineTo(canvas.width, canvas.height / 2);
  ctx.strokeStyle = '#888';
  ctx.lineWidth = 1;
  ctx.stroke();

  drawPrimes(ctx, scale, canvas);
  
  drawSegments(ctx, scale, canvas);
 
  drawNotes(ctx, scale, canvas);
}
