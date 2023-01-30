import cv2

# Read the two videos
background_video = cv2.VideoCapture(r'H:\automation_scripts\web_stories\n1.mp4')
foreground_video = cv2.VideoCapture(r'H:\automation_scripts\web_stories\sus.mp4')

# Get the video properties
fps = int(background_video.get(cv2.CAP_PROP_FPS))
frame_count = int(background_video.get(cv2.CAP_PROP_FRAME_COUNT))
frame_width = int(background_video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(background_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set up the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(r'H:\automation_scripts\web_stories\n12.mp4', fourcc, fps, (frame_width, frame_height))

# Overlay the two videos
frame_index = 0
while True:
    ret, background_frame = background_video.read()
    if not ret:
        break
    foreground_video.set(cv2.CAP_PROP_POS_FRAMES, frame_index % foreground_video.get(cv2.CAP_PROP_FRAME_COUNT))
    ret_fg, foreground_frame = foreground_video.read()
    foreground_frame = cv2.resize(foreground_frame, (frame_width, frame_height))
    blended = cv2.addWeighted(background_frame, 0.7, foreground_frame, 0.3, 0)
    out.write(blended)
    frame_index += 1

# Release resources
background_video.release()
foreground_video.release()
out.release()
