def get_num_words(strings):
    word_list = []
    word_list = strings.split()
    return len(word_list)


def get_char_num(strings):
    lower_case_string = str.lower(strings)
    char_dict = {}
    for char in lower_case_string:
        if char.isalpha():
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict


def get_sorted_dict(char_dict):
    sorted_char_dict = {}
    sorted_char_dict = dict(sorted(char_dict.items(), key=lambda x: x[1], reverse=True))
    return sorted_char_dict
