from typing import Dict

from app.abstract import AbstractStorage
from app.request import Request
from exceptions import NotEnoughProduct


class Courier:
    """Класс доставки (Курьера)"""
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        if self.__request.departure in storages:
            self.__from = storages[self.__request.departure]

        if self.__request.destination in storages:
            self.__to = storages[self.__request.destination]

    def move(self):
        try:
            self.__from.remove(name=self.__request.product, amount=self.__request.amount)
            print(f'Курьер забирает {self.__request.amount} {self.__request.product} из {self.__request.departure}а')

            print(f"Курьер везёт {self.__request.amount} {self.__request.product} из {self.__request.departure}а в "
                  f"{self.__request.destination}")

            self.__to.add(name=self.__request.product, amount=self.__request.amount)
            print(f'Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}')
        except NotEnoughProduct as err:
            print(err.message)

    def cancel(self, storages):

        store = storages[self.__request.departure]
        store.add(name=self.__request.product, amount=self.__request.amount)


