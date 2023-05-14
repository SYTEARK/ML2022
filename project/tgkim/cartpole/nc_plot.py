import matplotlib.pyplot as plt
import pandas as pd
import scienceplots

# Import parquet files
df_baseline = pd.read_parquet("./data/cartpole_baseline.parquet")
df_angle    = pd.read_parquet("./data/cartpole_angle.parquet")
df_omega    = pd.read_parquet("./data/cartpole_omega.parquet")
df_custom   = pd.read_parquet("./data/cartpole_custom.parquet")

# Prepare Data to Plot
episode = df_baseline['episode']
reward_baseline = df_baseline['reward']
reward_angle    = df_angle['reward']
reward_omega    = df_omega['reward']
reward_custom   = df_custom['reward']

# Plot params
pparam = dict(
    xlabel = 'Episode',
    ylabel = 'Reward',
    title = 'CartPole-v1',
    xscale = 'linear',
    yscale = 'linear',
    ylim = (0, 400)
)

# Plot
with plt.style.context(["science", "nature"]):
    fig, ax = plt.subplots()
    ax.autoscale(tight=True)
    ax.set(**pparam)
    ax.plot(episode, reward_baseline, '.-.', label='Baseline')
    ax.plot(episode, reward_angle, '.-.', label='Via angle')
    ax.plot(episode, reward_omega, '.-.', label='Via omega')
    ax.plot(episode, reward_custom, '.-.', label='Custom')
    ax.legend()
    fig.savefig('figs/cartpole_total.png', dpi=300, bbox_inches='tight')
