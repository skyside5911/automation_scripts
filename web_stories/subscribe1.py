from moviepy.editor import *

# Load the two videos
background_video = VideoFileClip(r'H:\automation_scripts\web_stories\n1.mp4')
foreground_video = VideoFileClip(r'H:\automation_scripts\web_stories\sus.mp4').resize(width=100,height=200)
# Repeat the foreground video if it's shorter than the background video
if foreground_video.duration < background_video.duration:
    repeat_count = int(background_video.duration / foreground_video.duration) + 1
    foreground_video = concatenate_videoclips([foreground_video for i in range(repeat_count)])

# Overlay the foreground video on top of the background video
final_video = CompositeVideoClip([background_video, foreground_video.set_pos((0,0))])

# Write the output video
final_video.write_videofile(r'H:\automation_scripts\web_stories\n12.mp4', fps=background_video.fps)
