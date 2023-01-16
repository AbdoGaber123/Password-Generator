"""
created on Tue Jan 17 8:32:20 2023
@auther:Abdallah_Gaber 
"""
"""
Now we are going to create a random pasword generatro program.
The program will ask the user to enter the lenght of the password
he wants to create.then will generate a password with this lenght.
$we will use stirng and random module at this program. 
"""
# At first we the modules help me in this program
import string                               # helps me creating a stirng of password characters
import random                               # makes the password charcters choosen randomly

# the next line we make list of types of characters which the password will consist from
# that means our generated password will consist of letter and digits and symbols
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# Now we create the function responsible for generating the password
def generate_random_password():
    # asking the user to enter the lenght of the password
    pass_lenght = int(input("Enter the lenght of the password: "))

    # we reorginize the items of characters list randomly before we bulid the passwrd from them.
    random.shuffle(characters)

    # creating a list and making it empty now and will fill it from the characters list
    password = []

    # starting filling the password list with characters to the create the password
    for i in range(pass_lenght):
        password.append(random.choice(characters))
    
    # make a shuffling again to the generated password to make it more randomly
    random.shuffle(password)

    # converting a password list to stirng to easily printing it
    password = "".join(password)

    #finally printing the passowrd
    print(password)

# Interacting with the user

choice = input("Do You want to generate random password?(Yes or No): ")
if choice.lower() == "yes":
    generate_random_password()
elif choice.lower() == "No":
    print("Program Ended")
    quit()
else:
    print("Invalid Input , Please try again")
    quit()
