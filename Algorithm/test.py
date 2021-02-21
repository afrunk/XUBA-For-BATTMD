# encoding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from typing import Iterable
from tqdm import tqdm
# 相邻离子的距离
R = 0.001


def alpha(length):
    """length为晶体长度，取值必须大于2R，即长度范围内至少包含一个晶胞"""
    num = int(length / (2 * R))
    center = np.array([num, num])

    energy = 0
    for y in range(2*num+1):
        for x in range(2*num+1):
            if x == num and y == num:
                continue
            particles = np.array([x, y])
            coop_diff = np.abs(particles - center)
            distance = np.sqrt(np.sum(coop_diff**2))
            sign = 1 if (np.sum(coop_diff) % 2 == 1) else -1
            energy += sign / distance
    return energy


def image(lengths: Iterable, zero: bool = False):
    if zero:
        l_2r = [0] + [ll/(2*R) for ll in lengths]
        alphas = [0] + [alpha(ll) for ll in lengths]
        plt.plot(l_2r, alphas, color='red', linewidth=1)
        plt.yticks(np.arange(start=0, stop=1.8, step=0.2))
        plt.xticks(np.arange(start=0, stop=60, step=10))
        plt.xlabel('L/2R')
        plt.ylabel('Madelung constant')
        plt.show()
    else:
        l_2r = []
        alphas = []
        for ll in tqdm(lengths):
            l_2r.append(ll/(2*R))
            alphas.append(alpha(ll))
        plt.plot(l_2r, alphas, color='red', linewidth=1)
        plt.yticks(np.arange(start=1.61475, stop=1.61490, step=0.00005))
        plt.xticks(np.arange(start=l_2r[0], stop=l_2r[-1] + 10, step=10))
        plt.xlabel('L/2R')
        plt.ylabel('Madelung constant')
        plt.show()


if __name__ == '__main__':
    image(np.arange(start=2*R, stop=50.5*2*R, step=2*R), True)
    image(np.arange(start=950*2*R, stop=1000.5*2*R, step=2*2*R), False)
