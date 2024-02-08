def merge(documents, w2v_model, threshold = 0.85):

    def get_custom_wv(word):
        try:
            return w2v_model.get_vector(word)
        except:
            return np.zeros(w2v_model.vector_size)

    documents_sentences = list(map(sent_tokenize, documents))
    largest_document = max(documents_sentences, key=len)
    final_document = largest_document
    for document in documents_sentences:
        if document == largest_document:
            continue
        for document_line_position, document_line in enumerate(document):
            position = list()
            for final_document_line_position, final_document_line in enumerate(final_document):
                document_line_vector = np.mean(
                    [get_custom_wv(word) for word in document_line.split()], axis=0)
                final_document_line_vector = np.mean(
                    [get_custom_wv(word) for word in final_document_line.split()], axis=0)
                similarity = cosineSimilarity(
                    document_line_vector, final_document_line_vector)
                position.append((final_document_line_position, similarity))
            position.sort(reverse=True, key=lambda x: x[1])
            best_position, highest_similarity = position[0]
            if highest_similarity >= threshold:
                final_document.insert(best_position, document_line)
    return " ".join(final_document)
