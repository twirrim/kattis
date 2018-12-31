""" Solve the Two Stones game on Kattis """
import sys

def main():
    """ Play the Game """
    stones = int(sys.stdin.read().strip())
    if stones % 2 == 0:
        print("Bob")
    else:
        print("Alice")


if __name__ == "__main__":
    main()
