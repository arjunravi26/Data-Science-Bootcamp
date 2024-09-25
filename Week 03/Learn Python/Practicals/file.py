# Write a function that accepts a filename and tries to open the file.
# If the file does not exist, catch the exception and return a user-friendly error message.
try:
    with open('file.txt','a+') as file:
        file.write("\nHello This is my file")
    content =  open('file.txt','r').read()
    print(f"{content} is present")
except FileNotFoundError as e:
    print(e)

