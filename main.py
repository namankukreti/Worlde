import pandas as pd
import numpy as nmp

print(pd.__version__)
print("Hello World")
wordbank = pd.read_csv("words.txt", header = None).squeeze("columns")
class Wordle:
    def comparitor(self, inputword: str, word: str) -> str:
            tryagain = []
            for i in range(len(inputword)):
                if inputword[i] != word[i]:
                    tryagain.append("*")
                else:
                    tryagain.append(inputword[i])
            return "".join(tryagain)
    def genword(self) -> bool:
        return wordbank.sample().item()
    def play(self):  
        word = self.genword()
        for i in range(5):
            inputword = input("Guess:\n")
            if inputword == word: 
                print(f"The word was: {word}, congrats!") 
                return True
            else:
                print(self.comparitor(inputword, word))
        return False
def main():
    game = Wordle()
    game.play()

if __name__ == "__main__":
    main()
    
        
    
