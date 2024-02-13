# Coordinates within an arc of vision

## Description
This is my attempt at writing a function for a gaming logic. 

Given a scatter graph of coordinates in the X-Y axis where each set of coordinates are given a number label and a direction of "North", "East", "South", "West". 

The function should return (in an array) all the coordinates which are within an arc segment "radiating" towards the direction associated with a specified coordinate. The arc segment is created based on user provided angle and distance (i.e. radius) of the arc segment.

### Methodology: Pseudo Code
* Ask user to select one numbered coordinate (1 - 20) as the point of origin (POO) from the list of coordinates.
* Ask user to specify the angle of the arc segment and also the distance (i.e. radius) of the arc segment.
* Using the radius specified by the user, parse through all other Potential Target Points (PTP) in the scatter plot to identify the PTPs which are within the direction of the arc segment radiating from the POO and within the radius. Eliminate any PTPs which are not within the radius or direction of the specific arc. 
  * Calculate the values of horizontal distance (along the x-axis) and the vertical distance (along the y-axis) of the POO (ax,ay) and the PTP (bx,by).
  * use Pythagoras theorem to find the hypotenuse between the POO and PTP.
      * if the hypotenuse is more than the radius, then the POO is ***not*** within the view of POO
      * if the hypotenuse is less than or equal to the radius, then check the direction of the PTP w.r.t POO. Reject any coordinates which do not fit the following logic
        *  if the POO is pointing "North" then (by-ay) > 0
        *  if the POO is pointing "South" then (by-ay) < 0
        *  if the POO is pointing "East" then (bx-ax) > 0
        *  if the POO is pointing "West" then (bx- ax) < 0
  * next, check that the remaining PTPs are within the angle of POO's vision.
    * first calculate the angle of made by the distance between POO and TPO using Pythagoras theorem. 
      * if the POO is pointing "North" or "South" then see if the adjacent angle (the angle touching the Y axis) is within the range
      * if the POO is pointing "East" or "West" then see if the adjacent angle (the angle touching the X axis) is within the range
    * the range of the POO is determined
      * for "North" facing, the range is hovering around the positive Y axis with half of the user provide angle on either side of the Y axis.
      * for "South" facing, the range is hovering as the "North" facing on the negative Y axis.
      * for "East" facing, the range is hovering around the positive X axis with half of the user provide angle on either side of the X axis.
      * for "West" facing, the range is hovering as the "East" facing on the negative X axis.
    * Eliminate all PTPs which do not fit into the arc segment.
*  Present the PTPs in an array to the user or return a message to say no PTP can be found. 



## User Story

AS A gammer

I WANT to identify all the points within a scatter graph that are within my view (that is defined by the direct, distance and angle of vision) 

SO THAT I can do something to these points that are within my "vision"





## Acceptance Criteria

* A function VisiblePoints(a, b, c) where a given point x will generate an arc segment of "vision' (in the direction associated with x) of y degrees and a radius of z. 




## Table of Contents (Optional)

* [Installation](#installation)
* [Usage](#usage)
* [Credits](#credits)
* [License](#license)
* [Features](#features)
* [Testing](#testing)
* [Contribution](#contribution)


# Installation

* Add the main.py to your local drive 
* run the python file in your terminal: 
```
python3 main.py
```



## Usage 

### Video Demos

#### Demo 1: Chosen point 1 with view of vision of 45 degrees and distance of 20 towards "North".

https://github.com/HaveTimeDrinkTea/coordsInSegment/assets/119045159/cdbd956c-ceac-4fc1-9bdd-e0dccb0b7381



#### Demo 2:Chosen point 3 with view of vision of 30 degrees and distance of 15 towards "South".

https://github.com/HaveTimeDrinkTea/coordsInSegment/assets/119045159/9a300a5c-7738-49e1-b4f6-0af48d3ce7b5



#### Demo 3: Chosen point 7 with view of vision of 20 degrees and distance of 10 towards the "South".

https://github.com/HaveTimeDrinkTea/coordsInSegment/assets/119045159/8de9f784-9daa-4309-8bce-3fbe8ddb0d2d



## Credits

* Example and data provided by [The Developer Academy](https://www.thedeveloperacademy.com) 



## License 

MIT License [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



## Features

Given a set of coordinates with their respective facing directions, a user can choose any coordinates in the set and find out which other coordinates can the chosen coordinate "see" based on the angle and distance of vision they specify



## Testing

This Python program has been tested by using the coordinates and point of vision values. 

Further testing can be done by creating testing script to perform the same test for very case.


## Contribution
* If you would like to contribute to this application, please contact me via
  * GitHub [https://github.com/HaveTimeDrinkTea](https://github.com/HaveTimeDrinkTea)
  * email to <havetimedrinktea@gmail.com>
