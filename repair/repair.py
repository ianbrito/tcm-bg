import logging
from datetime import datetime
import sys

def setting_logs():
    now = datetime.now()
    logger = logging.getLogger(__name__)
    dt_string = now.strftime("%d-%m-%Y-%H-%M")
    f_handler = logging.FileHandler(f"logs/repair-{dt_string}.log")
    logger.addHandler(f_handler)

def main():
    setting_logs()
    path = sys.argv[1]

    

if __name__ == '__main__':
    main()