"""Kleine Beispielanwendung für die CI/CD-Übung."""

import argparse


def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    args = parser.parse_args()
    print(add(args.a, args.b))
