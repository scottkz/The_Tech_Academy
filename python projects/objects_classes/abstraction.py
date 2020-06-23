# The Tech Academy - Software Developer BootCamp
#
# Python Version: 3.8.3
#
# Author: Scott Katzelnick
#
# Purpose:
#
# ABSTRACTION ASSIGNMENT
# Create a class that utilizes the concept of abstraction.
#
# 1. Your class should contain at least one abstract method and one regular method.
#
# 2. Create a child class that defines the implementation of its parents abstract method.
#
# 3. Create an object that utilizes both the parent and child methods.
#
# 4. Upload code to GitHub for review

# Import abstraction modules
from abc import ABC, abstractmethod


# Parent class
class Totals:
    def total(self, subtotal):
        self.stotal = subtotal
        self.stotal = 8 + 22 + 7 + 5
        print("\nYour subtotal is ${}.".format(self.stotal))

    @abstractmethod
    def tip_total(self, subtotal):
        pass


# Child class w/ abstraction definition
class Tips(Totals):
    def tip_total(self, subtotal):
        tipTotal = subtotal * .2
        print("\nTip due: ${}".format(tipTotal))
        print("\nYour total bill comes to: ${}".format(subtotal + tipTotal))


if __name__ == "__main__":
    totalBill = Tips()
    totalBill.total(42)
    totalBill.tip_total(42)

