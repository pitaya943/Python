import numpy as np
import matplotlib.pyplot as plt
import random


class EpsilonGreedy:
    def __init__(self, action):
        self.num_arm = 3
        # self.prbs = np.random.rand(self.num_arm)
        self.prbs = [0.9, 0.6, 0.3]

        self.action = action
        self.reward = [0]
        self.record = np.zeros((self.num_arm, 2))

    def pull(self, prob):
        reward = 0
        for i in range(10):
            if random.random() < prob:
                reward += 1
        return reward

    def update_record(self, action, reward):
        self.record[action, 0] += 1
        self.record[action, 1] = (self.record[action, 1]*(self.record[action, 0]-1) +
                                  reward)/self.record[action, 0]

    def softmax(self, av, tau=1.12):
        softm = (np.exp(av/tau)/np.sum(np.exp(av/tau)))
        return softm

    def calculate(self):
        for i in range(self.action):
            # choose arm
            p = self.softmax(self.record[:, 1])
            choice = np.random.choice(np.arange(self.num_arm), p=p)
            reward = self.pull(self.prbs[choice])
            self.update_record(choice, reward)

            mean_reward = ((i+1) * self.reward[-1] + reward) / (i+2)
            self.reward.append(mean_reward)

        # print('whole reward average: ', self.reward)
        print('--------- probs ---------\n',
              self.prbs)
        print('------- softmax probs -------\n', p)
        print('----------times/avg----------\n', self.record)
        # print(self.reward[-1])

    def plot(self):
        x = np.arange(len(self.reward))
        y1 = self.reward
        plt.plot(x, y1)
        plt.ylabel('Mean Rate of reward')
        # plt.xscale('log')
        plt.xlabel('Time Step')
        plt.show()


E = EpsilonGreedy(action=10000)
E.calculate()
E.plot()
