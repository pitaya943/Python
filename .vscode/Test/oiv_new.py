import numpy as np
import matplotlib.pyplot as plt
from epsilon_new import epsilonExperiment


class Bandit:
    def __init__(self, mu, bound):
        self.mu = mu
        self.mean = bound
        self.times = 0

    def pull_arm(self):
        return np.random.randn()+self.mu

    def update_mean(self, reward):
        self.times += 1
        self.mean = (self.mean * (self.times - 1) + reward) / self.times


def oivExperiment(means, times, bound):
    bandits = [Bandit(means[0], bound), Bandit(
        means[1], bound), Bandit(means[2], bound)]
    # , Bandit(means[3], bound), Bandit(
    #     means[4], bound), Bandit(means[5], bound), Bandit(means[6], bound), Bandit(means[7], bound), Bandit(means[8], bound), Bandit(means[9], bound)
    samples = np.zeros(times)

    for i in range(times):
        index = np.argmax([bd.mean for bd in bandits])
        reward = bandits[index].pull_arm()
        bandits[index].update_mean(reward)
        samples[i] = reward

    cum_avg = np.cumsum(samples)/np.arange(1, times+1)

    return cum_avg


if __name__ == '__main__':
    means = [0.9, 0.6, 0.3]
    # means = np.random.rand(10)
    # print(means)
    times = int(10e3)
    eps_avg = epsilonExperiment(means, times, epsilon=0.1)
    oiv_avg = oivExperiment(means, times, bound=10)

    plt.plot(eps_avg, label='Epsilon = 0.1')
    plt.plot(oiv_avg, label='Optmistic Initail Values = 10')
    plt.legend(loc='lower right')
    # plt.xscale('log')
    # plt.title('Moving Average Plot - Log Scale')
    plt.ylabel('Mean Rate of choosing best arm')
    plt.xlabel('Time Step')
    plt.show()
