import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logging.getLogger('AurithmaticApp')

def add(x, y):
    logging.debug(f'Adding {x} and {y}')
    return x + y    

def subtract(x, y):
    logging.debug(f'Subtracting {y} from {x}')
    return x - y

def multiply(x, y):
    logging.debug(f'Multiplying {x} and {y}')
    return x * y

def divide(x, y):
    if y == 0:
        logging.error('Division by zero attempted')
        raise ValueError("Cannot divide by zero")
    logging.debug(f'Dividing {x} by {y}')
    return x / y

add(5, 3)
subtract(10, 4)
multiply(2, 6)
divide(8, 2)

 