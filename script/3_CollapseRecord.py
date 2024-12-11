# Collapse record by subject, condition, and trial type

import pandas as pd

def collapse_record(input_file, output_file):

    '''
    Calculate the mean accuracy and median reaction time by subject and condition.

    Parameters:
        - input_file (str): Path to the original Excel file.
        - output_file (str): Path to save the new Excel file.
        - columns_to_keep (list): List of column names to keep.
    '''

    # Load the excel file
    df = pd.read_excel(input_file) 


    # Calculate mean accuracy and median RT grouped by Subject and TrialCond
    summary = (df.groupby(['Subject', 'Condition', 'TrialType'])
                 .agg(mean_accuracy=('CategorySlide.ACC', 'mean'),
                      median_rt=('CategorySlide.RT', lambda x: x[df.loc[x.index, 'CategorySlide.ACC'] == 1].median())
                      )
                 .reset_index()
               )

    summary['mean_accuracy'] = round(summary['mean_accuracy'] * 100, 2)
    
    # Save the summary table to a new Excel file
    summary.to_excel(output_file, index=False) 

input_file = 'DataLog_Condition.xlsx' # Original file
output_file = 'DataLog_Avg.xlsx' # New file with relevant fields

collapse_record(input_file, output_file)


