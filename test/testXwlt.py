import xlwt
from xlwt.Worksheet import Worksheet

workbook=xlwt.Workbook(encoding='utf-8')     #创建workbook对象
worksheet=workbook.add_sheet('sheet1')
for i in range(1,10):
    for j in range(i,10):
        worksheet.write(i-1,j-1,str(i)+'*'+str(j)+'='+str(i*j))

# worksheet.write(0,0,'hello')    #写入数据，第一行参数‘行’，第二个参数‘列’，第三个参数内容
workbook.save('student.xls')