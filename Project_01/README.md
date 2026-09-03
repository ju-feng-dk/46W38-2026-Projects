# Project 1 in 46W38

This is the first programming project of 46W38, which will be graded. 
Passing this project is one of the three requirements for passing this 
course. The other two requirements are passing programming project 2 and
 3.

**Due date of Project 1: 2026-Oct-4, 11:59 PM**

## Backgroud of the project
In wind energy, the power curve of a wind turbine, i.e., its power
output ($P$) as function of wind speed at hub height ($v$) is an 
important characteristics of the turbine. It is widely known that the
available power in the flow is a function of the cubic of the wind
speed, and thus the power output can be computed as:

$$
\begin{equation}
P = \frac{1}{2}C_pv^3A
\end{equation}
$$

where $C_p$ is the power coefficient that itself is a function of the
wind speed ($v$) and depends on the design and operation strategy of the
turbine, $A$ denotes the rotor area of the turbine.d

Normally, a customer can get the power curve from the turbine 
manufacturer. But as a researcher, sometimes it is not straightforward 
to get this kind of data for a given type of turbine.

Luckily, we can usually find the following parameters from the public
available data source:
* $P_{rated}$ : rated power [MW] of the turbine,
* $v_{in}$ : cut-in wind speed [m/s] that denotes the minimal wind speed
 the turbine starts to generate power,
* $v_{ratd}$ : rated wind speed [m/s] that denotes the wind speed the 
turbine reaches the rated power,
* $v_{out}$ : cut-out wind speed [m/s] that denotes the wind speed the
 turbine stops generating power.

Based on these parameters and the typical operational strategy of modern
wind turbines, we can formulate an approximate power curve model 
described by:

$$
\begin{equation}
P(v) =
\begin{cases} 
0 & \text{if } v < v_{in} \text{ or }  v \ge v_{out}, \\
g(v)\cdot P_{rated} & \text{if } v_{in} \le v < v_{rated}, \\
P_{rated} & \text{if }  v_{rated} \le v < v_{out}.
\end{cases}
\end{equation}
$$

In this equation, $g(v)$ is the weighting function denotes the 
ratio of generated power to the rated power. We can consider two ways of
computing this ratio by using different interpolation methods.

If linear interpolation is used, $g(v)$ takes the following form:

$$
\begin{equation}
g(v) = (v-v_{in})/(v_{rated}-v_{in}) 
\end{equation}
$$

If cubic interpolation is used, it will be given by:

$$
\begin{equation}
g(v) = v^3 / v_{rated}^3
\end{equation}
$$

## The Programming Task
In this project, you need to write a function to calculate the power 
output by implementing the model defined in the last section. Your 
function need to fullfil the following requirements:

1. Have a meaningful and proper name.
2. Takes the following inputs (each with proper variable name):
    * wind speed (we assume it will be a float number),
    * rated power, with a default value: 15,
    * cut-in wind speed, with a default value: 3,
    * rated wind speed, with a default value: 11,
    * cut-out wind speed, with a default value: 25,
    * interpolation option, a string to define the interpolation method,
      can only be "linear" or "cubic", with a default value: "linear".
3. Returns the computed power output using the model and the inputs.
4. Have proper docstring and several (at least 3) comments to explain
the function.
5. Include error handling by raising proper error when the user gives
an invalid input for the string defining the interpolation option.

You should also write the main script to run your function for at least
one example. These can be done in one script that looks like the 
following:
~~~
def add_two(x, y):
    """
    Docstring here.
    """
    # Add comment if needed.
    result = x +  y # Add comment if needed.

    return result

if __name__ == '__main__':
    # Write the main script to use the function here:
    x = 1
    y = 1

    # Add comments to explain if needed.
    z = add_two(x, y)
    print(f'x + y = {z}')  # Add comment when needed
~~~

## How to hand-in

Create a repository named **_Project01_46W38_** on GitHub. The owner 
should be you. Note also the following:
* Add a proper description.
* Choose visibility: Public or Private. (You may choose to make it only 
public after you hand-in or public since the beginning.)
* Start with a template: No template.
* Add README: On (_But leave it blank for now_).
* Add .gitignore: Python
* Add license: choose a license you want (like MIT license).

Inside this repository, there should be one python script named as 
"main.py".

You should write your function and code as required in the
previous section in this python script.

Write code incrementally and using Git to do version control. **You need
to have at least 3 commits.**

When you are satisfied with your code, please send us a link of your
repository before the hand-in deadline.

## Evaluation
Evaluation of the project will be solely based on the repository, with
focus on:
* Functionality: does it implement the model correctly and fulfill the
requirements listed in **The programming Task** section.
* Understandability: does it have proper naming, docstring, comments and
layout.
* Professional workflow: does the repository looks professional and has
it use version control properly (like meaningful commits). 

## Extension (if needed)
If you need an extension, you should apply at least 5 days before the
deadline, this needs to be done by email, i.e., write to Ju Feng 
(jufen@dtu.dk).


