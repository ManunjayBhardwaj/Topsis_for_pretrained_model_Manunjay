import matplotlib.pyplot as plt

# Example data for models and their corresponding TOPSIS scores
models = ['Model 1', 'Model 2', 'Model 3']
topsis_scores = [0.56021227, 0.49703687, 0.45328415]

# Create a bar chart
plt.figure(figsize=(8, 5))  # Set the size of the figure
bars = plt.bar(models, topsis_scores, color=['#4CAF50', '#FFC107', '#2196F3'])

# Add titles and labels
plt.title("TOPSIS Scores for Models", fontsize=14)
plt.xlabel("Models", fontsize=12)
plt.ylabel("TOPSIS Score", fontsize=12)

# Set the y-axis limits (0 to 1, since TOPSIS scores are between these values)
plt.ylim(0, 1)

# Customize ticks for better readability
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Add horizontal gridlines for clarity
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding the score labels above the bars for clarity
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.02, round(yval, 2), ha='center', va='bottom', fontsize=10)

# Display the plot
plt.show()
