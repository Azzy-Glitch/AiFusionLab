News Topic Classifier Using BERT

Objective:
The objective of this task is to develop a robust news topic classification system using transformer-based models, specifically BERT. The system classifies news headlines into predefined topic categories, demonstrating NLP proficiency and model fine-tuning capabilities.

Dataset:
AG News dataset (available via Hugging Face Datasets), consisting of news headlines labeled with four categories: World, Sports, Business, and Science/Technology.

Methodology:
1. Dataset Preprocessing:
   - Tokenization using BERT tokenizer
   - Padding and truncation to uniform sequence length
   - Encoding labels for classification

2. Model Development:
   - Fine-tuning 'bert-base-uncased' transformer model using Hugging Face Transformers
   - Adding a classification head for four classes
   - Training with AdamW optimizer and cross-entropy loss

3. Model Evaluation:
   - Metrics: Accuracy, F1-Score (macro and weighted)
   - Validation on held-out dataset
   - Analysis of misclassified examples

4. Deployment:
   - Integrated the fine-tuned model with Streamlit/Gradio for interactive news headline classification

Key Results / Observations:
- Achieved high classification accuracy (~90% on validation)
- Model successfully differentiates between topics despite short headlines
- Fine-tuning significantly improved performance over zero-shot baselines

Skills Gained:
- NLP using Transformers
- Transfer learning and fine-tuning
- Evaluation metrics for text classification
- Interactive model deployment using Streamlit/Gradio