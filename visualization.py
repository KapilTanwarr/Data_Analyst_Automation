
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_summary(df, output_path):
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        plt.figure()
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plot_path = os.path.join(output_path, f"{col}_distribution.png")
        plt.savefig(plot_path)
        plt.close()
