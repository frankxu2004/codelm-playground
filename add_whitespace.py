import transformers
import os

# tokenizer = transformers.GPT2TokenizerFast.from_pretrained("EleutherAI/gpt-neo-2.7B")
# tokenizer = transformers.GPT2TokenizerFast('../gpt-neox/data/code-vocab.json', '../gpt-neox/data/code-merges.txt')
from gpt2_tokenization import GPT2Tokenizer
tokenizer = GPT2Tokenizer('/data/vincent/Mining/CodeData/gpt-neox/data/python-vocab.json', '/data/vincent/Mining/CodeData/gpt-neox/data/python-merges.txt')
# special_whitespace_tokens = []
# for i in reversed(range(1, 25)):
#     special_whitespace_tokens.append(' '*i)
# for i in reversed(range(1, 7)):
#     special_whitespace_tokens.append('\t'*i)

# # print(special_whitespace_tokens)
# tokenizer.add_tokens(special_whitespace_tokens)


total_tokens = 0
for root, _, files in os.walk('../lm-evaluation-harness/evaldata/Code-sampled100/{}'.format('Python')):
    for file in files:
        content = open(os.path.join(root, file)).read().strip()
        if content:
            raw = open(os.path.join(root, file)).read()
            output = tokenizer.tokenize(raw)

            detok = "|".join(output).replace('\x03', ' ').replace('\x01', '\n')
            print(detok)   

            exit()
            total_tokens += len(output)

print(total_tokens)