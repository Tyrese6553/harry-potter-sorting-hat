# Harry Potter Sorting Hat

#### How to Download (Windows Only)

I've packaged this program into an executable file that can run on a Windows operating system.

__Steps to Download__:

1. At the top of this web page, locate and click on `HPSortingHat.exe` in the list of files.
2. There is a three-dot menu button at the top right, click on it and select the 'Download' option. Alternatively, you can use `Control + Shift + S` to automatically download the file.
3. You can now run the application on your computer.

#### Description

This program is a sorting hat, if you are not familiar with the fantasy world of Harry Potter, there are four houses a student can belong to: Gryffindor, Hufflepuff, Ravenclaw or Slytherin. New students don't get to decide which house they'll be in, it is up to the Sorting Hat. This hat uses magic to enter the new students' mind gaining insight into their personality, qualities and desires to find the most suitable house.

The program goes through ten questions with four options to pick from. Once all are answered, it will sort you into your house based on your answers.

#### Functions

There are four functions excluding the main function. Below is the order in which they are called:

* `get_name`
* `get_ans`
* `calculate_score`
* `get_house`

#### `get_name`

The `get_name` function is quite self-explanatory. However, instead of using `input`, it uses `InquirerPy` to get the user's name and stores it in a variable. The `inquirer.text` method includes a validation check to ensure the user enters their name. If the field is left blank, an error message appears stating to enter a name. I chose to use `InquirerPy` as it is something interesting to learn, given that it's similar to a game menu screen. This function does not take any parameters and returns the name that was given.

#### `get_ans`

This function is where the program asks the questions and returns the user's answers in a list. Once again, `InquirerPy` is used to print out the question and answer choices. The questions are stored in a standard list, but the answer choices are stored in a nested list. At each index in the list, there are four choices the user can pick from. This allows the `inquirer.select` method to display the each set of choices that corresponds with the question.

A `for` loop is used to display the questions and answers and stores the input in a list. I went with this approach to keep the code concise, efficient and readable. `enumerate` function allows the program to display both the questions and the choices, this is where the nested list comes into play. At the end of the loop, it appends the first letter of the choice (A, B, C or D). The list contains ten elements and returns it at the end of the function.

#### `calculate_score`

This function takes one parameter: the list returned from the `get_ans` function. Given that the list is already clean and each element is a letter, it makes calculating the score easier. Four variables are declared and initialised to 0, each variable represents a house. `enumerate` retrieves
the index and element. Since each question has different answers and each answer carries a different score towards the respective house, getting the index is important to ensure the correct question is being scored. After it finds the question and answer, a score is added to applicable house. Once it has gone through each question and adding the scores, a dictionary is returned, where the key is the house and the value is the score.

#### `get_house`

This function accepts one parameter given from the `calculate_score` function. It returns only the key with the maximum value.

#### `main`

Within the main function, below is how the functions are called and executed:

* The `ascii_magic` module displays a Harry Potter banner.
* `get_name` is called to prompt the user for a name, then assigns it the `name` variable.
* `get_ans` loops over the questions and answers so the user can choose their options for all ten questions. A list of answers are then stored in the `answers` variable.
* `calculate_score` now calculates the score in the background and returns a dictionary with the user's score, which is stored in a `score` variable.
* `get_house` is then called and given the dictionary with the user's score to sort them into their respective house based on their answers from the quiz. It returns the house name and stores it in the `house` variable.
* Once the house is decided, the `time.sleep` method is used to mimic the sorting hat's character and for a dramatic pause.
* `pyfiglet` displays text congratulating the user on the house they were sorted into.
* Finally, `ascii_magic` is used to display their respective house emblem.
