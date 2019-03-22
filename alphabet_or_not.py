class Character:
    def __init__(self):
        self.char = 'a'
        
    def set_char(self, char):
        char = list(char)[0]
        self.char = char

    def check_char(self):
        if(self.char.isalpha()):
            return "Alphabet"
        else:
            return "No"

def main():
    my_char = Character()

    my_char.set_char(input())
    print(my_char.check_char())
    
if __name__ == "__main__":
    main()