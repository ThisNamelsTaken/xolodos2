from abc import ABC, abstractmethod

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
    def open(self):
        self.is_open = True
        print("Холодильник открыт.")
    def close(self):
        self.is_open = False
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
    def put(self, product):
        self.products.append(product)
        print(f"Положили '{product}' в холодильник.")
    def get(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Достали '{product}' из холодильника.")
            return product
        else:
            print(f"В холодильнике нет '{product}'.")
            return None
    def info(self):
        if self.products:
            print(f"В холодильнике: {', '.join(self.products)}")
        else:
            print("Холодильник пуст.")

class Xolodos:
    def __init__(self):  
        self.door = ColdDoor()
        self.storage = ColdProduct()
    def open(self):
        self.door.open()
    def close(self):
        self.door.close()
    def put(self, product):
        self.storage.put(product)
    def get(self, product):
        return self.storage.get(product)
    def info(self):
        self.storage.info()

if __name__ == "__main__": 
    my_xolodos = Xolodos()
    my_xolodos.open()
    my_xolodos.put("Яблоко")
    my_xolodos.info()
    my_xolodos.get("Яблоко")
    my_xolodos.info()
    my_xolodos.close()
    my_xolodos.open()

