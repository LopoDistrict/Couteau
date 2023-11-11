```
     ______________________________ ______________________
    .'                              | (_)     (_)    (_)  |
  .'                                |  __________________ |
.'_.............................____|_(                  )|

``` 

# Couteau
Couteau is a Hybrid worldlist/dictionnary generator that used different level of generation to adapt to password security.
It also use, some leak + dehashed password  from secure database to guarantee the sucess of the attack




# functionning
At the begin you need to precise some attributes: 

1. Words commonly used by the target
1. Depth => Depth levels are from 1 to 5 to higher is th depth the stronger will be the list and couteau will try to find more about everything you indicates
1. Birth day
1. file rendered extension
1. Limit (Doesnt work properly)
1. filename
1. directory




# Beginning
## Since the project is under construction it might have bugs
- execute \couteau\main.py
- enter s to start the programm
- enter the birthday (19/08/1987) or n if not
- enter commonly used password separated by a space
- enter the depth (1 to 5) (1 is for low secured password)(5 is for highly secured password)
- That's it

# Exemple in windows cmd
```
Microsoft Windows [version 10.0.19045.3570]
(c) Microsoft Corporation. Tous droits réservés.

C:\Users\User1\Couteau>python main.py

     ______________________________ ______________________
    .'                              | (_)     (_)    (_)  |
  .'                                |  __________________ |
.'_.............................____|_(                  )|

launching process
> s
Enter the birthday like this 22/09/1987 if you dont have just enter n: 19/08/1987
Enter commonly used word, separated by a space: yankees batman ussr
Enter the depth [default:5]: 5
[+]Average size for 1 word : 15ko
[+]Average password for 1 word : 15000 lines
stop
19081987
 loading [####################] 100%

[+]the dictionnary has been finished generated
[+]You can find it here
>C:\Users\User1\Couteau\pswd_dictionnary.txt

``` 

