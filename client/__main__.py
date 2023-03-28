#!python3.8
import random

from faker import Faker

from .client import Client


def main():
    faker = Faker('zh_CN')

    def rand_name(number):
        for _ in range(number):
            yield faker.name()

    client_number = random.randint(2, 5)
    client_list = tuple(map(Client, rand_name(client_number)))
    # print(client_list)
    N = 10
    for _ in range(N):
        a, b = random.sample(client_list, k=2)
        a.send(b, faker.paragraph())


if __name__ == '__main__':
    main()
