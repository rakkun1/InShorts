def sumy_summarize(corpus, n):
    text = corpus
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, n)
    return summary

def summarize(corpus, mode='rank', ratio=0.5, num_sentences=7):
    if mode == "frequency":
        sentence_list = sent_tokenize(corpus)
        formatted_article_text = corpus
        word_frequencies = dict()
        for word in word_tokenize(formatted_article_text):
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
        maximum_frequncy = max(word_frequencies.values())

        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word] / maximum_frequncy)

        sentence_scores = dict()
        for sent in sentence_list:
            words = word_tokenize(sent.lower())
            count_words = len(words)
            for word in words:
                if word in word_frequencies.keys():
                    if count_words < 50:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word]
                        else:
                            sentence_scores[sent] += word_frequencies[word]
        summary_sentences = heapq.nlargest(
            num_sentences, sentence_scores, key=sentence_scores.get)
        summary = " ".join(summary_sentences)
        return summary
    else:
        return sumy_summarize(corpus, num_sentences)
