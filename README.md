# Sierpinski-Hexagon

### Description

This is a basic program I made to continue to familiarize myself more with the turtle module. It draws a Sierpinski's hexagon using a mathematical method, similar to the triangle's one.

This method consists in drawing the 6 apices of a regular hexagon and then drawing a random dot between the first apex and a random one. After that we follow two simple rules:
1. Take the last point drawn and randomly select one of the apices
2. Draw a point two thirds down the line that connects the last point drown with the selected apex. This way the new point will be closer to the selected apex than the last point drawn.

If you repeat this rules enough times you can see how the Sierpinski's hexagon is being constructed.

[Here you have the visual explanation](https://www.youtube.com/shorts/1cXDV12mv10) I used to do this in case you didn't understand it well enough.


### Usage

1. Open a terminal in the Sierpinski-Hexagon directory.
2. Run this command: `python3 main.py`
3. Enter the asked values (leave blank to use the default ones).
4. Now the turtle will automatically start drawing, just wait until it finishes.