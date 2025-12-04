def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    chars_count = {}
    for char in text:
        if char.lower() not in chars_count:
            chars_count[char.lower()] = 1
        else:
            chars_count[char.lower()] += 1

    return chars_count
    
def sort_on(items):
    return items["num"]

def get_sorted_list(chars_count):
    sorted_list=[]
    for char in chars_count:
        sorted_list.append({"char": char, "num": chars_count[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list