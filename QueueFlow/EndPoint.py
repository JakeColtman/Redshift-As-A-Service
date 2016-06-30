from time import sleep
from random import randint, choice
from string import ascii_letters


def random_delay_messages(queue):
    while True:
        sleep(randint(1, 10))
        queue.put(choice(ascii_letters))


