import torch
from torchvision import datasets, transforms
from torchvision.models import resnet50, ResNet50_Weights

# 设置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 加载预训练的 ResNet 模型
model = resnet50(weights=ResNet50_Weights.DEFAULT)  # 使用 weights 参数
model.eval()
model.to(device)

# 数据预处理
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # 调整图像大小
    transforms.Grayscale(num_output_channels=3),  # 转为 RGB
    transforms.ToTensor(),  # 转为张量
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # 归一化
])

# 下载 MNIST 数据集
mnist_data = datasets.MNIST(root='data', train=False, transform=transform, download=True)
data_loader = torch.utils.data.DataLoader(mnist_data, batch_size=32, shuffle=False)

# 运行推理
with torch.no_grad():
    correct = 0
    total = 0
    for images, labels in data_loader:
        images = images.to(device)
        labels = labels.to(device)  # 将标签移到设备上

        outputs = model(images)  # 使用图像进行推理

        _, predicted = torch.max(outputs.data, 1)  # 获取预测结果
        total += labels.size(0)
        correct += (predicted == labels).sum().item()  # 计算正确数量

    accuracy = correct / total
    print(f'准确率: {accuracy:.2f}')
