# JavaScript - Warm Up

This repository contains various JavaScript scripts designed to introduce and reinforce fundamental JavaScript concepts. These exercises are part of the SE Foundations curriculum, focusing on scripting and basic JavaScript concepts.

## Table of Contents
1. [Background Context](#background-context)
2. [Requirements](#requirements)
3. [Tasks](#tasks)

## Background Context
JavaScript is used for many purposes including scripting and web front-end development. This project focuses on scripting to learn basic concepts of the language. Later, these skills will be applied to make our AirBnB project dynamic using JavaScript and jQuery.


## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- A `README.md` file at the root of the folder is mandatory
- Your code should be semistandard compliant (version 16.x.x)
- All files must be executable
- File lengths will be tested using `wc`

### Setup
1. **Install Node 14**:
    ```sh
    $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
    $ sudo apt-get install -y nodejs
    ```
2. **Install semistandard**:
    ```sh
    $ sudo npm install semistandard --global
    ```

## Tasks

### 0. First constant, first print
- **File**: `0-javascript_is_amazing.js`
- **Description**: Write a script that prints “JavaScript is amazing”.
    - Create a constant variable called `myVar` with the value “JavaScript is amazing”.
    - Use `console.log(...)` to print all output.
    - Do not use `var`.
    
    ```sh
    $ ./0-javascript_is_amazing.js 
    JavaScript is amazing
    ```

### 1. 3 languages
- **File**: `1-multi_languages.js`
- **Description**: Write a script that prints 3 lines.
    - The first line: “C is fun”
    - The second line: “Python is cool”
    - The third line: “JavaScript is amazing”
    - Use `console.log(...)` to print all output.
    - Do not use `var`.

    ```sh
    $ ./1-multi_languages.js 
    C is fun
    Python is cool
    JavaScript is amazing
    ```

### 2. Arguments
- **File**: `2-arguments.js`
- **Description**: Write a script that prints a message depending on the number of arguments passed.
    - If no arguments are passed to the script, print “No argument”.
    - If only one argument is passed to the script, print “Argument found”.
    - Otherwise, print “Arguments found”.
    - Use `console.log(...)` to print all output.
    - Do not use `var`.

    ```sh
    $ ./2-arguments.js 
    No argument
    $ ./2-arguments.js Best
    Argument found
    $ ./2-arguments.js Best School
    Arguments found
    ```

### 3. Value of my argument
- **File**: `3-value_argument.js`
- **Description**: Write a script that prints the first argument passed to it.
    - If no arguments are passed to the script, print “No argument”.
    - Use `console.log(...)` to print all output.
    - Do not use `var`.
    - Do not use `length`.

    ```sh
    $ ./3-value_argument.js 
    No argument
    $ ./3-value_argument.js School
    School
    ```

### 4. Create a sentence
- **File**: `4-concat.js`
- **Description**: Write a script that prints two arguments passed to it, in the following format: `<arg1> is <arg2>`.
    - Use `console.log(...)` to print all output.
    - Do not use `var`.

    ```sh
    $ ./4-concat.js c cool
    c is cool
    $ ./4-concat.js c 
    c is undefined
    $ ./4-concat.js
    undefined is undefined
    ```

### 5. An Integer
- **File**: `5-to_integer.js`
- **Description**: Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer.
    - If the argument can’t be converted to an integer, print “Not a number”.
    - Use `console.log(...)` to print all output.
    - Do not use `var`.
    - Do not use `try/catch`.

    ```sh
    $ ./5-to_integer.js 
    Not a number
    $ ./5-to_integer.js 89
    My number: 89
    $ ./5-to_integer.js "89"
    My number: 89
    $ ./5-to_integer.js 89.89
    My number: 89
    $ ./5-to_integer.js School
    Not a number
    ```

### 6. Loop to languages
- **File**: `6-multi_languages_loop.js`
- **Description**: Write a script that prints 3 lines (like `1-multi_languages.js`) but using an array of strings and a loop.
    - The first line: “C is fun”
    - The second line: “Python is cool”
    - The third line: “JavaScript is amazing”
    - Use `console.log(...)` to print all output.
    - Do not use `var`.
    - Do not use any `if/else` statement.
    - Use only one `console.log`.
    - Use a loop (`while`, `for`, etc.).

    ```sh
    $ ./6-multi_languages_loop.js 
    C is fun
    Python is cool
    JavaScript is amazing
    ```

### 7. I love C
- **File**: `7-multi_c.js`
- **Description**: Write a script that prints `x` times “C is fun”.
    - Where `x` is the first argument of the script.
    - If the first argument can’t be converted to an integer, print “Missing number of occurrences”.
    - Use `console.log(...)` to print all output.
    - Do not use `var`.
    - Use only two `console.log`.
    - Use a loop (`while`, `for`, etc.).

    ```sh
    $ ./7-multi_c.js 2
    C is fun
    C is fun
    $ ./7-multi_c.js 5
    C is fun
    C is fun
    C is fun
    C is fun
    C is fun
    $ ./7-multi_c.js 
    Missing number of occurrences
    ```

### 8. Square
- **File**: `8-square.js`
- **Description**: Write a script that prints a square.
    - The first argument is the size of the square.
    - If the first argument can’t be converted to an integer, print “Missing size”.
    - Use the character `X` to print the square.
    - Use `console.log(...)` to print all output.
    - Do not use `var`.
    - Do not use `if/else` statement.
    - Use a loop (`while`, `for`, etc.).

    ```sh
    $ ./8-square.js 2
    XX
    XX
    $ ./8-square.js 6
    XXXXXX
    XXXXXX
    XXXXXX
    XXXXXX
    XXXXXX
    XXXXXX
    $ ./8-square.js 
    Missing size
    ```

### 9. Add
- **File**: `9-add.js`
- **Description**: Write a script that prints the addition of two integers.
    - The first argument is the first integer.
    - The second argument is the second integer.
    - Define a function named `add` that returns the addition of the two integers.
    - Use `console.log(...)` to print all output.
    - Do not use `var`.

    ```sh
    $ ./9-add.js 
    NaN
    $ ./9-add.js 1
    NaN
    $ ./9-add.js 1 7
    8
    ```

### 10. Factorial
- **File**: `10-factorial.js`
- **Description**: Write a script that computes and prints a factorial.
    - The first argument is the integer used for computing the factorial.
    - Define a function named `factorial` that returns the factorial of a given number.
    - Use `console.log(...)` to print all output.
    - Do not use `var`.
    - You must use recursion.

    ```sh
    $ ./10-factorial.js 
    1
    $ ./10-factorial.js 3
    6
    $ ./10-factorial.js 89
    1.650796e+136
    $ ./10-factorial.js 200
    7.886579e+374
    $ ./10-factorial.js -4
    1
    ```

### 11. Second biggest!
- **File**: `11-second_biggest.js`
- **Description**: Write a script that searches for the second biggest integer in the list of arguments.
    - You can assume all arguments can be converted to integer.
    - If no argument is passed, print `0`.
    - If the number of arguments is 1, print `0`.
    - Use `console.log(...)` to print all output.
    - Do not use `var`.

    ```sh
    $ ./11-second_biggest.js 
    0
    $ ./11-second_biggest.js 1
    0
    $ ./11-second_biggest.js 4 2 6 9 7 3
    7
    ```

### 12. Object
- **File**: `12-object.js`
- **Description**: Update the script to replace the value `12` with `89`.
    - You are not allowed to use `var`.
    - You should print the object before and after modifying it.

    ```sh
    $ ./12-object.js 
    { type: 'object', value: 12 }
    { type: 'object', value: 89 }
    ```

### 13. Add file
- **File**: `13-add.js`
- **Description**: Write a function that returns the addition of two integers.
    - The function must be visible from outside.
    - The name of the function must be `add`.
    - You are not allowed to use `var`.

    ```js
    exports.add = function (a, b) {
      return a + b;
    };
    ```

    - Test with the following script:

    ```sh
    $ cat 13-main.js 
    #!/usr/bin/node
    const add = require('./13-add').add;
    console.log(add(3, 5));
    $ ./13-main.js 
    8
    ```
