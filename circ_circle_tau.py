#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Sep 28, 2023
# This program asks the user for the radius of
# a circle in mm. It then calculates and displays
# the circumference using tau.

import constants


def main():
    # get the radius from the user
    print("This program will calculate the circumference of a circle")
    print("With your radius.")
    radius = float(input("Enter the radius of the circle (cm): "))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("")
    print("The circumference of your circle is = {:.2f} cm".format(circumference))


if __name__ == "__main__":
    main()
