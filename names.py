import sys, os, re, nltk

namesCorpus = nltk.corpus.names

names = []
names.extend(namesCorpus.words('male.txt'))
names.extend(namesCorpus.words('female.txt'))

def isname(word):
   if word in names:
      return True
   else:
      return False

      
def makeSingleString(wordList):
   #If given a list, do this
   alphaWords = [e for e in wordList if e.isalpha()]

   str = ''
   for aWords in alphaWords:
      str += aWords
      str += ' '
      
   return str
   

#POSSIBLE NAME FEATURE RESULTS
# name-type-1-strong    Nate (R) Morrison, where Nate is in corpus
# name-type-1-weak      Bjorkk (R) Jiklyson, where Bjorkk is not in corpus
# name-type-2-strong    Morrison Nate (R), ...
# name-type-2-weak
# name-type-3-strong    Nate, where Nate is in corpus
###############################################  

def getNameFeatures(words):
   #get the name regex matches
   
   features = set()
   #First (Middle) Last
   firstMLast = re.findall(r'([A-Z][A-Za-z]+)\s([A-Z][A-Za-z]*)?\s([A-Z][A-Za-z]+)', words)
   #Last First (M)
   lastFirstM = re.findall(r'([A-Z][A-Za-z]+)\s([A-Z][A-Za-z]+)\s([A-Z][A-Za-z]*)?', words)
   #First
   first = re.findall(r'[A-Z][A-Za-z]+', words)

   for match in firstMLast:
      if isname(match[0]):
         features.add('name-type-1-strong')
      else:
         features.add('name-type-1-weak')
   
   for match in lastFirstM:
      if isname(match[1]):
         features.add('name-type-2-strong')
      else:
         features.add('name-type-2-weak')
   
   for match in first:
      if isname(match):
         features.add('name-type-3-strong')
            
   return features

#Example
#corpus = nltk.corpus.gutenberg
#list = corpus.words('austen-emma.txt')
#str = makeSingleString(list)
#blah = getNameFeatures(str)
#print blah