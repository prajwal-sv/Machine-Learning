from logger import logging
# Example logging messages

def add(x, y):
    logging.debug(f"Adding {x} and {y}")
    return x + y    
logging.info("Starting the addition operation")
add(5, 3)