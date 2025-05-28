import * as Tone from 'https://cdn.skypack.dev/tone';
const reverb = new Tone.Reverb({ decay: 4, wet: 0.5 }).toDestination();
const synth = new Tone.PolySynth(Tone.Synth).connect(reverb);

export function playNote(frequency) {
  synth.triggerAttackRelease(frequency, "2n");
}

export function resumeAudio() {
  if (Tone.context.state !== 'running') {
    Tone.context.resume();
   }
 }

