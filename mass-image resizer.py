#! python3
# mass-image-resizer.py - Mass image resizer, reformatter and optimizer
#
# 1st arg is percentage for new filesize dimensions
# 2nd arg is image quality percentage
# If no arguments, default values are used

from PIL import Image
from pathlib import Path
import sys
import re

# Default settings
DEFAULT_QUALITY = 70  # default quality setting
DEFAULT_RESIZE_FACTOR = 95  # default resize factor
DEFAULT_WIDTH = 1300  # Default width for "res" mode

def resize_image(image, width, height):
	"""Resize image based on given width and height."""
	return image.resize((width, height))

def handle_image_conversion(image, extension):
	"""Convert image if needed based on its extension."""
	if extension in ['png', 'webp']:
		image = image.convert('RGB')
	return image

def main():
	# Default values
	raw_resize_factor = DEFAULT_RESIZE_FACTOR
	raw_quality = DEFAULT_QUALITY
	res_job = False

	# Handle command-line arguments
	if len(sys.argv) == 3:  # 3 arguments: mode + resize factor + quality
		if sys.argv[1] == 'res':  # "res" mode
			res_job = True
			raw_resize_factor = DEFAULT_RESIZE_FACTOR  # "res" mode ignores resize_factor
			raw_quality = DEFAULT_QUALITY  # Default quality for "res"
		else:  # "resize" mode (default)
			raw_resize_factor = sys.argv[1]
			raw_quality = sys.argv[2]
	elif len(sys.argv) == 2:  # 2 arguments: mode + resize factor or width
		if sys.argv[1] == 'res':  # "res" mode
			res_job = True
			raw_resize_factor = DEFAULT_RESIZE_FACTOR  # "res" mode ignores resize_factor
			raw_quality = DEFAULT_QUALITY  # Default quality for "res"
		else:  # Only resize_factor with no quality
			raw_resize_factor = sys.argv[1]
			raw_quality = DEFAULT_QUALITY  # Default quality if only resize factor provided
	elif len(sys.argv) == 1:  # No arguments
		raw_resize_factor = DEFAULT_RESIZE_FACTOR  # default value
		raw_quality = DEFAULT_QUALITY  # default value

	if not res_job:
		resize_factor = int(raw_resize_factor) / 100

	# Set paths
	source_path = Path(r'C:\Users\YOURNAMEHERE\Desktop')
	folder_name = 'resized'
	destination_path = source_path / folder_name
	destination_path.mkdir(parents=True, exist_ok=True)

	# Build regex for image files (jpg, png, jpeg, webp)
	image_pattern = re.compile(r".*\.(jpg|png|jpeg|webp)$", re.IGNORECASE)

	# Process images in the source folder
	for filename in source_path.iterdir():
		if not image_pattern.match(filename.name):
			continue

		# Open image
		image = Image.open(filename)

		# Handle extension-specific conversion
		file_extension = filename.suffix[1:].lower()  # Get the extension (without dot)
		image = handle_image_conversion(image, file_extension)

		# Resize logic
		width, height = image.size
		if res_job:
			# In "res" mode, the user provides the width, and the height is scaled proportionally.
			user_width = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_WIDTH  # Use default width if not provided
			height = round(height * (user_width / width))
			width = user_width
		else:
			# In "resize" mode, resize based on percentage factor.
			width = round(width * resize_factor)
			height = round(height * resize_factor)

		# Resize and save the image
		resized_image = resize_image(image, width, height)

		# Save the resized image with the correct file extension
		output_filename = filename.stem + '.jpg'
		resized_image.save(destination_path / output_filename, optimize=True, quality=int(raw_quality))

if __name__ == "__main__":
	main()
