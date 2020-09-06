command = ""
problem_solved = False
player_name = input('Please tell me your name... ')
response = input("Hello, " + player_name + "... Would you like to help me? ")
if "yes" in response.lower():
    print("Thank you so much!")
    input(" ")
elif "no" in response.lower():
    print("Oh, ok then...")
else:
    print("What was that? I didn't understand")
    # how to get the initial question to pop again after a failed response
while True:
	command = input('> ').lower()

