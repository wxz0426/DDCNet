from ultralytics import YOLO
import os
from tqdm import tqdm
import os
import torch

os.environ['CUDA_LAUNCH_BLOCKING'] = '1'
def main():
    model = YOLO(r'ultralytics\cfg\models\DDCNet\DDCNet.yaml')

# Train the model

    model.train(data=r'ultralytics\cfg\datasets\VisDrone.yaml', batch=1, epochs=1, imgsz=640, workers=0, seed=0, device=0,
            pretrained=False, lr0=0.01,
            resume=True)

if __name__ == '__main__':
    main()
