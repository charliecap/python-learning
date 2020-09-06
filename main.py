player_name = input('Please tell me your name... ')
response = input("Hello, " + player_name + "... Would you like to help me? ")
if response.lower() == "yes":
    print("Thank you so much!")
elif response.lower() == "no":
    print("Oh, ok then...")
else:
    print("What was that? I didn't understand")
    # how to get the initial question to pop again after a failed response










