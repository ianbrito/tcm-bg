import logging
import sys
from datetime import datetime
from progress.bar import Bar

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y-%H-%M")


def setting_logs():
    logger = logging.getLogger(__name__)
    f_handler = logging.FileHandler(f"logs/analyzer-{dt_string}.log")
    logger.addHandler(f_handler)
    return logger


def log(message):
    logger = setting_logs()
    logger.error(message)


def check_row(row: str, line: int):
    size = len(row)
    registro = row[0:3]
    sequencial = row[3:13]

    if size < 1201:
        log(f"Error: linha incompleta L: {line} T: {size} #R: {registro} S:{sequencial}\n{row}")
    elif ord(row[size - 1]) != 10:
        log(f"Error: fim da linha L: {line} T: {size} #R: {registro} S:{sequencial}")


def analyzer(path):
    with open(path, encoding='unicode_escape') as f:
        total_lines = len(f.readlines())

    bar = Bar('Processando', max=total_lines)

    with open(path, encoding='unicode_escape') as f:
        line = 1
        for row in f:
            check_row(row, line)
            line = line + 1
            bar.next()
    bar.finish()


def main():
    try:
        # Windows-1252
        path = sys.argv[1]
        analyzer(path)
    except Exception as e:
        print(e)
    finally:
        pass


if __name__ == '__main__':
    main()
