# The Tech Academy - Software Developer BootCamp
#
# Python Version: 3.8.3
#
# Author: Scott Katzelnick
#
# Purpose:
#
# ENCAPSULATION ASSIGNMENT
# Create a class that uses encapsulation.
#
# 1. This class should make use of a private attribute or function.
#
# 2. This class should make use of a protected attribute or function.
#
# 3. Create an object that makes use of protected and private.
#
# 4. Upload code to GitHub for review


# Parent protected class
class TopSecret:
    def __init__(self, code_name, access_level, restrictions, location):
        self._codeName = code_name
        self._access = access_level
        self._restrict = restrictions
        self._local = location

    def set_private(self, code_name, location):
        self.__codeName = code_name
        self.__local = location
        print("\nProject Assignment: {}\nCurrent Location: {}".format(self.__codeName, self.__local))

    def get_protected_info(self):
        print('\nRequired Access Level: {}\nCurrent Restrictions: {}'.format(self._access, self._restrict))


obj = TopSecret("Phoenix", "Level 3", "No Lab, Shadowed", "Fort Meyers")
obj.get_protected_info()
obj.set_private("Blue Book", "Roswell")

print(code_name)  # Will not print as it is private
