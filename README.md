# pacman-RL
This project focuses on developing a Reinforcement Learning (RL) model or the classic game of Pacman, utilizing the codebase provided by UC Berkeley. The goal is to train an RL agent that can navigate the Pacman game environment, collect rewards, and avoid ghosts to achieve high scores.

# Launching Pacman

Open a terminal and enter to the pacman directory. Launch the game by executing the following command in the terminal:
`python busters.py`

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

`python busters.py -p BasicAgentAA `

# RL Pacman

Open a terminal and enter to the pacman-RL directory. Launch the game by executing the following command in the terminal: `python busters.py -p QLearningAgent`

### Phase 1. Selection of the state information and reward function

First of all, we decided to take two attributes into consideration as they are the most relevant to the problem we want to solve: the distance of Pac-Man from the closest Ghost and its relative position to the latter (North East, North West, South East, South West). That is, our Q-Table looked like this at the end of our training:

<p align="center">
<img width="564" alt="Screenshot 2023-07-02 at 11 34 43 AM" src="https://github.com/Othmaneech/pacman-RL/assets/77905364/22f8baad-f70b-4e9a-8227-a00e52ae0cbe">
</p>

When it came to the reward function, we decided that every time Pac-Man gets closer to the closest Ghost, it gets +1, and it gets -1 if that is not the case. We also decided to make the reward for eating a Ghost the same as the bonus that adds up to the score: +200.

### Phase 2. Generation of the agent

When training our agent, we realised that the more it explores, the more accurate it becomes, and thus the less the α and ε values will need to be to make it work perfectly. However, as we want it to work on several layouts with more walls, it takes way too long to reach perfection. Thus, after around 100 exploration games for each of the 5 layouts, and after many trails, we found that the best values for our model are the following:

<p align="center">
<img width="329" alt="Screenshot 2023-07-02 at 11 35 54 AM" src="https://github.com/Othmaneech/pacman-RL/assets/77905364/88764a26-4c30-4564-85fb-07c3a1ac1bc7">
</p>

### Phase 3. Evaluation of the agent

After finding the best optimal values for our agent, we played it in the different mazes, where
it obtained the following scores:

labAA1:
<p> 
Average Score: 173.0
Scores: 171, 175, 171, 171, 177
Win Rate: 5/5 (1.00)
</p>

labAA2:
<p> 
Record: Win, Win, Win, Win, Win
Average Score: 365.8
Scores: 357, 373, 357, 371, 371
Win Rate: 5/5 (1.00)
Record: Win, Win, Win, Win, Win
</p>

labAA3:
<p> 
Average Score: 540.6
Scores: 545, 547, 549, 511, 551
Win Rate: 5/5 (1.00)
Record: Win, Win, Win, Win, Win
</p>

labAA4:
<p> 
Average Score: 546.6
Scores: 537, 551, 549, 545, 551
Win Rate: 5/5 (1.00)
Record: Win, Win, Win, Win, Win
</p>

labAA5:
<p>
Average Score: 696.0
Scores: 718, 722, 516, 734, 790
Win Rate: 5/5 (1.00)
Record: Win, Win, Win, Win, Win
</p>
