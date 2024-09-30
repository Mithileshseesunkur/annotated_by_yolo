import pandas as pd

gender_col=7
age_col=8
license_age=10
km_driven=11

ques_start=12
ques_end=102

df_collected=pd.read_excel(r'D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\annotated_by_yolo_300epochs\1_collect_data_from_sosci\test.xlsx',usecols=[gender_col,age_col,license_age,km_driven]+list(range(ques_start,ques_end)), skiprows=1)


# Display current headers
print("Current Headers:", df_collected)

# Rename specific headers
df_collected.rename(columns={
    'GenderSelection': 'Gender',  # Replace 'OldHeader1' with the actual name
    'AgeInput: Age': 'Age',
    'LicenseAge: [01]': 'Licence Age',  
    'kmDriven': 'kilometres driven'
}, inplace=True)

print(df_collected)

#workflow 1
w1_col_to_drop=df_collected.columns[34:102]
w1_df_collected=df_collected.drop(w1_col_to_drop, axis=1)
print(w1_df_collected)

#workflow 2
w2_col_to_drop=df_collected.columns[4:34]
w2_df_collected=df_collected.drop(w2_col_to_drop, axis=1)
print(w2_df_collected)


no_rows=len(df_collected)
print(f"this is no of rows in collected data: {no_rows}")

#the ground truth specific to this survey
df_GT=pd.read_excel(r'D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\annotated_by_yolo_300epochs\Groundtruth accordding to survey\GTsurvey.xlsx')

print("this")
#print(df_GT.iloc[0][1]) # iloc to locate exactly by row, col

#arrange table by ascending age
df_collected_age_ascend=df_collected.sort_values('Age', ascending=True)
#for i in range(0,)
ans_df_collected_age_ascend=df_collected_age_ascend.iloc[0][4:]
#age_completion_rate=

#arrange table by ascending license age
df_collected_licenceAge_ascend=df_collected.sort_values('Licence Age', ascending=True)
#print(df_collected_licenceAge_ascend)


#arrange table by ascending km driven
df_collected_km_ascend=df_collected.sort_values('kilometres driven', ascending=True)
#print(df_collected_km_ascend)


#arrange table by ascending likert points
