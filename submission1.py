import numpy as np


def topsis(data, weights, impacts):
    """
    Function to rank alternatives using the TOPSIS method.

    data: 2D array of alternatives (rows) and criteria (columns)
    weights: List of importance of each criterion
    impacts: List of '+' or '-' for each criterion, indicating whether higher is better ('+') or worse ('-')

    Returns the rankings and the closeness scores.
    """

    # Step 1: Convert 'impacts' to boolean array for easier use
    impacts = np.array(impacts) == '+'  # True for '+' (gain), False for '-' (loss)

    # Step 2: Convert the input data into a numpy array (just in case it’s not)
    data = np.array(data)
    weights = np.array(weights)  # Ensure weights are in numpy array format

    # Step 3: Normalize the data
    # We normalize each column by dividing by its Euclidean norm (sqrt of sum of squares)
    norm_data = data / np.sqrt((data ** 2).sum(axis=0))

    # Step 4: Apply weights to the normalized data
    weighted_data = norm_data * weights

    # Step 5: Determine the ideal (best) and negative-ideal (worst) solutions
    ideal_solution = np.max(weighted_data, axis=0) * impacts + np.min(weighted_data, axis=0) * (~impacts)
    negative_ideal_solution = np.min(weighted_data, axis=0) * impacts + np.max(weighted_data, axis=0) * (~impacts)

    # Step 6: Calculate the distance of each alternative from the ideal and negative-ideal solutions
    distance_to_ideal = np.sqrt(((weighted_data - ideal_solution) ** 2).sum(axis=1))
    distance_to_negative_ideal = np.sqrt(((weighted_data - negative_ideal_solution) ** 2).sum(axis=1))

    # Step 7: Calculate the closeness score for each alternative
    closeness = distance_to_negative_ideal / (distance_to_ideal + distance_to_negative_ideal)

    # Step 8: Rank the alternatives based on their closeness score
    rankings = closeness.argsort()[::-1] + 1  # Higher rank means better solution (1st = best)

    return rankings, closeness


# Example Usage
if __name__ == "__main__":
    # Here’s a simple example: 3 models with 3 evaluation criteria (e.g., accuracy, speed, cost)
    data = [
        [0.85, 70, 2],  # Model 1: Accuracy, Latency, Perplexity
        [0.56, 40, 9],  # Model 2
        [0.35, 35, 5],  # Model 3
    ]
    weights = [0.3, 0.2, 0.4]  # Importance of each criterion (Accuracy: 30%, Speed: 20%, Cost: 40%)
    impacts = ['+', '-', '-']  # '+' means higher value is better, '-' means lower value is better

    rankings, closeness_scores = topsis(data, weights, impacts)

    print("Rankings of Models:", rankings)
    print("Closeness Scores:", closeness_scores)
