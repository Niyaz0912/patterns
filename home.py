class Builder:
    def build_floor(self):
        pass

    def build_walls(self):
        pass

    def paint_walls(self):
        pass

    def get_result(self):
        pass


class TilerBuilder(Builder):
    def __init__(self):
        self.house = House()

    def build_floor(self):
        self.house.floor = "Подготовка пола, укладка плитки"

    def get_result(self):
        return self.house


class FinisherBuilder(Builder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "Нанесение шпаклевки, оштукатуривание стен"

    def get_result(self):
        return self.house


class PainterBuilder(Builder):
    def __init__(self):
        self.house = House()

    def paint_walls(self):
        self.house.walls = "Грунтование стен, окрашивание стен"

    def get_result(self):
        return self.house


class Foreman:
    def construct_floor(self, builder):
        builder.build_floor()

    def construct_walls(self, builder):
        builder.build_walls()

    def paint_walls(self, builder):
        builder.paint_walls()

    def construct_house(self, builder):
        builder.build_floor()
        builder.build_walls()
        builder.paint_walls()
        return builder.get_result()


class House:
    def __init__(self):
        self.floor = None
        self.walls = None

    def __str__(self):
        return f"Пол: {self.floor}, Стены: {self.walls}"


if __name__ == "__main__":
    foreman = Foreman()

    tiler_builder = TilerBuilder()
    tiler_house = foreman.construct_house(tiler_builder)
    print("Работа плиточника:", tiler_house)

    finisher_builder = FinisherBuilder()
    finisher_house = foreman.construct_house(finisher_builder)
    print("Работа отделочника:", finisher_house)

    painter_builder = PainterBuilder()
    painter_house = foreman.construct_house(painter_builder)
    print("Работа маляра:", painter_house)
