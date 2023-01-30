from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.audio.fx.volumex import volumex
# Load the video
video = VideoFileClip(r"H:\automation_scripts\web_stories\newvideo2.mp4")

# Load the audio
audio = video.audio

# Edit the audio (for example, reduce the volume by 50%)
audio_reduced = audio.fx(volumex, 0.5)

# Add the edited audio back to the video
video = video.set_audio(audio_reduced)

# Save the video with the edited audio
video.write_videofile(r"H:\automation_scripts\web_stories\newvideo21.mp4")
