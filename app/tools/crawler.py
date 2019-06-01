import os
from typing import Dict

import yaml

PHOTO_DIR = os.path.join(os.getcwd(), "app/static/pictures")  # create absolute path


def get_images() -> Dict[str, Dict]:
    """Returns image information and paths for photos view"""
    image_info = {}

    for file in os.listdir(PHOTO_DIR):
        if file.endswith(".jpg"):
            path = os.path.join(PHOTO_DIR, file)
            name = os.path.splitext(path)[0]  # remove file extension
            info_file = name + ".yml"
            image_info[file] = yaml.safe_load(open(info_file))["metadata"]

    return image_info
