from transformers import GPT2Config

config = GPT2Config(vocab_size=50256, bos_token_id=2, eos_token_id=2)
config.save_pretrained("./nepali-gpt2")