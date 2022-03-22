import numpy as np
import matplotlib.pyplot as plt
import random


class Greedy:
    def __init__(self):
        self.num_arm = 10
        self.prbs = np.random.rand(self.num_arm)
        # self.prbs = [0.5, 0.3, 0.7, 0.6, 0.5, 0.1, 0.2, 0.4, 0.8, 0.75]

        self.action = 100
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

    def get_best_option(self, record):
        index = np.argmax(record[:, 1]) + 1
        return index

    def get_best_option_value(self, index):
        value = self.record[index - 1, 1]
        return value

    def calculate(self):
        for i in range(self.action):
            choice = np.random.choice(np.arange(self.num_arm))
            reward = self.pull(self.prbs[choice])
            self.update_record(choice, reward)

        bestOption = self.get_best_option(self.record)
        bestOptionValue = self.get_best_option_value(bestOption)
        print(self.record)
        print('best option is: No.', bestOption)
        print('best option\'s value is: ', bestOptionValue)
        print('arm\'s probability: \n', self.prbs)


G = Greedy()
G.calculate()
