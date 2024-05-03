[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14588130&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  << Semester, Year >>

## Group Members

<< Zachary Latour >>

***

## Project Description

<< Welcome to the Classic Snake Game, where simple gameplay meets addictive fun! You are the the snake that moves around the screen, gobbling up food which makes you grow longer, and striving for the highest score. get around by trying to keep your snake as small as posible while getting the highest score and avoiding obsticles.>>

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Snake Movement:

The player controls a snake that moves around a grid or game area.
The snake can be controlled using arrow keys (or other input methods) to change direction.

2. Food (or Fruit) Generation:
Food items appear randomly on the game area.
When the snake collides with a food item, it grows longer.

3. Snake Growth and Length:
Eating food increases the length of the snake.
The player's score may increase each time the snake eats food.
White fruit adds 1 point and adds a part to the snake
Blue fruit add 2 points but doesn't add a part to the snake
Yellow fruit ends the game

4. Game Over Conditions:
The game ends if the snake collides with itself (hits its own body).
The game also ends if the snake collides with the game boundaries (walls).

5. Score Tracking:
The game keeps track of the player's score based on the number of food items eaten.
The highscore is displayed and saves.

6. Game Restart and Replay:
After a game over, the player can choose to restart the game and play again.
High scores or best performances may be recorded for comparison.


### Classes

- << snake: A list of tuples representing the coordinates of the snake segments.
snake_direction: A string representing the current direction of the snake ('LEFT', 'RIGHT', 'UP', 'DOWN').
food: A tuple representing the coordinates of the food item that the snake needs to eat.
extra_food: A tuple representing the coordinates of an additional food item that adds score when eaten.
yellow_block: A tuple representing the coordinates of a yellow block that, if collided with, ends the game.
score: An integer representing the player's current score.
high_score: An integer representing the highest score achieved in the game (loaded from and saved to a file).
running: A boolean indicating whether the game is currently running.
__init__(self): Initializes the game state by setting up the snake, initial direction, food positions, and scores.
random_food_position(self): Generates random coordinates for placing food on the game grid.
handle_events(self): Handles user input events to change the snake's direction.
update_snake_position(self): Updates the snake's position based on its current direction.
spawn_yellow_block(self): Spawns a yellow block at a random position on the grid.
check_collisions(self): Checks for collisions between the snake and other game elements (food, yellow block).
check_high_score(self): Updates the high score if the current score exceeds the previous high score.
save_high_score(self): Saves the high score to a file.
load_high_score(self): Loads the high score from a file (or initializes to 0 if file doesn't exist).
game_over(self): Ends the game and saves the high score.
restart_game(self): Resets the game state to start a new game.
draw(self): Draws all game elements (snake, food, yellow block) on the screen.
draw_grid(self): Draws a grid on the game screen for better visualization.
draw_score(self): Draws the current score on the game screen.
draw_high_score(self): Draws the high score on the game screen.
run(self): Main game loop that handles events, updates the game state, and redraws the screen. >>

## ATP

Test Case 1: Player Movement
Test Description: Verify that the snake moves left and right as expected.

Test Steps:

1 Start the game.
2 Press the left arrow key.
3 Verify that the snake's head moves left.
4 Press the right arrow key.
5 Verify that the snake's head moves right.
6 Expected Outcome: The snake's head should move left and right in response to the arrow key inputs.

Test Case 2: Collision Detection
Test Description: Ensure that collisions between the snake's head and food are detected correctly.

Test Steps:

1 Start the game.
2 Position the snake's head in line to a piece of white food.
3 Move the snake's head to collide with the food.
4 Verify that the snake grows in length after eating the food.
7 Verify that no collision is detected.

Expected Outcome: The snake should grow when its head collides with food, and no collision should occur when the snake moves without colliding with food.

Test Case 3: Game Over Condition
Test Description: Confirm that the game ends when the snake collides with itself or with the boundaries of the game area.

Test Steps:

1 Start the game.
2 Move the snake's head to collide with its own body or boundries.
3 Verify that the game displays a "Game Over" message.

Expected Outcome: The game should display a "Game Over" message when the snake collides with itself or with the game boundaries.

Test Case 4: Restart Navigation
Test Description: Test the navigation through the game's main menu.

Test Steps:

1 Start the game.
2 Move the snake into a waill or itself
3 Verify that the game displays a "Game Over" message.
4 Press R to restart the game

Expected Outcome: The game restrts after you die

Test Case 5: New highscore
Test Description: Verify that the program keeps your new highscore.

Test Steps:

1 Start the game.
2 Move your snake to eat food and get a score
3 Restart a new game butt get a higher score
4 Check if your new score is next tot the high score

Verify the program replaces the first score with your new higher score.
