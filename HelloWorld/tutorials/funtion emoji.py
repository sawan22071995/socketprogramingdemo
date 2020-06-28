def emojiconvertor(message):
    #it return the list of words in string
    word=mes.split(' ')
    print(word)
    emoji={
        ':)':'good',
        ':(':'sad'
    }
    out=''
    for i in word:
        out+=emoji.get(i,i)+' '
    return out

mes=input(">")
print(emojiconvertor(mes))