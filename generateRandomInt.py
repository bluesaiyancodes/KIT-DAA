# generate random integer values
from random import seed
from random import randint
import sys

# Save a reference to the original standard output
original_stdout = sys.stdout  

# seed random number generator
seed(1)

# generate some integers and save to file
with open('small_10.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created
    for _ in range(10):
        value = randint(0, 10)        
        print(value, end=" ")
sys.stdout = original_stdout # Reset the standard output to its original value        