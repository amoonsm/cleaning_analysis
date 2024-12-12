# Conduct analysis: Factor 1 (condition), Factor 2 (trial type)
#                   DV 1 (accuracy), DV 2 (reaction time)

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy import stats

df = pd.read_excel('DataLog_Avg.xlsx')

# We'll perform ANOVA separately for Accuracy and Reaction Time
for dv in ['mean_accuracy', 'median_rt']:
    print(f"\n2x2 ANOVA for {dv}:")
    
    # Create a model formula
    formula = f'{dv} ~ TrialType * Condition'
    
    # Fit the model
    model = ols(formula, data=df).fit()
    
    # Perform ANOVA
    anova_table = sm.stats.anova_lm(model, typ=2)
    print(anova_table)
    
