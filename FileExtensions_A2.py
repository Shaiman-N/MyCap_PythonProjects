# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 21:04:23 2023

@author: Aiman Sabah
"""

import os
from pathlib import Path
p=Path.home()
file=input("Enter the file name with extension : ")
file_name, file_extension = os.path.splitext(file)

print("Extension of the given file is ",file_extension)