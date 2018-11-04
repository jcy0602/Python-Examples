# -*- coding:utf-8 -*-
import sys
import xlwt
import MySQLdb

conn = MySQLdb.connect("localhost","root","123456","spider",charset="utf8")
cursor = conn.cursor()

count = cursor.execute("select * from quotes")
print(count)

#重置游标的位置
cursor.scroll(0,mode="absolute")
#搜取所有结果
results = cursor.fetchall()

#获取MySQL里面数据字段名称
fields = cursor.description
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('table_message',cell_overwrite_ok=True)

#写上字段信息
for field in range(0,len(fields)):
    sheet.write(0,field,fields[field][0])

#获取并写入数据段信息
row = 1
col = 0
for row in range(1,len(results)+1):
    for col in range(0,len(fields)):
        sheet.write(row,col,u"%s"%results[row-1][col])

workbook.save(r'./quotes.xlsx')

