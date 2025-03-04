from enums import Color, Material, ClothingStyle, Size, Category
class Item:
    def __init__(self, item_id: int, discription: str, color: Color, material: Material, name: str, category: Category, price: float):
        self.__item_id = item_id
        self.__name = name
        self.__discription = discription
        self.__color = color
        self.__material = material
        self.__category = category
        self.__price = price


    def get_item_id(self) -> int:
        return self.__item_id

    def get_discription(self) -> str:
        return self.__discription

    def get_material(self) -> Material:
        return self.__material

    def get_color(self) -> Color:
        return self.__color

    def get_name(self) -> str:
        return self.__name

    def get_category(self) -> Category:
        return self.__category

    def get_price(self) -> float:
        return self.__price

class ClothingItem(Item):
    def __init__(self, item_id: int, discription: str, color: Color, material: Material, name: str, category: Category, price: float,
                 style: ClothingStyle, size: Size):
        super().__init__(item_id, discription, color, material, name, category, price)
        self.__style = style
        self.__size = size

    def get_style(self) -> ClothingStyle:
        return self.__style

    def get_size(self) -> Size:
        return self.__size

    # Переопределение метода
    def get_category(self) -> str:
        return f"Clothes: {super().get_category()}"

    def get_clothes_category(self) -> Category:
        return super().get_category()