#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle

image_folder_path = "/home/chli/chLi/ScanNet/scans/scene0000_00/frames/color/"

output_file_path = "/home/chli/chLi/ScanNet/scannet_imgs"

image_filename_list = os.listdir(image_folder_path)

image_file_basename_list = [image_filename.split(".")[0] for image_filename in image_filename_list]

scannet_imgs_dict = {
    "scene0000_00": {
        "img_names": image_file_basename_list[:1000],
    }
}

with open(output_file_path, "wb") as f:
    pickle.dump(scannet_imgs_dict, f)

