# Python Snake game

This is python snake game as demonstrated by Engineer Man in his video https://www.youtube.com/watch?v=rbasThWVb-c
I made this project to better understand python windows-curses module.

## To run this project (in windows)

```
1. cd to directory

2. create virtual env

  py -m venv venv

3. If you are not using command prompt, open command prompt and cd to directory

4. activate the venv

  .\venv\Scripts\activate.bat

5. cd back to the root of directory, then run

  py game.py


6. play snake!

```

## Remarks

Some issues during the coding, compare to the video:

- Screen size and height can be an uneven number, dividing it by x value can result in float.
  Fixed this by rounding up the number.
- `window.addch` method should be inside a `try - except` block
