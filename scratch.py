from transformers import GPT2Tokenizer, GPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

text = "            tok_decode"
encoded_input = tokenizer(text)

print(encoded_input)

