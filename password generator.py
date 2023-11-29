import random 
char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-+=!@#$%^&*"
num = int(input("How many passwords do you want to generate? "))
print("Generating " +str(num)+" passwords")
length_of_pass = int(input("Enter the length of the password: "))
def pass_generator(num):
    password = ''
    for i in range(num):
        password += random.choice(char)
    return password
print(pass_generator(length_of_pass))