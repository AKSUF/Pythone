def count_words(text):
    word_counts = {}

    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


# Example usage
text = "This is a sample text to demonstrate word count. This text contains several words, and some words may repeat."

word_counts = count_words(text)

print("Word counts:")
for word, count in word_counts.items():
    print(word, ":", count)
