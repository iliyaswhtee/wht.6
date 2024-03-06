import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000) 
    return math.sqrt(number)

number_to_sqrt = int(input("квадрат сан енгізіңіз: "))
delay_in_ms = int(input("миллисекунда енгізіңіз: "))
result = delayed_sqrt(number_to_sqrt, delay_in_ms)
print(f"Түбір астынан өткен сан {number_to_sqrt} осынша {delay_in_ms} уақыттан соң: {result}")