import logging
logging.basicConfig(
    filename='app.log',
    filemode='w',  # 'w' to overwrite the log file, 'a' to append
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'

)