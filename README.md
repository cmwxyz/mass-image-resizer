# mass-image-resizer
Python script to quickly resize, reformat and optimize one or more image files.

I bind this script to batch file in Windows to quickly resize images. It's a very simple script but it's saved me hours upon hours of resizing in photoshop over the years.

Usage:

1. Set path for script to look for images.

2. Run script with or without arguments.

3. Not setting arguments will set default resizing and quality values.

4. Specifying a resize factor argument will resize the image according to a percentage. Ie. > "mass-image-resizer.py 33" will set the image or images in the path to 33 percent their original size.  > "mass-image-resizer.py 33 50" Will do the same, but at 50% image quality.

5. It's also possible to designate an exact resolution for the image's output width. Ie. > "mass-image-resizer.py res" will resize the width to the default width or > "mass-image-resizer.py res 2000" will set a width of 2000 pixels.

6. In addition to resizing and optimizing, the script also converts several image formats to a jpg output. It accepts as inputs jpg, png, jpeg, webp file formats. Others could be easily added. The script ignores files without these endings in the path folder.
