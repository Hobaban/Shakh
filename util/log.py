import logging

log_formatter = logging.Formatter(
    "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s"
)
root_logger = logging.getLogger()

console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
root_logger.addHandler(console_handler)

file_handler = logging.FileHandler(filename="icecream.log", mode="a")
file_handler.setLevel(level=logging.INFO)
file_handler.setFormatter(log_formatter)
root_logger.addHandler(file_handler)
root_logger.setLevel(level=logging.INFO)
