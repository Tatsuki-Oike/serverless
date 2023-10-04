import json
import base64
from io import BytesIO
from PIL import Image
import torch
from torchvision import models
import traceback
import urllib

model_url = 'https://[bucket-name].s3.ap-northeast-1.amazonaws.com/model.pth'

def image_recognition(image):

    # Step 1: Initialize model with the best available weights
    print("Load Model")
    model_buffer = BytesIO(urllib.request.urlopen(model_url).read())
    model = models.efficientnet_b0(pretrained=False)
    model.load_state_dict(torch.load(model_buffer))
    weights = models.EfficientNet_B0_Weights.DEFAULT
    model.eval()

    # Step 2: Initialize the inference transforms
    print("Preprocess")
    preprocess = weights.transforms()
    batch = preprocess(image).unsqueeze(0)

    # Step 3: Use the model and print the predicted category
    print("prediction")
    prediction = model(batch).squeeze(0).softmax(0)
    class_id = prediction.argmax().item()
    score = prediction[class_id].item()
    category_name = weights.meta["categories"][class_id]

    return score, category_name


def handler(event, context):
    try:
        
        if event.get("body"):
            body = event.get("body")
            image_b64 = json.loads(body)["image_b64"]
        else:
            image_b64 = event["image_b64"]

        image_byte = base64.b64decode(image_b64.encode("utf-8"))
        image_file = BytesIO(image_byte)
        image_pil = Image.open(image_file).convert('RGB')
        score, category_name = image_recognition(image_pil)

        response = {
            "status": "SUCCESS",
            "score": str(round(score, 2)),
            "category": str(category_name)
        }
        status_code = 200
    except Exception as e:
        response = {
            "status": "ERROR",
            "error": str(e),
            "details": str(traceback.format_exc())
        }
        status_code = 500
    return {
        'statusCode': status_code,
        'body': json.dumps(response)
    }