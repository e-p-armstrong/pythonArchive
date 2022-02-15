print("What is your name?")
na = input("\t>")
print("What is your quest?")
q = input("\t>")

print("What is the capital of Assyria?")
ca= input("\t>")

if ca == "Assur":
    print(f"Arg! Damn you, {na}! You're right! Fine, continue on your bloody quest {q}\n You win!")

elif ca == "assur":
    print(f"Arg! You're right! But, you didn't capitalize your answer, so off you go! \n You are dead. So close!")
else:
    print("*You get shot off into the air, screaming - such is the price for ignorance.* \n You are very, very dead.")

print(f"Your name is/was {na}, your quest was {q}, and your answer was {ca}")

print(f"{na+q+ca}")
 
n1 = int(input(f"What is the first number you wish to do arithmetic with? \n\t>"))
n2 = int(input(f"What is the second number you wish to do arithmetic with? \n\t>"))
op = input(f"And what operation do you wish to use?\n\t")

if op == "+":
    print (f"Your answer is... {n1+n2}")
elif op == "-":
    print (f"Your answer is... {n1-n2}")
elif op == "*":
    print (f"Your answer is... {n1*n2}")
elif op == "/":
    print (f"Your answer is... {n1/n2}")
else:
    print("You didn't input a valid operation you fool! Or you left a space/other character somewhere.")