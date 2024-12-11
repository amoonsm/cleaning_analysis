# Plot the data

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_acc_rt(input_file):
    '''
    Plots bar graphs for accuracy and reaction time by condition and trial type.
    
    Parameters:
    - input_file (str): Path to the Excel file with the necessary data.
    '''

    # Load the data
    df = pd.read_excel(input_file)

    # Define the new order of TrialType: flip Target and Foil
    trial_type_order = ['Target', 'Foil']

    # Define custom color palette for conditions (Pattern: grey, Random: white)
    custom_palette = {'Pattern': 'grey', 'Random': 'white'}
    
    # Plot accuracy
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='TrialType', y='mean_accuracy', hue='Condition',
                order=trial_type_order, errorbar='se', palette=custom_palette, edgecolor='black', capsize=.03)
    plt.title('Overall accuracy')
    plt.xlabel('Condition')
    plt.ylabel('Accuracy (%)')
    plt.ylim(90, 100)
    plt.legend(title='Condition', loc='lower right', bbox_to_anchor=(1.2, 0))
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.tight_layout()
    plt.show()
    
    # Plot reaction time
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='TrialType', y='median_rt', hue='Condition',
                order=trial_type_order, errorbar='se', palette=custom_palette, edgecolor='black', capsize=.03)
    plt.title('Overall Reaction Time')
    plt.xlabel('Condition')
    plt.ylabel('Reaction Time (ms)')
    plt.ylim(400, 700)
    plt.legend(title='Condition', loc='lower right', bbox_to_anchor=(1.2, 0))
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.tight_layout()
    plt.show()



input_file = 'DataLog_Avg.xlsx' # File with collapsed records by subject, condition, and trial type
plot_acc_rt(input_file)




