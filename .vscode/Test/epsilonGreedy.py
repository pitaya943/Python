import numpy as np
import matplotlib.pyplot as plt


class eGreedyBandit():
    def __init__(self, mu, mean):
        self.mu = mu
        self.mean = mean  # average of reward
        self.times = 0

    def pull(self):
        return np.random.randn()+self.mu  # 波動值 np.random.randn -> [0,1)

    def update(self, xn):  # xn currrent reward
        self.times += 1
        self.mean = (self.mean*(self.times-1)+xn)/self.times  # self.times = n
        # 平均累計獎賞 = 是第n步平均累計獎賞，首先要對之前n-1步獎賞求和，加上第n步獎勵，最后求平均

    def run(self, mu1, mu2, mu3, epsilon=0.1, N=10000):
        bandits = [eGreedyBandit(mu1, self.mean), eGreedyBandit(
            mu2, self.mean), eGreedyBandit(mu3, self.mean)]
        data = []
        # run simulation for N times
        for i in range(N):
            # 1. choose bandit
            p = np.random.random()  # if epsilon > random num -> choose one of three bandits
            if p < epsilon:
                j = np.random.choice(3)
            else:  # else -> take advantage of the biggist mean now
                j = np.argmax([b.mean for b in bandits])
            # 2.pull it
            x = bandits[j].pull()
            bandits[j].update(x)
            data.append(x)
        cumul_average = np.cumsum(data)/(np.arange(N)+1)
        return cumul_average


# =========== main=========
GreedyBandit = eGreedyBandit(0, 0)
results = GreedyBandit.run(0.9, 0.6, 0.3)
plt.plot(range(10000), results)
plt.show()
print(results[-1])
