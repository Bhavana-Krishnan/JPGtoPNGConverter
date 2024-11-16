# JPGtoPNGConverter.py

import os
import sys
from PIL import Image, ImageFilter

# Get the dirs name
input_dir = sys.argv[1]
output_dir = sys.argv[2]

# print(input_dir, output_dir)

if not os.path.exists(output_dir):
    os.mkdir(output_dir)


if os.path.exists(input_dir):
    for file in os.listdir(input_dir):
        if file.lower().endswith(('.jpg', '.jpeg')):
            image = Image.open("./" + input_dir + '/' + file)
            ext = os.path.splitext(file)
            # print(ext)
            filename = ext[0]
            image.save(output_dir + '/' + filename + '.png', 'png')
    print('All Done!')
