from moviepy.editor import *
'''clips=[]
clip1=ImageClip(r'imag\im.jpg').set_duration(5)
clip2=ImageClip(r'imag\raj.jpg').set_duration(5)
clip3=ImageClip(r'imag\ii.jpg').set_duration(5)
clip4=ImageClip(r'imag\iim.jpg').set_duration(5)
# clip3=ImageClip(r'H:\automation_scripts\learn\imag\4.png').set_duration(3)
clips.append(clip1)
clips.append(clip2)
clips.append(clip4)
clips.append(clip3)
video_clip=concatenate_videoclips(clips,method='compose')
aa=video_clip.write_videofile("video11.mp4",fps=24,remove_temp=True,codec='libx264',audio_codec='aac')'''
video11=VideoFileClip(r'H:\automation_scripts\web_stories\video11.mp4')
song=AudioFileClip(r"C:\Users\Acer\Desktop\New folder\song.mp3")
songg=song.subclip(0,30)
final_video=video11.set_audio(songg)
final_video.write_videofile(r'H:\automation_scripts\web_stories\newvideo.mp4')
