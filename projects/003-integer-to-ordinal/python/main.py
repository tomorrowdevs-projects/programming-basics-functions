def integer_to_ordinal(integer):
    if integer==1:
        result="first"
    elif integer==2:
        result="second"
    elif integer==3:
        result="third"
    elif integer==4:
        result="fourth"
    elif integer==5:
        result="fifth"
    elif integer==6:
        result="sixth"
    elif integer==7:
        result="seventh"
    elif integer==8:
        result="eighth"
    elif integer==9:
        result="ninth"
    elif integer==10:
        result="tenth"
    elif integer==11:
        result="eleventh"
    elif integer==12:
        result="twelfth"
    else:
        result=""
    return result

def main():
    for i in range(1,13):
        ordinal_number=integer_to_ordinal(i)
        print(f"{i} = {ordinal_number}")

if __name__=="__main__":
    main()