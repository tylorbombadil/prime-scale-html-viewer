import { playNote } from '../audio/tone_play.js';

let midiInputs = [];

export function setupMidiInput(scale) {
  navigator.requestMIDIAccess().then(midi => {
    // Clear old handlers
    for (const input of midiInputs) {
      input.onmidimessage = null;
    }

    midiInputs = [...midi.inputs.values()];

    for (const input of midiInputs) {
      input.onmidimessage = ({ data }) => {
        console.log('MIDI message:', data);
        const [status, note, velocity] = data;

        if (status === 144 && velocity > 0) {
          const index = note - 60; // Middle C = 60
          const scaleNote = scale.notes[index];

          if (scaleNote && scaleNote.frequency) {
            console.log(`Playing index ${index}: ${scaleNote.frequency}`);
            playNote(scaleNote.frequency);
          }
        }
      };
    }
  }).catch(err => {
    console.error("MIDI init failed:", err);
  });
}