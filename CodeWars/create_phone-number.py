def create_phone_number(n):
    #your code here
    start = "("
    stnum = n[0:3]
    midnum = n[3:6]
    endnum = n[6:]
    for x in stnum:
        start +=str(x)
    start+=") "
    
    for x in midnum:
        start +=str(x)
    start+="-"
    
    
    for x in endnum:
        start +=str(x)
    
    print(start)
    return start
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),
create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 
create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), 
create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
