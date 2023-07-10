# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 02:48:55 2023

"""

import torch
from pathlib import Path
from PIL import Image
from tqdm import tqdm

# YOLOv5 kütüphanesini projeye dahil et
yolov5_dir = Path('C:/Users/PC/yolov5-master')
weights = 'm'  # yolov5m modeli kullanılacak

data_dir = Path('C:/Users/PC/NesneTanıma/model_m/Dataset')
img_dir = data_dir / 'images'
train_txt = data_dir / 'train.txt'
test_txt = data_dir / 'test.txt'

# Sonuçların kaydedileceği dizin
results_dir_m = data_dir / 'results_m'
results_dir_m.mkdir(exist_ok=True)

# GPU kullanımı kontrolü
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# YOLOv5 modelini yükle
model_m = torch.hub.load(str(yolov5_dir), 'custom', path=str(yolov5_dir / 'weights' / f'yolov5{weights}.pt'), source='local').to(device)
model_m.conf = 0.25  # Algılama eşiği (confidence threshold) ayarı

# Eğitim işlemi
def train():
    with open(train_txt, 'r') as f:
        train_lines = f.readlines()
    
    for line in tqdm(train_lines, desc='Training'):
        img_path = line.strip()
        img = Image.open(img_path).convert('RGB')
        results = model_m(img)
      
# Tahmin işlemi
def predict_m():
    with open(test_txt, 'r') as f:
        test_lines = f.readlines()
    # Tahmin sonuçlarını txt dosyasına kaydet
    with open(results_dir_m / 'modelmtahmini.txt', 'a') as f:
        for line in tqdm(test_lines, desc='Predicting'):
            img_path = line.strip()
            img = Image.open(img_path).convert('RGB')
            results = model_m(img)
            results.print()  # Tahmin sonuçlarını konsola yazdır
            save_path = str(results_dir_m / Path(img_path).name)
            results.save(save_path)  # Tahmin sonuçlarını kaydet
            #tahmin verilerini txt olarak kaydetme
            f.write(f"Image: {img_path}\n")
            f.write(results.pandas().xyxy[0].to_csv(sep=' ', header=False, index=False))
            f.write("\n\n")
    
# Eğitim işlemi
train()

# Tahmin işlemi
predict_m()