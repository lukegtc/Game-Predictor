import ast
seasonlist = [(2008,2009)]
for item in seasonlist:
    startyear, endyear = item
    print(startyear)
    print(endyear)
    filename = 'season' + str(startyear) + str(endyear) + '.txt'
    filename2 = 's' + str(startyear) + str(endyear) + '.txt'
    print(filename)
    f = open(filename, 'r+')
    f2 = open(filename2, 'w+')
    for line in f:
        line = ast.literal_eval(line)
        line = line[:-1]
        f2.write(str(line) + '\n')

        #del line1[3]
        #line1 = str(line1)
        #f2.write(line1)





