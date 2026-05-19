import openpyxl 
# new workbook
wb = openpyxl.Workbook()
ws1 = wb.active
ws1.title = 'report'
ws2 = wb.create_sheet('personal_data')


# fill in the data
ws1.append(['product','price','stock','brand'])
ws1.append(['clock','150000000','500','rolex'])
ws1.append(['handphone','18000000','100','apple'])

ws2.append(['name','weight','height','hobby'])
ws2.append(['lisa','50kg','178cm','sleep'])
ws2.append(['rin','45kg','160cm','read'])
wb.save('multi_sheet.xlsx')