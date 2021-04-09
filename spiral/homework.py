def spiralize(number):
    number*=number
    start=1
    inc=2
    return_value = 1
    while start<number:
        for i in range(4):
            start+=inc
            return_value+=start
        inc+=2
    return return_value
print ( spiralize(501))
