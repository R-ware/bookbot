def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    letters = text.lower()
    counts = {}
    for char in letters:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def get_sorted(letters):
    sorted_chars=[]
    for letter, volume in letters.items():
        if letter.isalpha():
            only_letters = {"char": letter, "num": volume}
            sorted_chars.append(only_letters)

    sorted_chars.sort(key=lambda x: x["num"], reverse=True)
    return sorted_chars