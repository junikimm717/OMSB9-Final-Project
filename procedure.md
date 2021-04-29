# Procedure for carrying out an experiment

The following contains instructions for carrying out the experiment on a
particular test subject to yield desired results.

# Setting up the program

Please check the README for details on this

# Setup

The participant should be placed on a desk or table of reasonable size.
Place the computer to full screen, go to localhost:5000 on your browser in
order to access the website. 

It is recommended to place a thin object directly in front of the participant
as a means of allowing them to direct their vision correctly, thus allowing us
to test peripheral vision.

Once on the page, enter the participant's ID (or whatever way by which you wish
to identify the participant) and the first time that you would like to test.

# Testing

Once on the testing page, note that, if you are lazy, you can change the
time tested by modifying the GET parameters on the URL string. However, most of
the information should already be filled out based on what you previously put.

Before beginning the test, type the angle at which you are testing the
participant's peripheral vision (should be 0, 30, or 60).

Now click the button labeled "Conduct Test" in order to flash an image
containing an unknown number of dots. After the image has been flashed, ask the
participant to indicate how many dots they believe were on the picture.

Click "Submit" and you will be redirected to a handler page that records the
necessary data on your local computer in a file called "data.txt".

# Test table

|     | 0 degrees | 30 degrees | 60 degrees |
| --- | --- | --- | --- |
| 250ms | 5 | 5 | 5 |
| 500 ms | 5 | 5 | 5 |
| 750 ms | 5 | 5 | 5 |
| 1000 ms | 5 | 5 | 5 |

# Post-experiment

Copy the contents of data.txt to another file and send me the results in
whatever method that works.
