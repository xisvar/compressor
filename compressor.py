#Komments for twitta post
# i actually speak very good english.
import os
from PIL import Image

output_dir = "output_directory"

input_dir = "input_directory"
def compress_images(input_dir, output_dir, quality=2):
  # Create output directory if it doesn't exist
  if not os.path.exists(output_dir):
      os.makedirs(output_dir)
    
  # Gets a list of files in the input directory
  files = os.listdir(input_dir)

  for file in files:
      # Full path of the image file
      img_path = os.path.join(input_dir, file)
      
      # Check if the file is an image cause why not? you don't want to mess with other things yk
      if os.path.isfile(img_path) and file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
          # Open the image file
          img = Image.open(img_path)
          
          # Compresses to set quality and then saves the image
          #cool stuff
          output_path = os.path.join(output_dir, file)
          img.save(output_path, optimize=True, quality=quality)
          
          print(f"Compressed {file} and saved to {output_path}")


compress_images(input_dir, output_dir)

