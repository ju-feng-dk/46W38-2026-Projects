# Project 3 in 46W38
This is the third (final) programming project of 46W38, which will be graded.

Given that you have passed the first two programming projects (Project 1 and 2),
your final grade will be given based on your work for Project 3 in the following
three aspects:
1. The code you write for Project 3, i.e., the GitHub repository.
2. The report you write for Project 3, which is a maximal 3 pages description
of the structure, the design and the results you get for Project 3.
3. Your performance at the final oral exam, during which we will ask questions
on your code, and comment Git operations. 

**Note**:  It is required to organize your code in a Python module. 

Alternatively, you may choose to turn it into a Python package, so that the 
tool can be used also outside of your repository, after proper installation of 
the package. Anyhow, turn your code into a package is optional, you may consult 
this note to learn how to do it: [Note on packaging](../Notes_and_Tips/6_note_on_packaging.md)



**Due date of Project 3: 2026-Dec-6, 11:59 PM**


## Pre-defined final projects
We provide three pre-defined final projects for you to choose, but you may also
submit a request for a different project if you have an idea you would
like to pursue.

The three pre-defined final projects are as follows:

1. [**Wind resource assessment based on reanalysis data**](
   wind_resource_assessment/README.md)

2. [**Wind power forecasting using machine learning**](
   wind_power_forecasting/README.md)

3. [**Wind turbine modeling based on Blade Element Momentum (BEM) theory**](
   wind_turbine_modeling/README.md)

Introductions and details on these projects can be found in the respective 
sub-folders.


## Requirements to pass
1. Your final project should have the structure and required files as shown in 
the following diagram:
   ```
   Project03_46W38
   ├── inputs/
   │   ├── data_files_we_provide
   │   └── data_files_you_found (optional)
   ├── outputs/
   │   └── data_files_you_generate (no need to push to Github)
   ├── src/
   │   └── your_python_module_or_package_codes
   ├── tests/
   │   └── python_scripts_you_write_for_tests
   ├── examples/
   │   ├── main.py (will run in evaluation)
   │   └── other_example_scripts_you_write (optional)
   ├── .gitignore
   ├── LICENSE
   ├── README.md
   ├── pyproject.toml (optional, needed if you have packaged your code)
   └── any_other_files_you_may_want (optional)
   ```
2. Your Python module/package inside the `src` folder should include at least 
one class.

3. Your Python module/package should implement the required functions, either 
as listed in **functional requirements** in the pre-defined projects, or as we 
agreed on and documented if you work on a custom project.

4. The README file should contains:
   * A brief overview of the module/package.  
   * A description of the module/package architecture, with **at least one diagram**. 
   * A description of the class(es) you have implemented in your package, with
     clear reference to the file name of the code inside `src`.
   * (Optional) Installation instructions if you have packaged your code.

5. Your `main.py` script inside the `examples` folder should demonstrate, in a
clear and structured manner, how the required functions are called and 
executed.

6. Your `main.py` script should run successfully and generate the expected 
results (like plots) in a reasonable time (less than 10 mins). If needed,
define a "demo" mode and/or use saved intermediate results.


## Good to have features of your code
* Test coverage on your module/package should be higher than 70%, as evaluated using
`pytest-cov` on your `src` folder, i.e., by running:
   ```
   pytest --cov=src tests/
   ```

* You have implemented extra functions beyond the required ones.


## Custom project

If your choose to work on a custom project differs from the
three pre-defined ones, please note:

1. Your project should be somehow related to wind and energy systems.

2. The complexity of the project should be comparable to the pre-defined
ones.

3. You should be able to find relevant dataset by yourself, which preferably 
should be openly accessible.  

4. The size of your dataset, at lease for those needed to run your
`examples/main.py`, should not be too big, like less than 100 MB.

5. You will need to draft a general description and a list of **Functional
 requirements** for your custom project, similar to the README files in the
 pre-defined projects.

6. To get approval for your custom project idea, you need to send an email to
Ju Feng before midnight on Wednesday, April 9, including a document explaining 
the above points.  



# How to hand-in

Create a repository named Project03_46W38 on GitHub. The owner should be you. Note also the following:

* Add a proper description.
* Choose visibility: Public or Private. (You may choose to make it only public after you hand-in or public since the beginning.)
* Start with a template: No template.
* Add .gitignore: Python
* Add license: choose a license you want (like MIT license).
* Add README.
* Inside this repository, organize the code according the folder structure as 
stated in this documentation.

Write code incrementally and using Git to do version control. **You commit
history will be considered in the final grading.**

When you are satisfied with your code, please send us a link of your repository 
before the hand-in deadline. 

You also need to write a small report (maximal 3
pages) for this project and send it to us before the deadline.

**Note: There will be no extension for this project, as the week after the 
hand-in date we will have oral exams.**
