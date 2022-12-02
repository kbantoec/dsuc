import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import config


def prep_data(df):
    X = df.drop('Class', axis=1)
    X = np.array(X).astype(float)
    y = df.loc[:, 'Class']
    y=np.array(y).astype(float)
    return X, y


# Define a function to create a scatter plot of our data and labels
def plot_data(X, y, save=None):
    plt.scatter(X[y == 0, 0], X[y == 0, 1], label="Class #0", alpha=0.5, linewidth=0.15)
    plt.scatter(X[y == 1, 0], X[y == 1, 1], label="Class #1", alpha=0.5, linewidth=0.15, c='r')
    plt.legend()
    if save is not None:
        plt.savefig(config.OUTPATH / f"credit/{save}.pdf", dpi=600, transparent=True)
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv(config.DATAPATH / "chapter_1/creditcard_sampledata_3.csv", index_col=0)
    df.info()

    data = df.iloc[:, 1:].copy()
    print(data.head())

    # Explore the features available in your dataframe
    data.info()

    # Count the occurrences of fraud and no fraud and print them
    occ = data['Class'].value_counts()
    print(occ)

    # Print the ratio of fraud cases
    print(occ / len(data))

    # Create X and y from the prep_data function
    X, y = prep_data(data)

    # Plot our data by running our plot data function on X and y
    plot_data(X, y, "data")


