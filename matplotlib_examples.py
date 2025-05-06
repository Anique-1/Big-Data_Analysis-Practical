import numpy as np
import matplotlib.pyplot as plt

# Set style
plt.style.use('seaborn')

# 1. Basic Line Plot
def basic_line_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
    plt.title('Sine Wave')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.grid(True)
    plt.legend()
    plt.savefig('line_plot.png')
    plt.close()

# 2. Scatter Plot
def scatter_plot():
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
    plt.savefig('scatter_plot.png')
    plt.close()

# 3. Bar Plot
def bar_plot():
    categories = ['A', 'B', 'C', 'D']
    values = [10, 20, 15, 25]
    
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color='skyblue')
    plt.title('Bar Plot')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.savefig('bar_plot.png')
    plt.close()

# 4. Histogram
def histogram():
    data = np.random.normal(0, 1, 1000)
    
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, color='green', alpha=0.7)
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig('histogram.png')
    plt.close()

# 5. Pie Chart
def pie_chart():
    sizes = [30, 25, 15, 10, 20]
    labels = ['A', 'B', 'C', 'D', 'E']
    
    plt.figure(figsize=(10, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Pie Chart')
    plt.axis('equal')
    plt.savefig('pie_chart.png')
    plt.close()

# 6. Subplots
def subplots():
    x = np.linspace(0, 10, 100)
    
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
    plt.savefig('subplots.png')
    plt.close()

# 7. Customized Plot
def customized_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
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
    plt.savefig('customized_plot.png')
    plt.close()

# 8. Error Bar Plot
def error_bar_plot():
    x = np.arange(5)
    y = np.array([1, 2, 3, 4, 5])
    error = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
    
    plt.figure(figsize=(10, 6))
    plt.errorbar(x, y, yerr=error, fmt='o', capsize=5)
    plt.title('Error Bar Plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig('error_bar_plot.png')
    plt.close()

# 9. Stacked Bar Plot
def stacked_bar_plot():
    categories = ['A', 'B', 'C', 'D']
    values1 = [10, 20, 15, 25]
    values2 = [15, 10, 20, 15]
    
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values1, label='Group 1')
    plt.bar(categories, values2, bottom=values1, label='Group 2')
    plt.title('Stacked Bar Plot')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.legend()
    plt.savefig('stacked_bar_plot.png')
    plt.close()

# 10. Area Plot
def area_plot():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    plt.figure(figsize=(10, 6))
    plt.fill_between(x, y1, y2, color='skyblue', alpha=0.4)
    plt.plot(x, y1, color='blue', label='sin(x)')
    plt.plot(x, y2, color='red', label='cos(x)')
    plt.title('Area Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.savefig('area_plot.png')
    plt.close()

if __name__ == "__main__":
    # Run all plot functions
    basic_line_plot()
    scatter_plot()
    bar_plot()
    histogram()
    pie_chart()
    subplots()
    customized_plot()
    error_bar_plot()
    stacked_bar_plot()
    area_plot()
    
    print("All plots have been generated and saved as PNG files.") 