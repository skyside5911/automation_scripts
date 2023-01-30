import cv2
from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.audio.fx.volumex import volumex
import time

filename = r"H:\all_youtube_videos\top_10_youtube_shorts_knowledge"

with open(filename, "r") as file:
    contents = file.read()
    print(contents)
# loop through each link in the file
'''count=1
for line in file:
    print(line)'''
# Open the video file
'''cap = cv2.VideoCapture(r"H:\automation_scripts\web_stories\new.mp4")
    video = VideoFileClip(r"H:\automation_scripts\web_stories\new.mp4")
    duration = int(video.duration)
    # Load the audio
    audio = video.audio
    audio.write_audiofile(r"H:\automation_scripts\web_stories\audio.mp3")
    # Get the video frame dimensions
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Define the codec and create a video writer object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(r"H:\automation_scripts\web_stories\newv.mp4", fourcc, 30.0, (frame_width, frame_height))

    # Define the text and its properties
    text = "@raj-rana"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.4
    font_color = (255, 255, 255)

    # Define the background color (in this case, red)
    bg_color = (0, 0, 200)
    count=0
    while cap.isOpened():
        # Read a frame from the video
        ret, frame = cap.read()

        if ret:
            
            # Add the background color to the frame
            
            # (text_width, text_height)=50,200
            (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, 2)
            # text_origin = ((frame_width - text_width) // 2, (frame_height - text_height) // 2)
            text_origin = (226,1078)
            # print(text_origin) 
            # countt textwidth 434 == 660 981
            # (420 aage piche, 938 upr niche)

            # Add the background color to the frame
            frame = cv2.rectangle(frame,( 230, 1038 ), (460, 1100), bg_color, -1)
            cv2.putText(frame, text, text_origin, font, font_scale, font_color, 1, cv2.LINE_AA)
            
            # print("countt textwidth",count,'==',text_origin[0]+text_width, text_origin[1]+text_height)
            # frame = cv2.rectangle(frame, text_origin, (text_origin[0], text_origin[1]), bg_color, -1)
            


            # Write the frame to the output video
            out.write(frame)
            count+=1
            # cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
            # cv2.resizeWindow('frame', 600, 400)

            # # Display the frame
            # cv2.imshow('frame', frame)
            # cv2.waitKey(20)
            
            # print()
        else:
            break

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    # Release the video capture and writer objects
    time.sleep(2)
    video11=VideoFileClip(r"H:\automation_scripts\web_stories\newv.mp4")
    song=AudioFileClip(r'H:\automation_scripts\web_stories\audio.mp3')

    final_video=video11.set_audio(song)
    final_video.write_videofile(r'H:\automation_scripts\web_stories\n1.mp4')
'''