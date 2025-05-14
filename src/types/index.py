from typing import List, Dict, Any

# Define a type for the input data to the BioBERT model
InputData = Dict[str, Any]

# Define a type for the output predictions from the BioBERT model
Prediction = Dict[str, List[str]]

# Define a type for the application state
AppState = Dict[str, Any]