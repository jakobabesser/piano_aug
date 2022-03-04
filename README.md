# PIANO-AUG - Piano Multipitch Estimation with Augmentation Dataset 

## Reference

 - Jakob Abeßer, Christof Weiß, Sascha Grollmisch, Meinard Müller: Exploring U-Net Variants for Efficient Piano Multipitch Estimation (2022, to be published)

## Description

This dataset includes a 29 minutes long piano recording with a total of 4584 notes. 
The recording includes sections of single notes as well as groups of simultaneously sounding notes (intervals, chords), which ascend chromatically within the MIDI pitch range [21,92]. 

In particular, the segments cover single notes, intervals (two-note groups), as well as common three-
voiced and four-voiced chords. It must be noted that we do not investigate chord inversions here, all chords are used in their root position. 

The audio is created by rendering the MIDI file using the “Grand Piano” plugin in Ableton Live 8 with default
settings except from the “Reverb Amount” being set to zero. We use the [pedalboard](https://github.com/spotify/pedalboard) python library (0.4.1) to create multiple augmented versions of the unprocessed piano recording. In particular, we create pairs of mild (-) and heavy (+) augmentations for each of the compression (comp), gain (gain), low-pass filter (lpf), and reverb (rev) effects.

## Files

- Audio Files
  - ```live_grand_piano.wav``` - Unprocessed piano recording (download at [https://zenodo.org/6327395](https://zenodo.org/record/6327395))
  - ```live_grand_piano_comp-.wav``` - Mild compression
  - ```live_grand_piano_comp+.wav``` - Stronger compression
  - ```live_grand_piano_gain-.wav``` - Mild gain
  - ```live_grand_piano_gain+.wav``` - Stronger gain (clipping)
  - ```live_grand_piano_lpf-.wav``` - Mild low-pass filter
  - ```live_grand_piano_lpf+.wav``` - Stronger low-pass filter
  - ```live_grand_piano_rev-.wav``` - Mild reverb
  - ```live_grand_piano_rev+.wav``` - Stronger reverb

- Annotation Files
  - ```live_grand_piano.mid``` - Corresponding MIDI file (download at [https://zenodo.org/6327395](https://zenodo.org/record/6327395))
  - ```notes.csv``` - Note metadata (download at [https://zenodo.org/6327395](https://zenodo.org/record/6327395))


    - columns:
       - onset time [s]
       - offset time [s]
       - MIDI pitch
       - Segment ID
       
    - the segment ID encode the musical content:
      - SINGLE: single notes
      - 2-: minor second interval
      - 2: major second interval
      - 3-: minor third interval
      - 3+: major third interval
      - 4: perfect fourth interval
      - 5-: diminished fifth interval
      - 5: perfect fifth interval
      - 6-: minor sixth interval
      - 6+: major sixth interval
      - 7: minor seventh interval
      - 7+: major seventh interval
      - oct(1): root note + octave
      - oct(2): root note + second octave
      - oct(1+2): root note + first octave + second octave
      - oct(3): root note + third octave
      - oct(1+2+3): root note + first octave + second octave + third octave
      - min: minor triad
      - maj: major triad
      - sus2: sus2 triad 
      - sus4: sus4 triad
      - dim: diminished triad
      - aug: augmented triad
      - m7: minor seventh chord
      - 7: dominant seventh chord
      - maj7: major seventh chord
      - hdim7: half-diminished seventh chord
      - dim7: diminished seventh chord
      
    - Python code for mapping from segmentIDs to segmentLabels
```    
    segmentLabels = ['SINGLE', '2-', '2', '3-', '3+', '4', '5-',            
                     '5', '6-', '6', '7', '7+', 'oct(1)', 'oct(2)',
                     'oct(1+2)', 'oct(3)', 'oct(1+2+3)', 'min', 'maj', 'sus2', 'sus4', 'dim', 'aug', 'm7', '7', 'maj7', 'hdim7', 'dim7']

```

## Requirements

 - Python libraries used to create the augmented versions
    - pedalboard (0.4.1)
    - soundfile (0.9.0)
    
## Generate augmented audio files

 - run ```create_augmented_versions.py``` on unprocessed piano recording ```live_grand_piano.wav```