import json

vocabulary = json.load(open('/data/vincent/Mining/CodeData/gpt-neox/data/python-vocab.json'))

with open('vocab_sentencepiece.txt', 'w', encoding='utf-8') as outfile:
    for v in vocabulary:
        outfile.write(v+'\n')
