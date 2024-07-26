from abc import ABC, abstractmethod


class Pasta(ABC):
    def __init__(self):
        self.type = None
        self.sauce = None
        self.filling = None
        self.additions = []

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_sauce(self):
        pass

    @abstractmethod
    def get_filling(self):
        pass

    @abstractmethod
    def get_additions(self):
        pass


# Конкретные классы пасты
class Spaghetti(Pasta):
    def __init__(self):
        super().__init__()
        self.type = "Спагетти"
        self.sauce = "Томатный соус"
        self.filling = "Мясные фрикадельки"
        self.additions = ["Пармезан", "Базилик"]

    def get_type(self):
        return self.type

    def get_sauce(self):
        return self.sauce

    def get_filling(self):
        return self.filling

    def get_additions(self):
        return self.additions


class Fettuccine(Pasta):
    def __init__(self):
        super().__init__()
        self.type = "Феттучини"
        self.sauce = "Альфредо"
        self.filling = "Курица"
        self.additions = ["Петрушка", "Чеснок"]

    def get_type(self):
        return self.type

    def get_sauce(self):
        return self.sauce

    def get_filling(self):
        return self.filling

    def get_additions(self):
        return self.additions


class Penne(Pasta):
    def __init__(self):
        super().__init__()
        self.type = "Пенне"
        self.sauce = "Песто"
        self.filling = "Овощи"
        self.additions = ["Кедровые орехи", "Пармезан"]

    def get_type(self):
        return self.type

    def get_sauce(self):
        return self.sauce

    def get_filling(self):
        return self.filling

    def get_additions(self):
        return self.additions


# Фабрика пасты
class PastaFactory:
    @staticmethod
    def create_pasta(pasta_type):
        if pasta_type == "спагетти":
            return Spaghetti()
        elif pasta_type == "феттучини":
            return Fettuccine()
        elif pasta_type == "пенне":
            return Penne()
        else:
            raise ValueError("Неизвестный тип пасты")


# Функция для создания пасты на основе пользовательского ввода
def create_custom_pasta():
    print("Доступные типы пасты: спагетти, феттучини, пенне")
    pasta_type = input("Выберите тип пасты: ").strip().lower()

    try:
        pasta = PastaFactory.create_pasta(pasta_type)
    except ValueError as e:
        print(e)
        return

    sauce = input("Введите соус (по умолчанию: {}): ".format(pasta.get_sauce())) or pasta.get_sauce()
    filling = input("Введите начинку (по умолчанию: {}): ".format(pasta.get_filling())) or pasta.get_filling()
    additions = input(
        "Введите добавки через запятую (по умолчанию: {}): ".format(", ".join(pasta.get_additions()))) or ", ".join(
        pasta.get_additions())

    pasta.sauce = sauce
    pasta.filling = filling
    pasta.additions = additions.split(", ")

    print("\nВаше блюдо готово!")
    print(f"Тип пасты: {pasta.get_type()}")
    print(f"Соус: {pasta.get_sauce()}")
    print(f"Начинка: {pasta.get_filling()}")
    print(f"Добавки: {', '.join(pasta.get_additions())}")


if __name__ == "__main__":
    create_custom_pasta()