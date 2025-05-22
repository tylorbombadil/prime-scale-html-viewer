
const scaleDisplay = document.getElementById('scale-display');
const canvas = document.getElementById('line-readout');
const ctx = canvas.getContext('2d');

function drawLineReadout(scale) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  const primeY = canvas.height / 2;
  const noteY = primeY - 10; // Slight offset above prime ticks

  // Draw base prime line
  ctx.beginPath();
  ctx.moveTo(0, primeY);
  ctx.lineTo(canvas.width, primeY);
  ctx.strokeStyle = '#888';
  ctx.lineWidth = 1;
  ctx.stroke();

  // Draw note guide line
  ctx.beginPath();
  ctx.moveTo(0, noteY);
  ctx.lineTo(canvas.width, noteY);
  ctx.strokeStyle = '#bbb';
  ctx.lineWidth = 0.5;
  ctx.stroke();

  // Draw segment boundaries
  if (scale.segment_boundaries) {
    ctx.strokeStyle = '#ccc';
    scale.segment_boundaries.forEach(pos => {
      const x = pos * canvas.width;
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, canvas.height);
      ctx.stroke();
    });
  }

  // Draw reduced primes
  if (scale.log_prime_positions) {
    ctx.fillStyle = '#888';
    scale.log_prime_positions.forEach(pos => {
      const x = pos * canvas.width;
      ctx.fillRect(x, primeY - 5, 1, 10);
    });
  }

  // Draw selected notes slightly above the prime line
  ctx.fillStyle = 'black';
  scale.notes.forEach(note => {
    const x = note.log_position * canvas.width;
    ctx.beginPath();
    ctx.arc(x, noteY, 4, 0, 2 * Math.PI);
    ctx.fill();
  });
}

function loadScale(filename) {
  fetch('output/' + filename)
    .then(res => res.json())
    .then(scale => {
      scaleDisplay.innerHTML = '';

      const title = document.createElement('h2');
      title.textContent = scale.name;
      scaleDisplay.appendChild(title);

      scale.notes.forEach(note => {
        const btn = document.createElement('button');
        btn.textContent = `${note.frequency.toFixed(2)} Hz`;
        btn.onclick = () => {
          const ctx = new (window.AudioContext || window.webkitAudioContext)();
          const osc = ctx.createOscillator();
          osc.type = 'sine';
          osc.frequency.value = note.frequency;
          osc.connect(ctx.destination);
          osc.start();
          osc.stop(ctx.currentTime + 0.5);
        };
        scaleDisplay.appendChild(btn);
        scaleDisplay.appendChild(document.createTextNode(` → ${note.cents_from_base.toFixed(2)} cents`));
        scaleDisplay.appendChild(document.createElement('br'));
      });

      drawLineReadout(scale);
    })
    .catch(err => {
      scaleDisplay.textContent = 'Failed to load scale file.';
      console.error(err);
    });
}

// Fetch manifest.json to populate dropdown
fetch('output/manifest.json')
  .then(res => res.json())
  .then(manifest => {
    const dropdown = document.createElement('select');
    dropdown.onchange = () => loadScale(dropdown.value);

    manifest.scales.forEach(file => {
      const option = document.createElement('option');
      option.value = file;
      option.textContent = file;
      dropdown.appendChild(option);
    });

    document.body.insertBefore(dropdown, scaleDisplay);
    if (manifest.scales.length > 0) {
      loadScale(manifest.scales[0]);
    }
  })
  .catch(err => {
    scaleDisplay.textContent = 'Failed to load manifest file.';
    console.error(err);
  });
