from typing import Tuple, Optional

import matplotlib.pyplot as plt
import numpy as np

from lib.grid_world import GridWorld

POLICY_ANNOTATIONS = [r'$\uparrow$', r'$\downarrow$', r'$\leftarrow$', r'$\rightarrow$', r'$\cdot$']


def show_frozen_lake(env: GridWorld, policy: Optional[np.ndarray] = None, V: Optional[np.ndarray] = None):
    fig, ax = plt.subplots()

    height, width = env.world_size
    ax.set_xlim((-0.5, height - 0.5))
    ax.set_ylim((-0.5, height - 0.5))
    ax.set_xticks(np.arange(0, height, ))
    ax.set_yticks(np.arange(0, height, ))
    ax.set_xticks(np.arange(0.5, height + 0.5, 1), minor=True)
    ax.set_yticks(np.arange(0.5, height + 0.5, 1), minor=True)
    ax.grid(which='minor', color='k', linestyle='-', linewidth=2)

    desc = env.world_desc
    imshow_matrix = np.zeros((height, width)) if V is None else V
    for s in env.states:
        if policy is None:
            annotation = desc[s[1]][s[0]]
        else:
            annotation = POLICY_ANNOTATIONS[int(policy[s])]
        ax.annotate(annotation, xy=tuple(reversed(s)), horizontalalignment='center')
        if V is None:
            imshow_matrix[s] = env.get_reward(s)

    if V is None:
        imshow_matrix[imshow_matrix < 0] = -np.max(imshow_matrix)
    mappable = ax.imshow(imshow_matrix, cmap='coolwarm')

    ax.invert_yaxis()
    fig.colorbar(mappable)
    fig.show()


def compute_value_function_finite_horizon(env: GridWorld, T: int) -> Tuple[np.ndarray, np.ndarray]:
    V = np.zeros((T, *env.world_size))
    Q = np.zeros((T, *env.world_size, env.n_actions))
    t = T - 1
    for s in env.states:
        V[t][s] = env.get_reward(s)
    for t in reversed(range(T - 1)):
        for s in env.states:
            for a in env.actions:
                reward = env.get_reward(s)
                expected_value = np.sum([p[1] * V[t][p[0]] for p in env.get_next_states(s, a)])
                Q[t][s][a] = reward + expected_value
            V[t][s] = np.max(Q[t][s])
    return V[0], Q[0]


def compute_value_function_infinite_horizon(env: GridWorld, discount_factor: float) -> Tuple[np.ndarray, np.ndarray]:
    V = np.zeros(env.world_size)
    Q = np.zeros((*env.world_size, env.n_actions))
    V_prev = None
    iteration = 0
    while V_prev is None or np.linalg.norm(V - V_prev) > 1e-5:
        iteration += 1
        print(f'Iteration {iteration}')
        V_prev = V.copy()

        for s in env.states:
            for a in env.actions:
                reward = env.get_reward(s)
                expected_value = np.sum([p[1] * V[p[0]] for p in env.get_next_states(s, a)])
                Q[s][a] = reward + discount_factor * expected_value
            V[s] = np.max(Q[s])
    return V, Q


def extract_policy(env: GridWorld, Q: np.ndarray) -> np.ndarray:
    policy = np.zeros(env.world_size)
    for s in env.states:
        policy[s] = np.argmax(Q[s])
    return policy


def main():
    env = GridWorld()
    V_finite, Q_finite = compute_value_function_finite_horizon(env, T=10_000)
    # V_infinite, Q_infinite = compute_value_function_infinite_horizon(env, discount_factor=0.99)
    show_frozen_lake(env, policy=extract_policy(env, Q_finite), V=V_finite)
    show_frozen_lake(env)


if __name__ == '__main__':
    main()
