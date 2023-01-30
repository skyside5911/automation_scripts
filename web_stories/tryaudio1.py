import cv2
from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.audio.fx.volumex import volumex
# Open the video file
# cap = cv2.VideoCapture(r"H:\automation_scripts\web_stories\new.mp4")
# video = VideoFileClip(r"H:\automation_scripts\web_stories\new.mp4")

# # Load the audio
# audio = video.audio
# audio.write_audiofile(r"H:\automation_scripts\web_stories\audio.mp3")
# Get the video frame dimensions

video11=VideoFileClip(r"H:\automation_scripts\web_stories\newv.mp4")
song=AudioFileClip(r'H:\automation_scripts\web_stories\audio.mp3')
# songg=song.subclip(0,50)

final_video=video11.set_audio(song)
final_video.write_videofile(r'H:\automation_scripts\web_stories\n1.mp4')
