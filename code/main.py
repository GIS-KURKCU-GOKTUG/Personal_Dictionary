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
import os
import json
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


#Start - Controls
print("Welcome. First, a few checks will be run.")
Create_File().createFile()
sleep(3)
print("First Control: OK\nSecond Control Start")
Create_File().createFile()
sleep(3)
print("Second Control: OK\n\nAll Process: OK\nYou can use the program. If you think somethings are wrong, please contact with Mr Kurkcu(gis.goktugkurkcu@gmail.com).\n\n\nProgram Started...(Press 3 for Quit.)")
#End -Controls
#Start Program
while True:
    
    selectLanguage = input("\n\nPlease select language.\n1-English\n2-Türkçe\n\nPlease select 1 or 2(not word, enter numbers): ")
    
    if selectLanguage == "1":
        word = input("Enter Word: ")
        Operations(selectLanguage = selectLanguage, word = word).findWord()

    elif selectLanguage == "2":
        kelime = input("Kelime Girin: ")
        Operations(selectLanguage = selectLanguage, kelime = kelime).findWord()

    #QUIT
    elif selectLanguage == "3":
        break

    # Error
    else: print("Somethings are wrong, please contact with Mr Kurkcu(gis.goktugkurkcu@gmail.com).")
    