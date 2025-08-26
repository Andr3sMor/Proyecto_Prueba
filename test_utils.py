from utils import esPrimo

def test_is_prime():
    esPrimo(2) is True
    esPrimo(3) is True
    esPrimo(4) is False
    esPrimo(6) is False
    
