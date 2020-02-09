# -*- coding: utf-8 -*-
"""
    app.misc.imaging
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for image handling methods.
    -- Make thumbnails.
    -- Save image safely.

    :copyright: (c)2020 by rico0821

"""
import os
import uuid

from flask import current_app
from PIL import Image
from werkzeug.utils import secure_filename

from app.misc.logger import Log


def make_thumbnails(filename, usage):
    upload_folder = os.path.join(current_app.root_path,
                                 current_app.config["UPLOAD_FOLDER"],
                                 usage)
    original_file = upload_folder + filename
    target_name = upload_folder + "thumb_" + filename

    try:
        im = Image.open(original_file)
        im = im.convert('RGB')
        im.thumbnail((300, 300), Image.ANTIALIAS)
        im.save(target_name)

    except Exception as e:
        Log.error("Thumbnails creation error : " + target_name + " , " + str(e))
        raise e


def make_filename(img, user, extra=None):
    ext = img.filename.rsplit(".", 1)[1]
    filename = secure_filename(user.id +
                               "_" +
                               extra +
                               "_" +
                               str(uuid.uuid4()) +
                               "." +
                               ext)
    return filename


def save_image(img, filename, usage):
    upload_folder = os.path.join(current_app.root_path,
                                 current_app.config["UPLOAD_FOLDER"],
                                 usage)
    img.save(os.path.join(upload_folder, filename))
