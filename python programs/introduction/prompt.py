from sys import argv

script,user_name = argv,input("Enter your name: ")

prompt = " > "

print(f"Hi {user_name} !, I'm {script} script")
print("I would like to ask you some questions ")
print(f"Do you like me {user_name} ?")
like = input(prompt)