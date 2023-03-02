# Doc similarity ranker

Rank documents based on their cosine similarity on vectors of word counts.

## Example usage

**Set up:**
1. Pick some documents to rank.
2. Remove all punctuation from them (the program does not do it itself yet).
3. Store them in `./docs`.

**Run:**
```
> python doc_similarity_ranker.py 1984_ch1.txt
```

**Output:**
```
Top most similar documents to 1984_ch1.txt:

1. 1984_ch1 copy.txt                  score: 1.0
2. brave_new_world_ch1.txt            score: 0.92
3. animal_farm_ch1.txt                score: 0.904
4. emma_ch1.txt                       score: 0.76
5. pride_and_prejudice_ch1.txt        score: 0.66
```
