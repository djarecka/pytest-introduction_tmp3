<!--
  <<< Author notes: Step 2 >>>
  Start this step by acknowledging the previous step.
  Define terms and link to docs.github.com.
  TBD-step-2-notes.
-->

# Week 2: Introduction to `pytest`

In this part, we will continue working on the example from the part 1.
We will also learn about `pytest` - a testing framework for Python.

## 1 :keyboard: :white_check_mark: Exercise 1: Adding more tests

> [!TIP]
> - If you don't remember how to open Codespace, you can check the instruction in the [last week README](./week1/README.md). 
> - This exercise has :keyboard: and :white_check_mark:, that means you will have a specific task and the output will be checked by automatic tests I wrote for this course, and the repository will move to the enxt part after the task is completed.

In the new branch that was created for this week, `week2`, you will find a new directory `week2` that will be used as a working directory for this week. You can change the branch using the branch dropdown that is below the repository name.

We will start by returning to the code from the previous part that you can find in `week2/prime_factors.py`.
Last week we created a simple testing function `test_prime_factors`.
All the examples from the test are for numbers that are not prime and have more than one factor.
Now, we can add tests for prime numbers and numbers that have only one factor.
One of the examples could be a number 2, and the test could simply check the length of the list of factors:

```python
def test_prime_numbers():
    assert len(prime_factors(2)) == 1
```

1. You can add the test to `week2/prime_factors.py` file (remember to add to the `__main__` block) 
and rerun the script to check if the test passes. 
2. Add examples for other prime numbers, e.g., `7`, and run the script again. What do you see? 
If you haven't changed the function `prime_factors` you likely see that the test fails.
3. Fix the function `prime_factors`:
    - Try to read carefully the function `prime_factors` and find the reason it doesn't work for the number `7` (or other prime numbers)
    - Try to fix the function `prime_factors` and with every change, run the script `prime_factors.py` to check if the function works correctly for all the examples.
    - If you can't find the reason the function doesn't work, you can take a look at the solution in the `week2/solutions` directory,
and correct the function in the `week2/prime_factors.py` file. 
Don't forget to run the script again to check if the function works correctly for all the examples.


## 2 :book: :keyboard: Introduction to `pytest`

As we saw in the previous exercise, we can use run the script with testing functions using `assert` statements, 
but it is not the most efficient way to test the code.
As you probably noticed, there are a lot of repetitions and "boilerplate" code that you need to write on your own.
You also don't have a clear overview of which tests passed and which failed and the script stops after the first failed test.
This could be improved by writing more complex scripts, but it would require even more time and effort from you.
This is why many developers use testing frameworks that help them to write tests more efficiently and provide a clear overview of the test results.
In Python, one of the most popular testing frameworks is `pytest`.

Pytest is not a part of the python standard library, so if you want to use it on your own laptop, 
you should install it by running `pip install pytest` in your terminal, but it is already installed in the Codespace environment.

Pytest is well known for being easy to use when writing small tests, 
but it also scales to support complex functional testing for applications and libraries.
The simplest tests written in pytest are based on the `assert` statement, that we practiced in previous exercises, 
but pytest provides a lot of additional features that make writing tests easier and more efficient.

In fact, we can even use the tests that we wrote in the previous exercise in the pytest framework.
To do this, you can run in the terminal:

```bash
pytest week2/prime_factors.py
```

This will run all the tests that are in the `week2/prime_factors.py` file.
In order to see the output of the tests, you can run the command with the `-v` flag:

```bash
pytest -v week2/prime_factors.py
```

The reason pytest knows which functions are tests is that they are named with the `test_` prefix,
you don't need to actually call the test in the `__main__` block for pytest to run them.
You should remove the block and run pytest again.

It is accustomed keeping the tests in separate files, e.g., `week2/test_prime_factors.py`,
and then you can run pytest without any arguments. 
It will search for all the files that have the `test_` prefix in the current directory and all subdirectories.

## 3 :book: Introduction to `parametrize` feature

One of the annoying thing when we wrote our tests was that we had multiple repeated lines in order to test more cases.
Pytest offers a very simple, but powerful, solution by introducing `parametrize` feature.
The `parametrize` feature allows you to create a test function with arguments
and run the test for multiple values of the arguments.

In order to use the `parametrize` feature, you have to add `@pytest.mark.parametrize` decorator above the test function.
The decorator takes two arguments: a string with the names of the test arguments that you want to parametrize (in our case that will be the number and the expected output) separated by commas, and a list of tuples with the specific values, e.g.,

```python
import pytest

@pytest.mark.parametrize("number, expected", [
    (2, [2]),
    (7, [7]),
    (8, [2, 2, 2]),
    (18, [2, 3, 3]),
    (108, [2, 2, 3, 3, 3]),
])
def test_prime_factors(number, expected):
    assert prime_factors(number) == expected
```
So now you can easily separate the testing function itself, that is only one line in our example, and the list of values that you want to test, that could be always extended. 


## 4 :keyboard: :white_check_mark: Exercise 1: Using `pytest` for testing

In this exercise, we will create a separate file for the tests 
and learn how to make the tests shorter and more efficient using pytest features.

1. Move all the test functions to the new file: `week2/test_prime_factors.py`

   After moving the test functions, you should remove the `__main__` block from the `week2/prime_factors.py` file, and import the `prime_factors` function in the new test file.
Once this is done, you can run the tests using a simple `pytest -v` command.
In case you experience any problems, you can check the solution in the `week2/solutions` directory.
> [!TIP]
> - You can use a relative import to import the function by adding on top of the `test_prime_factors.py` line: `from .prime_factors import prime_factors`.
> - In order to use relative imports, you would need to include an `__init__.py` flie inside `week2`. You can simply use touch command: `touch __init__.py`.


2. Simplify the `assert` statements

   Remember that in the previous section you had to write the assert message for every test case? 
You don't have to do it anymore! Pytest will provide you with a clear overview of which test failed and why.
Remove the assert messages from the test functions and run the tests again.
You might want to introduce for a moment an error in the `prime_factors` function to see how the pytest output looks like when the test fails.
You will see that pytest provides you with a clear explanation if something gets wrong.

4. Use `parametrize` feature

   One thing that still isn't ideal is having multiple assert statements for each test case.
It's not just about style and repetition; the issue is that the test stops running after the first failed assertion, meaning not all cases are tested.
But in the last section, we learned about the `parametrize` feature, that we can use in this case.
Update the test and run it again. What do you see this time?
What happens if you introduce an error in the `prime_factors` function?


## 5 :book: Introduction to `pytest.mark` features
In the previous exercise, you learned about the `parametrize` feature, 
that you can access by importing `pytest` and using the `@pytest.mark.parametrize` decorator.
You can read more about the `parametrize` feature in the [pytest documentation](https://docs.pytest.org/en/stable/how-to/parametrize.html#pytest-mark-parametrize-parametrizing-test-functions).

In addition to `parametrize`, pytest provides many other features, including `skip`, `skipif` and `xfail` marks, 
that allow you to skip tests under certain conditions or mark tests that are expected to fail.
You can read more about these features in the [pytest documentation](https://docs.pytest.org/en/stable/skipping.html).

## 6 :book: Testing exceptions
Checking whether the function returns the expected values is not the only type of test that can be useful.
Sometimes you want to test if the function raises an exception under certain conditions.
You can do this by using the `pytest.raises` context manager.
For example, the `prime_factors` function should raise an exception (e.g., `ValueError`) when the input is not an integer.
You could test it by using the following code:

```python
import pytest
from .prime_factors import prime_factors

def test_prime_factors_raises():
    with pytest.raises(ValueError):
        prime_factors(2.5)
```

You could read more about the `pytest.raises` context manager in the [pytest documentation](https://docs.pytest.org/en/stable/assert.html#assertions-about-expected-exceptions).


## 7 :keyboard: :white_check_mark: Exercise 2: Using `pytest.mark` and pytest.raises

In this exercise, you will practice how to test exceptions and how to use the `skip` and `xfail` marks in pytest.
In the previous example, we started with the function and then wrote the test. However, in this exercise, you will write the test first and then update the function to make it pass. This approach is commonly used in test-driven development (TDD), which we will discuss in more detail later.

1. Create a new test function `test_prime_factors_raises` in the `test_prime_factors.py` file.
  
   You can use the code from the previous section as an example. Run the test to see if it fails.

2. Fix the code in the `prime_factors` function to pass the test.
  
   Remember to run the tests after every change in the code to check if the function works correctly.
Have you noticed that changing the code when you have tests is much easier and safer?

3. Create another test function for number `1` that should raise an exception and use `xfail`.
  
   What happens when you run the tests now? You can fix this by adding a condition in the `prime_factors` function, 
but you have also the option to mark the test as `xfail` if you want to fix it later. 
This is a very useful feature when you have a lot of tests and you want to focus on the most important ones first.
It also allows you to keep track of the tests that you need to fix in the future, instead of removing them.

4. Create a test function for number `0` that should raise an exception and use `skip`.
  
   Let's create another test that will check if the function raises an exception for the number `0`. 
We know that the function is not ready for this case, but we can see what happens when we run the test.
What happens this time when you run the tests? It is likely that you don't see any output from the test for the number `0`.
You can use `ctrl` + `c` to stop the tests and think what went wrong.
Could you use `xfail` for this test? What is the difference between `xfail` and `skip`?

5. In the last part, you can use `pytest.mark.parametrize` to merge all test that we wrote in this part.
  
   Note, that `xfail` and `skip` marks could be also used as arguments in the `parametrize` decorator!

## 8 Summary

In this part, you learned about the `pytest` framework and how to use it to write tests for your code.
You also learned how to use the `parametrize` feature to run the same test function with different arguments,
and how to use the `pytest.mark` features to skip tests or mark tests that are expected to fail.

In the next part, we will learn about pytest `fixtures` and how to use them to write more complex tests.

> [!IMPORTANT]
> Update the repository in order to move to the next week/part of the course:
>  - After finishing all the exercises, create a Pull Request from the `week2` branch to the `main` branch
>  - Check the status of tests
>  - If all tests pass, merge the Pull Request, this should update a new `README.md` on the main page of the repository 
> (you can reload the page after 30-60s if you don't see the new content)
