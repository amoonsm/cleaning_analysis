# About the database

The database (DataLog_Original.xlsx) is from the first pilot study that I conducted in graduate school. A final version of the study was published in Cognitive Research (https://link.springer.com/article/10.1186/s41235-022-00356-y)

# About the script

All scripts were written in Python 3.13.

Order of script:

1_FilterField.py - Creates a new table with relevant fields (DataLog_Filter.xlsx)<br />
2_NewField.py - Creates new fields with labels of experimental manipulation (DataLog_Condition.xlsx)
3_CollapseRecord.py - Compute average by participant (DataLog_Avg.xlsx)
4_PrepareAnalysis.py - Reorganize table to have fields as measures by experimental manipulation (DataLog_AnalysisTable.xlsx)
5_DoAnalysis.py - Conduct ANOVA (statistics in output)
6_Plot.py - Plot the results (figures in output)
7_DescriptiveStats.py - Create a table of descriptive statistics (DataLog_DescriptiveStat.xlsx)
