#!/usr/bin/env python3

import process as p
import scipy.stats as s
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
import math


def test_1(plot=False) -> None:
    x = np.array([x.correct for x in p.results])
    y = np.array([(abs(x.response - x.correct)) for x in p.results])
    means = np.array([np.std([
        (x.response - x.correct) for x in p.results if x.correct == i
    ]) for i in range(1, 10)])
    regress = s.linregress(x, y)

    if plot:
        slope, intercept, rvalue, pvalue, stderr = regress
        y_p = intercept + slope * x
        plt.plot(x, y_p, color='green')
        plt.title("Deviations from Answer based on number displayed")
        plt.xlabel('Number Displayed on Screen')
        plt.ylabel('Standard Deviation Of Responses')
        #plt.scatter(x, y)
        plt.scatter(range(1, 10), means, color='red')
        plt.savefig('../paper/images/regression.jpg')
        #plt.show()

    else:
        print("\n\nresults 1...")
        print(regress)
        print(s.spearmanr(range(1, 10), means))


def test_2(plot=False) -> None:
    if plot:
        def freq(ltd: list, el: object) -> int:
            res = 0
            for x in ltd:
                if el == x:
                    res += 1
            return res

        plt.title("Frequencies of Margin of Error Across Flash Time")
        data = [[abs(x.response - x.correct) for x in p.results if x.time == i]
                for i in [250, 500, 750, 1000]]

        colors = ['blue', 'green', 'red', 'yellow']
        for i in range(len(data)):
            lt = data[i]
            time = 250 * (i + 1)
            f = [freq(lt, j) for j in range(5)]
            plt.scatter(range(5), f, color=colors[i], label=f'{time}ms')

        plt.xlabel("Amount missed(|correct - answered|)")
        plt.ylabel("Frequency")
        plt.legend(loc='upper right')
        plt.savefig('../paper/images/reaction.jpg')
        #plt.show()
    else:
        print("\n\nresults 2...")
        deviations = [abs(x.response - x.correct) for x in p.results]
        print(s.spearmanr([x.time for x in p.results], deviations))


def test_3() -> None:
    print("\n\nresults 3...")
    deviations = [[abs(x.response - x.correct) for x in p.results if x.angle == i]
                  for i in [0, 30, 60]]
    print("\nANOVA Test for differences in deviations for peripheral vision")
    print(s.f_oneway(deviations[0], deviations[1], deviations[2]))


def test_4() -> None:
    print("\n\nresults 4...")
    print("\nT-Test for differences in deviations for peripheral vision")
    deviations = [[abs(x.response - x.correct) for x in p.results if x.angle == i]
                  for i in [30, 60]]
    print(s.ttest_ind(deviations[0], deviations[1], alternative='less', equal_var=False))


def test_5(plot=False) -> None:
    if plot:
        def freq(ltd: list, el: object) -> int:
            res = 0
            for x in ltd:
                if el == x:
                    res += 1
            return res

        plt.title("Frequencies of Margin of Error Across Peripheral Vision Angle")
        data = [[abs(x.response - x.correct) for x in p.results if x.angle == i]
                for i in [0, 30, 60]]

        colors = ['blue', 'green', 'red', 'yellow']
        labels = ['central vision', 'near peripheral vision', 'far peripheral vision']
        for i in range(len(data)):
            lt = data[i]
            angle = 30*i
            f = [freq(lt, j) for j in range(5)]
            plt.scatter(range(5), f, color=colors[i], label=f'{angle} degrees ({labels[i]})')

        plt.xlabel("Amount Missed (|correct - answered|)")
        plt.ylabel("Frequency")
        plt.legend(loc='upper right')
        plt.savefig('../paper/images/angle.jpg')
        plt.show()

    else:
        pass

def main():
    if len(argv) == 1:
        print("not enough args.")
        print("Format is (function to test) (boolean for whether or not you want a plot.)")
        exit(1)
    functions = [None, test_1, test_2, test_3, test_4, test_5]

    if len(argv) == 3:
        functions[int(argv[1])](bool(argv[2]))
    elif len(argv) == 2:
        functions[int(argv[1])]()


if __name__ == "__main__":
    main()
