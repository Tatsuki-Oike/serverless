import base64

# 設定
RESIZE_IMAGE = "../images/output.jpg"

# 画像をbase64形式に
print("\nLoad Image")
with open(RESIZE_IMAGE, "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode("utf-8")
print(image_b64)