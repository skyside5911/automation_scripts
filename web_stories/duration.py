from moviepy.video.io.VideoFileClip import VideoFileClip

video = VideoFileClip(r"H:\automation_scripts\web_stories\new.mp4")
duration = video.duration

print("Video duration: {:.2f} seconds".format(duration))