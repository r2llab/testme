# K-Means

For this assignment, you will implement K-means for clustering.


## Sample data and evaluation

### Input format

`../sample/data` contain examples of what the input to your program will look like.
The starter code takes these inputs and trains K-Means on the training data, saves model states, and generates predictions on the test data.


### Output format

`../sample/gold` contains an example of what the output of your program must look like.
During evaluation, we will give your program different test data.


### Your submission program

Please implement `myprogram.py`.
Remember to first train it using `--train` in order to create your model checkpoint.
We will run your program during evaluation without `--train`.

Your submission must adhere to the [TestMe API](https://github.com/r2llab/testme).
In addition, please include a file in your submission (e.g. `user.txt`) that contains your UserID.
For convenience, we have created a `submit.sh` that produces a submission zip file.
Please modify `submit.sh` to include the files you require for your program to run.


### Evaluation
`../grader.py` contains the evaluation script we will use to evaluate your submission.
You can check your submission using the sample data we provide.

```
# Compile the submissions folder
bash submit.sh
# Run the grader and store output in tmp
python ../grader.py --submission submit --data ../sample/data --gold ../sample/gold --output tmp
```

During development, you can also mount your current directory as `/src` as you edit `myprogram.py` to generate predictions.

```
python ../grader.py --submission $PWD --data ../sample/data --gold ../sample/gold --output tmp
```

However, to avoid submission errors, please do a final check by mounting `submit` to `/src`.
Once you are comfortable with your submission, please submit `submit.zip`.
