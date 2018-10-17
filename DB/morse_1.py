#참조 : http://codingdojang.com/scode/469?orderby=&langby=python#answer-filter-area

# dic={'':' ','.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}
# morse=".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"
# word=morse.split(" ")
# for i in word:
#     print(dic[i],end="")


Mos = {'.-':'A', '-.':'N', '-...':'B', '---':'O', '-.-.':'C', '.--.':'P', '-..':'D', '--.-':'Q',
           '.':'E', '.-.':'R', '..-.':'F', '...':'S', '--.':'G', '-':'T', '....':'H', '..-':'U', '..':'I', '...-':'V',
           '.---':'J', '.--':'W', '-.-':'K', '-..-':'X', '.-..':'L', '-.--':'Y', '--':'M', '--..':'Z'} 

msg = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'

c =''
trans = []
for x in range(len(msg)):
    if msg[x] == ' ' and c == '':
        trans.append(' ')
    elif msg[x] == ' ':
        trans.append(Mos[c])
        c = ''
    else:
        c += msg[x]

trans.append(Mos[c])
print('Translated message: ' + ''.join(trans).lower())