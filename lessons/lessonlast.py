from abc import ABC, abstractmethod


class YechAnalysContext:
    def __init__(self, strategy: "AbstractStrategy") -> None:
        self.strategy = strategy

    def set_strategy(self, strategy: "AbstractStrategy") -> None:
        self.strategy = strategy

    def execute_strategy(self) -> str:
        self.strategy.execute()

class AbstractStrategy(ABC):
    
    @abstractmethod
    def execute(self, message: str) -> str:
        pass

class StrategyAnalysOne(AbstractStrategy):
    def execute(self, message: str) -> str:
        return f"анализ 1 {message}"
    
class StrategyAnalysTwo(AbstractStrategy):
    def execute(self, message: str) -> str:
        return f"анализ 2 {message}"
    
user_choise = input("Выберите анализ (1 или 2): ")

try:
    int_choise = int(user_choise)

except ValueError:
    print("Вы ввели не число")
    exit(1)

if int_choise == 1:
    strategy = StrategyAnalysOne()

elif int_choise == 2:
    strategy = StrategyAnalysTwo()

context = YechAnalysContext(strategy)
result = context.execute_strategy("hello")

print(result)

