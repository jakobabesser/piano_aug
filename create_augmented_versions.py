from pedalboard import Reverb, Compressor, Gain, LowpassFilter, Pedalboard
import soundfile as sf


if __name__ == '__main__':

    # replace by path of unprocessed piano file if necessar
    fn_wav_source = 'live_grand_piano.wav'

    # augmentation settings using Pedalboard library
    settings = {'rev-': [Reverb(room_size=.4)],
                'rev+': [Reverb(room_size=.8)],
                'comp+': [Compressor(threshold_db=-15, ratio=20)],
                'comp-': [Compressor(threshold_db=-10, ratio=10)],
                'gain+': [Gain(gain_db=15)],  # clipping
                'gain-': [Gain(gain_db=5)],
                'lpf-': [LowpassFilter(cutoff_frequency_hz=50)],
                'lpf+': [LowpassFilter(cutoff_frequency_hz=250)]}

    # create augmented versions
    for s in settings.keys():

        # load unprocessed piano recording
        audio, sample_rate = sf.read(fn_wav_source)

        # create Pedalboard object
        board = Pedalboard(settings[s])

        # create augmented audio
        effected = board(audio, sample_rate)

        # save it
        fn_target = fn_wav_source.replace('.wav', f'_{s}.wav')
        sf.write(fn_target, effected, sample_rate)
