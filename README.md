# BioBERT Streamlit Application

This project is a Streamlit application that utilizes the BioBERT model for token classification tasks. The application allows users to input text and receive predictions based on the BioBERT model's capabilities.

## Project Structure

```
nlp-biobert-streamlit-app
├── src
│   ├── app.py               # Main entry point for the Streamlit application
│   ├── biobert_model.py     # Implementation for loading and using the BioBERT model
│   ├── tokenizer.py          # Tokenizer logic for processing input text
│   └── types
│       └── index.py         # Custom types and interfaces used throughout the application
├── requirements.txt          # List of dependencies required for the project
└── README.md                 # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd nlp-biobert-streamlit-app
   ```

2. **Install the required packages:**
   It is recommended to create a virtual environment before installing the dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application:**
   ```bash
   streamlit run src/app.py
   ```

## Usage

- Once the application is running, navigate to the provided local URL in your web browser.
- Input your text in the designated area and submit to receive predictions from the BioBERT model.

## BioBERT Model

BioBERT is a domain-specific language representation model pre-trained on large-scale biomedical corpora. This application leverages BioBERT's capabilities for token classification tasks, making it suitable for various biomedical text processing applications.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.