

class cold_door:
    
    def __init__(self):
        self.is_open = 0   
    def open(self):
        self.is_open = 1
        print("холодильник открыт.")   
    def close(self):
        self.is_open = 0
        print("холодильник закрыт.")

class cold_product:
    
    def __init__(self):
        self.producti = []   
    def put(self, list_product):
        self.producti.append(list_product)
        print(f"положили '{list_product}' в холодильник.")   
    def get(self, list_product):
        if list_product in self.producti:
            self.producti.remove(list_product)
            print(f"достали '{list_product}' из холодильника.")
            return list_product
        else:
            print(f"в холодильнике нет '{list_product}'.")
            return None   
    def info_holod(self):
        print(f"в холодильнике:", ", ".join(self.producti))

class Xolodos:
        
    def __init__(self):
        self.door = cold_door()
        self.storage = cold_product()   
    def open(self):
        self.door.open()   
    def close(self):
        self.door.close()    
    def put(self, list_product):
        self.storage.put(list_product)   
    def get(self, list_product):
        return self.storage.get(list_product)   
    def info_holod(self):
        self.storage.info_holod()

if __name__ == "__main__":
    my_xolodos = Xolodos()
    
    my_xolodos.open()
    my_xolodos.put("Яблоко")
    my_xolodos.info_holod()
    my_xolodos.get("Яблоко")
    my_xolodos.close()

    my_xolodos.get("Яблоко")
