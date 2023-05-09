import pathlib
from typing import Union

import numpy as np
from scipy.fft import rfft, rfftfreq


def read(path: Union[str, pathlib.Path], resolution: type = np.int16) -> np.ndarray:
    """载入PCM wave文件

    :param path: 文件路径
    :param resolution: Audio bit depth. Normally 16 bits, which is pcm_s16le
    :return: 一维ndarray
    """
    pcm_data = np.fromfile(path, resolution)
    return pcm_data


def pcm_rfft(pcm: np.ndarray, sample_rate: int) -> (np.ndarray, np.ndarray):
    """对PCM数据进行RFFT

    :param pcm: PCM数据
    :param sample_rate: 该数据的采样率
    :return:
    """
    n = pcm.shape[0]  # 样本数

    yf = rfft(pcm)
    xf = rfftfreq(n, 1 / sample_rate)  # 计算输出中每个仓中心的频率

    return xf, yf
