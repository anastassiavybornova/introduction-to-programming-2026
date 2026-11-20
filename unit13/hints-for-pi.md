# Hints for running a Monte Carlo simulation to estimate $\pi$.

<details>

<summary>Hint 0: How do we express pi?</summary>

Out of N tennis balls, we expect a certain percentage (proportional to the area) to land in the quarter-circle area. If we write down this proportionality as equation (ratio of areas equals ratio of tennis balls), plug in the values of the variables we know (radius) and reorder the variables, we get an analytical expression for $\pi$:

$\frac{A_{quartercircle}}{A_{total-area}} = \frac{N_{balls-in-quartercircle}}{N_{balls-in-total-area}}$

$A_{quartercircle}=\frac{r^{2}*\pi}{4}$

$A_{total-area}=r*r$

$r=1$

$\pi=...$

...and can use Python to figure out values for both $N_{balls}$.

</details>

<details>

<summary>Hint 1: How do we simulate many ball throws?</summary>

Create a for loop - just for the sake of "running the simulation" many, many times. You could simply iterate over a range(N) where N is large. At each step of the for-loop, "throw a tennis ball" and determine whether it is inside or outside the quarter-circle area.

</details>

<details>

<summary>Hint 2: How do we simulate ONE ball throw?</summary>

Our tennis balls are being thrown in 2-dimensional space. Each ball lands at a position with the coordinates (x,y). Both x and y are between 0 and 1, both included. So, randomly throwing a ball in Python means randomly choosing the x and y coordinates. You can treat x and y as separate variables, no need to combine them into a tuple or list. We only need them to compute whether our ball throw is inside or outside of the quarter-circle area (see hint 3).

**Use `random.uniform(0,1)` to draw a random number from 0 to 1.**

</details>

<details>

<summary>Hint 3: How do we figure out whether the ball is inside the quarter-circle?</summary>

Using what we already know about vectors and coordinates, for a point with coordinates $(x,y)$ and a circle with radius $r$:

$ \sqrt{x^2+y^2} = r$ formula for all points that are exactly ON the circle

$ \sqrt{x^2+y^2} < r$ formula for all points that are INSIDE the circle

$ \sqrt{x^2+y^2} > r$ formula for all points that are OUTSIDE the circle

In our example, $r=1$, and we can check for each randomly thrown ball (by looking at its coordinates) whether the point is *inside* or *outside* the circle. You can decide whether to include or exclude the points *exactly on* the circle -- these will be so few (if any) that it doesn't matter whether you count them or not.

</details>

<details>

<summary>Hint 4: How do we convert all of this into Python code?</summary>

Initiate the variable `in_quartercircle = 0`. Then, write a for loop that N times. N could be a million, or more. 

**At each loop step:**

1. Generate a point `(x,y)`, where both x and y coordinates are between 0 and 1, with `random.uniform(0,1)`. You can treat the `x` and `y` coordinates of each point as separate variables, no need to combine them into one object
2. Compute whether the point falls within the "quartercircle" (this is only the case if $x^2+y^2\leq 1$)
3. **If** the point is within the quartercircle, increase the value of `in_quartercircle` by 1.

**After the for-loop has finished:**

Compute an approximate value of $\pi$ as a function of `in_quartercircle` (and as a function of the total number of points).

</details>


