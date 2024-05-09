def ChirstmasSongVerse(VerseNumber):
    if type(VerseNumber)==int and VerseNumber in range(1,13):
        Day=['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']
        Gift=['Partridge in a pear tree','turtle doves','French hens','calling birds','golden rings','geese a-laying','swans a-swimming','maids a-milking','ladies dancing','lords a-leaping','pipers piping','drummers drumming']
        verse='On the {} day of Christmas my true love sent to me:'.format(Day[VerseNumber-1])
        for i in range(VerseNumber):
            if i==0:
                verse=verse+' {}'.format(Gift[i])
            else:
                verse=verse + ', {}'.format(Gift[i])
        return verse
    else:
        print('Not expected input parameter, please retry')
        return False

def ChristmasSong():
    for i in range(1,13):
        verse=ChirstmasSongVerse(i)
        print(verse)

def main():
    ChristmasSong()

if __name__=='__main__':
    main()