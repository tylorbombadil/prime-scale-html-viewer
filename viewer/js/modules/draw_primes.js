export function drawPrimes(ctx, scale, canvas) {
  const primes = scale.metadata?.log_prime_positions;
  if (!primes || !primes.length) return;

  ctx.strokeStyle = '#ccc';
  ctx.lineWidth = 1;

  primes.forEach(p => {
    const x = p * canvas.width;
    ctx.beginPath();
    ctx.moveTo(x, canvas.height / 2 - 10);
    ctx.lineTo(x, canvas.height / 2 + 10);
    ctx.stroke();
  });
}
