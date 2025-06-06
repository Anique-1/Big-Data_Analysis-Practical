# Data Analysis with NumPy, Scikit-learn, Matplotlib, and Seaborn Guide

This repository contains examples and explanations for working with NumPy arrays, scikit-learn machine learning tools, and data visualization using Matplotlib and Seaborn.

## Table of Contents
- [NumPy Basics](#numpy-basics)
  - [1D Arrays](#1d-arrays)
  - [Array Operations](#array-operations)
  - [Array Manipulation](#array-manipulation)
- [Scikit-learn](#scikit-learn)
  - [Feature Selection](#feature-selection)
  - [Model Training](#model-training)
- [Matplotlib](#matplotlib)
  - [Basic Plots](#basic-plots)
  - [Customization](#customization)
  - [Subplots](#subplots)
- [Seaborn](#seaborn)
  - [Statistical Plots](#statistical-plots)
  - [Distribution Plots](#distribution-plots)
  - [Categorical Plots](#categorical-plots)

## NumPy Basics

### Installation
```bash
pip install numpy
```

### 1D Arrays

NumPy provides several ways to create 1D arrays:

```python
import numpy as np

# Create array from list
basic_array = np.array([1, 2, 3, 4, 5])

# Create array with range
range_array = np.arange(10, 21, 1)  # Start=10, Stop=21, Step=1
# Output: [10 11 12 13 14 15 16 17 18 19 20]

# Create array of zeros
zeros_array = np.zeros(5)  # Creates [0. 0. 0. 0. 0.]

# Create array of ones
ones_array = np.ones(5)    # Creates [1. 1. 1. 1. 1.]

# Create evenly spaced numbers
linspace_array = np.linspace(0, 2, 5)  # 5 numbers from 0 to 2
```

### Array Operations

#### Basic Operations
```python
# Array arithmetic
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Addition
sum_array = array1 + array2  # [5, 7, 9]

# Multiplication
product = array1 * array2    # [4, 10, 18]

# Statistics
mean = array1.mean()         # 2.0
median = np.median(array1)   # 2.0
std = array1.std()          # Standard deviation
```

#### Array Indexing and Slicing
```python
array = np.array([10, 11, 12, 13, 14, 15])

# Basic slicing
first_three = array[0:3]    # [10, 11, 12]
last_two = array[-2:]       # [14, 15]
every_second = array[::2]   # [10, 12, 14]
```

### Array Manipulation

#### Reshaping Arrays
```python
# Convert 1D to 2D
array_1d = np.array([1, 2, 3, 4, 5, 6])
array_2d = array_1d.reshape((2, 3))  # 2 rows, 3 columns
# Result:
# [[1, 2, 3],
#  [4, 5, 6]]

# Add new axis
array_expanded = array_1d[:, np.newaxis]
# Converts [1, 2, 3] to [[1], [2], [3]]
```


#### Concatenation
```python
# Horizontal concatenation (1D)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
horizontal = np.concatenate((array1, array2))
# Result: [1, 2, 3, 4, 5, 6]

# Vertical concatenation (2D)
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
vertical = np.concatenate((a, b), axis=0)
# Result:
# [[1, 2],
#  [3, 4],
#  [5, 6],
#  [7, 8]]
```

## Scikit-learn

### Installation
```bash
pip install scikit-learn
```

### Feature Selection

#### Using SelectKBest
```python
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.datasets import load_breast_cancer

# Load dataset
X, y = load_breast_cancer(return_X_y=True)

# Select top 5 features
selector = SelectKBest(mutual_info_classif, k=5)
X_selected = selector.fit_transform(X, y)
```

#### Using VarianceThreshold
```python
from sklearn.feature_selection import VarianceThreshold

# Remove features with low variance
selector = VarianceThreshold(threshold=0.5)
X_selected = selector.fit_transform(X)
```

### Model Training

#### Classification Example
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
```

#### Cross Validation
```python
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

# Perform 10-fold cross validation
models = [
    LogisticRegression(max_iter=1000),
    DecisionTreeClassifier(),
    RandomForestClassifier(),
    GaussianNB()
]

for model in models:
    scores = cross_val_score(model, X, y, cv=10)
    print(f"{model.__class__.__name__}:")
    print(f"Mean accuracy: {scores.mean():.2f}")
    print(f"Standard deviation: {scores.std():.2f}")
```

## Common NumPy Functions Reference

### Array Creation Functions
- `np.array()`: Create array from list
- `np.arange()`: Create array with range of numbers
- `np.zeros()`: Create array filled with zeros
- `np.ones()`: Create array filled with ones
- `np.identity()`: Create identity matrix
- `np.linspace()`: Create evenly spaced numbers
- `np.random.rand()`: Create array with random values

### Array Information
- `array.shape`: Get dimensions
- `array.size`: Get total number of elements
- `array.ndim`: Get number of dimensions
- `array.dtype`: Get data type

### Array Manipulation
- `array.reshape()`: Change array shape
- `array.transpose()`: Transpose array
- `np.concatenate()`: Join arrays
- `np.expand_dims()`: Add new axis
- `array.flatten()`: Convert to 1D array

### Mathematical Operations
- `np.sum()`: Sum of elements
- `np.mean()`: Mean of elements
- `np.std()`: Standard deviation
- `np.min()`: Minimum value
- `np.max()`: Maximum value
- `np.sort()`: Sort array

## Best Practices

1. Always import NumPy as `np`
2. Use appropriate data types to save memory
3. Vectorize operations instead of using loops
4. Use built-in NumPy functions for better performance
5. Be careful with memory usage for large arrays
6. Use appropriate axis parameter for operations on multi-dimensional arrays

## Additional Resources

- [NumPy Documentation](https://numpy.org/doc/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [NumPy Cheat Sheet](https://numpy.org/doc/stable/user/cheatsheet.html)

## Matplotlib

### Installation
```bash
pip install matplotlib
```

### Basic Plots

#### Line Plot
```python
import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create figure and axis
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.legend()
plt.show()
```

#### Scatter Plot
```python
# Create random data
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar()
plt.show()
```

#### Bar Plot
```python
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='skyblue')
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
```

### Customization

#### Styling
```python
# Set style
plt.style.use('seaborn')

# Customize plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 
         color='red',
         linestyle='--',
         linewidth=2,
         marker='o',
         markersize=8,
         label='Data')
plt.title('Customized Plot', fontsize=16)
plt.xlabel('X-axis', fontsize=14)
plt.ylabel('Y-axis', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
```

### Subplots
```python
# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Plot 1
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Sine')

# Plot 2
axes[0, 1].plot(x, np.cos(x))
axes[0, 1].set_title('Cosine')

# Plot 3
axes[1, 0].plot(x, np.tan(x))
axes[1, 0].set_title('Tangent')

# Plot 4
axes[1, 1].plot(x, np.exp(x))
axes[1, 1].set_title('Exponential')

plt.tight_layout()
plt.show()
```

## Seaborn

### Installation
```bash
pip install seaborn
```

### Statistical Plots

#### Box Plot
```python
import seaborn as sns
import pandas as pd

# Create sample data
data = pd.DataFrame({
    'Category': ['A']*50 + ['B']*50,
    'Value': np.random.normal(0, 1, 100)
})

sns.boxplot(x='Category', y='Value', data=data)
plt.title('Box Plot')
plt.show()
```

#### Violin Plot
```python
sns.violinplot(x='Category', y='Value', data=data)
plt.title('Violin Plot')
plt.show()
```

### Distribution Plots

#### Histogram
```python
sns.histplot(data=data, x='Value', bins=30, kde=True)
plt.title('Histogram with KDE')
plt.show()
```

#### KDE Plot
```python
sns.kdeplot(data=data, x='Value', hue='Category')
plt.title('Kernel Density Estimation')
plt.show()
```

### Categorical Plots

#### Bar Plot
```python
sns.barplot(x='Category', y='Value', data=data)
plt.title('Seaborn Bar Plot')
plt.show()
```

#### Count Plot
```python
sns.countplot(x='Category', data=data)
plt.title('Count Plot')
plt.show()
```

#### Heatmap
```python
# Create correlation matrix
corr = data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
```

### Advanced Features

#### Pair Plot
```python
# Create sample data
iris = sns.load_dataset('iris')
sns.pairplot(iris, hue='species')
plt.show()
```

#### Joint Plot
```python
sns.jointplot(x='sepal_length', y='sepal_width', data=iris, kind='scatter')
plt.show()
```

#### Facet Grid
```python
g = sns.FacetGrid(iris, col='species')
g.map(sns.histplot, 'sepal_length')
plt.show()
```

## Best Practices for Visualization

1. Choose appropriate plot types for your data
2. Use consistent color schemes
3. Label axes and add titles
4. Use appropriate figure sizes
5. Add legends when necessary
6. Use appropriate font sizes
7. Consider colorblind-friendly palettes
8. Use grid lines when helpful
9. Keep plots clean and uncluttered
10. Save plots in appropriate formats (PNG for web, PDF for print)

## Additional Resources

- [NumPy Documentation](https://numpy.org/doc/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [NumPy Cheat Sheet](https://numpy.org/doc/stable/user/cheatsheet.html)
- [Matplotlib Cheat Sheet](https://matplotlib.org/cheatsheets/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
