"""
生成正弦波
"""

from config import SAMPLE_RATE, DURATION
from util.generator import generate_sine_wave
from util.import_common import *

# 产生持续5秒的2赫兹正弦波
x, y = generate_sine_wave(2, SAMPLE_RATE, DURATION)

plt.title('sin wave')
plt.plot(x, y)
plt.show()
