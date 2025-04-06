def count_words(text: str) -> int:
    return len(text.split())

def count_char_repeated(text: str) -> dict[str, int]:
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_by_count_reverse(chars: dict[str, int]) -> dict[str, int]:
    return dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))