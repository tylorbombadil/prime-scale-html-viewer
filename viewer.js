const scaleDisplay = document.getElementById('scale-display');

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
