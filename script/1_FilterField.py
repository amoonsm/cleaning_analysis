# Read Excel and filter out irrelevant fields

import pandas as pd

def save_specific_columns(input_file, output_file, columns_to_keep):

    '''
    Reads an Excel file and saves a new file with only the specified fields.


    Parameters:
        - input_file (str): Path to the original Excel file.
        - output_file (str): Path to save the new Excel file.
        - columns_to_keep (list): List of column names to keep.
    '''

    #Load the excel file
    df = pd.read_excel(input_file)

    # Select desired fields
    filtered_df = df[columns_to_keep] 
    filtered_df.to_excel(output_file, index=False)
    
input_file = 'DataLog_Original.xlsx' # Original file
output_file = 'DataLog_Filter.xlsx' # New file with relevant fields
columns_to_keep = ['Subject', 'LeftPos', 'RightPos', 'TrialList.Sample',
                   'CategorySlide.ACC', 'CategorySlide.RT', 'TrialCond'] # Relevant fields

save_specific_columns(input_file, output_file, columns_to_keep)

