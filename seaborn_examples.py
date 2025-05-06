import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set style
sns.set_style("whitegrid")

# 1. Box Plot
def box_plot():
    # Create sample data
    data = pd.DataFrame({
        'Category': ['A']*50 + ['B']*50,
        'Value': np.random.normal(0, 1, 100)
    })
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Category', y='Value', data=data)
    plt.title('Box Plot')
    plt.savefig('seaborn_box_plot.png')
    plt.close()

# 2. Violin Plot
def violin_plot():
    data = pd.DataFrame({
        'Category': ['A']*50 + ['B']*50,
        'Value': np.random.normal(0, 1, 100)
    })
    
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='Category', y='Value', data=data)
    plt.title('Violin Plot')
    plt.savefig('seaborn_violin_plot.png')
    plt.close()

# 3. Histogram with KDE
def histogram_kde():
    data = pd.DataFrame({
        'Value': np.random.normal(0, 1, 1000)
    })
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x='Value', bins=30, kde=True)
    plt.title('Histogram with KDE')
    plt.savefig('seaborn_histogram_kde.png')
    plt.close()

# 4. KDE Plot
def kde_plot():
    data = pd.DataFrame({
        'Category': ['A']*500 + ['B']*500,
        'Value': np.concatenate([np.random.normal(0, 1, 500),
                               np.random.normal(1, 1, 500)])
    })
    
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=data, x='Value', hue='Category')
    plt.title('Kernel Density Estimation')
    plt.savefig('seaborn_kde_plot.png')
    plt.close()

# 5. Bar Plot
def bar_plot():
    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 20, 15, 25]
    })
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Category', y='Value', data=data)
    plt.title('Seaborn Bar Plot')
    plt.savefig('seaborn_bar_plot.png')
    plt.close()

# 6. Count Plot
def count_plot():
    data = pd.DataFrame({
        'Category': np.random.choice(['A', 'B', 'C', 'D'], 100)
    })
    
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Category', data=data)
    plt.title('Count Plot')
    plt.savefig('seaborn_count_plot.png')
    plt.close()

# 7. Heatmap
def heatmap():
    # Create correlation matrix
    data = pd.DataFrame(np.random.randn(10, 10))
    corr = data.corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.savefig('seaborn_heatmap.png')
    plt.close()

# 8. Pair Plot
def pair_plot():
    # Load iris dataset
    iris = sns.load_dataset('iris')
    
    plt.figure(figsize=(10, 8))
    sns.pairplot(iris, hue='species')
    plt.savefig('seaborn_pair_plot.png')
    plt.close()

# 9. Joint Plot
def joint_plot():
    iris = sns.load_dataset('iris')
    
    plt.figure(figsize=(10, 8))
    sns.jointplot(x='sepal_length', y='sepal_width', data=iris, kind='scatter')
    plt.savefig('seaborn_joint_plot.png')
    plt.close()

# 10. Facet Grid
def facet_grid():
    iris = sns.load_dataset('iris')
    
    g = sns.FacetGrid(iris, col='species')
    g.map(sns.histplot, 'sepal_length')
    plt.savefig('seaborn_facet_grid.png')
    plt.close()

# 11. Regression Plot
def regression_plot():
    # Create sample data
    data = pd.DataFrame({
        'x': np.random.rand(100),
        'y': np.random.rand(100) * 2 + 1
    })
    
    plt.figure(figsize=(10, 6))
    sns.regplot(x='x', y='y', data=data)
    plt.title('Regression Plot')
    plt.savefig('seaborn_regression_plot.png')
    plt.close()

# 12. Swarm Plot
def swarm_plot():
    data = pd.DataFrame({
        'Category': ['A']*50 + ['B']*50,
        'Value': np.random.normal(0, 1, 100)
    })
    
    plt.figure(figsize=(10, 6))
    sns.swarmplot(x='Category', y='Value', data=data)
    plt.title('Swarm Plot')
    plt.savefig('seaborn_swarm_plot.png')
    plt.close()

if __name__ == "__main__":
    # Run all plot functions
    box_plot()
    violin_plot()
    histogram_kde()
    kde_plot()
    bar_plot()
    count_plot()
    heatmap()
    pair_plot()
    joint_plot()
    facet_grid()
    regression_plot()
    swarm_plot()
    
    print("All Seaborn plots have been generated and saved as PNG files.") 