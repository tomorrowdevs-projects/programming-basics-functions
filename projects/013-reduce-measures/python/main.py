def reduce_measures(quantity,unit):
    #--Defining general variables--#
    units=['cup','tablespoon','teaspoon']
    teaspoons_table=[48, 3, 1]
    r=quantity*teaspoons_table[units.index(unit)]
    reduced_qty=[]
    for i in range(len(units)):
        q=r//teaspoons_table[i]
        r%=teaspoons_table[i]
        if q>1:
            units[i]=units[i]+'s'
        reduced_qty.append(q)

    result='{} {}, {} {}, {} {}'.format(reduced_qty[0],units[0],reduced_qty[1],units[1],reduced_qty[2],units[2])
    return result

def main():
    result=reduce_measures(3,'teaspoon')
    print(result)

if __name__=='__main__':
    main()