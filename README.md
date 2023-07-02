# pacman-RL
This project focuses on developing a Reinforcement Learning (RL) model or the classic game of Pacman, utilizing the codebase provided by UC Berkeley. The goal is to train an RL agent that can navigate the Pacman game environment, collect rewards, and avoid ghosts to achieve high scores.

# Launching Pacman

Open a terminal and enter to the pacman directory. Launch the game by executing the following command in the terminal:
python busters.py

<p align="center">
<img width="363" alt="Screenshot 2023-07-02 at 10 56 08 AM" src="https://github.com/Othmaneech/pacman-RL/assets/77905364/e3633e67-5f8c-4d07-924e-98f188bf7ca0">
</p>

By default, the game starts with Pac-Man being controlled with the keyboard, ghosts are standing still and the maze is oneHunt. To check all the available options, you can execute the following command: `python busters.py --help`
The main arguments you can change are:

• -n GAMES Number of games (1 by default)

• -l LAYOUT FILE Maze (oneHunt by default)

• -p TYPE Type of Pac-Man agent (BustersKeyBoardAgent by default)

• -g TYPE Type of ghosts

• -k NUMGHOSTS Number of ghosts, from 1 to 4 (4 by default)

• -t Time delay between frames

# Automatic Pacman

I implemented a Breadth-First Search (BFS) algorithm for pathfinding that you can activate by choosing the pacman agent BasicAgentAA. It does the job but it is computationally not efficient, that's why reinforcement learning is important.  

