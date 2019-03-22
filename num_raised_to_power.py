class Number:
    def __init__(self):
        self.num = 0
        self.power = 1
        
    def set_number(self, num, power = 1):
        if(type(num) == type(power) == type(int())):
            self.num = num
            self.power = power
        else:
            raise ValueError("Expected two numbers")

    def calculate_power(self):
        return self.num ** self.power

def main():
    my_num = Number()
    num, power = map(int, input().split())
    try:
        my_num.set_number(num, power)
        print(my_num.calculate_power())
    except:
        print("Invalid Input")

if __name__ == "__main__":
    main()