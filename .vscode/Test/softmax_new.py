from ast import Not
import numpy as np
import matplotlib.pyplot as plt
from epsilon_new import epsilonExperiment
from oiv_new import oivExperiment


class Bandit():
    def __init__(self, mu):
        self.mu = mu
        self.mean = 0
        self.times = 0

    def pull_arm(self):
        return np.random.randn()+self.mu

    def update_mean(self, reward):
        self.times += 1
        self.mean = (self.mean * (self.times - 1) + reward) / self.times


def softmax(av, tau=1.12):
    softm = (np.exp(av/tau)/np.sum(np.exp(av/tau)))
    return softm


def softmaxExperiment(means, times, tau):
    bandits = [Bandit(means[0]), Bandit(means[1]), Bandit(means[2])]
    # , Bandit(means[3], bound), Bandit(
    # means[4], bound), Bandit(means[5], bound), Bandit(means[6], bound), Bandit(means[7], bound), Bandit(means[8], bound), Bandit(means[9], bound)
    samples = np.zeros(times)
    explore = []

    for i in range(times):
        bestOption = np.argmax([b.mean for b in bandits])
        lst = [b.mean for b in bandits]
        temp = np.array(lst)
        p = softmax(temp, tau=tau)
        index = np.random.choice(np.arange(len(bandits)), p=p)
        reward = bandits[index].pull_arm()
        bandits[index].update_mean(reward)
        samples[i] = reward

        if not index == bestOption:
            explore.append(i)

    cum_avg = np.cumsum(samples)/np.arange(1, times+1)

    print('softmax p-value: \n', p)
    print('softmax average reward: ', cum_avg[-1])
    print(
        'Tau Value = {0}, Number of Explored samples: {1}/{2}'.format(tau, len(explore), times))

    return cum_avg


if __name__ == '__main__':
    means = [0.9, 0.6, 0.3]
    # means = [1, 2, 3]
    # means = np.random.rand(10)
    # print('random means: \n', means)
    times = int(10e4)
    eps_avg = epsilonExperiment(means, times, epsilon=0.1)
    oiv_avg = oivExperiment(means, times, bound=10)
    softmax_avg = softmaxExperiment(means, times, tau=0.1)

    plt.plot(eps_avg, label='Epsilon = 0.1')
    plt.plot(oiv_avg, label='Optmistic Initail Values = 10')
    plt.plot(softmax_avg, label='Softmax')
    plt.legend(loc='lower right')
    plt.xscale('log')
    plt.title('Moving Average Plot - Log Scale')
    plt.ylabel('Mean Rate of choosing best arm')
    plt.xlabel('Time Step')
    plt.show()
