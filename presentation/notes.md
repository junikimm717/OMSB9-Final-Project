# Topic

- Subitization (see a image with a small number of objects, instant)
- Why cultures generally create a symbol after 4.
- Peripheral vision (check if one needs to focus on vision) and reaction time
- Constraints, 3 values for angle and 4 for reaction time.

# Methodology

- Collected 5 people, as I was constrained by COVID (mostly people from my proximity)

- In order to measure the accuracy of the answers, manual testing was futile.

- As I would have to do many tests, I have a sheet of paper with markings on it
so that I can consistently put my laptop at the same angles.

- Participant looks at a thin object in front of them so that they can look straight.

- I created a set of PHP scripts to run on localhost and send logs (just before
        I learned how to use MongoDB)

- Testing page, autofilled some information (participant's name and reaction time)

- Depending on the reaction time being tested, I have some javascript running
that flashes the appropriate image for the allocated number of time.

- After this is collected, the submit redirects to a handler, which will log the result.

# Tests

- I had a lot of variables that I was testing, so I just decided to do 4 statistical tests.
(also because I have the power of pythontex)

- PMCC for testing the precision of results against the number that was actually displayed.
(more or less a sanity test)

- SRCC for testing against time (do we see a monotonic correlation between time and precision?)

- ANOVA for testing if results across different modes of vision were statistically significantly different.
(absolute deviations from the answer)

- T-test for comparing near and far peripheral vision
(same as above)
