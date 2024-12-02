Student Declaration:

This project was created by Samuel Ajibola Bolarinde. I declare that this is my own work, completed as part of my school project. Any external resources or libraries used have been properly cited in this document.





Tower Defense Game
This is a simple Tower Defense game created using Pygame. The game allows players to input their name, start a new game, view player statistics, and simulate game progress. It was developed as part of a school project.

Features:
Name Input: Players are prompted to enter their name, which is saved and displayed during the game.
Start Game: Once the player enters their name, they can begin the game.
Player Stats: Players can view their game statistics, such as the number of rounds completed and total time spent in the game.
Instructions: Clear instructions are displayed during the name input phase and during gameplay.
Background & UI: The game includes a visually appealing background and custom buttons to start the game and view player stats.

Requirements:
Before running the game, make sure you have the following installed:

Python (>= 3.6)
Pygame (for the game logic and rendering)
To install Pygame, you can use the following pip command:

pip install pygame

How to Play:

Place Turrets:
Use the money you are given at the start of the game to buy turrets.
Place the turrets strategically in locations where they can best stop the enemy from advancing.
Defeat Enemies:

As enemies advance, your turrets will automatically attack them. Defeat as many enemies as possible to earn money.
Progress Through Rounds:

The more enemies you defeat, the more money you earn to buy additional turrets or upgrade existing ones.
Each round features stronger enemies, requiring you to carefully plan turret placement and upgrades.

Compete for Leaderboard:
Get past each level as quickly as possible to earn a spot at the top of the leaderboard.
Your stats, including the number of rounds completed and total time, are recorded.

Game Over:

If the enemies manage to advance past your defenses, the game will end. Your stats are saved for future sessions.

How to Run:
Ensure you have Python and Pygame installed.
Navigate to the project directory in your terminal/command prompt.

Run the following command:
python main.py
This will launch the game. The game will open in a Pygame window where you can start, input your name, and view player stats.

Game Flow:
Start Screen: The game starts by showing the main menu with buttons.
Name Input: After clicking the "Begin" button, you will be asked to input your name.
Gameplay: Place turrets, defeat enemies, and progress through rounds while earning money to buy more turrets.
Leaderboard: View your stats and compete for the top spot on the leaderboard.
Game Over: After completing a round or losing, the game updates your stats and returns to the start screen.


Good Parts:
Name Input and Stats: The game handles name input well, saving the player’s name and showing it during gameplay and in the stats.
Start and Stats Screens: Clear and easy-to-use UI elements, including buttons for starting the game and viewing stats.
Player Stats Saving: Player stats are stored in a JSON file (player_stats.json), which allows the game to keep track of rounds played and total time.
Gameplay Instructions: Detailed instructions make it easier for players to understand the game mechanics.


Limitations:
Level Starts at Level 11: Currently, the game always starts at level 11. This is an issue as the game's progression is not properly handled, and the starting point does not make sense. This could be fixed by resetting the game level at the start of each new session or adding a level progression system. There are also some other minor problems and bugs but overall the code works as intended

Incomplete Gameplay Logic: The game is incomplete in terms of actual tower defense mechanics. There's no tower placement, enemy waves, or game-over conditions based on player actions (other than simulated game-over). The game flow is currently just a placeholder for future work.

Stats Display Not Interactive: The player stats are not very interactive, and players cannot interact with them beyond viewing. This could be expanded into a more detailed view with options like resetting stats or sorting.

Sorting and Aggregation:
Player Stats Sorting: The stats (number of rounds played and total time) are stored in a JSON file, but there is no sorting mechanism currently in place to display the stats in any particular order (e.g., highest to lowest). Sorting could be added by implementing a sorting function in the stats screen.

Aggregation: Currently, the game only aggregates data (rounds played and total time) per player, but no further aggregation or advanced features like leaderboards or aggregating by multiple players over time have been implemented.





Citations

CHAT GPT
Youtube- Coding with Russ
