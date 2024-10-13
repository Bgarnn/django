import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
    def __init__(self):
        self.served_count = 0
        self.broken = False

    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__(price = 0.90, name = "empty cup")
        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.broken = False
        self.served_count = 0

    def serve(self, beverage_class):
        if self.broken:
            raise CoffeeMachine.BrokenMachineException()
        if self.served_count >= 10:
            self.broken = True
            raise CoffeeMachine.BrokenMachineException()
        self.served_count += 1
        return random.choice([beverage_class(), CoffeeMachine.EmptyCup()]) #random between serve drink and empty cup

if __name__ == "__main__":
    machine = CoffeeMachine()
    beverages = [Coffee, Tea, Chocolate, Cappuccino]

    try:
        for x in range(2):  # test 12 serves 2 times -> first time: the machine will break after 10, second time: dont happen because already broken
            for x in range(12):
                beverage = machine.serve(random.choice(beverages)) #random in beverage_class
                print(beverage)
                print()
    except CoffeeMachine.BrokenMachineException as e:
        print(e)
        machine.repair()
        print("Repair the machine success...\n")
        try:
            for x in range(12): #test that machine can run after repair, and will break after 10
                    beverage = machine.serve(random.choice(beverages)) 
                    print(beverage)
                    print()
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
