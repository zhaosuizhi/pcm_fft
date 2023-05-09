from .import_common import *


def generate_sine_wave(freq, sample_rate, duration):
    """生成正弦波

    :param freq: 正弦波的频率，单位赫兹
    :param sample_rate: 采样率，单位赫兹
    :param duration: 持续时间，单位秒
    :return:
    """
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq

    y = np.sin((2 * np.pi) * frequencies)
    return x, y
