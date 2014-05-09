#!/usr/bin/python

#Main Script for CPE 466 Project 2 - Genealogy
#Group Members: Joe E, Sean T, Nate M, Nate C

import sys, re, os

###################
#MAIN
###################
def main():
   urlTestFileName = sys.argv[1]
      
   urlTestFile = open(urlTestFileName, 'r')
   
   #Get a list of urls to test
   fileUrls = urlTestFile.read()
   urls = fileUrls.splitlines()
   
   #Test them urls and make a list of tuples (<URL>, <SCORE>)
   urlScores = {}
   for url in urls:
      #Find a score!
      score = 0.5
      urlScores[url] = score
   
   for url, value in urlScores.iteritems():
      print '\n',score,url
    

if __name__ == '__main__':
   main()

####################
#END MAIN
####################
