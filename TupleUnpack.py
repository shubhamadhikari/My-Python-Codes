def unpack_tup(list1):
    for name, score in list1:
        print(f'{name} has scored {score}')


myScoreList = [('Shubham', 99), ('Rohit', 95)]
unpack_tup(myScoreList)