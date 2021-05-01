#!/usr/bin/env python3

from dataclasses import dataclass
import os


@dataclass(order=True)
class Result:
    angle: int
    time: int
    response: int
    correct: int
    name: str


def parse(line: str) -> Result:
    line = line.split()
    line = [line[2 * i + 1] for i in range(5)]
    return Result(time=int(line[0]), name=line[1], response=int(line[2]),
                  correct=int(line[3]), angle=int(line[4]))


class Parser:
    lines: list

    def __init__(self, name):
        self.lines = []
        try:
            with open(name, "r") as r:
                self.lines = r.read().splitlines()
        except FileNotFoundError:
            pass

    def parse(self):
        return [parse(line) for line in self.lines]


files = os.listdir("../data")
files.remove("README.md")
files = [os.path.join("../data", x) for x in files]
results: list[Result] = []
for f in files:
    results += Parser(f).parse()
