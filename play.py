# example.py
import imageio
import gymnasium as gym
import numpy as np
import gym_aloha

env = gym.make("gym_aloha/AlohaInsertion-v0", obs_type="pixels_agent_pos")
observation, info = env.reset()
frames = []

for _ in range(1000):
    print("hi")
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    image = env.render()
    frames.append(image)

    if terminated or truncated:
        observation, info = env.reset()

env.close()
imageio.mimsave("example.mp4", np.stack(frames), fps=25)