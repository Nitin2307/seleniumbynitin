import time
import xlrd
from Page_object.frontend_reg_excel import Frontend_excel
frontend = Frontend_excel()
workbook = xlrd.open_workbook("frontend_excel.xlsx")
sheet = workbook.sheet_by_name("registration")
rowCount = sheet.nrows
colCount = sheet.ncols
print(rowCount)
print(colCount)

for curr_row in range(1, rowCount):
    name = sheet.cell_value(curr_row, 0)
    emailid = sheet.cell_value(curr_row, 1)
    mobileno = sheet.cell_value(curr_row, 2)
    university = sheet.cell_value(curr_row, 3)
    course = sheet.cell_value(curr_row, 4)
    specialization = sheet.cell_value(curr_row, 5)
    state = sheet.cell_value(curr_row, 6)
    city = sheet.cell_value(curr_row, 7)
    frontend.Name(name)
    frontend.Email(emailid)
    frontend.Mobile(mobileno)
    frontend.University(university)
    frontend.Course(course)
    frontend.Specialization(specialization)
    frontend.State(state)
    frontend.City(city)
    frontend.agree()
    frontend.regbtn()
    frontend.refresh()