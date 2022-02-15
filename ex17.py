from sys import argv
from os.path import exists
script, inFile, outFile = argv

print(f"File {inFile} being prepared for REPLICATION to {outFile}. Do you wish to proceed? This will ANNIHILATE the output file (if it exists)!")
prcd = input("\t> ")

if prcd == "Yes" or prcd == "yes":
    inData = open(inFile).read()
    print(f"The length of the input file is {len(inData)} bytes long")
    print(f"The statement \"The output file exists already\" is... {exists(outFile)}!")
    open(outFile,'w').write(inData)
    print("PROCEDURE: \nC\nO\nM\nP\nL\nE\nT\nE")
else:
    print("Then stop wasting my time, meatbag!")
