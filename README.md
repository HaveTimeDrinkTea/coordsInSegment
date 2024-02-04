# coordsInSegment

## Description
This is my attempt at writing a function for a gaming logic. Given a scatter graph of coordinates in the X-Y axis where each set of coordinates are given a number label and a direction of "North", "East", "South", "West". 

The function should return (in any array) all the coordinates which are within a arc segment of "radiating" towards the direction associated with a specified coordinate. The arc segment is created based on user provided angle of the arc segment and also the distance (i.e. radius) of the arc segment.

### Methodology: Pseudo Code
* Ask user to select one coordinates as the point of origin (POO) from the list of coordinates.
* Ask user to specify the angle of the arc segment and also the distance (i.e. radius) of the arc segment.
* Using the radius specified by the user, parse through all other coordinates in the scatter plot to identify the coordinates which are within the direction of the arc segment radiating from the POO and within the radius. Put these coordinates into an array.
  * Calculate the values of horizontal distance (along the x-axis) and the vertical distance (along the y-axis) of the POO (ax,ay) and the potential target point (PTP) of (bx,by).
  * use pythagaus theorem to find the hypotenuse between the POO and PTP.
      * if the hypotenuse is more than the radius, then the POO is ***not*** within the view of POO
      * if the hypotenuse is less than or equal to the radius, then check the direction of the PTP w.r.t POO. Reject any coordinates which do not fit the following logic
        *  if the POO is pointing "North" then (bx-ax) >= 0 and (by-ay) >= 0
        *  if the POO is pointing "South" then (bx-ax) =< 0 and (by-ay) =< 0
        *  if the POO is pointing "East" then (bx-ax) >= 0
        *  if the POO is pointing "West" then (bx- ax) <= 0
  * now check that the remaining PTPs are within the angle of POO's vision.




## User Story

AS A gammer

I WANT to identify all the points in a scatter graph that is within my view 

SO THAT I can do something to these points that are within my "vision"





## Acceptance Criteria

* A function VisiblePoints(x, y, z) where a given point x will generate an arc segment of "vision' (in the direction associated with x) of y degrees and a radius of z. 




## Table of Contents (Optional)

* [Installation](#installation)
* [Usage](#usage)
* [Credits](#credits)
* [License](#license)
* [Features](#features)
* [Testing](#testing)
* [Contribution](#contribution)


# Installation

* N.A.


## Usage 

### Screen Dumps:





## Credits

* 



## License 

MIT License [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



## Features

### Main Features

  
### Future Developments



## Testing


## Contribution
* If you would like to contribute to this application, please contact me via
  * GitHub [https://github.com/HaveTimeDrinkTea](https://github.com/HaveTimeDrinkTea)
  * email to <havetimedrinktea@gmail.com>
