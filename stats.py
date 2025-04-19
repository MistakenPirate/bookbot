def get_num_words(passage):
    return len(passage.split())

def get_char_frequencies(passage):
    frequencies = {}
    for char in passage.lower():
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies

def sort_char_frequencies(freq_dict):
    sorted_list = []
    for char, count in freq_dict.items():
        if char.isalpha():
            sorted_list.append({'char': char, 'count': count})
    sorted_list.sort(key=lambda x: x['count'], reverse=True)
    return sorted_list