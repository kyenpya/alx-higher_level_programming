SE Foundations - JavaScript Web jQuery Project
Project Overview
In this project, you will work with JavaScript and jQuery to manipulate web pages. You'll start by exploring basic DOM manipulation and progress to more complex tasks involving asynchronous data fetching and dynamic updates.

General
Allowed editors: vi, vim, emacs
Files must be interpreted on Chrome (version 57.0).
All files should end with a new line.
A README.md file, located at the root of the project folder, is mandatory.
Code should be compliant with the semistandard style guide using the flag --global $: semistandard *.js --global $.
Use jQuery version 3.x.
Avoid using var in your code.
Ensure that HTML pages do not reload for each action (DOM manipulation, data updates, etc.).
Importing jQuery
Include the following script in your HTML <head> section:
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>

Tasks
Task 0: No jQuery
Objective: Update the text color of the <header> element to red using plain JavaScript.
Instructions: Use document.querySelector to select the HTML tag. Do not use jQuery.
HTML File: 0-main.html
JavaScript File: 0-script.js

Task 1: With jQuery
Objective: Update the text color of the <header> element to red using jQuery.
Instructions: Do not use document.querySelector. Use the jQuery API.
HTML File: 1-main.html
JavaScript File: 1-script.js

Task 2: Click and Turn Red
Objective: Change the text color of the <header> element to red when clicking on <div id="red_header">.
Instructions: Use the jQuery API.
HTML File: 2-main.html
JavaScript File: 2-script.js

Task 3: Add .red Class
Objective: Add the class red to the <header> element when clicking on <div id="red_header">.
Instructions: Use the jQuery API.
HTML File: 3-main.html
JavaScript File: 3-script.js

Task 4: Toggle Classes
Objective: Toggle the class of the <header> element between red and green when clicking on <div id="toggle_header">.
Instructions: Use the jQuery API.
HTML File: 4-main.html
JavaScript File: 4-script.js

Task 5: List of Elements
Objective: Add a <li>Item</li> to <ul class="my_list"> when clicking on <div id="add_item">.
Instructions: Use the jQuery API.
HTML File: 5-main.html
JavaScript File: 5-script.js

Task 6: Change the Text
Objective: Update the text of the <header> element to "New Header!!!" when clicking on <div id="update_header">.
Instructions: Use the jQuery API.
HTML File: 6-main.html
JavaScript File: 6-script.js

Task 7: Star Wars Character
Objective: Fetch and display the character name from Star Wars API in <div id="character">.
Instructions: Use the jQuery API.
HTML File: 7-main.html
JavaScript File: 7-script.js

Task 8: Star Wars Movies
Objective: Fetch and list movie titles from Star Wars API in <ul id="list_movies">.
Instructions: Use the jQuery API.
HTML File: 8-main.html
JavaScript File: 8-script.js

Task 9: Say Hello!
Objective: Fetch and display the translation of "hello" from HelloSalut API in <div id="hello">.
Instructions: Your script must work when imported from the <head> tag. Use the jQuery API.
HTML File: 9-main.html
JavaScript File: 9-script.js
