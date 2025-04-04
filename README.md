# TestMe

This repo implements the TestMe assignment grading homework.


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

- A directory containing the **evaluation program** to be run
- A **Docker file** to build the environment in which the evaluation program can run

The evaluation program must meeting the following specification:
- It contains an **entrypoint script** `run.sh dinput doutput dgold deval` which executes the program
- It takes fourth arguments, the first is  `dinput`, the directory containing the input data. The second is `doutput`, the directory containing the submission program's output. The third is `dgold`, the directory containing the ground truth data. The fourth is `deval`, the directory into which the evaluation program writes the evaluation result


## How to Evaluate

To run a submission program against an evaluation program, the grader performs the following:

1. Build the Docker image for the submission
2. Run the program by mounting the program, the held-out test input data, and an output result folder
3. Run evaluation program by mounting the evaluation program, the input data, the submission program output result folder, the ground truth data, and an evaluation results folder

As best practice, we recommend that the grader share with the user:

1. The evaluation program `deval`
2. A sample input data `dsample_data`
3. A sample ground truth data for evaluation `dgold`

This way, the user can test their program as follows:

```
# suppose submission program is in ./myprogram/
# suppose evaluation program is in ./evalprogram/
# suppose ./tmp/out and ./tmp/eval contain the temporary directories for program output and evaluation result

# build the Docker image
cd myprogram; docker build -t mysubmission:0.01 -f Dockerfile; cd ..
cd evalprogram; docker build -t myeval:0.01 -f Dockerfile; cd ..

# run the submission program on the sample data
docker run --rm -v $PWD/myprogram:/src -v $PWD/dsample_data:/input -v $PWD/tmp/out:/output mysubmission:0.01 bash /src/run.sh /input /output

# run the evaluation program on the output result
docker run --rm -v $PWD/evalprogram:/src -v $PWD/dsample_data:/input -v $PWD/tmp/out:/output -v $PWD/dgold:/gold -v $PWD/tmp/eval:/eval mysubmission:0.01 bash /src/run.sh /input /output /gold /eval
```

The final result should be located in `./tmp/eval`.


## Example

An example of how to use TestMe for submission and for evaluation in `./example`.


## Considerations for the Grader

Containerization using Docker will simplify the execution of user submissions.
However, you should clarify with the reader the following important points:

- How will users identify themselves in the submission? A good way to do this is for the user to create a `user.txt` listing their user IDs
- What resource constraints will be set during evaluation? For instance, you can specify 30 minutes max to run the evaluation. Similarly you can specify limits for memory and disk usage.
