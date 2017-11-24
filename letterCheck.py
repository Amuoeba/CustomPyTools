import pickle

ALPHABET=['a','b','c','č','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','š','t','u','v','z','ž',"x","y","q","w"]
SWITCHDICT={"ó":"o","ò":"o","á":"a","à":"a","â":"a","é":"e","è":"e","ê":"e","ú":"u","í":"i","ì":"i","ô":"o"}
with open("./Data/CankarDumps/CankarListaBesedDUMP.txt","rb") as myfile:
    wordList= pickle.load(myfile)


for word in wordList:
      for letter in word:
            if letter.lower() not in ALPHABET:
                  print(letter, " ", word)


      

def findToReplace(WordList):
      toReplace = []
      for word in enumerate(WordList):
            for letter in enumerate(word[1]):                  
                  if letter[1].lower() not in ALPHABET:
                        toReplace.append([word[0],letter[0]])
                        
      for item in toReplace:
            
            letter = list(WordList[item[0]])[item[1]]
            word = list(WordList[item[0]])     
            print(word)
            word[item[1]] = SWITCHDICT[letter]
            print(WordList[item[0]])
            WordList[item[0]] = "".join(word)
            print("".join(word))
            print(WordList[item[0]])
      
      return WordList


cleaned = findToReplace(wordList)

with open("./Data/CankarDumps/CankarListaBesedDUMP.txt","wb") as myfile:
    pickle.dump(cleaned,myfile)
    