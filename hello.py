# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press Ctrl+F8 to toggle the breakpoint.
# if __name__ == '__main__':
#     print_hi('Charlie')


# formatted string example -------------------------------------

# first = 'Charlie
# last = 'Cline'
# message = f'{first} {last} is a coder'
# print(message)


# number guesser example ------------------------------------------------------------

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won!')
#         break
# else:
#     print('You failed')



# car program example ----------------------------------------
# command = ""
# started = False
# while True:
#     command = input('> ').lower()
#     if command == "start":
#         if started:
#             print("Car is already started, goof...")
#         else:
#             started = True
#             print("Car Started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped... Duh")
#         else:
#             started = False
#             print("Car Stopped...")
#     elif "help" in command:
#             print("""
# start - to start the car
# stop - stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I dont understand that... You can ask for help directly")

