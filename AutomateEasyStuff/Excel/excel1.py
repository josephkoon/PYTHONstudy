import openpyxl

#creates workbook file
wb = openpyxl.load_workbook('example.xlsx')

#get the sheet names
print(wb.get_sheet_names())

#make Sheet 3 the current worksheet object
sheet = wb.get_sheet_by_name('Sheet3')

#get worksheet title
sheet.title

#makes sheet2 the actively selected worksheet
sheet2 = wb.get_active_sheet()

#gets worksheet title
sheet2.title


