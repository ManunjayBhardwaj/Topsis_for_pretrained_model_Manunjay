# TOPSIS Implementation for Pre-Trained Model Selection

## Overview

This repository contains a Python implementation of the **Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)**. It is a multi-criteria decision analysis (MCDA) method used to rank alternatives (e.g., pre-trained models) based on multiple criteria such as **BLEU score**, **latency**, and **perplexity**. TOPSIS helps in selecting the best model that is closest to the ideal solution and farthest from the negative-ideal solution.

---

## Working

The TOPSIS method involves the following steps:

### Step 1: Normalization
- The decision matrix (which represents the models and their respective scores for each criterion) is **normalized** to scale the criteria into comparable units. This ensures that all criteria are on the same scale and can be compared fairly.

### Step 2: Weighted Matrix
- The normalized decision matrix is then **weighted** according to the importance of each criterion. The weights represent the relative importance of each criterion in the decision-making process.

### Step 3: Ideal and Negative-Ideal Solutions
- The **ideal solution** (best possible values) and **negative-ideal solution** (worst possible values) are determined for each criterion. Whether a criterion is considered a "gain" (positive) or "loss" (negative) will influence whether we seek the maximum or minimum value for that criterion.

### Step 4: Distance Calculation
- The **Euclidean distance** of each alternative (model) from both the ideal and negative-ideal solutions is calculated. This distance represents how close or far each model is from the ideal solution.

### Step 5: TOPSIS Score and Ranking
- The **closeness** of each alternative to the ideal solution is computed as the ratio of the distance to the negative-ideal solution over the sum of the distance to the ideal and negative-ideal solutions. The models are then ranked based on their closeness scores, with the higher score indicating a better alternative.

---

## Input Data Description

| **Criteria**  | **Description**                        | **Type (Gain/Loss)** | **Weight** |
|---------------|----------------------------------------|----------------------|------------|
| BLEU Score    | Measures model performance             | Gain (+)             | 0.3        |
| Latency (ms)  | Measures processing speed              | Loss (-)             | 0.2        |
| Perplexity    | Measures prediction uncertainty        | Loss (-)             | 0.4        |

---

## Example Input

Here’s an example of how the input data is structured:

| **Model**   | **BLEU Score** | **Latency (ms)** | **Perplexity** |
|-------------|----------------|------------------|----------------|
| **Model 1** | 0.85           | 70               | 4              |
| **Model 2** | 0.67           | 30               | 6              |
| **Model 3** | 0.70           | 45               | 3              |

---

## Output

The implementation will output two key pieces of information:
1. **Rankings**: A ranking of the models based on their closeness to the ideal solution. Higher ranks indicate better alternatives.
2. **Closeness/TOPSIS Score**: The closeness score for each model, where higher values represent alternatives that are closer to the ideal solution.

### Example Output

Rankings: [1 2 3] Closeness/Topsis Score: [0.56021227 0.49703687 0.45328415]


- **Model 1** is ranked the best, as it has the highest closeness score.
- **Model 2** is ranked second.
- **Model 3** is ranked last.

The analysis demonstrates clear rankings of the models based on their closeness scores, with Model 1 being the most preferred due to its higher BLEU score and lower latency and perplexity.

---

## Conclusion

In this implementation, we applied the **TOPSIS** method to evaluate and rank pre-trained models for text generation based on multiple criteria such as **BLEU score** (performance), **latency** (speed), and **perplexity** (prediction uncertainty). 

TOPSIS is a **versatile and effective decision-making tool**, particularly useful for evaluating machine learning models or systems with multiple performance criteria. This method simplifies complex decisions, offering a **transparent and objective ranking** of alternatives. By utilizing **TOPSIS**, you can ensure that the decision-making process is grounded in a structured and well-defined approach.

---

## How to Use

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/topsis-model-selection.git
   cd topsis-model-selection
