# GUI DEMOS
### Creates new window and displays cards.

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
