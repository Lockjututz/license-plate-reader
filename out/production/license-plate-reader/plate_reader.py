import cv2
import matplotlib.pyplot as plt
import pytesseract
import re
pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"

img = cv2.imread("resources/tesla2.jpg")

plt.imshow(img)
plt.axis('off')
plt.title('GWT2180 license plate')

resize_test_license_plate = cv2.resize(
    img, None, fx=2, fy=2,
    interpolation=cv2.INTER_CUBIC)

grayscale_resize_test_license_plate = cv2.cvtColor(
    resize_test_license_plate, cv2.COLOR_BGR2GRAY)

gaussian_blur_license_plate = cv2.GaussianBlur(
    grayscale_resize_test_license_plate, (5, 5), 0)

img_rgb = cv2.cvtColor(gaussian_blur_license_plate, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(img_rgb,
                                   lang='swe',
                                   config='--oem 3 --psm 6')
m = re.search('([A-Å]{2,} [0-9]{1,})', text)
if m:
    license_plate_number = m.group(1)
    print(f"Found something: {license_plate_number}")
