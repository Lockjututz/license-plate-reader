import cv2
import matplotlib.pyplot as plt
import pytesseract
import re

"""
Extract an Åland/Swedish/Finnish licence plate from a picture.

You must install tesseract separately before running this script. On MacOS:

brew install tesseract
brew install tesseract-lang

On Linux use apt-get. Windows? Google it.

Then you must install all the required packages specified in the requirements.txt file. Like this:

pip install -r requirements.txt

Run the script:

python plate_reader.py

"""

pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"

# Read the picture with the license plate
img = cv2.imread("resources/tesla2.jpg")

# Do some image enhancement
resize_test_license_plate = cv2.resize(
    img, None, fx=2, fy=2,
    interpolation=cv2.INTER_CUBIC)

grayscale_resize_test_license_plate = cv2.cvtColor(
    resize_test_license_plate, cv2.COLOR_BGR2GRAY)

gaussian_blur_license_plate = cv2.GaussianBlur(
    grayscale_resize_test_license_plate, (5, 5), 0)

img_rgb = cv2.cvtColor(gaussian_blur_license_plate, cv2.COLOR_BGR2RGB)

# Plot and show the image (visible in the SciView Plot tab in PyCharm)
# This isn't necessary, just fun to look at the picture after enhancement
plt.imshow(img_rgb)
plt.axis('on')
plt.title('License plate')
plt.show()

# Actually parse the license plate number from the picture
text = pytesseract.image_to_string(img_rgb,
                                   lang='swe',
                                   config='--oem 3 --psm 6')

# Do a regexp search to find strings that match an actual license plate
m = re.search('([A-Å]{2,} [0-9]{1,})', text)
if m:
    license_plate_number = m.group(1)
    print(f"Found something: {license_plate_number}")
