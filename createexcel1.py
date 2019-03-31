import xlwt
def write_excel():
    filename="CreateFruit.xls"
    workbook=xlwt.Workbook()
    sheet=workbook.add_sheet("2016")
    fruits={"FRUITS":"COLOR","mango":"yellow","apple":"red","gauva":"green","berry":"black","cheery":"red","ppaya":"shedy green","orange":"orange"}
    
    row=0
    colw=0
    i=0
    
    ctype = 'string'
    col=1
    for row,each in enumerate(fruits.keys()):
        sh=sheet.write(row,colw,i+row)
        sh=sheet.write(row,col,each)
        
    col1=2
    for row,ea in enumerate(fruits.values()):
        sh1=sheet.write(row,col1,ea)
    workbook.save(filename)
    
write_excel()
