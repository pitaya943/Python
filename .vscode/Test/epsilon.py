import numpy as np
import matplotlib.pyplot as plt
import random


class EpsilonGreedy:
    def __init__(self, epsilon, action):
        self.epsilon = epsilon  # epsilon value
        self.num_arm = 10  # number of arm

        self.prbs = np.random.rand(self.num_arm)
        self.action = action
        self.record = np.zeros((self.num_arm, 2))

    def pull(self, prob):
        reward = 0
        for i in range(10):
            if random.random() < prob:
                reward += 1
        return reward

    def update(self, index, reward):
        self.record[index, 0] += 1
        self.record[index, 1] = (self.record[index, 1]*(self.record[index, 0]-1) +
                                 reward)/self.record[index, 0]

    def calculate(self):
        sample = np.zeros(self.action)
        explore = []
        for i in range(self.action):
            if np.random.random() > self.epsilon:
                index = np.argmax(self.record[:, 1])
            else:
                index = np.random.randint(self.num_arm)
                explore.append(i)
            reward = self.pull(self.prbs[index])
            self.update(index, reward)
            sample[i] = reward

        print('For Epsilon Value: {0}, Number of Explored samples: {1}/{2}'.format(
            self.epsilon, len(explore), self.action))

        # print('reward\'s avg: \n', self.record[:, 1])
        # print('arm\'s probability: \n', self.prbs)
        # print(self.record)

        cum_avg = np.cumsum(sample)/np.arange(1, self.action+1)
        return cum_avg


E01 = EpsilonGreedy(epsilon=0.1, action=10000)
E02 = EpsilonGreedy(epsilon=0.2, action=10000)
E03 = EpsilonGreedy(epsilon=0.3, action=10000)
avg01 = E01.calculate()
avg02 = E02.calculate()
avg03 = E03.calculate()
plt.plot(avg01, label='Epsilon = 0.1')
plt.plot(avg02, label='Epsilon = 0.2')
plt.plot(avg03, label='Epsilon = 0.3')
plt.legend(loc='lower right')
plt.xscale('log')
plt.ylabel('Rate of choosing best arm')
plt.xlabel('Time Step')
plt.show()
