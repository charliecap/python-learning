# Gain access to the pygame library
import pygame

# Size of the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = 'RPG by Me'
# Colors according to RGB
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# Clock used to update game events and frames
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)


class Game:
    # Typical rate of 60, equivalent to FPS
    TICK_RATE = 60

    # Initializer for the game class to set up the width, height, and title
    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Create the window of specified size in white to display game
        self.game_screen = pygame.display.set_mode((width, height))
        # Set the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

        # Load and set the background image for the scene
        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False
        direction = 0

        player_character = PlayerCharacter('images/player.png', 325, 600, 50, 50)

        enemy_0 = NonPlayerCharacter('images/enemy.png', 20, 500, 50, 50)
        enemy_0.SPEED *= level_speed

        enemy_1 = NonPlayerCharacter('images/enemy.png', self.width - 35, 300, 50, 50)
        enemy_1.SPEED *= level_speed

        enemy_2 = NonPlayerCharacter('images/enemy.png', 60, 150, 50, 50)
        enemy_2.SPEED *= level_speed

        treasure = GameObject('images/treasure.png', 325, 10, 50, 50)

        # Main game loop, used to update all gameplay such as movement, checks, and graphics
        # Runs until is_game_over - True
        while not is_game_over:

            # A loop to get all of the events occurring at any given time
            # Events are most often mouse movement, mouse and button clicks, or exit events
            for event in pygame.event.get():
                # If we have a quit type of event (exit out) then exit out of the game loop
                if event.type == pygame.QUIT:
                    is_game_over = True
                    # Detect when key is pressed down
                elif event.type == pygame.KEYDOWN:
                    # Move up if up key pressed
                    if event.key == pygame.K_UP:
                        direction = 1
                    # Move down if down key pressed
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # Detect when key is released
                elif event.type == pygame.KEYUP:
                    # Stop movement when key no longer pressed
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0

                print(event)

            # Redraw game screen to a white window
            self.game_screen.fill(WHITE_COLOR)
            # Draw the image onto the background
            self.game_screen.blit(self.image, (0, 0))

            # Draw the treasure
            treasure.draw(self.game_screen)

            # Update the player position
            player_character.move(direction, self.height)
            # Draw the player at the new position
            player_character.draw(self.game_screen)

            # Move and draw enemy
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            if level_speed > 1:
                enemy_1.move(self.width)
                enemy_1.draw(self.game_screen)

            if level_speed > 2:
                enemy_2.move(self.width)
                enemy_2.draw(self.game_screen)

            # End game if collision between enemy or treasure
            # Close the game if we lose
            # Restart game loop if we win
            if player_character.detect_collision(enemy_0):
                is_game_over = True
                did_win = False
                text = font.render('You lose!', True, BLACK_COLOR)
                self.game_screen.blit(text, (250, 300))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detect_collision(enemy_1):
                is_game_over = True
                did_win = False
                text = font.render('You lose!', True, BLACK_COLOR)
                self.game_screen.blit(text, (250, 300))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detect_collision(enemy_2):
                is_game_over = True
                did_win = False
                text = font.render('You lose!', True, BLACK_COLOR)
                self.game_screen.blit(text, (250, 300))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detect_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render('You win!', True, BLACK_COLOR)
                self.game_screen.blit(text, (240, 300))
                pygame.display.update()
                clock.tick(1)
                break

            # Update all game graphics
            pygame.display.update()
            # Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)
        # Restart if we won, Quit the loop if we lost
        if did_win:
            self.run_game_loop(level_speed + 0.5)
        else:
            return


class GameObject:

    def __init__(self, image_path, x, y, width, height):
        # Load the player image from the file directory
        object_image = pygame.image.load(image_path)
        # Scale the image up
        self.image = pygame.transform.scale(object_image, (width, height))
        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


# Class to represent character controlled by player
class PlayerCharacter(GameObject):
    # How many tiles the character moves per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function will move character up if direction > 0 and down if < 0
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        # Make sure character never falls below bottom of screen
        if self.y_pos >= max_height - 50:
            self.y_pos = max_height - 50

    # Return False (no collision) if y positions and x positions do not overlap
    # Return True if x and y overlap
    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False

        return True


# Class to represent character controlled by player
class NonPlayerCharacter(GameObject):
    # How many tiles the character moves per second
    SPEED = 6

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function will move character up if direction > 0 and down if < 0
    def move(self, max_width):
        if self.x_pos <= 10:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 50:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED


# Initialize pygame !!!!!!!!!!!!!!!!!!!!!!
pygame.init()

new_game = Game('images/background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1)

# Quit pygame and the program
pygame.quit()
quit()

# Draw a rectangle on top of the game screen canvas (x, y, width, height)
# pygame.draw.rect(game_screen, BLACK_COLOR, [300, 300, 100, 100])
# Draw a circle on top of the game screen (x, y, radius)
# pygame.draw.circle(game_screen, BLACK_COLOR, (350, 250), 50)
# game_screen.blit(player_image, (300, 300))
