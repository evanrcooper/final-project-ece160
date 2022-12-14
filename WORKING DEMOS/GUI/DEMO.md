# GUI DEMOS
### Creates new window and displays cards.
##### Demos use tkinter in Python to create new windows and draw cards.

The math for the elipses in the center of the cards uses the regular formula for an elipse rotated using the 2D rotation matrix and then shifted over to the center of the canvas.
```
Special thanks to Professor Smyth for teaching us the math for the elipses even after office hours ended.
```

**main.py**<br />
    > Main gui script (*written in Python*).<br />
    > To run it (*on linux*), use **$python3 main.py**<br />
    > The console will ask you for a card input (*value and color*).<br />
    <br />
    > Valid inputs for card values:<br />
        >> **0-9** [any single digit] (*for basic numbered cards*) <sub>*requires color input</sub><br />
        >> **P** (*for draw two [+2] cards*) <sub>*requires color input</sub><br />
        >> **R** (*for reverse cards*) <sub>*requires color input</sub><br />
        >> **S** (*for skip cards*) <sub>*requires color input</sub><br />
        >> **C** (*for wild color cards*)<br />
        >> **P** (*for draw four [+4] cards*)<br />
        >> **B** (*for back of cards*)<br />
    <br />
    > Valid inputs for card colors (*for cards with required color inputs*):<br />
        >> **#**[**followed by 6 digit hex code**] (*example:* #**ffff00** *or* #**FFFF00** *for yellow*)<br />
        >> **css color codes** (*example:* **lime** *for css lime color**)<br />
