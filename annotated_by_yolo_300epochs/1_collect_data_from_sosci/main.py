import pandas as pd

df=pd.read_excel(r'D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\annotated_by_yolo_300epochs\1_collect_data_from_sosci\test.xlsx',usecols=[7,8,10,11], skiprows=1)

print(df)
