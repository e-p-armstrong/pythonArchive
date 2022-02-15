from sys import argv
script, filename = argv

print(f"File {filename} being prepared for IMMINENT DESTRUCTION. Do you wish to proceed?")
prcd = input("\t> ")

if prcd == "Yes" or prcd == "yes":
    print("PURGE PROTOCOLS: \nA\nC\nT\nI\nV\nA\nT\nE")
    target = open(filename,'w')
    print("Now, write three lines that shall make up the new file.")
    ln1 = input("\t1> ")
    ln2 = input("\t2> ")
    ln3 = input("\t3> ")
    print("Writing process INITIATED")
    target.write(ln1+"\n"+ln2+"\n"+ln3)
    print("PROCEDURE: \nC\nO\nM\nP\nL\nE\nT\nE")
else:
    print("You're a very boring meatbag")
