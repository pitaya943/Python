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

    def update_mean(self, record, index, reward):
        self.times += 1
        self.mean = (self.mean * (self.times - 1) + reward) / self.times
        record[index, 0] += 1
        record[index, 1] = (record[index, 1]*(record[index, 0]-1) +
                            reward)/record[index, 0]
        return record


def softmax(av, tau=1.12):
    softm = (np.exp(av/tau)/np.sum(np.exp(av/tau)))
    return softm


def softmaxExperiment(means, times):
    bandits = [Bandit(means[0]), Bandit(means[1]), Bandit(means[2])]
    # , Bandit(means[3], bound), Bandit(
    # means[4], bound), Bandit(means[5], bound), Bandit(means[6], bound), Bandit(means[7], bound), Bandit(means[8], bound), Bandit(means[9], bound)
    samples = np.zeros(times)
    record = np.zeros((len(bandits), 2))

    for i in range(times):
        lst = [b.mean for b in bandits]
        temp = np.array(lst)
        p = softmax(temp, tau=0.7)

        index = np.random.choice(np.arange(len(bandits)), p=p)
        reward = bandits[index].pull_arm()
        record = bandits[index].update_mean(record, index, reward)
        samples[i] = reward

    cum_avg = np.cumsum(samples)/np.arange(1, times+1)

    print('----------times/avg----------\n', record)
    print('softmax p-value: \n', p)
    print('softmax average reward: ', cum_avg[-1])

    return cum_avg


if __name__ == '__main__':
    means = [0.9, 0.6, 0.3]
    # means = [1, 2, 3]
    # means = np.random.rand(10)
    # print('random means: \n', means)
    times = int(10e4)
    eps_avg = epsilonExperiment(means, times, epsilon=0.1)
    oiv_avg = oivExperiment(means, times, bound=10)
    softmax_avg = softmaxExperiment(means, times)

    plt.plot(eps_avg, label='Epsilon = 0.1')
    plt.plot(oiv_avg, label='Optmistic Initail Values = 10')
    plt.plot(softmax_avg, label='Softmax')
    plt.legend(loc='lower right')
    # plt.xscale('log')
    # plt.title('Moving Average Plot - Log Scale')
    plt.ylabel('Mean Rate of choosing best arm')
    plt.xlabel('Time Step')
    plt.show()
