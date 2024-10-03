import pandas as pd

#cols of important values 
gender_col=7
age_col=8
license_age=11
km_driven=12

ques_start=13
ques_end=103
likert_start=104


likert_end=111
#for codespace
#df_collected=pd.read_excel('/workspaces/annotated_by_yolo/annotated_by_yolo_300epochs/1_collect_data_from_sosci/test.xlsx',usecols=[gender_col,age_col,license_age,km_driven]+list(range(ques_start,ques_end)), skiprows=1)

#df_GT=pd.read_excel('/workspaces/annotated_by_yolo/annotated_by_yolo_300epochs/1_collect_data_from_sosci/GTsurvey.xlsx')

df_collected=pd.read_excel(r'D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\annotated_by_yolo_300epochs\1_collect_data_from_sosci\test2.xlsx',usecols=[gender_col,age_col,license_age,km_driven]+list(range(ques_start,likert_end)), skiprows=1)

df_GT=pd.read_excel(r'D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\annotated_by_yolo_300epochs\1_collect_data_from_sosci\GTsurvey.xlsx')



# # Display current headers
#print("Current Headers:", df_collected)

# Rename specific headers
df_collected.rename(columns={
    'GenderSelection': 'Gender',  # Replace 'OldHeader1' with the actual name
    'AgeInput: Age': 'Age',
    'LicenseAge: [01]': 'Licence Age',  
    'kmDriven': 'kilometres driven',
    'LikertWFlow1: The workflow is too lengthy.':'W1 Lengthy',
    'LikertWFlow1: The workflow is difficult to understand.':'W1 Complicated',
    'LikertWFlow1: The questions are too lengthy.':'W1 Lengthy questions',
    'LikertWFlow1: The workflow is easy to work with.':'W1 User-friendly',
    'LikertWFlow2: The workflow is too lengthy.':'W2 Lengthy',
    'LikertWFlow2: The workflow is difficult to understand.':'W2 Complicated',
    'LikertWFlow2: The questions are too lengthy.':'W2 Lengthy questions',
    'LikertWFlow2: The workflow is easy to work with.':'W2 User-friendly',

}, inplace=True)

print("this is df collected", df_collected)

#---workflow 1
w1_col_to_drop = list(df_collected.columns[34:94]) + list(df_collected.columns[98:102])
w1_df_collected = df_collected.drop(w1_col_to_drop, axis=1)

w1_df_GT=df_GT.drop(df_GT.columns[30:],axis=1) #GT for w1 
print(f"this is w1_df_GT: {w1_df_GT}")
print(f"this is w1_df_collected: {w1_df_collected}")

#---workflow 2
w2_col_to_drop=list(df_collected.columns[4:34]) + list(df_collected.columns[94:97])
w2_df_collected=df_collected.drop(w2_col_to_drop, axis=1) #answers ffrom workflow 2 only
w2_df_GT=df_GT.drop(df_GT.columns[0:29],axis=1) #GT fr w2
print(f"this is w2_df_GT: {w2_df_GT}")
print(f"this is w2_df_collected top: {w2_df_collected}")

#no of rows in collected data
no_rows=len(df_collected)

print(f"this is no of rows in collected data: {no_rows}")

#the ground truth specific to this survey

print("this")

#---------------------------all agreements, disagreements or unanswered in a matrix, 1 array per row &likert score for w1
w1_agreement_matrix=[]
#w1_likert_score_array=[]

#after arranging table
likert_w1_start=34
likert_w1_end=38
likert_w2_start=98
likert_w2_end=101

for row in range(0,no_rows):

    w1_df_collected_ans=w1_df_collected.iloc[row][4:34] #only answers from that row
    print("this is w1_df_collected_ans", w1_df_collected_ans)
    print("this is w1_df_collected", w1_df_collected)

    
    w1_agreements=[]
    

    #summing w1 likert score
    #w1_likert_score=w1_df_collected.iloc[row][likert_w1_start:likert_w1_end].sum()
    #print(f"w1_likert_score {w1_likert_score}")

    #collecting agreements
    for ans in range(0, w1_df_collected_ans.shape[0]):
        
        print("ans",ans)
        print(f"ans is {w1_df_collected_ans.iloc[ans]}\n...this is ans from gtw1 {w1_df_GT.iloc[0,ans]}")

        
        #check if cell is empty
        if pd.isna(w1_df_collected_ans.iloc[ans]):

            w1_agreements.append('-1') #-1 is unanswered
            
        
        elif w1_df_collected_ans.iloc[ans]==float(w1_df_GT.iloc[0,ans]):
           
           w1_agreements.append('1') #1 for agreement, 0 for disagreement
        
        else:
            
            w1_agreements.append('0')        

    #agreements collected
    w1_agreement_matrix.append(w1_agreements)

    #w1 likert scores collected
   # w1_likert_score_array.append(w1_likert_score)
   # print(f"w1 likert score array {w1_likert_score_array}")

    #----------calculating metrics: agreement rate, disagreement rate, unanswered rate, completion rate

    #agreements matrix
    completion_rate_array=[]

    agreements_rate_array=[]

    disagreements_rate_array=[]
    
    unanswered_rate_array=[]

    for array in w1_agreement_matrix:

        #reset count for each loop
        count_1s=0
        count_0s=0
        counts_minus1s=0
        
        for element in array:
            if element=='1':
                count_1s+=1
            elif element=='0':
                count_0s+=1
            else:
                counts_minus1s+=1
        
        print(f"this is count_1s {count_1s}, this is count_0s {count_0s}, this is count_minus1s {counts_minus1s}")

        completion_rate=(count_1s+count_0s)/w1_df_collected_ans.shape[0]
        agreement_rate=count_1s/(w1_df_collected_ans.shape[0]-counts_minus1s) #over just answered questions
        disaagreement_rate=count_0s/(w1_df_collected_ans.shape[0]-counts_minus1s) #over just answered questions
        unanswered_rate=counts_minus1s/w1_df_collected_ans.shape[0] #over the total amount of questions

        completion_rate_array.append(round(completion_rate,3))
        agreements_rate_array.append(round(agreement_rate,3))
        disagreements_rate_array.append(round(disaagreement_rate,3))
        unanswered_rate_array.append(round(unanswered_rate,3))

print(w1_agreement_matrix)
print(agreements_rate_array,disagreements_rate_array,unanswered_rate_array,completion_rate_array)

#------------- Adding the new data columns to the DataFrame w1_df_collected

cols_to_drop_final=w1_df_collected.columns[4:34] 
w1_df_collected=w1_df_collected.drop(cols_to_drop_final,axis=1) #drop answers, not needed for final
w1_df_collected['Agreement rate'] = agreements_rate_array
w1_df_collected['Disagreement rate'] = disagreements_rate_array
w1_df_collected['Unanswered rate'] = unanswered_rate_array
w1_df_collected['Completion rate'] = completion_rate_array
#w1_df_collected['Workflow 1 Likert Score'] = w1_likert_score_array

print(w1_df_collected)

print(f"this is w2_collected {w2_df_collected}")
#---------------------------all agreements, disagreements or unanswered in a matrix, 1 array per row &likert score for -------------w2
w2_agreement_matrix=[]
#w2_likert_score_array=[]


for row in range(0,no_rows):

    w2_df_collected_ans=w2_df_collected.iloc[row][4:64] #only answers from that row
    
    w2_agreements=[]
    print("this is size of w2_collected_ans", w2_df_collected_ans.shape[0])

    #summing w1 likert score

    #w2_likert_score=df_collected.iloc[row][likert_w2_start:likert_w2_end].sum()
    #print(f"w1_likert_score {w2_likert_score}")

    #collecting agreements
    for ans in range(0, w2_df_collected_ans.shape[0]):
        
        print("ans",ans)
        print(f"ans is {w2_df_collected_ans.iloc[ans]}\n...this is ans from gtw2 {w2_df_GT.iloc[0,ans]}")

        
        #check if cell is empty
        if pd.isna(w2_df_collected_ans.iloc[ans]):

            w2_agreements.append('-1') #-1 is unanswered
            
        
        elif w2_df_collected_ans.iloc[ans]==float(w2_df_GT.iloc[0,ans]):
           
           w2_agreements.append('1') #1 for agreement, 0 for disagreement
        
        else:
            
            w2_agreements.append('0')        

    #agreements collected
    w2_agreement_matrix.append(w2_agreements)

    #w1 likert scores collected
   # w2_likert_score_array.append(w2_likert_score)
   # print(f"w1 likert score array {w2_likert_score_array}")

    #----------calculating metrics: agreement rate, disagreement rate, unanswered rate, completion rate w2----------

    #agreements matrix
    completion_rate_array=[]

    agreements_rate_array=[]

    disagreements_rate_array=[]
    
    unanswered_rate_array=[]

    for array in w2_agreement_matrix:

        #reset count for each loop
        count_1s=0
        count_0s=0
        counts_minus1s=0
        
        for element in array:
            if element=='1':
                count_1s+=1
            elif element=='0':
                count_0s+=1
            else:
                counts_minus1s+=1
        
        print(f"this is count_1s {count_1s}, this is count_0s {count_0s}, this is count_minus1s {counts_minus1s}")

        completion_rate=(count_1s+count_0s)/w2_df_collected_ans.shape[0]
        agreement_rate=count_1s/(w2_df_collected_ans.shape[0]-counts_minus1s) #over just answered questions
        disaagreement_rate=count_0s/(w2_df_collected_ans.shape[0]-counts_minus1s) #over just answered questions
        unanswered_rate=counts_minus1s/w2_df_collected_ans.shape[0] #over the total amount of questions

        completion_rate_array.append(round(completion_rate,3))
        agreements_rate_array.append(round(agreement_rate,3))
        disagreements_rate_array.append(round(disaagreement_rate,3))
        unanswered_rate_array.append(round(unanswered_rate,3))

print(w2_agreement_matrix)
print(agreements_rate_array,disagreements_rate_array,unanswered_rate_array,completion_rate_array)

#------------- Adding the new data columns to the DataFrame w2_df_collected
cols_to_drop_final=w2_df_collected.columns[4:65] 
w2_df_collected=w2_df_collected.drop(cols_to_drop_final,axis=1) #drop answers
w2_df_collected['Agreement rate'] = agreements_rate_array
w2_df_collected['Disagreement rate'] = disagreements_rate_array
w2_df_collected['Unanswered rate'] = unanswered_rate_array
w2_df_collected['Completion rate'] = completion_rate_array
#w2_df_collected['Workflow 2 Likert Score'] = w2_likert_score_array



print(w2_df_collected)

#export results to excel
w2_df_collected.to_excel(r'D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\annotated_by_yolo_300epochs\1_collect_data_from_sosci\w2_data.xlsx', sheet_name='w2data', index=False)
w1_df_collected.to_excel(r'D:\Coding_\Reflex_\MA_\yolo_\annotated_by_yolo\annotated_by_yolo_300epochs\1_collect_data_from_sosci\w1_data.xlsx', sheet_name='w2data', index=False)




























# #age_completion_rate=
# #print(w1_agreement_count)
# #arrange table by ascending license age
# df_collected_licenceAge_ascend=df_collected.sort_values('Licence Age', ascending=True)
# #print(df_collected_licenceAge_ascend)


# #arrange table by ascending km driven
# df_collected_km_ascend=df_collected.sort_values('kilometres driven', ascending=True)
# #print(df_collected_km_ascend)


# #arrange table by ascending likert points
