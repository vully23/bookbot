def count_words(book_text):
    split_text = book_text.split()
    total_words = len(split_text)
    return total_words

def count_characters(book_text):
    text = book_text.lower()
    char_dict = {}
    for i in text:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def sorted_dict(dict):
    sorted_list = []
    for i in dict:
        if i.isalpha():
            sorted_list.append({"character": i, "count": dict[i]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list