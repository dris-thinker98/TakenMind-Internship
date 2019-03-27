
#Importing various modules and dependencies
import pandas as pd
import numpy as np
import xlrd

#For extracting .csv for Sheet1
csv1 = pd.read_excel('InputFile.xlsx', 'Sheet1', index_col=None)
csv1.to_csv('csvfile1.csv', encoding='utf-8'index=False)

#For extracting .csv for Sheet2
csv2 = pd.read_excel('InputFile.xlsx', 'Sheet2', index_col=None)
csv2.to_csv('csvfile2.csv', encoding='utf-8'index=False)

#For extracting .csv for Sheet3
csv3 = pd.read_excel('InputFile.xlsx', 'Sheet3', index_col=None)
csv3.to_csv('csvfile3.csv', encoding='utf-8'index=False)

#For extracting .csv for Sheet4
csv4 = pd.read_excel('InputFile.xlsx', 'Sheet4', index_col=None)
csv4.to_csv('csvfile4.csv', encoding='utf-8'index=False)

#For extracting .csv for Sheet5
csv5 = pd.read_excel('InputFile.xlsx', 'Sheet5', index_col=None)
csv5.to_csv('csvfile5.csv', encoding='utf-8'index=False)

#For extracting .csv for Sheet6
csv6 = pd.read_excel('InputFile.xlsx', 'Sheet6', index_col=None)
csv6.to_csv('csvfile6.csv', encoding='utf-8'index=False)

#For extracting .csv for Sheet7
csv7= pd.read_excel('InputFile.xlsx', 'Sheet7, index_col=None)
csv7.to_csv('csvfile7.csv', encoding='utf-8'index=False)

#For extracting .csv for Sheet8
csv8 = pd.read_excel('InputFile.xlsx', 'Sheet8', index_col=None)
csv8.to_csv('csvfile8.csv', encoding='utf-8'index=False)

#For extracting .csv for Sheet9
csv9 = pd.read_excel('InputFile.xlsx', 'Sheet9', index_col=None)
csv9.to_csv('csvfile9.csv', encoding='utf-8'index=False)

#For extracting .csv for Sheet10
csv10 = pd.read_excel('InputFile.xlsx', 'Sheet10', index_col=None)
csv10.to_csv('csvfile10.csv', encoding='utf-8'index=False)




