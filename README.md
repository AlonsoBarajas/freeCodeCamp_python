# freeCodeCamps solutions for all 5 problems

### Note:
This repository shows the way in which I tackled each of the 5 problems. 
I hope that this can be helpful to anyone struggling with the projects.

## 1st Problem: Arithmetic Formatter

### What the program should do
* Input
  * list of up to 5 arithmetic operations (ex. `["5 + 3","125 - 287", "9999 + 1"]`)
  * Additional optional parameter to calculate the result (ex. `(["125 - 287"], True)`)

* Output
  * Formatted arithmetic operation **with or without calculation** (Depending on the optional parameter)

    ```python
      32         1      9999      523
    +  8    - 3801    + 9999    -  49
    ----    ------    ------    -----
      40     -3800     19998      474 
    ```
### Rules
1. **The limit is _five_ problems**, anything more will return: _Error: Too many problems_.
2. **Only addition and substraction are allowed**; multiplication and division will return an error. The error returned will be: _Error: Operator must be '+' or '-'_.
3. **Each number** (operand) **should only contain digits**. Otherwise, the function will return: _Error: Numbers must only contain digits_.
4. **Each operand** (aka number on each side of the operator) **has a max of _four_ digits in width**. Otherwise, the error string returned will be: _Error: Numbers cannot be more than four digits_.

### Additional formatting
1. There should be a **single space between the operator and the longest of the two operands**, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
2. Numbers should be **right-aligned**.
3. There should be **_four_ spaces between each problem**.
4. There should be **dashes at the bottom of each problem**. The dashes should **run along the entire length of each problem individually**. (The example above shows what this should look like.)



