# Create a table of descriptive statistics

import pandas as pd


def calculate_statistics(input_file, output_file):
    '''
    Calculate the mean, standard deviation, and standard error for each column except 'Subject'.
    
    Parameters:
    - input_file (str): Path to the input Excel file.
    - output_file (str): Path to save the summary statistics file.
    '''
    
    # Load the Excel file
    df = pd.read_excel(input_file)
    
    # Drop the 'Subject' column
    df_without_subject = df.drop(columns=['Subject'])
    
    # Calculate mean, standard deviation, and standard error for each column
    stats = df_without_subject.agg(['count','mean', 'std', 'sem'])
    stats = round(stats, 2)
    
    # Save the statistics to a new Excel file
    stats.to_excel(output_file)
    
# Example usage:
input_file = 'DataLog_AnalysisTable.xlsx'  # Your original data file
output_file = 'DataLog_DescriptiveStat.xlsx'  # Output file for the statistics

calculate_statistics(input_file, output_file)



