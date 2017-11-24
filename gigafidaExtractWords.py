# -*- coding: utf-8 -*-

import nltk
import codecs
import pickle
import os

#with codecs.open("./Data/Gigafida/F0000011.txt","r",encoding="utf-8") as f:
#    giga= f.read().splitlines()

#wordList = []    

#for i in giga:
#      words = nltk.word_tokenize(i)
#      words=[word.lower() for word in words if word.isalpha()]
#      for word in words:
#            wordList.append(word)
      
def extractWordsFromFiles(directory):
      wordList = []
      counter = 0
      for file in os.listdir(directory):
            counter += 1
            print("File no.:",counter)
            
            with codecs.open(directory+file,"r",encoding="utf-8") as f:
                  giga= f.read().splitlines()               
            
            for i in giga:
                  words = nltk.word_tokenize(i)
                  words=[word.lower() for word in words if word.isalpha()]
                  for word in words:
                        wordList.append(word)
      return wordList

def createCountDict(wordList):
      """Counts all the words in the word list and creates a dictionary of word:word_count key:value pairs"""
      countedWords={}
      for word in wordList:
            if word not in countedWords:
                  countedWords[word] = 1
            else:
                  countedWords[word] = countedWords[word] + 1      
      return countedWords

def countNtuples(wordList,endlen=3,concatenated=False,directory=False,prefix=""):
      #set Wordlist
      if concatenated:
            WL = []            
            while wordList:
                  subConcat =[]
                  for i in range(0,1000):
                        if wordList:
                              new=wordList.pop(0)
                              subConcat.append(new)
                        else:
                              break
                  subConcat = "".join(subConcat)
                  WL.append(subConcat)
      else:
            WL = wordList
            
      #ntuples
      dicts = []
      for length in range(2,endlen+1):
            ntupDict = {}
            for word in WL:
                 word = list(word)
                 for i in range(0,len(word)-(length-1)):
                       ntup=[]
                       for j in range(0,length):
                             ntup.append(word[i+j])
                       ntup = "".join(ntup)
                       
                       if ntup not in ntupDict:
                             ntupDict[ntup] = 1
                       else:
                             ntupDict[ntup] = ntupDict[ntup] + 1           
            dicts.append(ntupDict)
                        
      #Pickle dump
      if directory:
            tup = 2
            for d in dicts:
                  name= directory+prefix+tup*"X"+"tupleDUMP.txt"             
                  with open(name,"wb") as myfile:
                        pickle.dump(d,myfile)
                  tup += 1
      
      return dicts

            

###############################################
# THIS PART WAS FOR EXTRACTION ################
###############################################

#extracted=extractWordsFromFiles("./Data/Gigafida/")
#with open("./Data/gigaDUMP.txt","wb") as myfile:
#    pickle.dump(extracted,myfile)
    
###############################################
# THIS PART IS FOR COUNTING ###################
###############################################

#dct=createCountDict(extracted)
#with open("./Data/CankarDumps/cankarCountDUMP.txt","wb") as myfile:
#    pickle.dump(dct,myfile)
    
###############################################
   
#with open("./Data/gigaDUMP.txt","rb") as myfile:
#    wordList= pickle.load(myfile)

#with open("./Data/gigaCountDUMP.txt","rb") as myfile:
#    wordCountDict= pickle.load(myfile)

# Sort the dictionary    
#sortedCount=sorted(wordCountDict.items(),key=lambda x: x[1],reverse=True)



#NTUPLES

with open("./Data/CankarDumps/CankarListaBesedDUMP.txt","rb") as myfile:
    cankar= pickle.load(myfile)
#
#
#countNtuples(cankar,directory="./Data/CankarDumps/",prefix="Cankar")


with open("./Data/gigaDUMP.txt","rb") as myfile:
    giga= pickle.load(myfile)


countNtuples(giga,directory="./Data/",prefix="Giga")









#Skupaj = "".join(Besede)
#
#with open("CankarListaBesedDUMP.txt","wb") as besLista:
#    pickle.dump(Besede,besLista)