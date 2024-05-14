def center_string(s,w):
    if len(s)>=w:
        return s
    else:
        padding=str(len(s)+(w-len(s))//2)
        s='{:>{p}}'.format(s,p=padding)
        return s

def main():
    s=['Prova_1','Prova_10','Prova_100','Prova_1000','Prova_10000','Prova_100000000']
    for i in s:
        print(center_string(i,15))
    print('_______________')

if __name__=='__main__':
    main()