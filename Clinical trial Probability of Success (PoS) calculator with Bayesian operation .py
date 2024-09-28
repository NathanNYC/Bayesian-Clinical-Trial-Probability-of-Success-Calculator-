#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Let's first start by importing necessary libraries for the GUI and for the Bayesian calculation logic.
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Bayesian update calculation function
def update_bayesian_probability(prior_prob, adjustments):
    """
    Takes the prior probability (base rate) and a list of adjustments (positive or negative features)
    to compute the updated probability based on Bayesian odds.
    """
    prior_prob = float(prior_prob)  # Convert the prior probability input to float
    prior_odds = prior_prob / (1 - prior_prob)  # Calculate prior odds

    # Apply the positive or negative adjustments based on the feature list
    for adj in adjustments:
        if adj == "positive":
            prior_odds *= 1.1  # Apply +10% change to the odds
        elif adj == "negative":
            prior_odds *= 0.9  # Apply -10% change to the odds

    # Convert back to probability from odds
    new_prob = prior_odds / (1 + prior_odds)
    return new_prob

# Function to get the inputs from the GUI and compute the Bayesian result
def compute_result():
    try:
        prior_prob = float(prior_prob_entry.get())  # Get the prior probability from the input field
        if not (0 <= prior_prob <= 1):
            raise ValueError("Prior probability must be between 0 and 1")
        
        # Collect adjustments based on feature selections
        adjustments = []
        for i in range(10):
            if feature_checkboxes[i].get() == 1:
                adjustments.append("positive")
            elif feature_checkboxes[i].get() == -1:
                adjustments.append("negative")

        # Calculate new probability using Bayesian math
        new_prob = update_bayesian_probability(prior_prob, adjustments)

        # Display the results
        result_label.config(text=f"Updated Probability of Success: {new_prob:.4f}")

        # Update the tabular display of inputs
        summary_text = f"Prior Probability: {prior_prob:.4f}\n\nAdjustments:\n"
        for i, adj in enumerate(adjustments):
            feature = feature_entries[i].get()
            if feature:
                summary_text += f"{feature}: {'+positive' if adj == 'positive' else '-negative'}\n"
        summary_text += f"\nNew Probability of Success: {new_prob:.4f}"
        summary_label.config(text=summary_text)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main GUI window
root = tk.Tk()
root.title("Bayesian Clinical Trial Success Calculator")

# Prior probability input
prior_prob_label = tk.Label(root, text="Prior Prob - i.e. PoS base rate (0 to 1):")
prior_prob_label.grid(row=0, column=0, padx=10, pady=10)
prior_prob_entry = tk.Entry(root)
prior_prob_entry.grid(row=0, column=1, padx=10, pady=10)

# Create 10 fields for features with positive/negative checkboxes
feature_entries = []
feature_checkboxes = []
for i in range(10):
    # Feature name input field
    feature_label = tk.Label(root, text=f"Feature {i+1}:")
    feature_label.grid(row=i+1, column=0, padx=10, pady=5)
    feature_entry = tk.Entry(root)
    feature_entry.grid(row=i+1, column=1, padx=10, pady=5)
    feature_entries.append(feature_entry)
    
    # Positive/Negative Checkbox
    checkbox_var = tk.IntVar(value=0)  # 0 means no selection, 1 means positive, -1 means negative
    pos_checkbox = ttk.Radiobutton(root, text="Positive", variable=checkbox_var, value=1)
    pos_checkbox.grid(row=i+1, column=2, padx=5)
    neg_checkbox = ttk.Radiobutton(root, text="Negative", variable=checkbox_var, value=-1)
    neg_checkbox.grid(row=i+1, column=3, padx=5)
    feature_checkboxes.append(checkbox_var)

# Button to calculate the result
calc_button = tk.Button(root, text="Calculate", command=compute_result)
calc_button.grid(row=11, column=1, pady=20)

# Result display label
result_label = tk.Label(root, text="Updated Probability of Success: N/A", font=("Arial", 12, "bold"))
result_label.grid(row=12, column=0, columnspan=4, pady=10)

# Summary label to show tabular display
summary_label = tk.Label(root, text="Summary of Calculation", justify="left")
summary_label.grid(row=13, column=0, columnspan=4, padx=10, pady=10)

# Start the GUI loop
root.mainloop()


# In[ ]:




