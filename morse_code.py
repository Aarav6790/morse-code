from beeply import notes
import time
dot = notes.beeps(400)
dash = notes.beeps(800)

codes = {'a': '.-', 'b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---',
'k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--',
'x':'-..-','y':'-.--','z':'--..'}

empty = []
letters = input('enter message: ').lower()
for j in letters:
    if j in codes:
        empty.append(codes[j])
        empty.append(' ')
for every in empty:
    if every == ' ':
        time.sleep(1)
    else:
        for each in every:
            if each == '.':
                dot.hear('C')
            elif each == '-':
                dash.hear('C')
