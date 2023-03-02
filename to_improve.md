This program does not wrangle the data itself (yet).
If you want to run it on other documents effectively,
you need to remove all punctuation marks from them.

Issues:
- normalize counts by size of documents

To improve:
Question: "What is the best vectorial representation of a document?"

- For content similarity:
    - remove functional high-frequency words?
    - use n-grams?
    - pass each count through a function of the word's context?

- For language similarity (authorship):
    - use syntactic representations?
    - use n-grams?
    - add in punctuation?