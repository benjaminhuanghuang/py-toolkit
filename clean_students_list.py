
import os
import openpyxl

FILE_NAME = '2018_all_students.xlsx'
NEW_FILE_NAME = 'students_new.xlsx'

ALL_STUDENTS_SHEET = '總名單'
NEW_ALL_STUDENTS_SHEET = 'all_students'

DISMISSED_STUDENTS_SHEETS = [
  '2015新生開除名單',
  '2016開除名單',
  '2018 開除名單'
]

STUDENT_NUM_COL_IN_DISMISSED_SHEETS = [
  1,
  1,
  4
]

def isDismissed(studentNum, wb):
  for sheet_name in DISMISSED_STUDENTS_SHEETS:
    sheet_dismissed = wb[sheet_name]
    row_count = sheet_dismissed.max_row
    for row in range(2, row_count + 1):
      if sheet_dismissed.cell(row=row, column=4).value == studentNum:
        print('Student {} is dismissed in {}'.format(studentNum, sheet_name))
        return True

  return False


if __name__ == "__main__":
  wb = openpyxl.load_workbook(FILE_NAME)
  sheet_all = wb[ALL_STUDENTS_SHEET]
  
  # Print statistics information
  row_count_all = sheet_all.max_row
  all_students_count = row_count_all - 1
  print ("There are {} students in {}".format(all_students_count, ALL_STUDENTS_SHEET)

  
  dismissed_students_count = 0
  for sheet_name in DISMISSED_STUDENTS_SHEETS:
    sheet_dismissed = wb[sheet_name]
    row_count_all = sheet_dismissed.max_row
    students_count = row_count_all - 1
    dismissed_students_count += students_count

    print ("There are {} students in {}".format(students_count, sheet_name)

  print ("There are {} students were dismissed".format(dismissed_students_count)
  
  sheet_result = wb.create_sheet(title = NEW_ALL_STUDENTS_SHEET)

  # copy the field names in the first row
  column_count_all = sheet_all.max_column
  for col in range(1, column_count_all + 1):
    sheet_result.cell(row=1, column=col,
                      value=sheet_all.cell(row=1, column=col).value)

  row_result = 2
  # filter the students infor
  for row in range(2, row_count_all + 1):
    if isDismissed(sheet_all.cell(row=row, column=4).value, wb):
      continue
    for col in range(1, column_count_all + 1):
      sheet_result.cell(row=row_result, column=col,
                        value=sheet_all.cell(row=row, column=col).value)
    row_result += 1

  wb.save('NEW_FILE_NAME')
