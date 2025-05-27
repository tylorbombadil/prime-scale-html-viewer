export function drawNotes(ctx, scale, canvas) {
  if (!scale.notes) return;

  ctx.fillStyle = 'black';
  const offset = 14;

  scale.notes.forEach(note => {
    const x = note.log_position * canvas.width;
    const y = canvas.height / 2 - offset;

    ctx.beginPath();
    ctx.arc(x, y, 4, 0, 2 * Math.PI);
    ctx.fill();
  });
}
