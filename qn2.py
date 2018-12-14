#Question2:
    # Write a program that accepts sequence of lines as input 
    # and prints the lines after making all characters in the sentence capitalized.
sentence1 = [] #this is an empty list that will accept inputt from the keyboard
while True:
    lne = input()#this helps to input keybord characters by typing
    if lne:
        sentence1.append(lne.upper())# thisappends lne to the empty list(sentence1) and converts keyboard characters entered to upercase
    else:
        break;

for lne in sentence1:
    print(lne)
er