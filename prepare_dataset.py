import os
import cv2

final_size = [512, 512]
folder = 'ui_dataset_cropped'
results_folder = 'results'

# creating the results folder
os.mkdir(results_folder)

files = os.listdir(folder)
images = []

#reading all images
for file in files:
    address = f'{folder}/{file}'
    images.append(cv2.imread(address))

print(len(images))