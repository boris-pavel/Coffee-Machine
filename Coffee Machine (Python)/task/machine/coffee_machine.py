class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def subtract_water(self, water):
        self.water -= water

    def subtract_milk(self, milk):
        self.milk -= milk

    def subtract_beans(self, beans):
        self.beans -= beans

    def subtract_cups(self, cups):
        self.cups -= cups

    def subtract_money(self, money):
        self.money -= money

    def add_water(self, water):
        self.water += water

    def add_milk(self, milk):
        self.milk += milk

    def add_beans(self, beans):
        self.beans += beans

    def add_cups(self, cups):
        self.cups += cups

    def add_money(self, money):
        self.money += money

    def get_supplies(self):
        return f"""The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.beans} g of coffee beans
{self.cups} disposable cups
${self.money} of money\n"""

    def fill(self, water, milk, beans, cups):
        self.add_water(water)
        self.add_milk(milk)
        self.add_beans(beans)
        self.add_cups(cups)

    def take_money(self):
        print(f'I gave you ${self.money}')
        self.subtract_money(self.money)

    def check_resources(self, coffee):
        lst = []
        if self.water < coffee.water:
            lst.append('water')
        if self.milk < coffee.milk:
            lst.append('milk')
        if self.beans < coffee.beans:
            lst.append('beans')
        return lst


class Coffee:
    def __init__(self, water, milk, beans, cost):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cost = cost


class Espresso(Coffee):
    def __init__(self):
        super().__init__(250, 0, 16, 4)


class Latte(Coffee):
    def __init__(self):
        super().__init__(350, 75, 20, 7)


class Cappuccino(Coffee):
    def __init__(self):
        super().__init__(200, 100, 12, 6)


def main():
    machine = CoffeeMachine(400, 540, 120, 9, 550)
    while True:
        inp = input('Write action (buy, fill, take, remaining, exit):\n')
        print('')
        match inp:
            case 'buy':
                coffe_type = input(
                    "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
                coffee = Coffee(0, 0, 0, 0)
                match coffe_type:
                    case '1':
                        coffee = Espresso()
                    case '2':
                        coffee = Latte()
                    case '3':
                        coffee = Cappuccino()
                    case 'back':
                        continue
                empty_resources = machine.check_resources(coffee)
                if not empty_resources:
                    print('I have enough resources, making you a coffee!\n')
                    machine.subtract_water(coffee.water)
                    machine.subtract_milk(coffee.milk)
                    machine.subtract_beans(coffee.beans)
                    machine.add_money(coffee.cost)
                    machine.subtract_cups(1)
                else:
                    print(f"Sorry, not enough {', '.join(empty_resources)}!\n")

            case 'fill':
                water = int(input('Write how many ml of water you want to add:\n'))
                milk = int(input('Write how many ml of milk you want to add:\n'))
                beans = int(input('Write how many grams of coffee beans you want to add:\n'))
                cups = int(input('Write how many disposable cups you want to add:\n'))
                print('')
                machine.fill(water, milk, beans, cups)
            case 'take':
                machine.take_money()
            case 'remaining':
                print(machine.get_supplies())
            case 'exit':
                break


main()
