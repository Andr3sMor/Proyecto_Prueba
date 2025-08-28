import pandas as pd
from utils import esPrimo

def f(event, context):
    print("Hola desde lambda con zappa")
    print(esPrimo(5))
    return {}
    