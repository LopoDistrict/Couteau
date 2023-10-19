# Warning Couteau is still in open build and you need to modify Couteau\main.py to start an attack
# Couteau
Couteau is a Hybrid worldlist/dictionnary generator that used different level of generation to adapt to password security.
It also use, some leak + dehashed password  from secure database to guarantee the sucess of the attack

# functioning
At the begin you need to precise some attributes: 1- Words commonly used by the target
                                                  2 - Depth => Depth levels are from 1 to 5
                                                  to higher is th depth the stronger will be the list and couteau will try to find more about everything you indicates
                                                  3 - Birth day
                                                  4 - file rendered extension
                                                  5 - Limit (Doesnt work properly)
                                                  6- filename
                                                  7 - directory
                                                  
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

# Beginning
## Since the project is under construction it might have bugs
- Make sure you have shutil installed
- open \couteau\main.py
- modify at the end begin = Pswd("cat doggo fishy", 5) by the value you want
- [!] Be careful the order of parameters are those : words, depth, name, limit, render, file_name, dir

