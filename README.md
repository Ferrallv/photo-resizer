# photo-resizer
photo-resizer is a command-line app that will resize the images in the current directory to fit the aspect ratios required by DoorDash and UberEats.

By default, the application compares the current aspect ratio to the desired aspect ratio in deciding the least destructive cropping option (to crop by width or height).

The application can also pad the image with white bordering to create the appropriate aspect ratio.

Images can be proportionately scaled down (or up, but it's not recommended) to meet filesize requirements.

## Method
Be sure to create an environment using either the environment.yml or requirements.txt file.

Activate the environment and copy the application to the directory where the images you would like to edit are. You can do that with something like:
~~~ commandline
cp app.py Users/Desktop/your/images/here
~~~

Run the application from the command-line using:
~~~ commandline
python app.py
~~~

The application accepts some command-line arguments. Available options are available using `-h`.

The `--pad` flag will pad the images with white to reach the desired aspect ratio.

The `--reduce` flag followed by an integer will scale the image by the percentage indicated by the integer.

