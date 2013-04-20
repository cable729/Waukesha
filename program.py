import faces
import os

help = """
help - prints out help message
exit - exits the program
"""

print "Enter a command"
while(True):
    input = raw_input();
    if(input == "help"):
        print help
    elif(input == "exit"):
        print "Program will now exit"
        exit()
    else:
        print "Uncrecognized command"