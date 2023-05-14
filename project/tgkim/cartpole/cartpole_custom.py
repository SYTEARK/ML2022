# Gymnasium (Successor of OpenAI-Gym)
import gymnasium as gym
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation

def save_frames_as_gif(frames, path='./', filename='gym_animation.gif'):

    #Mess with this to change frame size
    plt.figure(figsize=(frames[0].shape[1] / 72.0, frames[0].shape[0] / 72.0), dpi=72)

    patch = plt.imshow(frames[0])
    plt.axis('off')

    def animate(i):
        patch.set_data(frames[i])

    anim = animation.FuncAnimation(plt.gcf(), animate, frames = len(frames), interval=50)
    anim.save(path + filename, writer='imagemagick', fps=60)

env = gym.make('CartPole-v1', render_mode='human')

observation, info = env.reset(seed=11977)
reward_vec = []
curr_reward = 0
episode = 0

while episode < 10:
    if observation[3] > 0:
        action = 1
    else:
        action = 0

    if observation[1] > 1:
        action = 1
        if observation[3] < -0.3:
            action = 0
    elif observation[1] < -1:
        action = 0
        if observation[3] > 0.3:
            action = 1

    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()
        print(f"reward:{curr_reward}")
        reward_vec.append(curr_reward)
        curr_reward = 0
        episode += 1
    else:
        curr_reward += reward
        
env.close()

episode_vec = np.arange(1, len(reward_vec) + 1)

df = pd.DataFrame({
    "episode": episode_vec,
    "reward": reward_vec
})

df.to_parquet("./data/cartpole_custom.parquet")

plt.figure(figsize=(10,6), dpi=300)
plt.plot(df["episode"], df["reward"], color='blue', marker='o', linestyle='dashed', linewidth=1, markersize=3)
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.title("CartPole-v1 Custom")
plt.grid()
plt.savefig("figs/cartpole_custom.png", dpi=300)

