from app.courier import Courier
from app.shop import Shop
from app.store import Store
from app.request import Request
from exceptions import InvalidRequest, BaseError, InvalidStoreName, NotEnoughProduct

store = Store(items={
    "печеньки": 25,
    "собачки": 25,
    "елки": 25,
})

shop = Shop(items={
    "печеньки": 2,
    "собачки": 2,
    "елки": 2,
})

storages = {
    "магазин": shop,
    "склад": store,
}


def main():
    print('\nДобрый день\n')

    while True:
        for storage_name in storages:
            print(f"В {storage_name}е хранится:\n {storages[storage_name].get_items()}")

        user_input = input(
            "Введите запрос в формате 'Доставить 3 печеньки из склад в магазин'\n"
            "Введите 'стоп' или 'stop', если хотите закончить:\n"
        )

        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request=user_input, storages=storages)
        except (InvalidRequest, InvalidStoreName) as err:
            print(err.message)
            continue

        courier = Courier(
            request=request,
            storages=storages
        )

        try:
            courier.move()
        except BaseError as err:
            if NotEnoughProduct:
                print(f"{err.message}, курьер вернул товар обратно")
            courier.cancel(storages)


if __name__ == "__main__":
    main()
