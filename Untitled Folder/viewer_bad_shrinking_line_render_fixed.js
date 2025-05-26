
const scaleDisplay = document.getElementById('scale-display');
const canvas = document.getElementById('line-readout');
const ctx = canvas.getContext('2d');

function drawLineReadout(scale) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw base line
  ctx.beginPath();
  ctx.moveTo(0, canvas.height / 2);
  ctx.lineTo(canvas.width, canvas.height / 2);
  ctx.strokeStyle = '#888';
  ctx.lineWidth = 1;
  ctx.stroke();

// Draw vertical lines for primes with length decreasing as prime value increases
const primes = scale.metadata.primes;
const positions = scale.metadata.log_prime_positions;

primes.forEach((prime, i) => {
  const x = positions[i] * canvas.width;

  const maxHeight = 50;
  const minHeight = 4;
  const decay = 200; // The larger the decay, the slower the shrink
  const height = Math.max(minHeight, maxHeight - prime * (maxHeight / decay));

  const y1 = canvas.height / 2 + height / 2;
  const y2 = canvas.height / 2 - height / 2;

  ctx.strokeStyle = '#000';
  ctx.beginPath();
  ctx.moveTo(x, y1);
  ctx.lineTo(x, y2);
  ctx.stroke();
});

// Draw only floating scale notes
ctx.fillStyle = 'black';
const scaleLineOffset = 14;

scale.notes.forEach(note => {
  const x = note.log_position * canvas.width;
  const y = canvas.height / 2 - scaleLineOffset;

  ctx.beginPath();
  ctx.arc(x, y, 4, 0, 2 * Math.PI);
  ctx.fill();
});

// Draw segment boundaries from metadata
if (scale.metadata && scale.metadata.segment_boundaries) {
  ctx.strokeStyle = '#cc0'; // Yellowish for visibility
  ctx.lineWidth = 2;

  scale.metadata.segment_boundaries.forEach(pos => {
    const x = pos * canvas.width;
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, canvas.height);
    ctx.stroke();
  });

  ctx.lineWidth = 1; // Reset after drawing
}

// Draw density map as grayscale gradient
if (scale.metadata && scale.metadata.density_map && scale.metadata.x_axis) {
  const max = Math.max(...scale.metadata.density_map);
  const min = Math.min(...scale.metadata.density_map);

  scale.metadata.density_map.forEach((val, i) => {
    const x = scale.metadata.x_axis[i] * canvas.width;
    const norm = (val - min) / (max - min);
    const gray = Math.floor(norm * 255); // 0–255 grayscale
    ctx.strokeStyle = `rgb(${gray}, ${gray}, ${gray})`;

    ctx.beginPath();
    ctx.moveTo(x, canvas.height / 2 + 30);
    ctx.lineTo(x, canvas.height / 2 + 35);
    ctx.stroke();
  });
}

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
