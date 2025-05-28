import { setupMidiInput } from '../midi/midi_input.js';
import { playNote, resumeAudio } from '../audio/tone_play.js';
export function setupDropdown(drawCallback) {
  const scaleDisplay = document.getElementById('scale-display');

  fetch('../output/manifest.json')
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

  function loadScale(filename) {
    fetch('../output/' + filename)
      .then(res => res.json())
      .then(scale => {
        scaleDisplay.innerHTML = '';
        drawCallback(scale);

  setupMidiInput(scale);
 
     console.log('scale.notes:', scale.notes)

     const buttonContainer = document.createElement('div');
      buttonContainer.style.marginTop = '1em';

      scale.notes.forEach(note => {
        const btn = document.createElement('button');
        btn.textContent = note.frequency.toFixed(2) + ' Hz';
        btn.style.margin = '4px';
        btn.onclick = () => playNote(note.frequency);
        buttonContainer.appendChild(btn);
      });

      scaleDisplay.appendChild(buttonContainer);
      })
      .catch(err => {
        scaleDisplay.textContent = 'Failed to load scale file.';
        console.error(err);
      });
  }
}
