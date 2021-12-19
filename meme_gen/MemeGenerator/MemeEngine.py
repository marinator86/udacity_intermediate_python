"""Contains the MemeEngine class."""
from PIL import Image, ImageDraw, ImageFont
import random
import os


class MemeEngine:
    """Generates a meme."""

    def __init__(self, output_dir):
        """Construct a MemeEngine.

        :param output_dir: the directory to save created memes in
        """
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path: str, text: str, author: str,
                  width: int = 500) -> str:
        """Create a meme with a quote.

        :param img_path: the file location for the input image.
        :param text: the quote text.
        :param author: the quote author.
        :param width: the pixel width value. Default=500.
        :return: the file path to the output image.
        """
        with Image.open(img_path) as im:
            if width > 500:
                width = 500
            height = int(width * im.size[1] / im.size[0])
            im2 = im.resize((width, height))

            # get a font
            fnt = ImageFont.truetype("./_data/fonts/LilitaOne-Regular.ttf",
                                     int(width/12))
            # get a drawing context
            d = ImageDraw.Draw(im2)
            # draw multiline text
            d.multiline_text((width * 1/20, height * 4/5),
                             f"\"{text}\"\n{author}",
                             font=fnt, fill=(255, 255, 255))

            out_path = f"{self.output_dir}/{random.randint(0, 100000000)}.jpg"
            im2.save(out_path)
            return out_path
