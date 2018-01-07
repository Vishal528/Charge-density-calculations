# Charge_density

 Overview
 ============
 The file charge_densities contains charge density values for Pt atom. 
 The Pt atom is located at [0.5,0.5] in space.
 The points where the charge densities are calculated are basically of a 120*120 grid of a square of side length 10.460582 units in the first   
 quadrant of the x-y plane.
 find_theta.py finds the minimum theta value for rotation of a vector required to cover all the points of the grid in one full rotation.
 charge_density.py finds the coordinates of points which have maximum charge densities along multiple directions.

 Dependencies
 ============
 * numpy
 * copy

 Usage 
 ============
 * Run find_theta.py and figure out the best theta possible by changing the update value for theta in every iteration (for very less theta 
   values processing may be slow)
 * Run charge_density.py in terminal.

 
