def analyze_text(text):
    words=text.split()
    total_words=len(words)
    unique_words=len(set(words))
    total_characters=sum(len(word) for word in words)
    average_word_length=total_characters/total_words

    word_frequency={}
    for word in words:
        if word in word_frequency:
            word_frequency[word]+=1
        else:
            word_frequency[word]=1

    analysis_result={
        "total_words":total_words,
        "unique_words":unique_words,
        "average_word_length":average_word_length,
        "word_frequency":word_frequency
    }
    return analysis_result
text="This is a sample txt.Itcontains some words.Sample txt is used for analysis"
result=analyze_text(text)
print("Total Words",result["total_words"])
print("Unique Words",result["unique_words"])
print("Average Word Length",result["average_word_length"])
print("Word Frequency",result["word_frequency"])
