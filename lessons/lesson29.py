class SingLeTone:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __str__(self):
        return f"экземпляр класса {id(self)}"
    
    
if __name__ == "__main__":
    first = SingLeTone()
    second = SingLeTone()
    print(first)
    print(second)

