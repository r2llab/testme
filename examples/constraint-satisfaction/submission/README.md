# Constraint Satisfaction

For this assignment, you will implement the AC3 algorithm for (binary) constraint satisfaction problems.


## Sample data and evaluation

### Input format

`../sample/data/csp.py` contain examples of what the input to your program will look like.
The starter code takes these inputs and constructs a CSP.


### Output format

`../sample/gold/output.json` contains an example of what the output of your program must look like.
The file is a JSON object of variable domains after each round of AC3.
During evaluation, we will give your program different CSPs.


### Your submission program

Please implement `myprogram.py`.
Please use the provided data structures to help you implement AC3.

Your submission must adhere to the [TestMe API](https://github.com/r2llab/testme).
In addition, please include a file in your submission (e.g. `user.txt`) that contains your UserID.
For convenience, we have created a `submit.sh` that produces a submission zip file.
Please modify `submit.sh` to include the files you require for your program to run.


### Evaluation
`eval` contains the evaluation script we will use to evaluate your submission.
You can check your submission using the sample data we provide.

First, build the Docker image for the evaluation program:

```
cd ../eval
docker build . -t testme-example-eval:0.1
```

Second, build your Docker image for your submission:

```
cd submission
docker build . -t testme-example-submission:0.1
```

Finally, test your submission:

```
# Compile the submissions folder
bash submit.sh

# Make a temporary directory for evaluation
rm -rf tmp
mkdir -p tmp/output
mkdir -p tmp/eval

# Generate output using your submission
docker run --rm -v $PWD/submit:/src -v $PWD/../sample/data:/input -v $PWD/tmp/output:/output testme-example-submission:0.1 bash run.sh /input /output

# Evaluate your generated outputs
docker run --rm -v $PWD/../eval:/src -v $PWD/../sample/data:/input -v $PWD/tmp/output:/output -v $PWD/../sample/gold:/gold -v $PWD/tmp/eval:/eval testme-example-eval:0.1 bash run.sh /input /output /gold /eval
```

The evaluation output will be stored in `tmp/eval`.

During development, you can also mount your current directory as `/src` as you edit `myprogram.py` to generate predictions.
However, to avoid submission errors, please do a final check by mounting `submit` to `/src`.
Once you are comfortable with your submission, please submit `submit.zip`.
