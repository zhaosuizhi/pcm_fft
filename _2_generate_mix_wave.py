from scipy.io import wavfile

# 归一化
from config import SAMPLE_RATE, DURATION, DATA_MAX
from util.generator import generate_sine_wave
from util.import_common import *

# 叠加正弦波
_, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.3

mixed_tone = nice_tone + noise_tone

# 归一化
normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * DATA_MAX)

plt.title('2 sin waves')
plt.plot(nice_tone[:600])
plt.plot(noise_tone[:600])
plt.show()

plt.title('mix wave')
plt.plot(normalized_tone[:600])
plt.show()

wavfile.write('mix_wave.wav', SAMPLE_RATE, normalized_tone)
