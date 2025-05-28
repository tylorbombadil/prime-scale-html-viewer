import * as Tone from 'https://cdn.skypack.dev/tone';
import { enableAudioOnClick } from './audio/startup_audio.js';

window.addEventListener('DOMContentLoaded', () => {
  enableAudioOnClick(); 
});

import { drawScale } from './draw.js';
import { loadScale } from './utils.js';
import { setupDropdown } from './ui/dropdown.js';

setupDropdown(drawScale);
