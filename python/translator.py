import sys

letters = {"a":"o.....", "b": "o.o...", "c":"oo....", "d":"oo.o..", "e":"o..o..", "f":"ooo...",
                "g": "oooo..", "h":"o.oo..","i":".oo...", "j":".ooo..", "k":"o...o.", "l":"o.o.o.",
                "m":"oo..o.","n":"oo.oo.", "o":"o..oo.", "p":"ooo.o.", "q":"ooooo.", "r":"o.ooo.",
                "s":".oo.o.", "t":".oooo.", "u":"o...oo", "v":"o.o.oo", "w":".ooo.o", "x":"oo..oo",
                "y":"oo.ooo", "z":"o..oooo"}

follows = {"CAPITAL":".....o", "DECIMAL":".o...o", "NUMBER":".o.ooo"}

special = {".":"..oo.o", ",":"..o...", "?":"..o.oo", "!":"..ooo.", ":":"..oo..", ";":"..o.o.",
                "-":"....oo", "/":".o..o.", "<":".oo..o", ">":"o..oo.", "(":"o.o..o", ")":".o.oo.", " ": "......"}

numbers ={"1":"o.....", "2": "o.o...", "3":"oo....", "4":"oo.o..", "5":"o..o..", "6":"ooo...",
                "7":"oooo..", "8":"o.oo..", "9":".oo...", "0":".ooo.."}
def isBraille():
    if all(c in 'o. ' for c in word):
        braille_to_english()
    elif any(c.isalpha() or c.isspace() or c.isdigit() for c in word):
        english_to_braille()
        
        

def english_to_braille():
    dictionary = letters
    current_letter = 0
    length = len(word)
    
    while length > 0:
        if word[current_letter].isupper():
            print(follows["CAPITAL"], end="")
        if word[current_letter] in numbers and (word[current_letter-1] not in numbers or current_letter==0) :
            print(follows["NUMBER"],end="")
            dictionary = numbers
        if dictionary == numbers and word[current_letter] == " ":
            dictionary = letters
        if word[current_letter].lower() in dictionary:
            print(dictionary[word[current_letter].lower()], end="")
        elif word[current_letter] in special:
            print(special[word[current_letter]], end="")
            
        current_letter+=1
        length-=1
          
def braille_to_english():
    dictionary = letters
    length = len(word)
    current= 0
    capitalize = False
    
    while current < length-1:
        theWord = word[current: current+6]
        character = next((key for key, value in follows.items() if value == theWord), None)  
        if character == "CAPITAL":
           capitalize = True
        elif character == "NUMBER":
           dictionary=numbers
        elif dictionary == numbers and theWord == special[" "]:
            dictionary = letters
        else:
            toPrint = next((key for key, value in dictionary.items() if value == theWord), None)
            if toPrint == None:
                toPrint = next((key for key, value in special.items() if value == theWord), None)
            if capitalize == True:
                print(toPrint.upper(),end="")
                capitalize = False
            else:
                print(toPrint,end="")
                capitalize = False
        current+=6

if __name__ == "__main__":
    word=""
    if len(sys.argv)==2:
        word = sys.argv[1]
    else:
        word = " ".join(sys.argv[1:])
    isBraille()
