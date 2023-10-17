import logging, os
from pathlib import Path

print(os.path.dirname(os.path.abspath(__file__)))

def getLogger():
    absoluteFilePath = os.path.dirname(os.path.abspath(__file__)) + "/enqi.log"
    print(absoluteFilePath)

    logger = logging.getLogger('enqi')
    hdlr = logging.FileHandler(absoluteFilePath)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)
    FTPADDR = "some ftp address"
    return logger

