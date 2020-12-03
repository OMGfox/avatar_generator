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


def random_eyes():
    path_to_eyes = os.path.join("face_parts", "eyes")
    eyes = random.choice(os.listdir(path_to_eyes))
    image = Image.open(os.path.join(path_to_eyes, eyes), mode="r")
    return image.resize((SIZE, SIZE))


def random_nose():
    path_to_nose = os.path.join("face_parts", "nose")
    nose = random.choice(os.listdir(path_to_nose))
    image = Image.open(os.path.join(path_to_nose, nose), mode="r")
    return image.resize((SIZE, SIZE))


def random_mouth():
    path_to_mouth = os.path.join("face_parts", "mouth")
    mouth = random.choice(os.listdir(path_to_mouth))
    image = Image.open(os.path.join(path_to_mouth, mouth), mode="r")
    return image.resize((SIZE, SIZE))


def create_random_avatar():
    image = Image.new(mode="RGB", size=(SIZE, SIZE), color=random.choice(DEFAULT_COLORS))
    eyes = random_eyes()
    nose = random_nose()
    mouth = random_mouth()
    image.paste(eyes, (0, 0), eyes)
    image.paste(eyes, (0, 0), nose)
    image.paste(eyes, (0, 0), mouth)
    image.show()


create_random_avatar()
