"""
=====================================================
Project: Private Dictionary for Learning Languages
Author: Kurkcu, Goktug
Date: 14.01.2022 - 00.01
=====================================================
:EXAMPLE:
=====================================================
==> Is this first run?
++ Yes => dict_en = {
                    "word_1":"word_2",
                    }
         dict_tr = {
                    "kelime_1":"kelime_2"
                     }
++ No => Continue
**********************************************

==> Select Language (For Selected English)

Select Language
    1- English
    2- Türkçe

    Select: 
**********************************************

++ 1
-*Select dict_en

Input Word: ...

==> Is word in dict_en 
++ Yes => print(f"Word: {word_1} => {word_2}")

++ No => Input Word_2: ...
        dict_en[word_1] = "word_2"
**********************************************

++ 2
-*Select dict_tr

Kelime Gir: ...

==> aranan kelime dict_tr'de var mı 
++ Evet => print(f"Kelime: {kelime_1} => {kelime_2}")

++ Hayır => Kelime_2 Gir: ...
        dict_tr[kelime_1] = "kelime_2"
**********************************************
"""
# import
from ast import keyword
import os
import json
import random
from time import sleep

# class for file operations
class Create_File:

    # __init__
    def __init__(self, filename_en = "en-dict.txt", filename_tr = "tr-dict.txt", dict_en = {"word_1":"word_2"}, dict_tr = {"kelime_1":"kelime_2"}):
        
        # self.XYZ
        self.filename_en = filename_en
        self.filename_tr = filename_tr
        self.dict_en = dict_en
        self.dict_tr = dict_tr

    # create files
    # If first open; there aren't files for saving so this -def- is run.
    def createFile(self):
        # filenames
        fileNames = [self.filename_en, self.filename_tr]
        
        # If there are files (This mean; the program has been run before!!)
        if os.path.exists("./files") == True:
            
            # Files are ready for operations!!
            if self.filename_en in os.listdir("./files") and self.filename_tr in os.listdir("./files"):
                print("Files Found!!")
            
            # If this program has been run and created folder(folder name: files) but files(en-dict.txt and tr-dict.txt) is lost; this -if- is run and files will be created. 
            else:
                # Create en-dict.txt  
                with open("./files/" + self.filename_en, "w", encoding = "utf-8") as w_dict_en:
                    w_dict_en.write(json.dumps(self.dict_en))
                w_dict_en.close()
                print(f"File : {self.filename_en} : CREATED")

                # Create + tr-dict.txt
                with open("./files/" + self.filename_tr, "w", encoding = "utf-8") as w_dict_tr:
                    w_dict_tr.write(json.dumps(self.dict_tr))
                w_dict_tr.close()
                print(f"File : {self.filename_tr} : CREATED")


        # If there aren't files (This mean; the program is run for first time)
        elif os.path.exists("./files") == False:
            os.mkdir("./files") # First operation: Create Folder == files (for save files (en-dict.txt and tr-dict.txt))
            folder = os.path.exists("./files") #DELETE
            print(f"Folder : {folder} : CREATED")

            # Create en-dict.txt  
            with open("./files/" + self.filename_en, "w", encoding = "utf-8") as w_dict_en:
                w_dict_en.write(json.dumps(self.dict_en))
            w_dict_en.close()
            print(f"File : {self.filename_en} : CREATED")

            # Create + tr-dict.txt
            with open("./files/" + self.filename_tr, "w", encoding = "utf-8") as w_dict_tr:
                w_dict_tr.write(json.dumps(self.dict_tr))
            w_dict_tr.close()
            print(f"File : {self.filename_tr} : CREATED")
                         
            print("Files Created!!")

#======================================================
#======================================================
#======================================================
# All Operations
class Operations:
    
    # init
    def __init__(self, selectLanguage,filename_en = "en-dict.txt", filename_tr = "tr-dict.txt", word = None, kelime = None):
        self.selectLanguage = selectLanguage
        self.filename_en = filename_en
        self.filename_tr = filename_tr
        self.word = word
        self.kelime = kelime

    #findWord
    def findWord(self):
        #for english
        if self.selectLanguage == "1":
            file = open("./files/" + self.filename_en)
            words = json.load(file)
            #search word and print it
            try:
                for i in range(0,1):
                    print(f"Word: {self.word} => {words[self.word]}")
            #if cant find the word; add it
            except:
                word_2 = input(f"The Word isn't find. Please enter the second word.\n\n {self.word} : ")
                words[self.word] = word_2
                with open("./files/" + self.filename_en, "w", encoding = "utf-8") as w_dict_en:
                    w_dict_en.write(json.dumps(words))
                w_dict_en.close()
                
        #Türkçe için
        elif self.selectLanguage == "2":        
            file = open("./files/" + self.filename_tr)
            kelimeler = json.load(file)
            #kelimeyi ara ve ekrana yazdır
            try:
                for i in range(0,1):
                    print(f"Kelime: {self.kelime} => {kelimeler[self.kelime]}")
            #kelime dosyada yoksa; ekle
            except:
                kelime_2 = input(f"The Word isn't find. Please enter the second word.\n\n {self.kelime} : ")
                kelimeler[self.kelime] = kelime_2
                with open("./files/" + self.filename_tr, "w", encoding = "utf-8") as w_dict_tr:
                    w_dict_tr.write(json.dumps(kelimeler))
                w_dict_tr.close()
            
        #Error
        else: 
            print("Somethings are wrong, please contact with Mr Kurkcu(gis.goktugkurkcu@gmail.com).")                

#======================================================
#======================================================
#======================================================
# QUIZ
class Quiz:

    # __init__
    def __init__(self, language, filename_en = "en-dict.txt", filename_tr = "tr-dict.txt"):
        self.language = language
        self.filename_en = filename_en
        self.filename_tr = filename_tr

    # ask question
    def askQuestion(self):
        #English File
        if self.language == "1":
            file = open("./files/" + self.filename_en)
        #Turkce File
        elif self.language == "2":
            file = open("./files/" + self.filename_tr)
        words = json.load(file)
        keyWords = words.keys()
        keyWords = list(keyWords)
        #how many question 
        how_many_question = int(input(f"how many question(max {len(keyWords)}): "))
        #quesitons
        trueAnswer = 0
        for i in range(0, how_many_question):
            #find random keys
            randomKey = random.choice(keyWords)
            print(f"RandomKey:{randomKey}")
            if self.language == "1":
                valueWord = input("Please enter Turkish: ")
            elif self.language == "2":
                valueWord = input("Please enter English: ")            
            #if key = value => answer true
            if valueWord == words[randomKey]:
                print("Good Job!!")
                trueAnswer += 1
            #else you have 3 rights for find true word
            else:
                print("Wrong Answer... Try Again..")
                for j in range(0,3):
                    if j < 2:
                        if self.language == "1":
                            print(f"RandomKey:{randomKey}")
                            valueWord = input("Please enter Turkish: ")
                        elif self.language == "2":
                            print(f"RandomKey:{randomKey}")
                            valueWord = input("Please enter English: ")
                        if valueWord == words[randomKey]:
                            print("Good Job!!")
                            trueAnswer += 1
                            break
                        else:
                            print("Wrong Answer... Try Again..")
                    elif j == 2:
                        print(f"RandomKey:{randomKey}")
                        valueWord = input("Please enter Turkish: ")
                        if valueWord == words[randomKey]:
                            print("Good Job!!")
                            trueAnswer += 1
                            break
                        else:    
                            print("You cant find True word.")
        if trueAnswer == how_many_question:
            print("You are Great. You have full")
        elif trueAnswer < how_many_question and how_many_question - 5 <= trueAnswer:
            print(f"You must study. You have {trueAnswer} true answers.")
        elif trueAnswer < how_many_question - 5:
            print(f"You are bad. You do only {trueAnswer} true answers.")
        else: 
            print("Somethings Wrong...")
#======================================================
#======================================================
#======================================================

#Start - Controls
print("Welcome. First, a few checks will be run.")
Create_File().createFile()
sleep(3)
print("First Control: OK\nSecond Control Start")
Create_File().createFile()
sleep(3)
print("Second Control: OK\n\nAll Process: OK\nYou can use the program. If you think somethings are wrong, please contact with Mr Kurkcu(gis.goktugkurkcu@gmail.com).\n\n\nProgram Started...(Press 4 for Quit.)")
#End -Controls
#Start Program
while True:
    
    selectLanguage = input("\n\nPlease select language or Quiz.\n1-English\n2-Türkçe\n3-Quiz\n\nPlease select 1, 2 or 3(not word, enter numbers): ")
    
    if selectLanguage == "1":
        word = input("Enter Word: ")
        Operations(selectLanguage = selectLanguage, word = word).findWord()

    elif selectLanguage == "2":
        kelime = input("Kelime Girin: ")
        Operations(selectLanguage = selectLanguage, kelime = kelime).findWord()

    #QUIZ
    elif selectLanguage == "3":
        language = input("\n\nPlease select language.\n1-English\n2-Türkçe\n\nPlease select 1 or 2(not word, enter numbers): ")
        Quiz(language).askQuestion()

    #QUIT
    elif selectLanguage == "4":
        break

    # Error
    else: print("Somethings are wrong, please contact with Mr Kurkcu(gis.goktugkurkcu@gmail.com).")
    