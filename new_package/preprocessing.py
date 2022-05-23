from urllib import response
import pandas as pd

def num_change(number, number2):
    if type(number) == float:

        new_column = int(number + number2)

    else:
        new_column = 10

    return new_column

def need_help(y):
    if y == 'Y':
        response = "Coming for you!"
    else:
        response = 'Good luck!'

    return response
