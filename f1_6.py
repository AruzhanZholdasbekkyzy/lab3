def rev(sen):
    word=sen.split()
    rev_word = word[::-1]
    rev_sen=' '.join(rev_word)
    print(rev_sen)
sen=input()
rev(sen)