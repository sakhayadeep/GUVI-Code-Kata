class Character:
    def __init__(self):
        self.char = 'a'
        
    def set_char(self, char):
        char = list(char)[0]
        if(char.isalpha()):
            self.char = char
        else:
            raise ValueError("Expected a alphabet")

    def check_char(self):
        vowels = "aeiou"
        if(self.char.lower() in vowels):
            return "Vowel"
        else:
            return "Consonant"

def main():
    my_char = Character()

    try:
        my_char.set_char(input())
        print(my_char.check_char())
    except:
        print("Invalid Input")

if __name__ == "__main__":
    main()