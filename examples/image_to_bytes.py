# import pprint
#
# with open(r"..\1.png", "rb") as image:
#     f = image.read()
#     b = bytearray(f)
#     # pprint.pprint(b)
#     print(b)

import io
from PIL import Image

# Open image using the pillow package
img = Image.open(r"..\icon.png",)
# initialiaze io to_bytes converter
img_byte_arr = io.BytesIO()
# define quality of saved array
img.save(img_byte_arr, format='PNG', subsampling=0, quality=100)
# converts image array to bytesarray
img_byte_arr = img_byte_arr.getvalue()
print(img_byte_arr)
