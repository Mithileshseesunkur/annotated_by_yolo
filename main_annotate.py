import os
from ultralytics import YOLO
import numpy as np
from PIL import Image

def yolo_(image_path):
    model = YOLO(r"D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\best_300.pt")

    source_image = image_path
    result = model.predict(source_image,classes=[0,1,2,5]) #add classes=[...] to predict specific classes 

    predicted_classes = []

    for r in result:
        for c in r.boxes.cls:
            predicted = model.names[int(c)]
            predicted_classes.append(predicted)

        im_array = r.plot(line_width=1) #line_width to change line thickness
        im = Image.fromarray(im_array[..., ::-1])

    predicted_classes = np.unique(predicted_classes)
    predicted_classes = predicted_classes.tolist()

    # Save the image to path
    image_name = os.path.basename(image_path)
    image_save_path = os.path.join(r'D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\annotated_by_yolo_300epochs\cars_and_stuff_yolo_detected', image_name)
    im.save(image_save_path)

    # Save the predicted classes to path
    #txt_save_path = os.path.join(r'D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\annotated_by_yolo_300epochs\test_part_2\TL_yolo_detected_labels', os.path.splitext(image_name)[0] + '.txt')
    #with open(txt_save_path, 'w') as f:
        #for cls in predicted_classes:
            #f.write(cls + '\n')

#listing all files
def list_files_in_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

#folder_path_bikes_cars_etc = r'D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\photos with GT\test_part_2\chosen_cars_and_stuff_photos'
folder_path_TL = r'D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\annotated_by_yolo_300epochs\cars_etc_orig'
files = list_files_in_folder(folder_path_TL)

for file in files:
    yolo_(file)





# Load a model



# def yolo_(image_path):
    
#     model= YOLO(r"D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\best.pt")    

#     #source_image=r"D:\Coding_\Reflex_\Reflex_\assets\test_images\t1.png"
#     source_image=image_path #for current image being shown
#     #source_predicted=r"D:\Coding_\Reflex_\Reflex_\assets\test_images"
#     result=model.predict(source_image) # using directly as PIL image therefore
#                                 #not necessary to save result

#     predicted_classes = []

#     for r in result:
#         for c in r.boxes.cls:
#             predicted=model.names[int(c)] 
#             predicted_classes.append(predicted)
#             #new
#             im_array=r.plot() #plot a BGR numpy array of predictions
#             im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image to be used to display
#                                                         # wo saving

#     predicted_classes = np.unique(predicted_classes) # remove duplicates
#     predicted_classes=predicted_classes.tolist() # convert to type list
#     print(predicted_classes)
#     im.show()
#     return predicted_classes, im


    

