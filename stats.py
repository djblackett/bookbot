def get_word_count(text):
    words = text.split()
    return len(words)


def count_chars_in_text(text):
    char_counts = {}
    for char in text:
        if char.lower() not in char_counts:
            char_counts[char.lower()] = 1
        else:
            char_counts[char.lower()] += 1
    return char_counts


def create_dicts(chars_dict):
    dict_list = []
    for key, val in chars_dict.items():
        dict_list.append({"char": key, "num": val})
    dict_list.sort(key=lambda x: x["num"], reverse=True)
    return dict_list
