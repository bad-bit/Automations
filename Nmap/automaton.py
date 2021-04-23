#!/usr/bin/python3
# Script to automate nmap scanning and converting scan results to HTML
# ToDo - Add screenshot utility to take screenshot of webpages
#

import os
import shutil
import argparse
from threading import Thread
from os import path, walk



def main():
	print("""


███████╗██╗   ██ ████████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗ ██████╗ ███╗   ██╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝██╔═══██╗████╗  ██║
███████║██║   ██║   ██║   ██║   ██║██╔████╔██║███████║   ██║   ██║   ██║██╔██╗ ██║
██╔══██║██║   ██║   ██║   ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██║   ██║██║╚██╗██║
██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║██║  ██║   ██║   ╚██████╔╝██║ ╚████║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝
                                                                                  
																				                         - @stackslash


		\n""")
	# print("[+] Automate nmap scanning, nmap html output geenration, taking screenshots, tesssl output generation")
	print("Automation tool for VAPT. Automates the following:\n1. NMAP scan\n2. XML to HTML report conversion of scanned IPs\n3. Screenshot of default web pages\n4. SSL scal from testssl")
	print("______________________________\n\n")

	# OS check
	# if Win - xsltproc check in path 
	# Input - File containing line seperated IPs

	parser = argparse.ArgumentParser(
		description = "Automation tool for VAPT. Automates the following:\n1. NMAP scan\n2. XML to HTML report conversion of scanned IPs\n3. Screenshot of default web pages\n4. SSL scal from testssl",
		usage = "automaton.py -l ipList.txt")

	parser.add_argument("-l", "--ipList", help="List of IPs to be scanned", required=True, dest="ipList")
	args = parser.parse_args()

	ipList = args.ipList

	with open(ipList, "r") as ipList:
		ips = ipList.readlines()

	nmapScanner(ips)

def nmapScanner(ips):
	xmlOutputs = []
	htmlOutputs = []
	currentDir = os.getcwd()

	for i in ips:
		os.system("nmap -sS -sV -O %s -oA %s"%(i, i))

	fileList = os.listdir()

	#segregating xml output
	for i in fileList:
		if i.endswith(".xml"):
			xmlOutputs.append(i)
	#converting to html
	for j in xmlOutputs:
		os.system("xsltproc %s -o %s"%(j, j))
	#segregating html output
	fileList = os.listdir()
	for k in fileList:
		if k.endswith(".html"):
			htmlOutputs.append(k)

	#copy all html files to a new directory
	
	sourceFiles = []
	currentDir = os.getcwd()

	for root, directories, files in os.walk(currentDir):
		for filename in files:
			# Join the two strings in order to form the full filepath.
			filepath = os.path.join(root, filename)
			sourceFiles.append(filepath)  # Add it to the list.

	if (path.exists("HTML_Outputs")):
		# Copy only html outputs
		destDir = currentDir+"/HTML_Outputs"
		for i in sourceFiles:
			if i.e.endswith(".html"):
				shutil.copy(i, destDir)
	else:
		os.mkdir("HTML_Outputs")
		destDir = currentDir+"/HTML_Outputs"
		for i in sourceFiles:
			if i.e.endswith(".html"):
				shutil.copy(i, destDir)
				
if __name__ == '__main__':
	main()
