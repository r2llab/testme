# Problem Definition

For this project, we will develop a program that takes in a prefix string and tries to predict 3 choices for the next character.
For illustration purposes, this repo contains a dummy program that simply generates 3 random guesses of the next character.


## Sample data and evaluation

### Input format

`../sample/data/input.txt` contains an example of what the input to your program will look like.
Each line in this file correspond to a string, for which you must guess what the next character should be.


### Output format

`../sample/output/output.txt` contains an example of what the output of your program must look like.
Each line in this file correspond to guesses by the program of what the next character should be.
In other words, line `i` in `../sample/output/output.txt` corresponds to what character the program thinks should come after the string in line `i` of `../sample/data/input.txt`.
In this case, for each string, the program produces 3 guesses.


### Your submission program

Please implement `myprogram.py`.
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

The evaluation output will be stored in `tmp/eval/eval.txt`.

During development, you can also mount your current directory as `/src` as you edit `myprogram.py` to generate predictions.
However, to avoid submission errors, please do a final check by mounting `submit` to `/src`.
Once you are comfortable with your submission, please submit `submit.zip`.
