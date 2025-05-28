# BioBERT Streamlit Application

This project is a  user-friendly Streamlit web application for biomedical named entity recognition (NER) using the BioBERT model. Users can input biomedical text and receive token-level predictions, with vibrant visualizations for each entity label.

**Key Features:**
- **Interactive NER:** Enter biomedical text and instantly see token-level predictions using the BioBERT model.
- **Supported Labels:** The app highlights four entity labels: `O`, `B-AC`, `B-LF`, and `I-LF`, each with a distinct, vibrant color for easy interpretation.
- **Graphical Visualization:** Entities are visually highlighted in the text, making it easy to spot and understand predictions.
- **Interaction Log:** The sidebar displays your last 5 analyses, including input, predictions, and timestamps.
- **Easy to Use:** Clean interface with sidebar instructions and a simple workflow.

## How It Runs

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mohansree14/Token-Classification.git

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

4. **Use the Application:**
   - To access the deployed app here: [Streamlit App Link](https://token-classification.streamlit.app/)
>>>>>>> 895f7604f7e4de2f68f482195768849b38801c8f
   - Enter your biomedical text in the main area and click **Analyze**.
   - View all tokens and their predicted labels in a table and as a colorful graphical visualization.
   - Check the sidebar for instructions and your last 5 interactions.

## BioBERT Model

BioBERT is a domain-specific language representation model pre-trained on large-scale biomedical corpora. This application leverages BioBERT's capabilities for token classification tasks, making it suitable for biomedical text mining and NER applications.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

