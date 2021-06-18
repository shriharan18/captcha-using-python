# This code was written by Shreeharan for the YouTube Channel Stark Intelligence
# import the package
from captcha.image import ImageCaptcha

# store it in image and set the dimensions
image = ImageCaptcha(width=280, height=90)

# generate method
data = image.generate('7gb9hju58f')

#write it into a file
image.write('7gb9hju58f', 'captcha1.png')
