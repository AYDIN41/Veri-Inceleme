import pandas as pd

df = pd.read_excel("my_excel_file.xlsx",sheet_name="First_Sheet")
print(df)
wb = pd.ExcelFile("my_excel_file.xlsx")
"""df2 = pd.read_excel("my_excel_file.xlsx",sheet_name="Second_Sheet")
print(df2)"""
print(wb.sheet_names)
excelSheetDict = pd.read_excel("my_excel_file.xlsx",sheet_name=None) #If we say sheet_name is equal to None variable would read this excel as a dictionary type
print(excelSheetDict)
print(type(excelSheetDict))
print(excelSheetDict.keys())
print(excelSheetDict["First_Sheet"])