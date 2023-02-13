import os
import cv2

final_size = [512, 512]
folder = 'ui_dataset_cropped'
results_folder = 'results'

# creating the results folder
os.mkdir(results_folder)

files = os.listdir(folder)
images = []
resized_images = []

#reading all images
for file in files:
    address = f'{folder}/{file}'
    images.append(cv2.imread(address))

print(len(images))

#resizing all images
for image in images:
    image = cv2.resize(image, final_size)
    resized_images.append(image)

for name, image in zip(files, resized_images):
    print(name, image.shape)