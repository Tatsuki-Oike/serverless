from PIL import Image

# 設定
SAMPLE_IMAGE = "../images/cat.jpg"
RESIZE_IMAGE = "../images/output.jpg"

with Image.open(SAMPLE_IMAGE) as img:
    resized_img = img.resize((256, 256))
    resized_img.save(RESIZE_IMAGE)