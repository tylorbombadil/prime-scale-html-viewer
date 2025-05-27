export function drawSegments(ctx, scale, canvas) {
  if (!scale.metadata?.segment_boundaries) return;

  ctx.strokeStyle = '#aaa';
  ctx.lineWidth = 1;
  ctx.setLineDash([5, 4]); // dashed

  scale.metadata.segment_boundaries.forEach(pos => {
    const x = pos * canvas.width;
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, canvas.height);
    ctx.stroke();
  });

  ctx.setLineDash([]); // reset dash
}
