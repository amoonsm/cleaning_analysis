# Add fields based on what the subject saw in each trial. Drop records where target was absent

import pandas as pd


def add_field(input_file, output_file):

    '''
    Adds two new columns: TrialType and Condition. TrialType is based on TrialCond, and 
    Condition is based on LeftPos, RightPos, and TrialCond.

    Parameters:
    - input_file (str): Path to the input Excel file.
    - output_file (str): Path to save the updated Excel file.
    '''

    # Load the excel file
    df = pd.read_excel(input_file)

    # Define a function to determine TrialType based on TrialCond
    def determine_trial_type(trial_cond):
        if trial_cond in ['TargetL', 'TargetR']:
            return 'Target'
        elif trial_cond in ['FoilL', 'FoilR']:
            return 'Foil'
        
    # Define a function to determine Condition based on LeftPos, RightPos, and TrialCond
    def determine_condition(row):
        pattern_side = 'Left' if row['LeftPos'] == 'set 1' else 'Right'
        if (pattern_side == 'Left' and row['TrialCond'] in ['TargetL', 'FoilL']) or \
           (pattern_side == 'Right' and row['TrialCond'] in ['TargetR', 'FoilR']):
            return 'Pattern'
        return 'Random'

    # Apply the functions to create the new columns
    df['TrialType'] = df['TrialCond'].apply(determine_trial_type)
    df['Condition'] = df.apply(determine_condition, axis=1)

    # Drop rows where TrialCond is 'TargetA'
    df = df[df['TrialCond'] != 'TargetA']

    # Save the updated DataFrame to a new file
    df.to_excel(output_file, index=False) 


input_file = 'DataLog_Filter.xlsx'  # Filtered file
output_file = 'DataLog_Condition.xlsx'  # Relabeled file
    
add_field(input_file, output_file)



