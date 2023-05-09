# PCM FFT

参考链接：[Python信号处理，使用scipy.fft进行大学经典的傅立叶变换 - 刘润森！](https://blog.csdn.net/weixin_44510615/article/details/117391598)

## 测试数据

`test_resource`文件夹中为测试数据，其中包括：

### a-team_intro.pcm

来自 [WavSource.com](https://www.wavsource.com/tv/a-team.htm)，WAV文件为其中的Intro。

该pcm文件采样率为11025 Hz，使用 [FFmpeg](https://ffmpeg.org/) 解封装，命令如下：

```sh
ffmpeg -i ./a-team_intro.wav -f s16le -acodec pcm_s16le ./a-team_intro.pcm
```

参考链接：[Can ffmpeg convert audio to raw PCM? If so, how? [closed]](https://stackoverflow.com/a/4854627/13833174)
