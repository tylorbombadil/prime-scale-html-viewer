import * as Tone from 'https://cdn.skypack.dev/tone';
export function enableAudioOnClick() {
  document.body.addEventListener('click', async () => {
    await Tone.start();
    console.log('Audio context resumed by user gesture');
  }, { once: true });
}
