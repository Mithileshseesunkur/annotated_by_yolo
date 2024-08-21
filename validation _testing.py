from ultralytics import YOLO

model=YOLO(r"D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\best.pt")
model.val()