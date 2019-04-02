#!/usr/bin/env python2

from argparse import ArgumentParser
import sys
import os
import psycopg2   # pip install psycopg2-binary

Table_Excluded = ['session', 'session_location', 'flyway_schema_history']
Column_Excluded = ['created_by', 'created_at', 'modified_by', 'modified_at']


def main():
	# 
  conn_local = psycopg2.connect(host="localhost", dbname="quantumdb", user="quantumdb", password="qu%ntu3DB")
  conn_dev = psycopg2.connect(host="localhost",  port="5433", dbname="quantumdb", user="quantum_api_temp", password="akjankjdaHHAS")

  cursor_local = conn_local.cursor()
  cursor_dev = conn_dev.cursor()
  # Compare tables
  cursor_local.execute("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'quantumdb'""")
  cursor_dev.execute("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'quantumdb'""")
  tables_local = cursor_local.fetchall()
  tables_dev = cursor_dev.fetchall()

  print("There are {0} tables in local".format(len(tables_local)))
  print("There are {0} tables in dev".format(len(tables_dev)))

  for table in tables_local:
    table_name = table[0]
    if table_name in Table_Excluded:
      continue
    compareTableData(cursor_local, cursor_dev, table_name)
    
  conn_local.close()
  conn_dev.close()

def compareTableData(cursor_local, cursor_dev, table_name):
  print("#### Comparing Table {}".format(table_name))
  
  cursor_local.execute("SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = '" + table_name+"'")
  columns_local = cursor_local.fetchall()
  cursor_dev.execute("SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = '" + table_name+"'")
  columns_dev = cursor_dev.fetchall()
  if(len(columns_local) != len(columns_dev)): 
    print(">>>> Table {} have differnt columns".format(table_name))
    print(">>>>>>>> Table {} in cocal has {} columns.".format(table_name, len(columns_local)))
    print(">>>>>>>> Table {} in dev has {} columns".format(table_name, len(columns_dev)))
    return

  cursor_local.execute("SELECT * FROM " + table_name)
  rows_local = cursor_local.fetchall()
  
  cursor_dev.execute("SELECT * FROM " + table_name)
  rows_dev = cursor_dev.fetchall()
  # print(">>>>>>>> Table {} in cocal has {} rows.".format(table_name, len(rows_local)))
  # print(">>>>>>>> Table {} in dev has {} rows".format(table_name, len(rows_dev)))
   
  if(len(rows_local) != len(rows_dev)): 
    print(">>>> Table {} have differnt data count".format(table_name))
    print(">>>>>>>> Table {} in cocal has {} rows.".format(table_name, len(rows_local)))
    print(">>>>>>>> Table {} in dev has {} rows".format(table_name, len(rows_dev)))
    return

  for i in range(len(rows_local)):
    for j in range(len(columns_local)):
      column_name = columns_local[j][0]
      if(column_name in Column_Excluded):
        continue
      if(rows_local[i][j] != rows_dev[i][j]):
        print(">>>>>>>> Table {} row{} column {} in cocal is {} .".format(table_name, i,  column_name, rows_local[i][j]))
        print(">>>>>>>> Table {} row{} column {} in dev is {} .".format(table_name,  i,  column_name, rows_dev[i][j]))
      
if __name__ == "__main__":
	main()
