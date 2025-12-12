import logging

def log():
    logging.basicConfig(filename="..\\logs\\logfile.log",format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",level=logging.INFO)
    logger = logging.getLogger()
    return logger