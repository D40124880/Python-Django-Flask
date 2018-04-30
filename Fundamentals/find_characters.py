def finding(char):
    new_list = []
    word_list = ['hello', 'world', 'my', 'is', 'Anna']
    for i in range(0, len(word_list)):
        if word_list[i].find(char) != -1:
            new_list.append(word_list[i])
    print new_list

finding('o')