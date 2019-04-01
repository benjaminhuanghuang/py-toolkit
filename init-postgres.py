#!/usr/bin/env python2

from argparse import ArgumentParser
import sys
import os
import json
import psycopg2

def main():
	# Initialize and gather input parameters. We're looking for the file
	# path for the initialization json.

	print("Initializing postgres")

	parser = ArgumentParser()

	parser.add_argument("-n", "--name", dest="name", help="specify name of config entry within json")
	parser.add_argument("-f", "--file", dest="filePath", help="specify input json file")

	args = parser.parse_args()

	print("Checking if '{0}' exists".format(args.filePath))

	if not os.path.isfile(args.filePath):
		print("Initialization settings not specified. Exiting")
		sys.exit(0)

	# The specified file exists, so we need to load the data and process
	# what might be included in the spec. If nothing specified, then skip.

	print("Reading settings")

	spec = None

	with open(args.filePath, "r") as init:
		try:
			spec = json.load(init)
		except Exception as eX:
			print("Failed to load initialization spec")
			print(str(eX))
			sys.exit(1)

	if args.name not in spec:
		print("Settings specified, but not for '{0}'. Exiting".format(args.name))
		sys.exit(0)

	# Walking specified resources and initializing target with statements.

	conn = psycopg2.connect(host="localhost", dbname="quantumdb", user="quantumdb", password="whatever")

	print("Loading statements set from '{0}'".format(args.name))
	
	for statement in spec[args.name]["statements"]:
		try:
			print("Executing statement ({0})".format(statement["execute"]))
			crsr = conn.cursor()
			crsr.execute(statement["execute"])
			crsr.close()
		except Exception as eX:
			print("Failed to execute {0}".format(statement))
			print(str(eX))

	try:
		print("Committing statements")
		conn.commit()
	except Exception as eX:
		print("Failed to commit")
		print(str(eX))
	
	conn.close()
	
if __name__ == "__main__":
	main()
