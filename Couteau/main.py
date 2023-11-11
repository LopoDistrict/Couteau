import csv
import os
import json
import shutil
import time
import sys


"""" 
@author LOPODISTRICT/
COUTEAU  
WORDLIST GENERATOR FOR BRUTE FORCE.
DICTIONNARY FOR BRUTE FORCE
@version 0.0.8
"""

print("""  
     ______________________________ ______________________
    .'                              | (_)     (_)    (_)  |
  .'                                |  __________________ |
.'_.............................____|_(                  )|
      """)

time.sleep(0.5)
print("launching process")





class Pswd:
    def __init__(self, words="",depth=1,  bday=False,name="",  limit=500, render=".txt", file_name="pswd_dictionnary", directory=""):
        self.words = words
        self.bday = bday
        self.name = name
        self.depth = depth
        self.limit = limit
        self.render = render
        self.file_name = file_name
        self.directory = directory

    def help(self):
       print("""
               COMMANDS / ARGS                                     DESCRIPTION:
               -n or --name [name of the rendered file]            => Name of the rendered file. (Default : pswd_dictionnary)
               -w or --words [words]                               => Words for more precise search. Increace chance of finding password.
                                                                   [!] Cant be empty
               -d or --depth [depth 1 to 5]                        => The greater the depth, the more secure the passwords. ex depth1 is
                                                                   for very low secured pswd (Default: 1)
               -bd or --bday [bday ex 8/06/1955]                   => Birthday Help for more precise pswd. Increace chance of finding password.
               -l or --limit [limit]                               => Limit of Pswd/word that can be include in the file(Default: 500)   
               -r or --render [ex: .txt]                           => Extension of the rendered file (Default: .txt)
               -dir or --directory                                 => Directory of the rendered file. (Default is \Couteau\Rendered)

                e or exit                                          => quit command
                c or cls or clear                                  => clear command
                s or start                                         => start the programm

                """)    
       time.sleep(0.5)
       self.choice()

    def Checking(self):
        if self.limit <= 0: 
            False
        elif len(self.bday) != 10 and self.bday != False:
            return False
        else:
            return True

    def choice(self):
        command = input("> ")
        #beta command
        if command == "s":
            self.Confirmation()
            #beta command
        if command == "help":
            self.help()

        if command == "e" or command == "exit":
            print("goodbye!")
            exit()

        if command == "c" or command == "clear" or command == "cls":
            os.system('cls')
        else:
            print("Command not found")
            self.choice()
    
   


    def Confirmation(self):
        self.bday = input("Enter the birthday like this 22/09/1987 if you dont have just enter n: ")
        if self.bday == "n" or self.bday == "N":
            self.bday = False
            print(self.bday)
        self.Process()

    def birthday(self):
        #delete /
        self.bday.replace("/", "")

        with open("bday.txt", "a", encoding='utf-8') as filebday:
            #bday all changment adding to password of 1 to 5
            filebday.write(self.bday+ '\n')
            #4last digits
            filebday.write(self.bday[4:8]+ '\n')
            #4digits + years
            filebday.write(self.bday[4:8] + self.bday[2:4]+ '\n') 
            inverse = self.bday[4:8]
            filebday.write(inverse[::-1]+ '\n')
            filebday.write(self.bday[6:8]+self.bday[4:6]+ '\n')
            self.bday == False


            print("stop")
            with open(f"{self.file_name}{self.render}", "a", encoding="utf-8") as file:
                shutil.copyfile('bday.txt',f"{self.file_name}{self.render}")

        filebday.close()
        os.remove("bday.txt")



    def Process(self):
        count = 0
        self.words = input("Enter commonly used word, separated by a space: ")
        self.depth = int(input("Enter the depth [default:5]: "))

        with open(f"{self.file_name}{self.render}", "a", encoding="utf-8") as file:
            if self.depth == 1:
                sys.stdout.write('\rloading [--------------------] 0%')
                sys.stdout.flush()
                """FIRST DEPTH for pin code and barely no secured password"""
                if self.bday == False:
                    pass

                else:
                    self.birthday()
                

                time.sleep(0.2)

                #including basic password
                shutil.copyfile('pswd/common-pswd.txt', f"{self.file_name}{self.render}")
                count += 196
                time.sleep(0.5)
                sys.stdout.write('\rloading [#####--------------] 20%')
                sys.stdout.flush()
                #taking the words from self.words and stocking them into var
                word = []
                temp = ""
                self.words = self.words + " " 
                time.sleep(0.2)
                sys.stdout.write('\rloading [##########----------] 50%')
                
                sys.stdout.flush()
                #print(repr(self.words))
                for l in self.words:
                    if l == " ":
                        word.append(temp)
                        temp = ""
                    else:
                        temp += l
                time.sleep(0.2)
                sys.stdout.write('\rloading [##############------] 80%')
                sys.stdout.flush()

                for i in word:
                    if count > self.limit:
                        self.finish()
                    else:    
                        file.write(i+ '\n')
                        file.write(i.capitalize()+ '\n')
                        if bool == True:
                            file.write(i + self.bday[4:8]+ '\n')
                            file.write(i + self.bday[4:8] + self.bday[2:4]+ '\n')
                            file.write(i + self.bday[6:8] + self.bday[4:6]+ '\n')
                            count += 5
                        else:
                            pass

                
                sys.stdout.write('\r loading [####################] 100%')
                sys.stdout.flush()
                time.sleep(0.2)
                self.finish()





            if self.depth == 2:
                """2ND DEPTH for low secured paswword"""
                if self.bday == False:
                    pass

                else:
                    self.birthday()

                sys.stdout.write('\rloading [--------------------] 0%')
                sys.stdout.flush()

                #common root password
                shutil.copyfile(f"{self.file_name}{self.render}", 'pswd/common-pswd2.txt')
                count += 22


                word = []
                temp = ""
                self.words = self.words + " " 

                sys.stdout.write('\rloading [#####--------------] 20%')
                sys.stdout.flush()

                print(repr(self.words))
                for l in self.words:
                    if l == " ":
                        word.append(temp)
                        temp = ""
                    else:
                        temp += l

                sys.stdout.write('\rloading [##########----------] 50%')
                sys.stdout.flush()
                for i in word:
                    if count > self.limit:
                        self.finish()
                    else:
                        file.write(i+ '\n')
                        file.write(i.capitalize()+ '\n')
                        count += 5

            
                    for j in word:
                        #take in parameters few special char
                        file.write(j + "."+ '\n')
                        file.write(j + "@"+ '\n')
                        file.write(j + "!"+ '\n')
                        file.write(j + "_"+ '\n')

                    for k in range(100):
                        #try to detect with all numbers frm 1 to 100
                        file.write(i + str(k) + '\n')
                    sys.stdout.write('\r loading [####################] 100%')
                    sys.stdout.flush()
                self.finish()
            
            if self.depth == 3:
                """DEPTH 3 Entering in solid password with stronger security"""
                if self.bday == False:
                    pass

                else:
                    self.birthday()

                #common root password
                shutil.copyfile(f"{self.file_name}{self.render}", 'pswd/common-pswd3.txt')
                count += 22
                word = []
                temp = ""
                self.words = self.words + " " 

                print(repr(self.words))
                for l in self.words:
                    if l == " ":
                        word.append(temp)
                        temp = ""
                    else:
                        temp += l

                for i in word:
                    if count > self.limit:
                        self.finish()
                    else:
                        file.write(i+ '\n')
                        file.write(i.capitalize() + '\n')

                        #trying to put nicknames for password
                        file.write(i.replace("i", "1")+ '\n')
                        file.write(i.replace("a", "4")+ '\n')
                        file.write(i.replace("o", "0")+ '\n')
                        file.write(i.replace("e", "3")+ '\n')

                        file.write(i.replace("I", "1")+ '\n')
                        file.write(i.replace("A", "4")+ '\n')
                        file.write(i.replace("O", "0")+ '\n')
                        file.write(i.replace("E", "3")+ '\n')
                        count += 5
                    for j in word:
                        #take in parameters few special char
                        file.write(j + "."+ '\n')
                        file.write(j + "@"+ '\n')
                        file.write(j + "!"+ '\n')
                        file.write(j + "_"+ '\n')
                    for k in range(100):
                        #try to detect with all numbers frm 1 to 100
                        file.write(i + str(k) + '\n')
                self.finish()
            

            if self.depth == 4:
                """DEPTH 4 Entering in solid password with stronger sec"""
                if self.bday == False:
                    pass
                else:
                    self.birthday()
                #common root password/ more complicated password
                #leak db password are getting stronger with the depth argument
                shutil.copyfile(f"{self.file_name}{self.render}", 'pswd/common-pswd4.txt')
                count += 22
                word = []
                temp = ""
                self.words = self.words + " " 
                print(repr(self.words))
                for l in self.words:
                    if l == " ":
                        word.append(temp)
                        temp = ""
                    else:
                        temp += l

                for i in word:
                    if count > self.limit:
                        self.finish()
                    else:
                        file.write(i+ '\n')
                        file.write(i.capitalize() + '\n')
                        #trying to put nicknames for password
                        file.write(i.replace("i", "1")+ '\n')
                        file.write(i.replace("a", "4")+ '\n')
                        file.write(i.replace("o", "0")+ '\n')
                        file.write(i.replace("e", "3")+ '\n')
                        file.write(i.replace("I", "1")+ '\n')
                        file.write(i.replace("A", "4")+ '\n')
                        file.write(i.replace("O", "0")+ '\n')
                        file.write(i.replace("E", "3")+ '\n')
                        count += 5
                    for j in word:
                        #take in parameters few special char
                        file.write(j + "."+ '\n')
                        file.write(j + "@"+ '\n')
                        file.write(j + "!"+ '\n')
                        file.write(j + "_"+ '\n')
                        file.write(j + "?"+ '\n')
                        file.write(j + "-"+ '\n')
                        file.write(j + "$"+ '\n')
                    for k in range(100):
                        #try to detect with all numbers frm 1 to 100
                        file.write(i + str(k) + '\n')
                    
                self.finish()
            





            if self.depth == 5:
                """Last Depth of the beta [+]Strong password [-] leak db password"""
                print("[+]Average size for 1 word : 15ko")
                print("[+]Average password for 1 word : 15000 lines")

                if self.bday == False:
                    pass
                    
                else:
                    self.birthday()
                    file.write("debut"+ '\n')

                    word2 = []
                    temp = ""
                    self.words = self.words + " " 
                    #print(repr(self.words))
                    self.bday = str(self.bday).replace("/", "")
                    print(self.bday)

                    for l in self.words:
                        if l == " ":
                            word2.append(temp)
                            temp = ""
                        else:
                            temp += l
                    for i in word2:
                        #year
                        file.write(i + self.bday[5:8]+ '\n')
                        #2last digits year
                        file.write(i + self.bday[6:8]+ '\n')
                        #month + 2last digits year
                        file.write(i + self.bday[2:4] + self.bday[6:8]+ '\n')

                        file.write(i + self.bday[2:4] + self.bday[0:2] + self.bday[6:8]+ '\n')
                        file.write(i + self.bday[0:2] + self.bday[6:8]+ '\n')
                        file.write(i + self.bday[0:2]+ '\n')
                        file.write(i + self.bday[0:2] + self.bday[2:4]+ '\n')
                        
                        
                        file.write((i + self.bday[5:8]+ '\n').capitalize())
                        #2last digits year
                        file.write((i + self.bday[6:8]+ '\n').capitalize())
                        #month + 2last digits year
                        file.write((i + self.bday[2:4] + self.bday[6:8]+ '\n').capitalize())

                        file.write((i + self.bday[2:4] + self.bday[0:2] + self.bday[6:8]+ '\n').capitalize())
                        file.write((i + self.bday[0:2] + self.bday[6:8]+ '\n').capitalize())
                        file.write((i + self.bday[0:2]+ '\n').capitalize())
                        file.write((i + self.bday[0:2] + self.bday[2:4]+ '\n').capitalize())


                    
                """#common root password/ more complicated password
                #leak db password are getting stronger with the depth argument
                shutil.copyfile(f"{self.file_name}{self.render}", 'pswd/common-pswd4.txt')"""

                count += 22
                word = []
                temp = ""
                self.words = self.words + " " 

                #print(repr(self.words))
                sys.stdout.write('\rloading [--------------------] 0%')
                sys.stdout.flush()
                for l in self.words:
                    if l == " ":
                        word.append(temp)
                        temp = ""
                    else:
                        temp += l

                for i in word:
                    if count > self.limit:
                        self.finish()
                    else:
                        file.write(i+ '\n')
                        file.write(i.capitalize() + '\n')
                        #trying to put nicknames for password
                        file.write(i.replace("i", "1")+ '\n')
                        file.write(i.replace("a", "4")+ '\n')
                        file.write(i.replace("o", "0")+ '\n')
                        file.write(i.replace("e", "3")+ '\n')
                        file.write(i.replace("I", "1")+ '\n')
                        file.write(i.replace("A", "4")+ '\n')
                        file.write(i.replace("O", "0")+ '\n')
                        file.write(i.replace("E", "3")+ '\n')
                        count += 5
                
                    sys.stdout.write('\rloading [#####--------------] 20%')
                    sys.stdout.flush()
                

                    for j in word:
                        #take in parameters few special char
                        file.write(j + "."+ '\n')
                        file.write(j + "@"+ '\n')
                        file.write(j + "!"+ '\n')
                        file.write(j + "_"+ '\n')
                        file.write(j + "?"+ '\n')
                        file.write(j + "-"+ '\n')
                        file.write(j + "$"+ '\n')
                        file.write((j + "."+ '\n').capitalize())
                        file.write((j + "@"+ '\n').capitalize())
                        file.write((j + "!"+ '\n').capitalize())
                        file.write((j + "_"+ '\n').capitalize())
                        file.write((j + "?"+ '\n').capitalize())
                        file.write((j + "-"+ '\n').capitalize())
                        file.write((j + "$"+ '\n').capitalize())
                        file.write((j + "."+ '\n').upper())
                        file.write((j + "@"+ '\n').upper())
                        file.write((j + "!"+ '\n').upper())
                        file.write((j + "_"+ '\n').upper())
                        file.write((j + "?"+ '\n').upper())
                        file.write((j + "-"+ '\n').upper())
                        file.write((j + "$"+ '\n').upper())

                        sys.stdout.write('\rloading [##########----------] 50%')
                        sys.stdout.flush()
                    
                        for k in range(100):
                            #try to detect with all numbers frm 1 to 100
                            file.write((j + str(k) +   "."+'\n').capitalize())
                            file.write((j + str(k) + "@"+ '\n').capitalize())
                            file.write((j + str(k) + "!"+ '\n').capitalize())
                            file.write((j + str(k) + "_"+ '\n').capitalize())
                            file.write((j + str(k) + "?"+ '\n').capitalize())
                            file.write((j + str(k) + "-"+ '\n').capitalize())
                            file.write((j + str(k) + "$"+ '\n').capitalize())
                            file.write((j + str(k) +  "."+ '\n' ))
                            file.write((j + str(k) + "@"+ '\n'))
                            file.write((j + str(k) + "!"+ '\n'))
                            file.write((j + str(k) + "_"+ '\n'))
                            file.write((j + str(k) + "?"+ '\n'))
                            file.write((j + str(k) + "-"+ '\n'))
                            file.write((j + str(k) + "$"+ '\n'))
                
                    sys.stdout.write('\rloading [##############------] 80%')
                    sys.stdout.flush()
                    for l in range(len(word)):
                        #all upper not the first
                        file.write(word[l][0:1]+ word[l][1:].upper()+ '\n')
                        file.write(word[l][0:1]+ word[l][1:].upper()+ "."+ '\n')
                        file.write(word[l][0:1]+ word[l][1:].upper()+ "@"+ '\n')
                        file.write(word[l][0:1]+ word[l][1:].upper()+ "!"+ '\n')
                        file.write(word[l][0:1]+ word[l][1:].upper()+ "_"+ '\n')
                        file.write(word[l][0:1]+ word[l][1:].upper()+ "?"+ '\n')
                        file.write(word[l][0:1]+ word[l][1:].upper()+ "-"+ '\n')
                        file.write(word[l][0:1]+ word[l][1:].upper()+ "$"+ '\n')
                        file.write(word[l].replace("i", "1").upper()+ '\n')
                        file.write(word[l].replace("a", "4").upper()+ '\n')
                        file.write(word[l].replace("o", "0").upper()+ '\n')
                        file.write(word[l].replace("e", "3").upper()+ '\n')
                        file.write(word[l].replace("I", "1").upper()+ '\n')
                        file.write(word[l].replace("A", "4").upper()+ '\n')
                        file.write(word[l].replace("O", "0").upper()+ '\n')
                        file.write(word[l].replace("E", "3").upper()+ '\n')
                        file.write((word[l][0:1]+ word[l][1:].upper())+ '\n')
                        file.write((word[l][0:1]+ word[l][1:].upper()+ ".").replace("i", "1")+ '\n')
                        file.write((word[l][0:1]+ word[l][1:].upper()+ "@").replace("a", "4")+ '\n')
                        file.write((word[l][0:1]+ word[l][1:].upper()+ "!").replace("o", "0")+ '\n')
                        file.write((word[l][0:1]+ word[l][1:].upper()+ "_").replace("e", "3")+ '\n')
                        file.write((word[l][0:1]+ word[l][1:].upper()+ "?").replace("I", "1")+ '\n')
                        file.write((word[l][0:1]+ word[l][1:].upper()+ "-").replace("A", "4")+ '\n')
                        file.write((word[l][0:1]+ word[l][1:].upper()+ "$").replace("O", "0")+ '\n')
                        file.write(word[l] + "123"+ '\n')
                        file.write(word[l] + "12345678"+ '\n')
                        file.write("123456Seven"+ '\n')
                        file.write(word[l] + "0000"+ '\n')
                        file.write(word[l] + "12"+ '\n')




                        
                    

                sys.stdout.write('\r loading [####################] 100%')
                sys.stdout.flush()
                self.finish()

                            

                        
                                

                                


    def finish(self):
        print()
        print("\n[+]the dictionnary has been finished generated")
        print()
        print("\n[+]You can find it here", self.directory)
        print(">" + os.path.normpath(r"%s\Couteau"%(os.environ['USERPROFILE'])) +f"\{self.file_name}{self.render}")
        count = 0
                                


if __name__ == "__main__":
    begin = Pswd("", 5)
    begin.choice()


    
