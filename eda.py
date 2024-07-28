import matplotlib.pyplot as plt
import seaborn as sns

# Calculate churn rate
def calculate_churn_rate(df):
    churn_rate = df['Exited'].mean() * 100
    return churn_rate

# Visualize churn distribution across various customer segments
def visualize_churn_distribution(df):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Churn distribution by Geography
    sns.countplot(x='Geography', hue='Exited', data=df, ax=axes[0])
    axes[0].set_title("Churn by Geography")
    
    # Churn distribution by Gender
    sns.countplot(x='Gender', hue='Exited', data=df, ax=axes[1])
    axes[1].set_title("Churn by Gender")
    
    plt.tight_layout()
    return fig

