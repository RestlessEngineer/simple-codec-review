#!/usr/bin/env python3

import matplotlib.pyplot as plt
import math

def plot_statistic(values: list[list[int]], plot_names: list[str], title_axis: tuple[str, str], show_figure = True, save_figure = True):
    if len(values) != len(radiuses) != len(plot_names):
        raise Exception(f"count of countours radiuses and names must be equal. \
                        current sizes {len(values)}, {len(radiuses)}, {len(plot_names)}")
    
    figure_name, value_name = title_axis

    fig = plt.figure(figure_name)
    plt.title(figure_name)

    plt.xlabel("frame number")
    plt.ylabel(value_name)
    for i in range(len(values)):
        plt.plot(values[i], label=plot_names[i])
    plt.legend()

    if save_figure:
        plt.savefig(figure_name + ".png")        
    
    if show_figure:
        plt.show()
    plt.close(fig)     


def read_statistic(file_names: list[str]) -> tuple[list[list[int]], list[list[int]]]:
    contours = []
    radiuses = []
    for name in file_names:
        contour = []
        radius = []
        with open(name,'r') as f:
            contour = list(map(int, f.readline().split()))
            radius = list(map(float, f.readline().split()))
        contours.append(contour)
        radiuses.append(radius)

    return contours, radiuses


import argparse

parser = argparse.ArgumentParser(description="Example script with command-line arguments")

parser.add_argument("--metric_files", nargs='+', type=str, default=None, help="pathes to metric files")
parser.add_argument("--plot_names", nargs='+', type=str, default=None, help="names for labels in figure")
parser.add_argument("--figure_name", type=str, default="encode", help="figure name for saving")
parser.add_argument("--directory", type=str, default="", help="directory with metric files")
parser.add_argument("--save_figure", action='store_true', help="set this flag to save png image or not")
parser.add_argument("--show_figure", action='store_true', help="set this flag to show figure or not")

args = parser.parse_args()

directory_path = args.directory if args.directory[-1] == '/' else args.directory 
file_names = args.metric_files 
plot_names = args.plot_names
figure_name = args.figure_name

save_figure = args.save_figure
show_figure = args.show_figure

file_names = map(lambda x: directory_path + x, file_names)

contours, radiuses = read_statistic(file_names)
plot_statistic(contours, plot_names, ('conrours ' + figure_name, 'contours count'), show_figure, save_figure)

average_radiuses = []
for i in range(len(contours)):
    couple = zip(radiuses[i], contours[i])
    average_radiuses.append(list(map(lambda x: 0 if math.isclose(x[1], 0) else x[0]/x[1], couple)))

plot_statistic(average_radiuses, plot_names, ('radiuses ' + figure_name, 'average radius'), show_figure, save_figure)