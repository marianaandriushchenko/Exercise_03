score = input('Enter Score: ')
try :
    scr = float(score)
except :
    scr = -1
if scr < 0.0 :
    print('Bad score')
    quit()
elif scr > 1.0 :
    print('Bad score')
    quit()
else :
    if scr >= 0.9 :
        print('A')
    elif scr >= 0.8 :
        print('B')
    elif scr >= 0.7 :
        print('C')
    elif scr >= 0.6 :
        print('D')
    elif scr < 0.6 :
        print('F')
