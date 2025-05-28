import streamlit as st
from biobert_model import BioBERTModel
from tokenizer import BioBERTTokenizer

# Initialize model and tokenizer only once (caching for performance)
@st.cache_resource
def get_model_and_tokenizer():
    tokenizer = BioBERTTokenizer()
    model = BioBERTModel()
    return tokenizer, model

def main():
    st.title("BioBERT Named Entity Recognition")
    st.write("This application uses the BioBERT model to perform named entity recognition on biomedical text.")

    # Sidebar instructions
    st.sidebar.header("Instructions")
    st.sidebar.info(
        "1. Enter  text in the main area.\n"
        "2. Click 'Analyze' to see predicted entities.\n"
        "3. Results will be shown in a table below."
        "4. The interaction log will be displayed in the sidebar.\n"
        "5. The log will show the last 5 interactions.\n"
        "6. The log will be saved in a JSON file named 'interaction_log.json'.\n"
    )

    # Display interaction log in sidebar
    import os
    import json
    log_path = "interaction_log.json"
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as f:
            try:
                log_data = json.load(f)
            except json.JSONDecodeError:
                log_data = []
        if log_data:
            st.sidebar.markdown("---")
            st.sidebar.subheader("Interaction Log")
            for entry in reversed(log_data[-5:]):  # Show last 5 interactions
                st.sidebar.markdown(f"**Input:** {entry['input_text']}")
                st.sidebar.markdown(f"**Labels:** {', '.join(entry['pred_labels'])}")
                st.sidebar.markdown("---")
        else:
            st.sidebar.info("No interactions logged yet.")
    else:
        st.sidebar.info("No interactions logged yet.")

    # Main area input
    input_text = st.text_area("Enter biomedical text:", height=200)
    analyze = st.button("Analyze")

    if analyze:
        if input_text.strip():
            tokenizer, model = get_model_and_tokenizer()
            pred_tokens, pred_labels = model.predict(input_text)
            st.subheader("Predicted Entities (All Labels):")
            import pandas as pd
            min_len = min(len(pred_tokens), len(pred_labels))
            # Show all tokens and their predicted labels
            df = pd.DataFrame(
                {
                    "Token": pred_tokens[:min_len],
                    "Predicted Label": pred_labels[:min_len]
                }
            )
            st.table(df)

            # --- Visual Highlighting ---
            st.subheader("Entity Visualization")
            def get_color(label):
                if label == "O":
                    return "white"
                elif label.startswith("B-"):
                    return "red"
                elif label.startswith("I-"):
                    return "blue"
                else:
                    return "orange"

            highlighted_text = ""
            for token, label in zip(pred_tokens[:min_len], pred_labels[:min_len]):
                color = get_color(label)
                if label != "O":
                    highlighted_text += f'<span style="color:{color}; font-weight:bold">{token}</span> '
                else:
                    highlighted_text += f'{token} '
            st.markdown(highlighted_text, unsafe_allow_html=True)

            # --- Graphical Entity Visualization ---
            st.subheader("Entity Visualization (Colorful)")

            # Assign vibrant colors to each entity type
            ENTITY_COLORS = {
                "O": "#ffffff",      # White for non-entities
                "B-AC": "#ff1744",  # Vibrant Red
                "B-LF": "#00e676",  # Vibrant Green
                "I-LF": "#2979ff",  # Vibrant Blue
            }

            def get_bgcolor(label):
                return ENTITY_COLORS.get(label, "#e0e0e0")  # Default gray

            highlighted_text = ""
            for token, label in zip(pred_tokens[:min_len], pred_labels[:min_len]):
                bgcolor = get_bgcolor(label)
                if label != "O":
                    display_label = f'<span style="font-size:10px;color:#333;background:#eee;border-radius:3px;padding:1px 3px;margin-left:2px;">{label}</span>'
                else:
                    display_label = ""
                highlighted_text += (
                    f'<span style="background-color:{bgcolor};padding:2px 4px;border-radius:4px;margin:2px;display:inline-block;">'
                    f'{token} {display_label}</span> '
                )
            st.markdown(highlighted_text, unsafe_allow_html=True)

            # --- Save interaction to log file ---
            import json
            import os
            from datetime import datetime

            log_entry = {
                "input_text": input_text,
                "pred_tokens": pred_tokens[:min_len],
                "pred_labels": pred_labels[:min_len],
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            log_path = "interaction_log.json"
            # Load existing log or start new
            if os.path.exists(log_path):
                with open(log_path, "r", encoding="utf-8") as f:
                    try:
                        log_data = json.load(f)
                    except json.JSONDecodeError:
                        log_data = []
            else:
                log_data = []
            # Append new entry and save
            log_data.append(log_entry)
            with open(log_path, "w", encoding="utf-8") as f:
                json.dump(log_data, f, indent=2, ensure_ascii=False)
        else:
            st.warning("Please enter some text to analyze.")

if __name__ == "__main__":
    main()
