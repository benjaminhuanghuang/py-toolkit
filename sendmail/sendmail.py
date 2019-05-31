import os
import configparser # python 3
import openpyxl
# Import smtplib for the actual sending function
import smtplib

# will contain the HTML and plain-text
from email.mime.text import MIMEText
# instance combines these into a single message with two alternative rendering options:
from email.mime.multipart import MIMEMultipart

FILE_NAME = 'students_test.xlsx'
SHEET_NAME = 'students'
TEXT_TEMPLATE = 'text.txt'
HTML_TEMPLATE = 'html.txt'

# Should enable: Less secure app access
EMAIL_SERVER = 'smtp.gmail.com'

COL_NAME = 3
COL_EMAIL = 4
COL_SCORE = 5

def replaceTemplate(text, name, score):
  return text.replace("#name#", name).replace("#score#", str(score))


if __name__ == "__main__":
  # Read template
  htmlFile = open(HTML_TEMPLATE, "r")
  htmlContent = htmlFile.read()
  htmlFile.close()

  textFile = open(TEXT_TEMPLATE, "r")
  textContent = textFile.read()
  textFile.close()

  # Read students
  wb = openpyxl.load_workbook(FILE_NAME)
  sheet_students = wb[SHEET_NAME]

  row_count = sheet_students.max_row

  # Send the message via SMTP server.
  server = smtplib.SMTP_SSL(EMAIL_SERVER, 465)
  config = configparser.ConfigParser()
  config.read('config.ini')

  username = config['DEFAULT']['USER']
  password = config['DEFAULT']['PASSWORD']
  #print(username, password)
  server.login(username, password)
 
  for row in range(2, row_count + 1):
    # Get students info
    name = sheet_students.cell(row=row, column=COL_NAME).value
    email_address = sheet_students.cell(row=row, column=COL_EMAIL).value
    score = sheet_students.cell(row=row, column=COL_SCORE).value

    if(email_address):
      message = MIMEMultipart("alternative")
      message["Subject"] = "Hello!"
      message["From"] = "Panda <sender@gmail.com>"
      message["To"] = name

      # Replace emial body
      textPart = MIMEText(replaceTemplate(textContent, name, score), "plain")
      htmlPart = MIMEText(replaceTemplate(htmlContent, name, score), "html")

      message.attach(textPart)
      message.attach(htmlPart)

      server.sendmail("sender@gmail.com", email_address, message.as_string())
  server.quit()
