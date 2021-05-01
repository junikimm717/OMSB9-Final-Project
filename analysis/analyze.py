#!/usr/bin/env python3

import process as p
import scipy.stats as s
import numpy as np
import matplotlib.pyplot as plt
from sys import argv

def test_1(plot=False) -> None:
    x = np.array([x.correct for x in p.results])
    y = np.array([abs(x.response - x.correct) for x in p.results])
    regress = s.linregress(x, y)

    if plot:
        slope, intercept, rvalue, pvalue, stderr = regress
        y_p = intercept + slope*x
        plt.plot(x, y_p, color='green')
        plt.title("Test 1")
        plt.xlabel('Number displayed on screen')
        plt.ylabel('Deviation from answer')
        plt.scatter(x, y)
        plt.show()

    else:
        print("\n\nresults 1...")
        # anything relating to deviations by number.
        print(regress)


def test_2(plot=False) -> None:
    if plot:
        def freq(lt: list, el: object) -> int:
            res = 0
            for x in lt:
                if el == x:
                    res += 1
            return res

        plt.title("Frequencies of margin of error across reaction times.")
        data = [[abs(x.response - x.correct) for x in p.results if x.time == i ]
                for i in [250, 500, 750, 1000]]

        colors = ['blue', 'green', 'red', 'yellow']
        for i in range(len(data)):
            lt = data[i]
            time = 250*(i+1)
            f = [freq(lt, j) for j in range(5)]
            plt.scatter(range(5), f, color=colors[i], label=f'Frequencies with {time}ms')
        plt.legend(loc='upper right')
        plt.show()
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



def main():
    if len(argv) == 1:
        print("not enough args.")
        print("Format is (function to test) (boolean for whether or not you want a plot.)")
        exit(1)
    functions = [None, test_1, test_2, test_3, test_4]
    try:
        if len(argv) == 3:
            functions[int(argv[1])](bool(argv[2]))
        elif len(argv) == 2:
            functions[int(argv[1])]()
    except Exception:
        print("Error. Format is (function to test) (boolean for whether or not you want a plot.)")


if __name__ == "__main__":
    main()