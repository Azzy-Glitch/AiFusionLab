Task 5: Auto Tagging Support Tickets Using Large Language Models

Objective:
Automatically classify support tickets into categories using a large language model (LLM), leveraging prompt engineering, zero-shot and few-shot learning, and multi-class prediction.

Dataset:
Free-text support ticket dataset containing user-reported issues and corresponding categories.

Methodology:
1. Zero-Shot Classification:
   - Used pre-trained models (e.g., BART or FLAN-T5)
   - Classified tickets without task-specific training
   - Extracted top-3 probable tags per ticket

2. Few-Shot Learning:
   - Constructed prompts with labeled examples
   - Generated predictions using instruction-tuned LLM
   - Improved accuracy with contextual guidance

3. Fine-Tuning / Baseline:
   - Optional fine-tuned classical ML model (e.g., Logistic Regression with TF-IDF features) for comparison
   - Evaluated performance differences

4. Evaluation:
   - Metrics: Top-1 Accuracy, Top-3 Accuracy
   - Analysis of misclassified tickets for further refinement

5. Deployment:
   - Integrated with Gradio for interactive tagging interface
   - System outputs most probable tags for new support tickets

Key Results / Observations:
- Zero-shot LLM provides strong baseline predictions
- Few-shot prompt engineering improves classification for ambiguous tickets
- Multi-modal evaluation (zero-shot vs few-shot vs ML) offers insight into best deployment strategy

Skills Gained:
- Prompt engineering and LLM-based classification
- Zero-shot and few-shot learning
- Multi-class prediction and ranking
- Practical deployment with Gradio