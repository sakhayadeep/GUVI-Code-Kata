class Number:
    def __init__(self):
        self.num = 0
        
    def set_number(self, num = 0):
        if(type(num) == type(int()) or type(num) == type(float())):
            self.num = num
        else:
            raise ValueError("Expected a number, {} given.".format(type(num)))

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
        print(my_num.check_number())
    except:
        print("Invalid Input")

if __name__ == "__main__":
    main()