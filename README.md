# MPwI_Lab_3
Application created for 'Metody Probabilistyczne w Informatyce' course at Gdansk University of Technology.
Author: Łukasz Zdziarski
## Note
Both generators are made to be customizable by the user. In order to achieve this Inverted Distrubiution Generator can be constructed with intervals that do not add up to 1, or add up to more than one. Implementation lets this happen and handles it by taking the first random number from a smaller/wider range, depending on what do the intervals sum up to.  
Elimination Generator does not print out U2: f(U1), unless the '10000 values' option is selected. In every other case it just returns f(U1).
