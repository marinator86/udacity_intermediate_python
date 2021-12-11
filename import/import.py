import sys
import PIL
from PIL import Image, ImageDraw, ImageFont
from pprint import pprint


def generate_postcard(in_path, out_path, message=None, crop=None, width=None):
    """Create a Postcard With a Text Greeting

    Arguments:
        in_path {str} -- the file location for the input image.
        out_path {str} -- the desired location for the output image.
        crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
        width {int} -- The pixel width value. Default=None.
    Returns:
        str -- the file path to the output image.
    """
    with Image.open(in_path) as im:
        if not crop:
            crop = (0, 0, *im.size)
        if not width:
            width = im.size[0]
        height = int(width * (crop[3] - crop[1]) / (crop[2] - crop[0]))
        im2 = im.resize((width, height), box=crop)
        if message:
            # get a font
            fnt = ImageFont.truetype("LilitaOne-Regular.ttf", 40)
            # get a drawing context
            d = ImageDraw.Draw(im2)
            # draw multiline text
            d.multiline_text((width/2, height/2), message, font=fnt, fill=(255, 255, 255))
        im2.save(out_path)
        im2.show()
        return im2

if __name__ == '__main__':
    pprint(sys.path)
    pprint(sys) # builtin
    pprint(PIL)

    im = Image.open("dog.jpeg")
    print(im)
    print(im.size)
    #im.show()
    print(generate_postcard('dog.jpeg', 'dog2.jpeg', message="Mami?", crop=(400, 20, 920, 404)))
