from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

class BioBERTModel:
    def __init__(self, model_name='dmis-lab/biobert-v1.1', num_labels=4, id2label=None, label2id=None):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        # You should fine-tune and save your model with correct label mappings for best results
        self.model = AutoModelForTokenClassification.from_pretrained(
            model_name,
            num_labels=num_labels,
            id2label=id2label or {0: "O", 1: "B-AC", 2: "B-LF", 3: "I-LF"},
            label2id=label2id or {"O": 0, "B-AC": 1, "B-LF": 2, "I-LF": 3}
        )
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)
        self.model.eval()
        self.label_map = self.model.config.id2label

    def predict(self, text):
        # Tokenize as a sequence of words for NER
        tokens = text.split()
        encoding = self.tokenizer(tokens, is_split_into_words=True, return_tensors="pt", truncation=True, padding=True)
        encoding = {k: v.to(self.device) for k, v in encoding.items()}

        with torch.no_grad():
            outputs = self.model(**encoding)
        logits = outputs.logits
        predictions = torch.argmax(logits, dim=2)

        # Align predictions with input tokens
        word_ids = encoding['input_ids'][0]
        pred_labels = []
        for idx, token_id in enumerate(word_ids):
            # Skip special tokens ([CLS], [SEP], etc.)
            if self.tokenizer.convert_ids_to_tokens(token_id.item()).startswith(('[CLS]', '[SEP]', '[PAD]')):
                continue
            pred_label = self.label_map[predictions[0][idx].item()]
            pred_labels.append(pred_label)
        return tokens, pred_labels

    def decode_predictions(self, tokens, pred_labels):
        return list(zip(tokens, pred_labels))