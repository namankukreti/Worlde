import pandas as pd
import numpy as nmp

print(pd.__version__)
print("Hello World")
wordbank = pd.read_csv("words.txt", header = None).squeeze("columns")
class Wordle:
    def comparitor(self, inputword: str, word: str) -> str:
            tryagain = []
            window = set()
            for i in word:
                window.add(i)
            for i in range(len(inputword)):
                if inputword[i] != word[i]:
                    if inputword[i] in window:
                        tryagain.append("^")
                    else:
                        tryagain.append("*")
                else:
                    tryagain.append(inputword[i])    
            return "".join(tryagain)
    def genword(self) -> str:
        return wordbank.sample().item()
    def play(self):  
        word = self.genword()
        print("Guess (If you want to quit, press q):")
        for i in range(5):
            inputword = input("").lower()
            if inputword == "q":
                print(f"The word was: {word}, better luck next time!")
                return False
            if inputword == word: 
                print(f"The word was: {word}, congrats!") 
                return True
            else:
                print(f"\033[F\t",self.comparitor(inputword, word))
        print(f"The word was: {word}, better luck next time!")
        return False
def main():
    game = Wordle()
    continueplay = 0 
    while continueplay == 0: 
        game.play()
        continueplay = input("Do you want to keep playing? (Type y for a new input, n to quit)\n")
        if continueplay == "y":
            continueplay = 0
        elif continueplay == "n":
            continueplay = 1            
if __name__ == "__main__":
    main()
    
        
    
