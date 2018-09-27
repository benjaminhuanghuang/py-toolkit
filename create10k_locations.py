import os
import openpyxl

FILE_NAME = '10k_locations.xlsx'
SHEET_NAME = 'locations'

COUNT = 10000

if __name__ == "__main__":
  wb = openpyxl.Workbook()

  # sheet = wb.create_sheet(SHEET_NAME)
  sheet = wb.active

  # Create header
  sheet.cell(row=1, column=1, value='StreetAddress')
  sheet.cell(row=1, column=2, value='City')
  sheet.cell(row=1, column=3, value='County')
  sheet.cell(row=1, column=4, value='State')
  sheet.cell(row=1, column=5, value='Country')
  sheet.cell(row=1, column=6, value='PostalCode')
  sheet.cell(row=1, column=7, value='Latidute')
  sheet.cell(row=1, column=8, value='Logitude')
  sheet.cell(row=1, column=9, value='TIV')
  sheet.cell(row=1, column=10, value='TIVCurrency')
  sheet.cell(row=1, column=11, value='Occupancy')
  sheet.cell(row=1, column=12, value='Constuction')
  sheet.cell(row=1, column=13, value='NumOfStories')
  sheet.cell(row=1, column=14, value='YearBuilt')
  sheet.cell(row=1, column=15, value='Contract Excess')
  sheet.cell(row=1, column=16, value='Contract Excess Currency')
  sheet.cell(row=1, column=17, value='Contract Limit')
  sheet.cell(row=1, column=18, value='Contract Coverage')
  sheet.cell(row=1, column=19, value='Perils')

  # Create locations
  for row in range(2, COUNT + 2):
    sheet.cell(row=row, column=1, value='7575 gateway blvd')
    sheet.cell(row=row, column=2, value='Newark')
    sheet.cell(row=row, column=3, value='Alameda')
    sheet.cell(row=row, column=4, value='CA')
    sheet.cell(row=row, column=5, value='USA')
    sheet.cell(row=row, column=6, value='94560')
    sheet.cell(row=row, column=7, value='')
    sheet.cell(row=row, column=8, value='')
    sheet.cell(row=row, column=9, value='')
    sheet.cell(row=row, column=10, value='USD')
    sheet.cell(row=row, column=11, value='AFM31')
    sheet.cell(row=row, column=12, value='ATC72A')
    sheet.cell(row=row, column=13, value='2')
    sheet.cell(row=row, column=14, value='1994')
    sheet.cell(row=row, column=15, value='12345')
    sheet.cell(row=row, column=16, value='USD')
    sheet.cell(row=row, column=17, value='2000')
    sheet.cell(row=row, column=18, value='20000')
    sheet.cell(row=row, column=19, value='EQ')

  wb.save(FILE_NAME)
