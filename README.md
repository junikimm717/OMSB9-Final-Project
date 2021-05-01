# Juni's MSB Final Project (Re-done with a new topic)

This project will concern the collection of experimental results of subitizing within peripheral
vision.

The website is **meant** to be run on localhost, and will send all appropriate
data to a file called data.txt.

With the data that I have, I will be able to

1. Conduct an ANOVA test to determine if subitizing speed and accuracy depends
   on angle viewed, and

2. Conduct a simple linear regression to determine how accurate participants
   are with certain numbers over others (and do the same over angle).

# Technology stack

- Plain old PHP (Django took too long for me to RTFM for)

- Vanilla Javascript

- Python (for data analysis)

# Running

If you **really** want to run this script, do the following:

```sh
git clone https://github.com/junikimm717/OMSB9-final-project.git
cd OMSB9-final-project/website
php -S localhost:5000
```

# Python Scripts

In order to run the scripts,

```sh
cd analysis
./analyze.py (number) (True if you want a graph, only works with certain functions)
```

## Functions

- 1 - Prints Linear Regression Data (graphs the scatter plot and linear regression)

- 2 - Prints SRCC Test across reaction times. (graphs frequencies of each deviation.)

- 3 - Prints an ANOVA across all of the tested angles of peripheral vision **(no graphing)**

- 4 - Prints a T-test between near and medium peripheral vision (30 and 60
        degrees) **(no graphing)**


# Notices

- As this solution is hacked together, you should not test for reaction times under 150ms.
