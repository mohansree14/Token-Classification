from transformers import AutoTokenizer

class BioBERTTokenizer:
    def __init__(self, model_name='dmis-lab/biobert-v1.1'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def tokenize(self, text):
        return self.tokenizer.tokenize(text)

    def encode(self, tokens, max_length=512):
        # tokens: list of words for NER
        encoding = self.tokenizer(
            tokens,
            is_split_into_words=True,
            add_special_tokens=True,
            max_length=max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        return encoding['input_ids'], encoding['attention_mask']

    def decode(self, token_ids):
        return self.tokenizer.decode(token_ids, skip_special_tokens=True)

    def save_tokenizer(self, dirpath):
        self.tokenizer.save_pretrained(dirpath)

    def load_tokenizer(self, dirpath):
        self.tokenizer = AutoTokenizer.from_pretrained(dirpath)