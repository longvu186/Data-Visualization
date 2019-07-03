from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from pandas import read_excel
from scipy import stats
import json
from sys import stdout


def loading(value, data_list):
    stdout.write('\r')
    stdout.write('{}%'.format(round(value / len(data_list) * 100)))


# Data interpolation for smooth animation
def interpolate_lists_data(input_list, input_num):
    list_transpose = np.transpose(input_list)
    interpolated_data_transpose = []
    for row in list_transpose:
        interpolated_list = [row[0]]
        for number in range(1, len(row)):
            interpolated_list = interpolated_list + list(np.linspace(row[number - 1],
                                                                     row[number],
                                                                     num=input_num)[1:])
        interpolated_data_transpose.append(interpolated_list)
    output_data = np.transpose(interpolated_data_transpose)
    return output_data


# Read json
with open('Bar Chart Race.json', 'r') as json_file:
    json_data = json.load(json_file)

# Handle data
colors = json_data.get('colors')
time_text_color = json_data.get('time_text_color')
value_format = json_data.get('value_format')
transparent_background = json_data.get('transparent_background')
data_interpolation = json_data.get('data_interpolation')
fps = json_data.get('fps')
floating_point = json_data.get('floating_point')
font_size = json_data.get('font_size')

data_frame = read_excel('Bar Chart Race.xlsx')
time = list(data_frame['Time'])
data_frame.drop(columns='Time', inplace=True)
labels = list(data_frame)
data = data_frame.values.tolist()

# Get data ranking
data_rank = []
for item in data:
    rank_list = list(stats.rankdata(item, method='ordinal'))
    highest_rank = max(rank_list)
    for index, rank in enumerate(rank_list):
        rank_list[index] = rank + (10-highest_rank)
    for index, rank in enumerate(rank_list):
        if rank <= 0:
            rank_list[index] = rank - 1
    data_rank.append(rank_list)


# Interpolate data
time_interpolated = []
for item in time:
    time_interpolated = time_interpolated + [item for i in range(data_interpolation-1)]
data_interpolated = interpolate_lists_data(data, data_interpolation)
data_rank_interpolated = interpolate_lists_data(data_rank, data_interpolation)


# Animate data
fig, ax = plt.subplots(figsize=[19.20, 10.80])
min_rank = min(data_rank_interpolated[0])
max_rank = max(data_rank_interpolated[0])
categories_count = len(data_rank_interpolated[0])


def update(num):
    ax.clear()
    ax.tick_params(length=0, labelsize=font_size)
    plt.box(False)
    plt.grid(True, axis='x', color='#f2f2f2')
    plt.barh(data_rank_interpolated[num],
             data_interpolated[num],
             height=0.5,
             color=colors,
             zorder=3)
    max_value = float(max(data_interpolated[num]))
    plt.yticks(range(int(min_rank), int(max_rank)))
    plt.yticks(data_rank_interpolated[num], labels)
    if categories_count < 10:
        plt.axis([0, max_value, 10-categories_count, 11])
    else:
        plt.axis([0, max_value, 0, 11])
    ax.text(x=max_value*0.8,
            y=10-categories_count+0.25*categories_count,
            s=time_interpolated[num],
            fontsize=50,
            fontweight='bold',
            color=time_text_color)
    for index, value in enumerate(data_interpolated[num]):
        ax.text(x=max_value/50+value,
                y=data_rank_interpolated[num][index],
                s=value_format.format('{0:g}'.format(round(value, floating_point))),
                verticalalignment='center',
                fontsize=font_size)
    loading(num, data_rank_interpolated)


ani = animation.FuncAnimation(fig, update, frames=len(data_rank_interpolated),
                              interval=1000/fps)

if transparent_background == "true":
    ani.save('output.mov',
             codec="png",
             dpi=100,
             bitrate=-1,
             savefig_kwargs={'transparent': True,
                             'facecolor': 'none'})
else:
    ani.save('output.mp4')

plt.show()
