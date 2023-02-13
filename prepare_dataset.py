import os
import cv2

final_size = [512, 512]
folder = 'ui_dataset_cropped'
results_folder = 'results'

# creating the results folder
os.mkdir(results_folder)

files = os.listdir(folder)
images = []