class Duck:
    def __init__(self, name: str = "Дональд") -> None:
        self.name: str = name
        self.status = "alive"

    def __str__(self) -> str:
        return f"Утка {self.name} is {self.status}"
    def __call__(self, cooking_time: int) -> None:
        self.status: str = cooking_time
        print(f"Утка {self.name} is {self.status} after {cooking_time} minutes")
        

    def __len__(self) -> int:
        rounded_weight = round(self.weight, 1)
        return len (rounded_weight)
    
    def __bool__(self) -> bool:
        return self.status != self._class__.default_status
    
duck1 = Duck("Дональд", 3.5)
duck2 = Duck("Майк", 4.5)

ducks: list[Duck] = [duck1, duck2]

[print(duck) for duck in ducks]
        