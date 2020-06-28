mes=input(">")
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
print(out)