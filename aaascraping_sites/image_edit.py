from PIL import Image,ImageFont,ImageDraw
text='this is new text'
colour=255,255,255
img_width,img_height=800,600
img=Image.open()
font=ImageFont.truetype("")
draw=ImageDraw.Draw(img)
t_width,t_height=draw.textsize(text,font)
position=((img_width-t_width)/2,(img_height-t_height)/2)
draw.text(position,text,colour,font=font)
img.save("imag.jpg")