# Keyword Frequency Analysis

This Python script generates and analyzes keyword frequency distributions, comparing random and power-law distributions. It visualizes the fit of these distributions using the power-law model and performs statistical tests to evaluate the goodness of fit.

## Requirements

- `numpy`
- `powerlaw`
- `matplotlib`
- `random`
- `collections`
- `nltk`

Ensure you have the `nltk` words corpus downloaded:

```python
import nltk
nltk.download('words')
```

## Code Overview

### Generate Keywords

- 100 unique English words are randomly selected.

### Generate Frequencies

- **Set 1**: Randomly generated keyword frequencies.
- **Set 2**: Frequencies following a power-law distribution (Zipf's law).

### Fit and Compare Distributions

- Fit both sets to a power-law distribution and compare using log-likelihood ratio.
- Print results and p-values.

### Plot Results

- Visualize the frequency distributions and power-law fits for both keyword sets.


## Output

- **Keywords from Power-Law Set**: Prints top 10 keywords with their frequencies.
- **Fitting Results**: Displays alpha values and log-likelihood ratios for both random and power-law sets.
- **Plots**: Generates two plots showing the keyword frequency distributions and the power-law fit.

### Example Output

- **Random Set**:
- Alpha: 1.87
- Xmin: 1
- Log-likelihood ratio: -4.32
- p-value: 0.023

- **Power-Law Set**:
- Alpha: 2.12
- Xmin: 1
- Log-likelihood ratio: -1.56
- p-value: 0.110