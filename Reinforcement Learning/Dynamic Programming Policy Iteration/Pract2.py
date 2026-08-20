import numpy as np

GRID_SIZE = 4
GAMMA = 1.0
THETA = 1e-4

ACTIONS = ['U', 'D', 'L', 'R']
terminal_states = [(0, 0), (3, 3)]

V = np.zeros((GRID_SIZE, GRID_SIZE))
policy = np.ones((GRID_SIZE, GRID_SIZE, len(ACTIONS))) / len(ACTIONS)

def next_state_reward(state, action):
    i, j = state
    if state in terminal_states:
        return state, 0
    if action == 'U': ni, nj = max(i - 1, 0), j
    elif action == 'D': ni, nj = min(i + 1, GRID_SIZE - 1), j
    elif action == 'L': ni, nj = i, max(j - 1, 0)
    elif action == 'R': ni, nj = i, min(j + 1, GRID_SIZE - 1)
    return (ni, nj), -1

def policy_evaluation(V, policy):
    while True:
        delta, new_V = 0, V.copy()
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if (i, j) in terminal_states: continue
                v = 0
                for a_idx, action in enumerate(ACTIONS):
                    (ni, nj), reward = next_state_reward((i, j), action)
                    v += policy[i, j, a_idx] * (reward + GAMMA * V[ni, nj])
                new_V[i, j] = v
                delta = max(delta, abs(V[i, j] - new_V[i, j]))
        V = new_V
        if delta < THETA: break
    return V

def policy_improvement(V, policy):
    policy_stable = True
    print("\n--- Final Policy Improvement Summary ---")
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i, j) in terminal_states: continue
            old_action = np.argmax(policy[i, j])
            action_values = np.zeros(len(ACTIONS))
            for a_idx, action in enumerate(ACTIONS):
                (ni, nj), reward = next_state_reward((i, j), action)
                action_values[a_idx] = reward + GAMMA * V[ni, nj]
            best_action = np.argmax(action_values)
            policy[i, j] = np.eye(len(ACTIONS))[best_action]
            if old_action != best_action: policy_stable = False
            print(f"State {i,j}: values={action_values}, best={ACTIONS[best_action]}")
    return policy, policy_stable

# Policy Iteration
while True:
    V = policy_evaluation(V, policy)
    policy, stable = policy_improvement(V, policy)
    if stable: break

print("\nOptimal Value Function:")
print(V)

print("\nOptimal Policy (U,D,L,R):")
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if (i, j) in terminal_states:
            print("T", end=" ")
        else:
            print(ACTIONS[np.argmax(policy[i, j])], end=" ")
    print()
