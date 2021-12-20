"""Contains the MemeEngine class."""
from PIL import Image, ImageDraw, ImageFont
import random
import os
import textwrap
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
        self.textbox_ratio = 0.8
        self.text_fraction = 15
        self.font_path = "./_data/fonts/LilitaOne-Regular.ttf"

    def make_meme(self, img_path: str, text: str, author: str,
                  width: int = 500) -> str:
        """Create a meme with a quote.

        :param img_path: the file location for the input image.
        :param text: the quote text.
        :param author: the quote author.
        :param width: the pixel width value. Default=500.
        :return: the file path to the output image.
        """
        with Image.open(img_path) as initial_image:
            if width > 500:
                width = 500
            image = self.resize(initial_image, width)
            text_size = self.find_initial_size(image)
            min_wrap = len(max(text.split()))
            wrapped_text = f"\"{text}\"\n{author}"
            x, y = self.measure(image, wrapped_text, text_size)

            while self.check_textbox_size(image, x, y):
                wrap_chars = int(image.width * self.textbox_ratio
                                 / x * len(text))
                wrap_width = max(wrap_chars, min_wrap)
                wrapped_text = f"\"{textwrap.fill(text, wrap_width)}" \
                               f"\"\n{author}"
                x, y = self.measure(image, wrapped_text, text_size)
                if self.check_textbox_size(image, x, y):
                    text_size -= 1

            x_rand = random.randrange(10, image.width - x - 10)
            y_rand = random.randrange(10, image.height - y - 10)

            self.draw_text(image, wrapped_text, text_size, (x_rand, y_rand))
            out_path = f"{self.output_dir}/{random.randint(0, 100000000)}.jpg"
            image.save(out_path)
            return out_path

    def resize(self, initial_image, width):
        """Resize the image to the given width."""
        height = int(width * initial_image.size[1] / initial_image.size[0])
        image = initial_image.resize((width, height))
        return image

    def find_initial_size(self, image):
        """Find the inital (and maximum) size of the text to write.

        :param image: the image to check.
        :return: the intial size, in points.
        """
        size = 10
        desired_height = image.height / self.text_fraction
        fnt = ImageFont.truetype("./_data/fonts/LilitaOne-Regular.ttf", size)
        x1, y1, x2, y2 = ImageDraw.Draw(image).multiline_textbbox((0, 0), "O",
                                                                  font=fnt)
        return int(size * desired_height / (y2 - y1))

    def check_textbox_size(self, image, x, y):
        """Check if the box given by x,y fits into the given image."""
        x_oversized = x > image.width * self.textbox_ratio
        y_oversized = y > image.height * self.textbox_ratio
        return x_oversized or y_oversized

    def measure(self, image, text, text_size):
        """Measure the given text and author on the given image.

        :param image: the image to measure on.
        :param author: the quote's author.
        :param text: the quote's text.
        :param text_wrap_width: the width of the textwrap.
        :param text_size: the text size to measure.
        :return:
        """
        fnt = ImageFont.truetype(self.font_path, text_size)
        textsize = ImageDraw.Draw(image).multiline_textbbox((0, 0), text,
                                                            font=fnt)
        return textsize[2] - textsize[0], textsize[3] - textsize[1]

    def draw_text(self, image, text, text_size, location):
        """Draw the text on the image on the given location with given size."""
        fnt = ImageFont.truetype(self.font_path, text_size)
        ImageDraw.Draw(image).multiline_text(location, text, font=fnt,
                                             fill=(255, 255, 255))
