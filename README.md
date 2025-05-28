Certainly! Here’s a comprehensive README.md file for your Token-Classification repository, integrating all the details you’ve provided:

---

# Token Classification

A Streamlit app for biomedical Named Entity Recognition (NER) using BioBERT. Enter biomedical text and get instant, colorful token-level predictions for labels `O`, `B-AC`, `B-LF`, and `I-LF`. Includes graphical visualization and an interaction log for enhanced usability.

---

## Web Application

This repository features an interactive web application built with **Streamlit** for biomedical NER. The web app allows you to:

- Enter biomedical text in your browser
- Instantly receive token-level predictions with color-coded labels: `O`, `B-AC`, `B-LF`, and `I-LF`
- Visualize predictions with intuitive graphical displays
- View an interaction log for tracking your queries and results

The web app is designed for simplicity and speed, making advanced biomedical text analysis accessible even to users without programming experience. The backend leverages the **BioBERT** model, selected after extensive comparisons.

---

## Algorithms and Models Explored

The project explores several algorithms and models for biomedical NER, including:

- HMM (Hidden Markov Model)
- CRF (Conditional Random Field)
- SVM (Support Vector Machine)
- BiLSTM (Bidirectional Long Short-Term Memory)
- BiLSTM + CNN (Convolutional Neural Network)
- Tuned BiLSTM
- RoBERTa
- BioBERT
- SciBERT
- Zero-shot and Few-shot learning approaches

### Model Selection

After comprehensive evaluation in the included Jupyter notebooks, **BioBERT** was chosen for powering the web app. BioBERT consistently outperformed all other models for biomedical NER tasks, providing the best accuracy and robustness.

---

## Features

- Biomedical NER with industry-leading BioBERT
- Easy-to-use, interactive Streamlit web interface
- Colorful, token-level entity predictions (`O`, `B-AC`, `B-LF`, `I-LF`)
- Visual graphical analysis of results
- Interaction log for session history

---

## Getting Started

1. **Clone this repository:**
   ```bash
   git clone https://github.com/mohansree14/Token-Classification.git
   cd Token-Classification
   ```

2. **Install the requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** to the local URL provided by Streamlit (usually http://localhost:8501).

---

## Notebooks

Refer to the provided Jupyter notebook(s) for details on model training, evaluation, and performance comparisons. These notebooks thoroughly document the experimentation with different algorithms and justify the selection of BioBERT for deployment.

---

## Why BioBERT?

BioBERT was chosen for the deployed web application because, during evaluation, it demonstrated the best performance on biomedical NER tasks—surpassing all alternative algorithms and models in both accuracy and robustness.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- [BioBERT](https://github.com/dmis-lab/biobert) for providing pre-trained biomedical language models.
- [Streamlit](https://streamlit.io/) for enabling rapid development of interactive data apps.

---

Feel free to further customize this README as your project evolves! If you need a section for contributing, citation, or have other requests, just let me know.
