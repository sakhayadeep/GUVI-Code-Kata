class Number:
    def __init__(self, num = 0):
        if((type(num) == type(int()) or type(num) == type(float())) and num >= 0):
            self.num = num
        else:
            raise ValueError("Expected a int, {} given.".format(type(num)))

    def set_number(self, num = 0):
        if((type(num) == type(int()) or type(num) == type(float())) and num >= 0):
            self.num = num
        else:
            raise ValueError("Expected a int, {} given.".format(type(num)))

    def check_number(self):
        if(self.num % 2 == 0):
            return "Even"
        else:
            return "Odd"

def main():
    my_num = Number()

    try:
        my_num.set_number(int(input()))
        print(my_num.check_number())
    except:
        print("Invalid Input")

if __name__ == "__main__":
    main()