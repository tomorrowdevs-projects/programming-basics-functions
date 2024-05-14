def capitalize_it(s):
    s=list(s)
    #--Swapping first letter case--#
    i=0
    while s[i]==' ':
        i+=1
    s[i]=s[i].upper()
    i+=1

    #--Swapping first letter case after a period--#
    while i<len(s)-1:
        if s[i] in '.?!':
            while s[i+1]==' ':
                i+=1
            i+=1
            s[i]=s[i].upper()
        else:
            i+=1

    #--Swapping I pronoun case--#
    s=''.join(s)
    old_string=[' i ',' i.',' i?',' i!',' i\'']
    new_string=[' I ',' I.',' I?',' I!',' I\'']
    for i,j in zip(old_string, new_string):
        s=s.replace(i,j)
    return s

def main():
    s=input('Please, enter the string that you want to check:')
    s=capitalize_it(s)
    print(s)

if __name__=='__main__':
    main()