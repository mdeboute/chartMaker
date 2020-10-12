"""
Creates spider charts for user's
"""

# built-in modules
from math import pi

# third-party modules
import matplotlib.pyplot as plt

# my module
import user_dataframe as cd


# df = dataframe, col = column label, col_num = numeric column index, title = graph's title, color = graph's color
def make_spider(df, col, col_num, title, color):
    """
    plot user stats into a spide chart (support func to fig_setup)
    INPUT (passed by fig_setup func):
    df = dataframe, col = column label, col_num = numeric column index, title = graph's title, color = graph's color
    DATAFRAME: from dict {user_name:[use_stats_list]}
    DATAFRAME_INDEX: [name_of_stats]
    """
    columns = list(df.columns)
    index = list(df.index)

    # position of ticks on x axis in radians (coinciding beginning and end)
    # len(index) sets number of xticks (number of statistics for each user)
    angles = []  # inizializes angles list
    for n in range(0, len(index)):
        # divides the round angle (360°) in n parts and transforms the values ​of the angles from degrees to radians
        angles.append(n / float(len(index)) * 2 * pi)
    angles += angles[:1]  # equal beginning and end to close the figure (coinciding start and end point)

    #  polar subplot setup
    if len(columns) == 1:
        ax = plt.subplot(111, polar=True)
    else:
        ax = plt.subplot(len(columns), len(columns), col_num,
                         polar=True)  # various subplots in square pattern (len grid (columns) * len(columns))

    # x axis setuwp (posizione tick, label tick, color, dimension)
    plt.xticks(angles, labels=index, color='grey',
               size=8)  # angles identifies the position of the ticks, labels identifies the name of the ticks

    # extracts column from the dataframe and turns it into a list
    df_columns = [float(n) for n in df[col].tolist()]  # list containing current column (column = user stat list)
    # first and last value equal to build closed fig ([:1] repeats first value putting it at the bottom)
    df_columns += df_columns[:1]

    # setup y axis
    max_col_value = max(df_columns)  # gets maximum value of each column
    # defines step yticks (1 or 1/5 of max_col_value)
    if (max_col_value // 5) < 1:
        step = 1
    else:
        step = int(max_col_value) // 5

    # creates sequence of yticks (step 1/5 maximum DataFrame value),
    # last tick to max_col_value + step to leave space after graph and improve readability
    list_yticks = list(range(0, int(max_col_value) + step, step))
    # creates labels for yticks (convert list_yticks to list of strings)
    yticks_labels = [str(item) for item in list_yticks]
    plt.yticks(list_yticks, yticks_labels, color="grey", size=10)  # creates ticks on y axis
    plt.ylim(0, max_col_value + step)  # establishes y-axis limits

    # draws the graph with a continuous line
    ax.plot(angles, df_columns, color, linewidth=2, linestyle='solid')
    ax.fill(angles, df_columns, color, alpha=0.4)

    # setup subplot title
    plt.title(title, size=11, color=color, y=1.1)


# setup figure
def fig_setup(df):
    """
    plot figures setup

    INPUT:
    - dataframe({use_name:[use_stats_list]}
    OUTPUT:
    - matplotlib plot
    """
    my_dpi = 175
    fig = plt.figure(figsize=(1000 / my_dpi, 1000 / my_dpi), dpi=my_dpi)

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    if len(list(df.index)) > len(colors):
        colors = colors * 2

    # Loops subplot creation
    col_num = 1
    for col in df.columns.tolist():  # df.columns is numpy array --> numpy method .tolist()
        make_spider(df, col, col_num, title=f"{col}", color=colors[col_num])
        col_num += 1

    return fig    # usefull for figure manipulation or enbedding


if __name__ == '__main__':
    user_stats = cd.make_mean_dataframe()
    fig_setup(user_stats)  # creates spider charts
    plt.show()  # vizualizes graphs
