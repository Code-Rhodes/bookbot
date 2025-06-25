def get_num_words(text):
    words = text.split()
    return len(words)

def get_lower_count(text):
    text = text.lower()
    lower = {}
    for char in text:
        if char in lower:
            lower[char] += 1
        else:
            lower[char] = 1
    return lower

def sort_on(dict):
    return dict["num"]

def sort_char_counts(char_dict):
    sorted_chars = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_chars.append({"char": char, "num": count})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars