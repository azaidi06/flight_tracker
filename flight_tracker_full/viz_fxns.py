import matplotlib as mpl
mpl.use('TkAgg')

import matplotlib.pyplot as plt

def four_destination_scatter(price_data_frame, destinations):
    fig, ax = plt.subplots(2, 2, figsize=(12,10))
    axis_coord = [[0,0], [0,1], [1,0], [1,1]]
    x = 0
    colors = ['green', 'red', 'blue', 'orange']
    for destination in destinations:
        coords = axis_coord[x]
        x_vals = list(price_data_frame.columns)
        y_vals = list(price_data_frame.loc[destination])
        ax[coords[0], coords[1]].scatter(x_vals, y_vals, label = destination, color=colors[x])
        ax[coords[0], coords[1]].set_title("Prices for {}".format(destination))
        ax[coords[0], coords[1]].set_ylim([500,1000])
        x += 1   
    fig.autofmt_xdate()
    plt.show()



#plot all on a single plot - can handle > 4 destinations
#THIS WON'T LOOK CLEAN IF INCLUDING DESTINATIONS WITH MISSING VALUES
def dest_single_plot(price_data_frame, destinations):
    fig = plt.figure(figsize=(10,6))
    for destination in destinations:
        x_vals = list(price_data_frame.columns)
        y_vals = list(price_data_frame.loc[destination])
        plt.scatter(x_vals, y_vals, label=destination)

    plt.ylim([500, 1000])
    fig.autofmt_xdate()
    plt.legend(loc='best')
    plt.show()