from urllib import response
import pandas as pd

def num_change(number):
    if type(number) == float:

        new_column = int(number)

    else:
        new_column = 10

    return new_column

def need_help(y):
    if y == 'Y':
        response = "Coming for you!"
    else:
        response = 'Good luck!'

    return response
