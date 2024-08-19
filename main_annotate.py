import os
from ultralytics import YOLO
import numpy as np
from PIL import Image

#listing all files
def list_files_in_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

folder_path_bikes_cars_etc = r'C:\Users\mseesunker\Desktop\YOLO\trained_model\MA_model-20240819T084430Z-001\to_send\to_send\chosen_15_bikes_pedestrial_car_truck'
files = list_files_in_folder(folder_path_bikes_cars_etc)
for file in files:
    print(file)

file=files[1]



# Load a model



def yolo_(image_path):
    
    model= YOLO("best.pt")    

    #source_image=r"D:\Coding_\Reflex_\Reflex_\assets\test_images\t1.png"
    source_image=image_path #for current image being shown
    #source_predicted=r"D:\Coding_\Reflex_\Reflex_\assets\test_images"
    result=model(source_image) # using directly as PIL image therefore
                                #not necessary to save result

    predicted_classes = []

    for r in result:
        for c in r.boxes.cls:
            predicted=model.names[int(c)] 
            predicted_classes.append(predicted)
            #new
            im_array=r.plot() #plot a BGR numpy array of predictions
            im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image to be used to display
                                                        # wo saving

    predicted_classes = np.unique(predicted_classes) # remove duplicates
    predicted_classes=predicted_classes.tolist() # convert to type list
    print(predicted_classes)
    return predicted_classes, im

yolo_(file)