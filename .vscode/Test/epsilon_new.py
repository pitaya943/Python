import numpy as np
import matplotlib.pyplot as plt


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


def epsilonExperiment(means, times, epsilon):
    bandits = [Bandit(means[0]), Bandit(means[1]), Bandit(means[2])]
    # , Bandit(means[3], bound), Bandit(
    # means[4], bound), Bandit(means[5], bound), Bandit(means[6], bound), Bandit(means[7], bound), Bandit(means[8], bound), Bandit(means[9], bound)
    samples = np.zeros(times)
    explore = []

    for i in range(times):
        rand = np.random.random()
        if rand < epsilon:
            index = np.random.choice(len(bandits))
            explore.append(i)
        else:
            index = np.argmax([bd.mean for bd in bandits])
        reward = bandits[index].pull_arm()
        bandits[index].update_mean(reward)
        samples[i] = reward

    cum_avg = np.cumsum(samples)/np.arange(1, times+1)
    print(
        'Epsilon Value = {0}, Number of Explored samples: {1}/{2}'.format(epsilon, len(explore), times))

    return cum_avg


# main
if __name__ == '__main__':
    means = [0.9, 0.6, 0.3]
    # means = np.random.rand(10)
    # print(means)
    numberOfaction = int(10e4)
    cum_avg1 = epsilonExperiment(means, numberOfaction, epsilon=0.1)
    cum_avg2 = epsilonExperiment(means, numberOfaction, epsilon=0.2)
    cum_avg3 = epsilonExperiment(means, numberOfaction, epsilon=0.3)

    plt.plot(cum_avg1, label='Epsilon = 0.1')
    plt.plot(cum_avg2, label='Epsilon = 0.2')
    plt.plot(cum_avg3, label='Epsilon = 0.3')
    plt.legend(loc='lower right')
    plt.xscale('log')
    plt.title('Moving Average Plot - Log Scale')
    plt.ylabel('Mean Rate of choosing best arm')
    plt.xlabel('Time Step')
    plt.show()
    
