import numpy as np
import matplotlib.pyplot as plt
import random


class OIV:
    def __init__(self, bound, action):
        self.num_arm = 10  # number of arm

        self.prbs = np.random.rand(self.num_arm)
        self.action = action
        self.record = np.zeros((self.num_arm, 2))
        self.record[:, 1] = bound

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
        for i in range(self.action):
            index = np.argmax(self.record[:, 1])
            reward = self.pull(self.prbs[index])
            self.update(index, reward)
            sample[i] = reward

        # print('reward\'s avg: \n', self.record[:, 1])
        # print('arm\'s probability: \n', self.prbs)
        # print(self.record)
        cum_avg = np.cumsum(sample)/np.arange(1, self.action+1)
        return cum_avg


O01 = OIV(action=10000, bound=100)
O02 = OIV(action=10000, bound=10)
O03 = OIV(action=10000, bound=1)

ovi1 = O01.calculate()
ovi2 = O02.calculate()
ovi3 = O03.calculate()
plt.plot(ovi1, label='Optmistic Initail Values = 100')
plt.plot(ovi2, label='Optmistic Initail Values = 10')
plt.plot(ovi3, label='Optmistic Initail Values = 1')
plt.legend(loc='lower right')
plt.xscale('log')
plt.ylabel('Mean Rate of reward')
plt.xlabel('Time Step')
plt.show()
