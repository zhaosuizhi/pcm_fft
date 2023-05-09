import pathlib

from util.import_common import *
from util.pcm import pcm_rfft
from util.pcm import read


def draw_fft_result_for_pcm_file(path: str, sample_rate: int):
    input_filepath = pathlib.Path(path)

    pcm = read(input_filepath)
    n = pcm.shape[0]
    duration = n / sample_rate

    plt.title(f'{input_filepath.stem} wave')
    plt.plot(np.linspace(0, duration, num=n), pcm)
    plt.show()

    xf, yf = pcm_rfft(pcm, sample_rate)

    plt.title(f'FFT for {input_filepath.stem}')
    plt.plot(xf, np.abs(yf))
    plt.show()


if __name__ == '__main__':
    draw_fft_result_for_pcm_file('test_resource/a-team_intro.pcm', 11025)
    draw_fft_result_for_pcm_file('test_resource/mixkit-classic-alarm-995.pcm', 44100)
