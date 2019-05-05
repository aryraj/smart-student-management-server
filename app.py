import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')

worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Sl. No.')
worksheet.write('B1', 'USN')
worksheet.write('C1', 'Sub1')
worksheet.write('D1', 'Sub2')

workbook.close()