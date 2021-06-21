#!/usr/bin/env python3

import os
import random

from PIL import Image

SIZE = 500

DEFAULT_COLORS = (
    0x81bef1,
    0xad8bf2,
    0xbff288,
    0xde7878,
    0xa5aac5,
    0x6ff2c5,
    0xf0da5e,
    0xeb5972,
    0xf6be5d,
)


def random_part(part: str):
#    path = os.path.join("avatar_generator", "face_parts", part)
    path = os.path.join("face_parts", part)
    part_name = random.choice(os.listdir(path))
    image = Image.open(os.path.join(path, part_name), mode="r")
    return image.resize((SIZE, SIZE))


def create_random_avatar() -> Image:
    image = Image.new(mode="RGB", size=(SIZE, SIZE), color=random.choice(DEFAULT_COLORS))
    eyes = random_part(part="eyes")
    nose = random_part(part="nose")
    mouth = random_part(part="mouth")
    image.paste(eyes, (0, 0), eyes)
    image.paste(eyes, (0, 0), nose)
    image.paste(eyes, (0, 0), mouth)
    return image


if __name__ == "__main__":

    avatar = create_random_avatar()
    avatar.save("avatar.png", formate="png")
