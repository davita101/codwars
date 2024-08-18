def encode(st):
    vovel_dict = {
        "a":"1",
        "e":"2",
        "i":"3",
        "o":"4",
        "u":"5",
    }
    new_word = ''
    for i in st:
        if i in vovel_dict:
            new_word += vovel_dict[i]
        else:
            new_word += i
    return new_word
    
def decode(st):
    vovel_dict = {
        "1":"a",
        "2":"e",
        "3":"i",
        "4":"o",
        "5":"u",
    }
    new_word = ''
    for i in st:
        if i in vovel_dict:
            new_word += vovel_dict[i]
        else:
            new_word += i
    return new_word