from sys import argv
scr, filename = argv

txt = open(filename)

print(f"{filename}'s contents are...")
print(txt.read())

y = input("Type the file name again, or a different file name\n\t> ")
z = open(y)

print(f"{y}'s contents are...\n", z.read())

z.close()
txt.close()



