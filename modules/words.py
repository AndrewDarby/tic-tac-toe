def filter_words(word_list, letter):
    return(list(filter(lambda x: x[0]==letter, word_list)))

def display_list(mylist):
    print(mylist)