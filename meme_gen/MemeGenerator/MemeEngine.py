"""Contains the MemeEngine class."""
from PIL import Image, ImageDraw, ImageFont
import random
import os
import math


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
            fnt = ImageFont.truetype("./_data/fonts/LilitaOne-Regular.ttf",
                                     self.calculate_text_size(text, width))
            d = ImageDraw.Draw(im2)
            d.multiline_text((width * 1/20, height * 4/5),
                             f"\"{text}\"\n{author}",
                             font=fnt, fill=(255, 255, 255))

            out_path = f"{self.output_dir}/{random.randint(0, 100000000)}.jpg"
            im2.save(out_path)
            return out_path

    def calculate_text_size(self, text, width):
        """Calculate the best size for the text to write.

        :param text: the text to write.
        :param width: the width of the picture.
        :return: the best size for the text to write.
        """
        text_length = len(text)
        nominal = int(1.5 * width / text_length)
        return nominal if nominal < 40 else 40
