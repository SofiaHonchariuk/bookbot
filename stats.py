def count_words(text):
    return len(text.split())

def count_characters(text):
    counter_c = {}
    for c in text.lower():
        if c in counter_c:
            counter_c[c] += 1
        else: counter_c[c] = 1
    return counter_c

def sort_on(item):
    return item["num"]

def sorted_list_dict(counter_c):
    list_of_dict = []
    for i in counter_c:
        list_of_dict.append({"char": i, "num": counter_c[i]})
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict



