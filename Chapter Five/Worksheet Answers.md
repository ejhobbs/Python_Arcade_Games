# Chapter 5

1. Cartesian has all 4 quadrants, computers have the bottom right only. Y also increases as it goes further down the page, rather than up

2. `import pygame` to import the libraries, `pygame.init()` to initialise the pygame engine

3. pygame colours are specified in RGB values, so `(255,255,255)` is white

4. all upper for constants, lower for things that could change, e.g. `sky_colour`

5. sets the screen size

6. gets a list of events from the pygame engine, and iterates over them

7. used for timing for framerate

8. `screen` is the window to draw to, `[0,0]` sets the start of the line, `[100,100]` sets the end of the line, `5` sets the width of the line

9. for loop

10. shape will be filled completely with the colour

11.
    1. `20,20`
    2. the top left of the ellipse, as if it were a rectangle
    3. `250` and `100`

12. start angle, and end angle

13. load font, create image, add to display

14. you don't want to load the font multiple times

15. `(50,100)`, `(0,200)`, `(200,200)`, `(100,50)`

16. draws the objects created to the screen

17. ends the pygame engine etc.

18. `pygame.draw.circle(screen,BLACK,[100,100],20,5`