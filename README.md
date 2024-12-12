# About the database

The database (DataLog_Original.xlsx) is from the first pilot study (n = 38) that I conducted in graduate school. A final version of the study was published in [Cognitive Research](https://link.springer.com/article/10.1186/s41235-022-00356-y). Below is a poster presentation I gave at the Vision Sciences Society, 2020.

![ObstatPoster_V3](https://github.com/user-attachments/assets/9bae25a5-be6f-406b-b5cc-8a26af1dd500)

# About the script

All scripts were written in Python 3.13.

1_FilterField.py
-
Creates a new table with relevant fields (DataLog_Filter.xlsx)

2_NewField.py
-
Creates new fields with labels of experimental manipulation (DataLog_Condition.xlsx)

![image](https://github.com/user-attachments/assets/3e484b9c-fe87-4ee5-8367-d6c310bf3bd7)

3_CollapseRecord.py
-
Compute average by participant (DataLog_Avg.xlsx)

![image](https://github.com/user-attachments/assets/0547bd9f-900a-461e-8608-fa2d578cea14)

4_PrepareAnalysis.py
-
Reorganize table to have fields as measures by experimental manipulation (DataLog_AnalysisTable.xlsx)

![image](https://github.com/user-attachments/assets/edb41554-da49-4f78-b67d-3e9289d14d4b)

5_DoAnalysis.py
-
Conduct ANOVA

![image](https://github.com/user-attachments/assets/9dec3447-7c1a-431f-854e-4c3140444a42)

6_Plot.py
-
Plot the results

![image](https://github.com/user-attachments/assets/0a177173-e518-4fec-995c-f576bf4edbba)
![image](https://github.com/user-attachments/assets/b62d850b-bee7-4c01-9b5d-82e83df36c65)


7_DescriptiveStats.py
-
Create a table of descriptive statistics (DataLog_DescriptiveStat.xlsx)

![image](https://github.com/user-attachments/assets/72ceaddb-48b6-45b3-a209-d91d813cfbb1)
