  // Draw density map as grayscale
export function drawDensity(ctx, scale, canvas) {
  if (scale.metadata && scale.metadata.density_map && scale.metadata.x_axis) {
    const max = Math.max(...scale.metadata.density_map);
    const min = Math.min(...scale.metadata.density_map);
    const range = max - min || 1;

    scale.metadata.density_map.forEach((val, i) => {
      const x = scale.metadata.x_axis[i] * canvas.width;
      const norm = (val - min) / range;
      const gray = Math.floor(norm * 255);
      ctx.strokeStyle = `rgb(${gray}, ${gray}, ${gray})`;

      ctx.beginPath();
      ctx.moveTo(x, canvas.height / 2 + 30);
      ctx.lineTo(x, canvas.height / 2 + 35);
      ctx.stroke();
    });
  }
}
