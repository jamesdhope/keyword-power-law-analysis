import numpy as np
import powerlaw
import matplotlib.pyplot as plt
import random
from collections import Counter
from nltk.corpus import words

# Ensure you have the nltk words corpus downloaded
import nltk
nltk.download('words')

# Generate 100 unique English keywords
all_words = words.words()  # List of English words
keywords = random.sample(all_words, 100)  # Randomly select 100 unique words

# Generate frequencies following a Zipf distribution
def generate_power_law_frequencies(size, a):
    frequencies = np.random.zipf(a=a, size=size)
    frequencies = frequencies[frequencies <= 100]  # Limit frequencies to top 100
    return frequencies

# Create keyword frequencies for two sets
def create_keyword_set(frequencies, keywords):
    keyword_freq = random.choices(keywords, k=len(frequencies))
    return Counter(keyword_freq)

# Generate two sets of keywords
# Set 1: Randomly selected keywords
random_frequencies = np.random.randint(1, 50, size=100)  # Random frequencies
random_keyword_freq = create_keyword_set(random_frequencies, keywords)

# Set 2: Power-law distribution
power_law_frequencies = generate_power_law_frequencies(1000, a=2.0)
power_law_keyword_freq = create_keyword_set(power_law_frequencies, keywords)

# Print the keywords from the power-law set
print("Keywords from the Power-Law Set:")
for keyword, freq in power_law_keyword_freq.most_common(10):  # Print top 10 keywords for brevity
    print(f"{keyword}: {freq}")

# Convert frequency data to lists
random_frequency_data = list(random_keyword_freq.values())
power_law_frequency_data = list(power_law_keyword_freq.values())

# Fit both sets to a power-law distribution
def fit_power_law(data):
    return powerlaw.Fit(data)

random_results = fit_power_law(random_frequency_data)
power_law_results = fit_power_law(power_law_frequency_data)

# Perform the K-S tests
random_R, random_p = random_results.distribution_compare('power_law', 'exponential')
power_law_R, power_law_p = power_law_results.distribution_compare('power_law', 'exponential')

# Print results
print("\nRandom Set - Alpha:", random_results.power_law.alpha, "Xmin:", random_results.power_law.xmin)
print("Random Set - Log-likelihood ratio:", random_R, "p-value:", random_p)
print("Power-Law Set - Alpha:", power_law_results.power_law.alpha, "Xmin:", power_law_results.power_law.xmin)
print("Power-Law Set - Log-likelihood ratio:", power_law_R, "p-value:", power_law_p)

# Plot both sets
fig, ax = plt.subplots(2, 1, figsize=(10, 12))

# Plot Random Set
ax[0].set_title('Keyword Frequency Distribution (Random)')
random_results.plot_ccdf(ax=ax[0], color='b', label='Random Data')
random_results.power_law.plot_ccdf(ax=ax[0], color='r', linestyle='--', label=f'Power-law fit: alpha={random_results.power_law.alpha:.2f}')
ax[0].legend()

# Plot Power-Law Set
ax[1].set_title('Keyword Frequency Distribution (Power-Law)')
power_law_results.plot_ccdf(ax=ax[1], color='b', label='Power-law Data')
power_law_results.power_law.plot_ccdf(ax=ax[1], color='r', linestyle='--', label=f'Power-law fit: alpha={power_law_results.power_law.alpha:.2f}')
ax[1].legend()

plt.tight_layout()
plt.show()