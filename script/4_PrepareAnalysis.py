# Prepare table with dependent variables as fields


import pandas as pd

def reorganize_table(input_file, output_file):
    '''
    Reorganize the collapsed data table to create separate columns for accuracy and RT 
    based on condition and trial type, rounding values and converting accuracy to percentages.

    Parameters:
        - input_file (str): Path to the input Excel file with collapsed data.
        - output_file (str): Path to save the reorganized Excel file.
    '''
    # Load the collapsed data
    df = pd.read_excel(input_file)

    # Create unique labels for each combination of condition and trial type
    df['Metric'] = df['TrialType'] + '_' + df['Condition']  # e.g., 'Target_Pattern', 'Foil_Random'

    # Pivot the table to create separate columns for each metric
    pivot_table = df.pivot(index='Subject', columns='Metric', values=['mean_accuracy', 'median_rt'])

    # Flatten the MultiIndex columns
    pivot_table.columns = ['_'.join(col).strip() for col in pivot_table.columns.values]

    # Reset index to make 'Subject' a column
    pivot_table.reset_index(inplace=True)

    # Round values to two decimal points
    for col in pivot_table.columns:
        if 'mean_accuracy' in col or 'median_rt' in col:
            pivot_table[col] = pivot_table[col].round(2)

    # Save the reorganized table to a new Excel file
    pivot_table.to_excel(output_file, index=False)

# Input and output files
input_file = 'DataLog_Avg.xlsx'  # Collapsed data file
output_file = 'DataLog_AnalysisTable.xlsx'  # Prep for analysis

reorganize_table(input_file, output_file)


