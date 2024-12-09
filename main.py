def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        print(f"--- Begin report of {book_path} ---")
        print(f"{count_words(file_contents)} words found in the document")
        print("\n")
        character_counts = count_characters(file_contents)
        for character in character_counts:
            if character.isalpha():
                print(f"The '{character}' character was found {character_counts[character]} times")
        print("--- End report ---")
        #print(character_counts)

def count_words(file_text):
    words = str(file_text).split()
    return len(words)

def count_characters(file_text):
    lowercase_text = str(file_text).lower()
    character_counts = { }
    for char in lowercase_text:
        if char not in character_counts:
            character_counts[char] = 0
        character_counts[char] += 1
    sorted_character_counts = dict(sorted(character_counts.items(), key=lambda item: item[1], reverse = True))
    return sorted_character_counts

main()