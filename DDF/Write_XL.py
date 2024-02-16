import openpyxl


path="C:\\Users\\MyPc\\Desktop\\DDF.xlsx"
workbook=openpyxl.load_workbook(path)
sheet=workbook['Sheet2']

for r in range(1,11):
    for c in range(1,4):
        sheet.cell(row=r,column=c).value='python'

workbook.save(path)