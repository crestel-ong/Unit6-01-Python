#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Oct 2021
# this program uses arrays(for this one it's actually a list)

import random


def main():
    # this function uses an array

    all_numbers_list = []
    all_numbers_added = 0

    # input
    for loop_counter in range(0, 10):
        single_number = random.randint(1, 100)
        all_numbers_list.append(single_number)
        all_numbers_added = all_numbers_added + single_number
        print("The random number is: {0}".format(single_number))

    average = all_numbers_added / len(all_numbers_list)
    average = round(average, 2)
    print("")
    print("The average is {0}".format(average))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
