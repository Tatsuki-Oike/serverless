import torch
from torchvision import models

# 学習済みモデルの保存
model = models.efficientnet_b0(pretrained=True)
torch.save(model.state_dict(), 'model.pth')