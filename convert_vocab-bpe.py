import json

def convert_vocab_bpe_to_huggingface_format(vocab_bpe_path, vocab_json_path, merges_txt_path):
    # Step 1: Read vocab.bpe
    with open(vocab_bpe_path, 'r', encoding='utf-8') as f:
        lines = f.read().strip().split('\n')
    
    # Create a dictionary for vocab.json
    vocab = {}
    for index, line in enumerate(lines):
        token, rank = line.split()
        vocab[token.replace('▁', ' ')] = index

    # Write vocab.json
    with open(vocab_json_path, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=4)
    
    # Create merges.txt
    merges = ["#version: 0.2"]
    for token in vocab.keys():
        # Ignore single character tokens and special tokens
        if len(token) > 1 and not token.startswith('Ġ') and not token in ['<|endoftext|>', '</s>']:
            merges.append(' '.join(list(token)))

    # Write merges.txt
    with open(merges_txt_path, 'w', encoding='utf-8') as f:
        for merge in merges:
            f.write(f"{merge}\n")

# Usage
convert_vocab_bpe_to_huggingface_format("C:\\Users\\Robert Malka\\Desktop\\Capstone_3_GPT-2-Relationship-Advice\\vocab.bpe", "C:\\Users\\Robert Malka\\Desktop\\Capstone_3_GPT-2-Relationship-Advice\\pytorch_version\\vocab.json", "C:\\Users\\Robert Malka\\Desktop\\Capstone_3_GPT-2-Relationship-Advice\\pytorch_version\\merges.txt")
