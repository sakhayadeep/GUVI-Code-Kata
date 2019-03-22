class Number:
    def __init__(self, num = 0):
        if(type(num) == type(int())):
            self.num = num
        else:
            raise ValueError("Expected a int, {} given.".format(type(num)))

    def set_number(self, num = 0):
        if(type(num) == type(int())):
            self.num = num
        else:
            raise ValueError("Expected a int, {} given.".format(type(num)))

    def check_number(self):
        if(self.num > 0):
            return "Positive"
        elif(self.num < 0):
            return "Negative"
        else:
            return "Zero"

def main():
    my_num = Number()

    try:
        my_num.set_number(int(input()))
    except:
        print("Invalid Input")

    print(my_num.check_number())

if __name__ == "__main__":
    main()