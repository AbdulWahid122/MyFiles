"""
1. What does RGBA stand for?

Red Green Blue Alpha, RGB color model is extended in this specification to include "alpha" to 
allow  specification of the opacity of a color.

2. From the Pillow module, how do you get the RGBA value of any images?

Import the image module from the pillow library
 
 from PIL import image

Open any image and get the RAGBAG Values by

 img=Image.open('image.png')
 rgba=img.convert('RGBA')
 datas=rgba.getdata()


3. What is a box tuple, and how does it work?

The box.tuple submodule provides read only access for the tuple userdata type.It allows for a 
single tuple:selective retrieval of the field contents, retrieval of information of the field
contents, retrieval of information about size, iteration over all the field and conversation 
to a Lua table.

4. Use your image and load in notebook then, How can you find out the width and height of an
Image object?

from PIL import Image

img=Image.open('image.png')

width=img.width
height=img.height

print('The height of the image is:',height)
print('The width of the image is:',width)

5. What method would you call to get Image object for a 100×100 image, excluding the lower-left
quarter of it?

The Image class contains methods allowing you to manipulate regions within an image.
To extract a sub rectangle from an image, use the crop() method.

6. After making changes to an Image object, how could you save it as an image file?

 image.save("filename") 


7.what module contains Pillow's shape-drawing code?

ImageDraw module


8. Image objects do not have drawing methods. What kind of object does? How do you get this kind
of object?

Drawing objects include shapes,diagrams,flowcharts,curves,lines, and WordArt.

ImageDraw Module

This provides options like draw on images, draw lines, circles,rectangles and even write and 
format text on an image.


from PIL import Image, ImageDraw

img=Image.open('filename.png')
img.show()

we can draw shapes and figures on an Image using the Draw method by creating draw object.

ImageDraw.rectangle(xy,fill,outline,width)









"""