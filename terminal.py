"""
V: 1 => Terminal için oluşturuldu.
V: 2 => Kullanıcı Arayüzü Oluşturulacak.

0- Dosya Kontrol -----OK-----
1- Google Çeviri  -----OK-----
2- Telaffuz Kontrol -----OK-----
3- Kendi Dosyanı Oluşturma(Bilmediğiniz kelimeleri yazarak kendinizi QUIZ yapabilirsiniz.)  -----OK-----
4- Quiz -----OK-----
"""
#================
#import
import os
import json
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import speech_recognition as sr
from time import sleep

#================
global mainPath
mainPath = "./bin/"
global driverPath
driverPath = "./driver/chromedriver.exe"
global translate_url
translate_url = """https://translate.google.com/"""

#================ CLASS YAPILARI ============
#Dosya İşlemleri
class File:

    def __init__(self,folder = "bin", filename = "dict-lang.txt", word_1 = "__word__", word_2 = "__word__"):
        self.folder = folder
        self.filename = mainPath + filename
        self.word_1 = word_1
        self.word_2 = word_2 

    def createFile(self):
        #Dosya Var       
        if os.path.exists(self.filename) == True:
            print("Dosya Bulundu...")
            sleep(3)
        #Dosya Yok : Program ilk defa çalışıyor(ya da dosyalar silindi)
        else:
            #./bin dizini var
            if os.path.exists("bin") == True:
                dict_lang = {self.word_1 : self.word_2}
                with open(self.filename, "w", encoding = "utf-8") as file:
                    file.write(json.dumps(dict_lang))
                file.close()
                print("Dosya Oluşturuldu.")
                sleep(3)
            #./bin dizini yok
            else:
                os.makedirs("bin")
                print("Klasör Oluşturuldu.") 
                dict_lang = {self.word_1 : self.word_2}
                with open(self.filename, "w", encoding = "utf-8") as file:
                    file.write(json.dumps(dict_lang))
                file.close()
                print("Dosya Oluşturuldu.")
                sleep(3)

#================
#Dosya Yönetimi
#Dosyaya kelime ekle - Kelime dosyada varsa anlamını göster yoksa ekle
class Manage_DataFile:

    def __init__(self, filename = "dict-lang.txt", word_1 = "__word__"):
        self.filename = mainPath + filename
        self.word_1 = word_1

    def controlDataFile(self):
        file = open(self.filename)
        words = json.load(file)
        #Kelime Ara; Dosyada varsa ekrana yazdır
        try:
            print(f"Kelime: {self.word_1} => {words[self.word_1]}")
        #Kelime ara; Dosyada yoksa ekle
        except:
            word_2 = input(f"Kelime Bulunamadı. Lütfen Karşıt Kelimeyi Giriniz.\n\n {self.word_1} : ")
            words[self.word_1] = word_2
            with open(self.filename, "w", encoding = "utf-8") as file:
                file.write(json.dumps(words))
            file.close()

#================
#quiz
class Quiz:

    def __init__(self, filename = "dict-lang.txt"):
        self.filename = mainPath + filename
    
    def askQuestion(self):
        file = open(self.filename, "r", encoding = "utf-8")
        words = json.load(file)
        keyWords = words.keys()
        keyWords = list(keyWords) 
        how_many_question = int(input(f"Kaç soru istiyorsunuz?(max {len(keyWords)}): ")) #how many question 
        
        #quesitons
        trueAnswer = 0
        for i in range(0, how_many_question):
            #find random keys
            randomKey = random.choice(keyWords)
            print(f"RandomKey:{randomKey}")
            valueWord = input("Kelime Giriniz: ")            
            #Doğru Cevap
            if valueWord == words[randomKey]:
                print("Güzel!!")
                trueAnswer += 1
            #Yanlış Cevap: 3 hak var.
            else:
                print("Yanlış Cevap... Yeniden Deneyin..")
                for j in range(0,3):
                    if j < 2:
                        print(f"RandomKey:{randomKey}")
                        valueWord = input("Lütfen Kelime Girin: ")
                        if valueWord == words[randomKey]:
                            print("Güzel!!")
                            trueAnswer += 1
                            break
                        else:
                            print("Yanlış Cevap... Yeniden Dene..")
                    elif j == 2:
                        print(f"RandomKey:{randomKey}")
                        valueWord = input("Lütfen Kelime Gir: ")
                        if valueWord == words[randomKey]:
                            print("Güzel!!")
                            trueAnswer += 1
                            break
                        else:    
                            print("Doğru Kelimeyi Bulamadın.")
        if trueAnswer == how_many_question:
            print("Harikasın! Hepsi Doğru.")
        elif trueAnswer < how_many_question and how_many_question - 5 <= trueAnswer:
            print(f"Biraz çalışman lazım. {trueAnswer} doğrun var.")
        elif trueAnswer < how_many_question - 5:
            print(f"Maalesef sonuç kötü. Sadece {trueAnswer} doğru yapabildin.")
        else: 
            print("Birşeyler ters gitti...")

    #================
    #translate
class Translate:

    def __init__(self, word):
        self.word = word
        
    #browser ayarları
    def browser(self):
        #option
        opt = Options()
        opt.add_argument("headless")
        global browser
        browser = webdriver.Chrome(executable_path = driverPath, options = opt)
        browser.get(translate_url)

    #spider
    def spider(self):
        translate_box_path = """//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea""" 
        browser.find_element_by_xpath(translate_box_path).send_keys(self.word)
        sleep(5) #wait for translate
        word_2 = browser.find_element_by_xpath("""//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]/span[1]/span/span""").text
        sleep(2)                                  
        print(word_2)

    #close browser
    def closeBrowser(self):
        browser.close()

    #================
    #Pronounce Test
class Pronounce_Test:

    def __init__(self, word = None):
        self.word = word

    def test(self):    
        def takeVoice():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Lütfen test için bir kelime söyleyin: ")
                data = r.record(source, duration=5)
                print("Ses Tanımlanıyor...") 
                global voiceText
                voiceText = r.recognize_google(data,language="en")
        #PRONOUNCE TEST
        for i in range(0,3):
            takeVoice()
            if voiceText == self.word:
                print("Telaffuz Başarılı...")
                break
            else:
                if i == 0 or i == 1:
                    print("Tekrar Deneyin...")
                else:
                    print("Telaffuza Çalışmalısın.")
#================

print("Uygulamaya Hoşgeldiniz. Bu uygulama İngilizcenizi geliştirmeniz için yapıldı. İyi eğlenceler...\n\nKontroller Yapılıyor. Lütfen Bekleyiniz...")
sleep(3)
File().createFile()
print("Kontroller Tamamlandı.")
while True:
    selection = input("Ne İstersiniz? \n1- Çeviri yapmak\n2- Dosyaya kelime ekle\n3- Quiz\n4- Telaffuz Testi\n5- Çıkış")


    #Çeviride sorun yok. -Çeviri sonucu dosyaya otomatik kaydedilebilir.-
    if selection == "1":
        word = input("Kelime Girin: ")
        Translate(word).browser();Translate(word).spider();Translate(word).closeBrowser()
        
    #Hata yok!
    elif selection == "2":
        word = input("Kelime Girin: ")
        Manage_DataFile(word_1 = word).controlDataFile()

    #Hata yok!
    elif selection == "3":
        Quiz().askQuestion()

    #ses verisi olmazsa hata veriyor. -"Null veri default qwe ayarlanabilir. Ses verisi girilmezse otomatik hatalı sonuç döner."-
    elif selection == "4":
        word = input("Test için kelime gir: ")
        Pronounce_Test(word = word).test()

    #not taken error
        #QUit app
    elif selection == "5":
        print("Uygulama Kapatılıyor. İyi Günler.")
        break

    #not taken error
        #False Entry
    else:
        print("Hatalı Giriş...")