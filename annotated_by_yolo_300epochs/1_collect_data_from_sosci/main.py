import pandas as pd

gender_col=7
age_col=8
license_age=10
km_driven=11

ques_start=12
ques_end=102

df_collected=pd.read_excel(r'D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\annotated_by_yolo_300epochs\1_collect_data_from_sosci\test.xlsx',usecols=[gender_col,age_col,license_age,km_driven]+list(range(ques_start,ques_end)), skiprows=1)

df_GT=pd.read_excel(r'D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\annotated_by_yolo_300epochs\1_collect_data_from_sosci\GTsurvey.xlsx')



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

w1_df_GT=df_GT.drop(df_GT.columns[30:],axis=1) #GT for w1 
print(f"this is w1_df_GT: {w1_df_GT}")
print(f"this is w1_df_collected: {w1_df_collected}")

#workflow 2
w2_col_to_drop=df_collected.columns[4:34]
w2_df_collected=df_collected.drop(w2_col_to_drop, axis=1)

w2_df_GT=df_GT.drop(df_GT.columns[0:29],axis=1) #GT fr w2
print(f"this is w2_df_GT: {w2_df_GT}")
print(f"this is w2_df_collected: {w2_df_collected}")


no_rows=len(df_collected)

print(f"this is no of rows in collected data: {no_rows}")

#the ground truth specific to this survey

print("this")
#print(df_GT.iloc[0][1]) # iloc to locate exactly by row, col
w1_agreement_matrix=[]

#arrange table by ascending age
w1_df_collected_age_ascend=w1_df_collected.sort_values('Age', ascending=True)

#print(w1_df_collected_age_ascend.iloc[0,1])

for row in range(0,no_rows):

    w1_ans_df_collected_age_ascend=w1_df_collected_age_ascend.iloc[row][4:] #only answers from that row
    
    w1_agreements=[]

    for ans in range(0, w1_ans_df_collected_age_ascend.shape[0]):
        
        print(f"ans is {w1_ans_df_collected_age_ascend.iloc[ans]}\n...this is ans from gtw1 {w1_df_GT.iloc[0,ans]}")

        
        
        if pd.isna(w1_ans_df_collected_age_ascend.iloc[ans]):

            w1_agreements.append('-1') #-1 is unanswered
            
        
        elif w1_ans_df_collected_age_ascend.iloc[ans]==float(w1_df_GT.iloc[0,ans]):
           
           w1_agreements.append('1') #1 for agreement, 0 for disagreement
        
        else:
            
            w1_agreements.append('0')        
    
    w1_agreement_matrix.append(w1_agreements)

    print(w1_agreement_matrix)
         
#age_completion_rate=
#print(w1_agreement_count)
#arrange table by ascending license age
df_collected_licenceAge_ascend=df_collected.sort_values('Licence Age', ascending=True)
#print(df_collected_licenceAge_ascend)


#arrange table by ascending km driven
df_collected_km_ascend=df_collected.sort_values('kilometres driven', ascending=True)
#print(df_collected_km_ascend)


#arrange table by ascending likert points
