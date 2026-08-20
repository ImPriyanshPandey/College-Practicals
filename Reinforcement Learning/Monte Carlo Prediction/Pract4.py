import numpy as np
import random
from collections import defaultdict

GRID_SIZE = 4
ACTIONS = ['U', 'D', 'L', 'R']
TERMINAL_STATES = [(0, 0), (3, 3)]
GAMMA = 1.0
EPISODES = 5000  

V = defaultdict(float)
returns_count = defaultdict(int)

# Policy
def policy(state):
    return random.choice(ACTIONS)

# Environment
def step(state, action):
    i, j = state

    if state in TERMINAL_STATES:
        return state, 0, True

    if action == 'U':
        next_state = (max(i-1, 0), j)
    elif action == 'D':
        next_state = (min(i+1, GRID_SIZE-1), j)
    elif action == 'L':
        next_state = (i, max(j-1, 0))
    else:  # 'R'
        next_state = (i, min(j+1, GRID_SIZE-1))

    reward = -1
    done = next_state in TERMINAL_STATES
    return next_state, reward, done


# Monte Carlo Prediction
for episode in range(EPISODES):

    state = random.choice([
        (i, j) for i in range(GRID_SIZE)
        for j in range(GRID_SIZE)
        if (i, j) not in TERMINAL_STATES
    ])

    episode_data = []

    # Generate episode
    while True:
        action = policy(state)
        next_state, reward, done = step(state, action)
        episode_data.append((state, reward))
        state = next_state

        if done:
            break   # 

    # First-Visit MC
    visited_states = set()
    G = 0

    for t in reversed(range(len(episode_data))):
        state_t, reward_t = episode_data[t]
        G = reward_t + GAMMA * G

        if state_t not in visited_states:
            visited_states.add(state_t)
            returns_count[state_t] += 1
            V[state_t] += (G - V[state_t]) / returns_count[state_t]

    # 🔹 Show learning progress every 1000 episodes
    if (episode + 1) % 1000 == 0:
        print(f"\nEpisode {episode+1}")
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                row.append(f"{V[(i,j)]:6.2f}")
            print(" ".join(row))

print("\nMonte Carlo Prediction completed.")