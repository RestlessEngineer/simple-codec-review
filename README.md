# simple-codec-review
The main goal of this repository is to provide a simple means of analyzing the quality of encoded video.\
This project contains short, simple instructions for analyzing the quality of image encoding by h264, h265 codecs. \
How to manipulate video describes [here](gstreamer_instruction.md) 

## using libraries

 - numpy
 - opencv-python
 - matplotlib

## how to use video metrics:

You may create metrics from the video file by read_video_metric.py.\
You only need to set **VIDEO_FILE_PATH** and **METRIC_FILE_PATH** for plotting statistics\
example:
```
./video_anilize.py --video_file VIDEO_FILE_PATH --output_file OUTPUT_VIDEO_FILE_PATH --data_file METRIC_FILE_PATH
```

for more information:
```
./video_anilize.py --help
```

## how to use plot statistics:
You may visualize all metrics from METRIC_FILE generated by **./video_anilize.py**
For example you have 5 *.dat files with names **'bunny_short_original.dat' 'bunny_shortb2000.dat' 'bunny_shortb4000.dat' 'bunny_shortb8000.dat' 'bunny_shortb16000.dat'** and you want to distinguish them with labels **'raw_video' 'h264enc btrate=2000' 'h264enc btrate=4000' 'h264enc btrate=8000' 'h264enc btrate=16000'**. Also, you want to save the figure and see it before saving this one. So you need to run the next command:
```
./plot_statistic.py --directory /home/vladislav/Videos/ --plot_names 'raw_video' 'h264enc btrate=2000' 'h264enc btrate=4000' 'h264enc btrate=8000' 'h264enc btrate=16000' --metric_files 'bunny_short_original.dat' 'bunny_shortb2000.dat' 'bunny_shortb4000.dat' 'bunny_shortb8000.dat' 'bunny_shortb16000.dat' --save_figure --show_figure
```
and you would see for contours:\
![Contour Image](images/contours%20h264enc.png) \
\
for average radiuses:\
![Radius Image](images/radiuses%20h264enc.png) \
\
So now you want to compare only images with bitrate 2000 kbit/sec. Just run following command:

```
./plot_statistic.py --directory /home/vladislav/Videos/ --plot_names 'raw_video' 'h264enc btrate=2000' 'h265enc btrate=2000' --metric_files 'bunny_short_original.dat' 'bunny_shortb2000.dat' 'bunny_short265b2000.dat' --save_figure --figure_name 'btrate=2000'
```

You might see for contours:\
![Contour Image](images/contours%20btrate=2000.png) \
\
for average radiuses:\
![Radius Image](images/radiuses%20btrate=2000.png) \


for more information:
```
./plot_statistic.py --help
```