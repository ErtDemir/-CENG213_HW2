def algorithm(grammar, word):

    length = len(word)
    table = [[set() for _ in range(length+1)] for i in range(length+1)] #Generate a table

    for a in range(length):     #Adding main elements to table
        table[a][a].add(word[a])

    for h in range(length):                           #Calculation
        for i in range(length - h + 1):
            for j in range(i,h+i):
                for k in grammar.keys():
                    for l in table[i][j]:
                        for m in  table[j+1][h+i]:
                            if l + m in grammar[k]:
                                table[i][h+i].add(k)
    if "S" in table[0][length-1]:   #Finding S at end of table
        print("true")
        return True
    print("false")
    return False


grammar =   { "S" : {"AB","Ab","aB","ab"},  "A" : {"BB","Bb","bB","bb"}, "B" : {"AB","Ab","aB","ab"} }
word = ["a","a","b","b","b"]
algorithm(grammar, word)