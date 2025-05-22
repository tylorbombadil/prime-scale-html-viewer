// Clean rebuild viewer for rendering prime field lines and selected notes
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = 300;

const dropdown = document.getElementById('scaleDropdown');

fetch('output/manifest.json')
  .then(res => res.json())
  .then(manifest => {
    manifest.scales.forEach(scale => {
      const option = document.createElement('option');
      option.value = scale;
      option.textContent = scale;
      dropdown.appendChild(option);
    });

    dropdown.addEventListener('change', () => {
      loadAndDraw(dropdown.value);
    });

    // Auto-load the first one
    if (manifest.scales.length > 0) {
      dropdown.value = manifest.scales[0];
      loadAndDraw(dropdown.value);
    }
  });

function loadAndDraw(scaleName) {
  fetch(`output/${scaleName}`)
    .then(res => res.json())
    .then(scale => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Draw prime field lines
      if (scale.metadata && scale.metadata.log_prime_positions) {
        ctx.strokeStyle = '#ccc';
        scale.metadata.log_prime_positions.forEach(pos => {
          const x = pos * canvas.width;
          ctx.beginPath();
          ctx.moveTo(x, 0);
          ctx.lineTo(x, canvas.height);
          ctx.stroke();
        });
      }

      // Draw selected notes as large black dots
      if (scale.notes) {
        ctx.fillStyle = '#000';
        scale.notes.forEach(note => {
          const x = note.log_position * canvas.width;
          const y = canvas.height / 2;
          ctx.beginPath();
          ctx.arc(x, y, 4, 0, 2 * Math.PI);
          ctx.fill();
        });
      }
    });
}
