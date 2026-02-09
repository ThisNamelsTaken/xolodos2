from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

class Door(ABC):
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def close(self):
        pass

class ColdDoor(Door):
    def __init__(self):
        self.is_open = False
        logger.info("Создана дверь холодильника (состояние: закрыта)")
    def open(self):
        self.is_open = True
        logger.info("Дверь холодильника открыта")
        print("Холодильник открыт.")
    def close(self):
        self.is_open = False
        logger.info("Дверь холодильника закрыта")
        print("Холодильник закрыт.")

class Storage(ABC):
    @abstractmethod
    def put(self, product):
        pass
    @abstractmethod
    def get(self, product):
        pass
    @abstractmethod
    def info(self):
        pass

class ColdProduct(Storage):
    def __init__(self):
        self.products = []
        logger.info("Создано хранилище продуктов (холодильник пуст)")
    def put(self, product):
        logger.debug(f"Попытка положить продукт: {product}")
        
        if type(product) != str:
            logger.error(f"Ошибка: '{product}' не является строкой. Можно класть только текстовые названия.")
            print(f"Ошибка: '{product}' не является строкой. Можно класть только текстовые названия.")
            return 
        all_letters = True
        for char in product:
            if not ('A' <= char <= 'Z' or 'a' <= char <= 'z' or 
                    'А' <= char <= 'Я' or 'а' <= char <= 'я'):
                all_letters = False
                break
        if not all_letters:
            logger.error(f"Ошибка: '{product}' содержит цифры или специальные символы. Можно класть только слова из букв.")
            print(f"Ошибка: '{product}' содержит цифры или специальные символы. Можно класть только слова из букв.")
            return
        self.products.append(product)
        logger.info(f"Продукт '{product}' успешно добавлен в холодильник")
        print(f"Положили '{product}' в холодильник.")
    def get(self, product):
        logger.debug(f"Попытка достать продукт: {product}")
        if product in self.products:
            self.products.remove(product)
            logger.info(f"Продукт '{product}' извлечён из холодильника")
            print(f"Достали '{product}' из холодильника.")
            return product
        else:
            logger.warning(f"Продукт '{product}' не найден в холодильнике")
            print(f"В холодильнике нет '{product}'.")
            return None
    def info(self):
        if self.products:
            products_str = ', '.join(self.products)
            logger.info(f"Состояние холодильника: {products_str}")
            print(f"В холодильнике: {products_str}")
        else:
            logger.info("Холодильник пуст")
            print("Холодильник пуст.")

class Xolodos:
    def __init__(self):
        logger.info("Создан экземпляр холодильника Xolodos")
        self.door = ColdDoor()
        self.storage = ColdProduct()
    def open(self):
        logger.info("Вызов метода open() холодильника")
        self.door.open()
    def close(self):
        logger.info("Вызов метода close() холодильника")
        self.door.close()
    def put(self, product):
        logger.info(f"Вызов метода put() с продуктом: {product}")
        self.storage.put(product)
    def get(self, product):
        logger.info(f"Вызов метода get() с продуктом: {product}")
        return self.storage.get(product)
    def info(self):
        logger.info("Вызов метода info() холодильника")
        self.storage.info()

if __name__ == "__main__":
    logger.info("Запуск программы")
    my_xolodos = Xolodos()
    my_xolodos.open()
    my_xolodos.put(123)
    my_xolodos.put("1Яблоко")
    my_xolodos.put("Яблоко")
    my_xolodos.info()
    my_xolodos.get("Яблоко")
    my_xolodos.info()
    my_xolodos.close()
    my_xolodos.open()
    logger.info("Завершение программы")
