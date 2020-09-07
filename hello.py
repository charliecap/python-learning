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
#         print("Sorry, I don't understand that... You can ask for help directly")


# control flow
# if statements

# if condition:
#     code to execute if condition is true
#

# is_game_over = False
# p_0_x_pos = 0
# e_0_x_pos = 3
# e_1_x_pos = 5
#
# p_0_x_pos += 2
# if p_0_x_pos == e_0_x_pos:
#     is_game_over = True
# elif p_0_x_pos == e_1_x_pos:
#     is_game_over = True
# else:
#     e_0_x_pos += 1
#     e_1_x_pos += 1
#
# if p_0_x_pos == e_0_x_pos or e_1_x_pos:   # or / and
#     is_game_over = True
# else:
#     e_0_x_pos += 1
#     e_1_x_pos += 1


# is_game_over = False
# p_x_pos = 2
# e_x_pos = 3
# end_x_pos = 10
#
# while not is_game_over:
#     print(p_x_pos)
#     print(e_x_pos)
#     if p_x_pos == e_x_pos:
#         print("You lose!")
#         is_game_over = True
#     elif p_x_pos >= end_x_pos:
#         print("You win!!!")
#         is_game_over = True
#     else:
#         p_x_pos += 3
#         e_x_pos += 1
#
# x_pos = 5
# movements = [1, -2, 6, -3, -2, 4]
#
# for movement in movements:
#     x_pos += movement
# print(x_pos)

# FUNCTIONS _________________________________________________________________

# x_pos = 0
# e_x_pos = 4
#
# def move():
#     global x_pos
#     x_pos += 1
#
# move()
#
# # Function to increase x_pos by 'amount'
# def move_by(amount):
#     global x_pos
#     x_pos += amount
#
#
# # Function to check if player and enemy collide
# # Output True if they collide and False if they don't
# def check_for_collision():
#     global x_pos
#     global e_x_pos
#     if x_pos == e_x_pos:
#         return True
#     else:
#         return False
#
#
# move_by(3)
#
# did_collide = check_for_collision()
#
#
# print(x_pos)
# print(did_collide)
#
# Classes and object ---------------------------------------------------------------------------
#Class fields, methods, and constructors
# Object instantiation

# class GameCharacter:
#
#     speed = 5
#
#     def __init__(self, name, width, height, x_pos, y_pos):
#         self.name = name
#         self.width = width
#         self.height = height
#         self.x_pos = x_pos
#         self.y_pos = y_pos
#
#     def move(self, by_x_amount, by_y_amount):
#         self.x_pos += by_x_amount
#         self.y_pos += by_y_amount
#
# character_0 = GameCharacter('char_0', 50, 100, 100, 100)
# character_0.name = 'char_1'
# character_0.move(50, 100)
#
#
#
# class PlayerCharacter(GameCharacter):
#
#     speed = 10
#
#     def __init__(self, name, x_pos, y_pos):
#         super().__init__(name, 100, 100, x_pos, y_pos)
#
#     def move(self, by_y_amount):
#         super().move(0, by_y_amount)
#
# player_character = PlayerCharacter("P_character", 500, 500)
# player_character.move(100)
# print(player_character.x_pos)
# print(player_character.y_pos)
#
#
#

# my goof around code ----------------------------------------------
# player_name = input('Please tell me your name... ')
# response = input("Hello, " + player_name + "... Would you like to help me? ")
# if response.lower() == "yes":
#     print("Thank you so much!")
# elif response.lower() == "no":
#     print("Oh, ok then...")
# else:
#     print("What was that? I didn't understand")
#     # how to get the initial question to pop again after a failed response
#
#
#
#
#















