from scipy.fft import irfft
from scipy.io import wavfile

from _3_fft_for_mix_wave import xf, yf
from config import SAMPLE_RATE, DATA_MAX
from util.import_common import *

# 过滤高频
# 最大频率为采样率的一半
points_per_freq = len(xf) / (SAMPLE_RATE / 2)

# 我们的目标频率是4000赫兹 将44100变成4000
target_idx = int(points_per_freq * 4000)

yf[target_idx - 1: target_idx + 2] = 0

plt.title('After filtering high frequency')
plt.plot(xf, np.abs(yf))
plt.show()

# 逆变换到时域
new_sig = irfft(yf)

plt.title('Filtered signal')
plt.plot(new_sig[:600])
plt.show()

# 归一化
norm_new_sig = np.int16(new_sig * (DATA_MAX / np.max(new_sig)))

wavfile.write("clean.wav", SAMPLE_RATE, norm_new_sig)
