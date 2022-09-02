#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

pickle_file_path = "./result/e2e/scene0000_00/scene0000_00"

with open(pickle_file_path, "rb") as f:
    data_dict = pickle.load(f)

print(data_dict["quadrics"][0])

