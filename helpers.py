"""

        This file contains only helper functions that are not
        a fundamental part of the algotithm.

"""


# Given a dictionary and a pair of values, creates the key-value pair in the dictionary.
# Does not return, because in this case variables are passed by reference

def createDict(dic,a):
	if isinstance(a[1], str):
		a[1] = (a[1].strip("\n")).split(",")
        dic[a[0]] = a[1]
