from moviepy.editor import *

video = VideoFileClip("input.mp4") # input video file, same folder as app.py
W,H = video.size

# Input logo, preferable png with no background
logo = (ImageClip("logo.png")
          .set_duration(video.duration)
          .resize(height=H/5) # if you need to resize...
          .margin(right=int(W/20), top=int(H/20), opacity=0) # position of logo
          .set_pos(("right","top")))

final = CompositeVideoClip([video,logo])
final.write_videofile("output.mp4") # output file
