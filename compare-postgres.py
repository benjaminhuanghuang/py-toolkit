#!/usr/bin/env python2

from argparse import ArgumentParser
import sys
import os
import psycopg2   # pip install psycopg2-binary


def main():

	# Walking specified resources and initializing target with statements.

	conn_local = psycopg2.connect(
		host="localhost", dbname="quantumdb", user="quantumdb", password="qu%ntu3DB")
	conn_dev = psycopg2.connect(host="localhost",  port="5433", dbname="quantumdb",
	                            user="quantum_api_temp", password="akjankjdaHHAS")

	cursor_local = conn_local.cursor()
	conn_dev = conn_local.cursor()
	# Compare tables
	cursor_local.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'quantumdb'""")
	conn_dev.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'quantumdb'""")
	tables_local = cursor_local.fetchall()
	tables_dev = conn_dev.fetchall()
	
	print("There are {0} tables in local".format(len(tables_local)))
	print("There are {0} tables in dev".format(len(tables_dev)))
	
	for table in tables_local:
			print(table[0])


	conn_local.close()
	conn_dev.close()


def compareTableSchema():
	pass

def compareTableData():
  	pass


if __name__ == "__main__":
	main()
