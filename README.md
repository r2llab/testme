# TestMe

This repo implements the TestMe assignment grading homework.


## Installation

```bash
pip install git+https://github.com/r2llab/testme
```


## TestMe Submission Requirement

A TestMe submission by an **user** consists of:

- A directory containing the **submission program** to be run
- A **Docker file** to build the environment in which the program can run

The program must meeting the following specification:
- It contains an **entrypoint script** `run.sh dinput doutput` which executes the program
- It takes two arguments, the first is `dinput`, the directory containing the input data. The second is `doutput`, the directory into which the submission program writes output

During evaluation:
- The program directory will be mounted to `/src`, where it will be run from
- The input data will be mounted to `dinput`
- The program will write data to `doutput`


## TestMe Evaluation Requirement

A TestMe **evaluation** by a **grader** consists of:

- A **Grader** script that subclasses from `testme.TestMe`

Please see examples in [the examples directory](examples).


## Considerations for the Grader

Containerization using Docker will simplify the execution of user submissions.
However, you should clarify with the reader the following important points:

- How will users identify themselves in the submission? A good way to do this is for the user to create a `user.txt` listing their user IDs
- What resource constraints will be set during evaluation? For instance, you can specify 30 minutes max to run the evaluation. Similarly you can specify limits for memory and disk usage.
