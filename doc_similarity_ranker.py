"""
            HONOR CODE
        
All the code in this file is a product
of my own work.

                        Giulio Cusenza
"""

import argparse
import os
import numpy as np
import bisect
from bisect import bisect_left


def binary_search(seq, item):
    """
    Search for an item in a sequence through binary search.

    :seq: sequence to search in
    :item: item to be searched for
    :return: the index of the item, or -1 if it was not found.
    """
    i = bisect_left(seq, item)
    if i != len(seq) and seq[i] == item:
        return i
    else:
        return -1
    
    
def get_vocab(docs):
    """
    Get all word types in a list of documents.

    :param docs: list of text file paths.
    :return: alphabetically sorted list of word types.
    """
    vocab = []
    for doc in docs:
        with open(doc, "r", encoding="utf-8") as doc:
            for line in doc:
                for word in line.strip().lower().split():
                    if binary_search(vocab, word) == -1:
                        bisect.insort(vocab, word)           
    return vocab


def build_vectors(docs, vocab):
    """
    Build a vector of word counts for each document in
    a list of documents.
    
    :param docs: list of text file paths.
    :param vocab: alphabetically sorted list of word types.
    :return: list of vectors of word counts.
    """
    vectors = []
    for doc in docs:
        vector = np.zeros(len(vocab), dtype=int)
        with open(doc, "r", encoding="utf-8") as doc:
            for line in doc:
                for word in line.strip().lower().split():
                    word_i = binary_search(vocab, word)
                    vector[word_i] += 1
        vectors.append(vector)
    return vectors
    

def cosine(v1, v2):
    """
    Compute the cosine similarity of two vectors.

    :param v1: first vector.
    :param v2: second vector.
    :return: cosine similarity of the two vectors.
    """
    return np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))


def rank_docs(docs, reference_doc_idx):
    """
    Ranks documents based on their similarity to a reference
    document. The similarity is computed as the cosine between
    vectors of word counts (each document having its own vector).
    
    :param docs: list of text file paths.
    :param reference_doc_idx: index of the reference document.
    :return: reverse iterator of a sorted list of (cos, document) pairs.
    """
    vocab = get_vocab(docs)
    vectors = build_vectors(docs, vocab)
    
    # split in reference vector and compared vectors
    reference_vector = vectors[reference_doc_idx]
    compared_vectors = vectors[:reference_doc_idx] + vectors[reference_doc_idx+1:]
    
    # compute cosine similarities
    cos_similarities = []
    for compared_vector in compared_vectors:
        cos_similarities.append(cosine(reference_vector, compared_vector))
    
    compared_docs = docs.copy()
    compared_docs.remove(docs[reference_doc_idx])
    
    # return ranked documents sorted by decreasing cosine similarity
    return reversed(sorted(zip(cos_similarities, compared_docs)))


def parse_args():
    parser = argparse.ArgumentParser(\
        description="Compares documents in the ./docs folder and ranks them by similarity to a reference document.")
    parser.add_argument("doc",\
        help= "Name of the reference document to compare the other documents to. This document should also be in the\
            ./docs folder. Name should not include path (e.g. \"1984_ch1.txt\", and not \"docs/1984_ch1.txt\")")
    return parser.parse_args()


def main(args):
    """
    Print similarity ranks between a reference document and
    other documents included in the ./docs folder.

    :args: console paramters
    :args.doc: name of the reference document.
    """
    # save names of the files in ./docs
    files = os.listdir("docs")
    docs = []
    for file in files:
        docs.append("docs/" + file)
    reference_doc_idx = docs.index("docs/" + args.doc)
    
    # print the ranked documents
    print("\nTop most similar documents to " + args.doc + ":\n")
    i = 1
    for cos_similarity, doc in rank_docs(docs, reference_doc_idx):
        print(str(i) + ". {}{}".format(doc[5:].ljust(35), "score: " + str(round(cos_similarity, 3))))
        i += 1
    print()


if __name__ == "__main__":
    main(parse_args())