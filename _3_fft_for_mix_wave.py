from scipy.fft import rfft, rfftfreq

from _2_generate_mix_wave import normalized_tone
from config import SAMPLE_RATE, DURATION
from util.import_common import *

# 标准化音调中的样本数
N = SAMPLE_RATE * DURATION

yf = rfft(normalized_tone)
xf = rfftfreq(N, 1 / SAMPLE_RATE)  # 计算输出中每个仓中心的频率

plt.title('FFT for mix wave')
plt.plot(xf, np.abs(yf))
plt.show()
