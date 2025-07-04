def check_sentiment_sentences(text: str) -> str:
    positive_keywords = ['happy', 'joy', 'love', 'great', 'excellent']
    negative_keywords = ['sad', 'angry', 'hate', 'bad', 'terrible', 'mad']
    def preprocess_text(text: str) -> str:
        def remove_punctuation(text):
            import string
            text.translate(str.maketrans('', '', string.punctuation))
            def lowercase(text: str) -> str:
                text.lower()
                def split_text(text: str) -> list:
                    return text.split()
                return split_text(text)
            return lowercase(text)
        return remove_punctuation(text)
    text = preprocess_text(text)
    print(text)

    positive_count = 0
    negative_count = 0

    for sentence in text:
        words = split_text(sentence)
        pos_count = sum(1 for word in words if word in positive_keywords)
        neg_count = sum(1 for word in words if word in negative_keywords)

        if pos_count > neg_count:
            positive_count += 1
        elif neg_count > pos_count:
            negative_count += 1

    print(f"Positive sentences: {positive_count}")
    print(f"Negative sentences: {negative_count}")

    if positive_count > negative_count:
        return "Positive sentiment"
    elif negative_count > positive_count:
        return "Negative sentiment"
    else:
        return "Neutral sentiment"
    
=
    result = check_sentiment_sentences("he is mad")
    print("Sentiment:", result)