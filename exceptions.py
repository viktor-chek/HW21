class BaseError(Exception):
    message = "Неожиданная ошибка"


class NotEnoughSpace(BaseError):
    message = "Недостаточно места на складе"


class NotEnoughProduct(BaseError):
    message = "Недостаточно товара в наличии"


class TooManyDifferentProducts(BaseError):
    message = "Слишком много разных товаров"


class InvalidRequest(BaseError):
    message = "Неправильный запрос. Попробуйте снова"


class InvalidStoreName(BaseError):
    message = "Склад не найден. Или введён не корректно"
