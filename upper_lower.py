def swap_case(s):
    n=''
    for i in s:
        if (i.islower()) == True:
            n+=(i.upper())
        
        else:
            n+=(i.lower())

    return n

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
