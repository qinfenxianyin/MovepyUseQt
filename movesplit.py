# -*- coding: utf-8 -*-
import imageio
import tools

# imageio.plugins.ffmpeg.download()
# import win_unicode_console

# win_unicode_console.enable()
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel,
                             QApplication, QFileDialog)
# from moviepy.video.io.VideoFileClip import VideoFileClip
# from moviepy.video.io.CompositeVideoClips import concatenate_videoclips
from moviepy.editor import *


class login(QWidget):
    def __init__(self):
        super(login, self).__init__()
        self.initUI()

    def initUI(self):
        # 源文件选择按钮和选择编辑框
        self.source_btn = QPushButton('源文件', self)
        self.source_btn.move(30, 30)
        self.source_btn.resize(80, 30)
        self.source_btn.clicked.connect(self.select_source)
        self.source_le = QLineEdit(self)
        self.source_le.move(120, 30)
        self.source_le.resize(250, 30)

        # 存储文件选择按钮和选择编辑框
        # self.target_btn = QPushButton('目标路径', self)
        # self.target_btn.move(30, 90)
        # self.target_btn.resize(60, 30)
        # self.target_btn.clicked.connect(self.select_target)
        # self.target_le = QLineEdit(self)
        # self.target_le.move(120, 90)
        # self.target_le.resize(250, 30)

        # 截切开始时间输入框和提示
        self.startLabel = QLabel(self)
        self.startLabel.move(30, 150)
        self.startLabel.resize(100, 30)
        self.startLabel.setText("分成的份数")
        self.start_le = QLineEdit(self)
        self.start_le.move(120, 150)
        self.start_le.resize(50, 30)

        # 视频比特率输入框和提示
        self.stopLabel = QLabel(self)
        self.stopLabel.move(230, 90)
        self.stopLabel.resize(80, 30)
        self.stopLabel.setText("视频比特率")
        self.stop_le = QLineEdit(self)
        self.stop_le.move(320, 90)
        self.stop_le.resize(50, 30)
        self.stopLabel2 = QLabel(self)
        self.stopLabel2.move(370, 90)
        self.stopLabel2.resize(10, 30)
        self.stopLabel2.setText("k")

        # 音频比特率输入框和提示
        self.audioLabel = QLabel(self)
        self.audioLabel.move(230, 150)
        self.audioLabel.resize(80, 30)
        self.audioLabel.setText("音频比特率")
        self.audio_le = QLineEdit(self)
        self.audio_le.move(320, 150)
        self.audio_le.resize(50, 30)
        self.audioLabel2 = QLabel(self)
        self.audioLabel2.move(370, 150)
        self.audioLabel2.resize(10, 30)
        self.audioLabel2.setText("k")

        # 保存按钮，调取数据增加函数等
        self.save_btn = QPushButton('开始', self)
        self.save_btn.move(30, 210)
        self.save_btn.resize(140, 30)
        self.save_btn.clicked.connect(self.addNum)

        # 自定义按钮，调取数据增加函数等
        self.auto_btn = QPushButton('clear', self)
        self.auto_btn.move(250, 210)
        self.auto_btn.resize(140, 30)
        self.auto_btn.clicked.connect(self.autoNum)

        # 执行成功返回值显示位置设置
        self.result_le = QLabel(self)
        self.result_le.move(30, 270)
        self.result_le.resize(340, 30)

        # 整体界面设置
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('视频剪切')  # 设置界面标题名
        self.show()

    # 打开的视频文件名称
    def select_source(self):
        target, fileType = QFileDialog.getOpenFileName(self, "选择源文件", "C:/")
        self.source_le.setText(str(target))

    # 保存的视频文件名称，要写上后缀名
    def select_target(self):
        target, fileType = QFileDialog.getSaveFileName(self, "选择保存路径", "C:/")
        self.target_le.setText(str(target))

    def addNum(self):
        self.result_le.setText("Runing!")  # 输出文件后界面返回OK
        self.result_le.setStyleSheet("color:green;font-size:40px")  # 设置OK颜色为红色，大小为四十像素
        self.result_le.setAlignment(Qt.AlignCenter)  # OK在指定框内居中
        # QApplication.processEvents()
        source = self.source_le.text().strip()  # 获取需要剪切的文件
        # target = self.target_le.text().strip()  # 获取剪切后视频保存的文件
        times = int(self.start_le.text().strip())  # 获取开始剪切时间
        bitrate = self.stop_le.text().strip()+'k'  # 获取剪切的结束时间
        audio_bitrate = self.audio_le.text().strip()+'k'  # 获取剪切的结束时间
        self.video = VideoFileClip(source)  # 视频文件加载
        self.end=self.video.end
        split_len=int(self.end/times)
        fps=self.video.fps
        for x in range(int(times)):
            stop_time=self.end if (x+1==int(times)) else (x+1)*split_len
            video_x=self.video.subclip(x*split_len, stop_time)   # 执行剪切操作
            # video_x.to_videofile(tools.move_fileto_out(source,x), fps=fps, remove_temp=True,audio_codec="aac")  # 输出文件 ,audio_codec="aac" 要加上才有声音
            video_x.write_videofile(tools.move_fileto_out(source,x), \
                                    fps=fps, remove_temp=True,\
                                    audio_codec="aac",preset='placebo',threads=16,\
                                    audio_fps=self.video.audio.reader.infos['audio_fps'],\
                                    bitrate=bitrate,audio_bitrate=audio_bitrate)  # 输出文件 ,audio_codec="aac" 要加上才有声音
        # self.video = self.video.subclip(int(start_time), int(stop_time))
        # self.video.to_videofile(target, fps=20, remove_temp=True,audio_codec="aac")  # 输出文件 ,audio_codec="aac" 要加上才有声音
        self.result_le.setText("ok!")  # 输出文件后界面返回OK
        self.result_le.setStyleSheet("color:red;font-size:40px")  # 设置OK颜色为红色，大小为四十像素
        self.result_le.setAlignment(Qt.AlignCenter)  # OK在指定框内居中

    def autoNum(self):
        # source = self.source_le.text().strip()  # 获取需要剪切的文件
        # self.video = VideoFileClip(source)  # 视频文件加载
        # print(self.video.audio.reader.infos['audio_fps'])
        # print(self.video.__dict__)
        # print(self.video.reader.__dict__)
        # print(self.video.audio.__dict__)
        # print(self.video.audio.reader.__dict__)
        self.result_le.setText("Ready!")  # 输出文件后界面返回OK
        self.result_le.setStyleSheet("color:green;font-size:30px")  # 设置OK颜色为红色，大小为四十像素
        self.result_le.setAlignment(Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = login()
    sys.exit(app.exec_())

# if __name__ == "__main__":
#     video = VideoFileClip('/Users/xiwenkai/1100/mycode/1598080495180776.mp4')
#     print(video.size)
#     print(video.start)
#     print(video.end)
#     final_clip = concatenate_videoclips([video, video])  # 视频合并
#     final_clip.write_videofile("/Users/xiwenkai/1100/mycode/hebing.mp4",\
#                 temp_audiofile='temp-audio.m4a', remove_temp=True, \
#                 codec="libx264", audio_codec="aac")
#     print('ok')
