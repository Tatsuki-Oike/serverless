import torch
from torchvision import models

# 学習済みモデルの保存
model = models.efficientnet_b0(weights=models.EfficientNet_B0_Weights.DEFAULT)
torch.save(model.state_dict(), 'model.pth')