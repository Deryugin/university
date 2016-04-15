#!/bin/bash
set -x
if (($# < 1))
then
        echo "USAGE: $0 [Directory of the set]"
        echo "For example: $0 ./Exp_8564_8567"
        exit
fi

if [ ! -f "./svm_learn" ]
then
        echo "No ./svm_learn found in current directory"
        echo "Extract svm_light for Linux in current directory"
        exit
fi

if [ ! -f "./svm_classify" ]
then
        echo "No ./svm_learn found in current directory"
        echo "Extract svm_light for Linux in current directory"
        exit
fi

FOLDER=$1
VECTOR_FILE="$FOLDER/vectors.dat"
EXAMPLE_FILE=$VECTOR_FILE
MODEL_FILE="$FOLDER/model"

cp $VECTOR_FILE inp_tmp
VECTOR_FILE=inp_tmp

OPTIONS="-z c -q 20 -w 0.001 -k 100 -t 1"

# Remove comments
sed -i '/#./ d' $VECTOR_FILE

SAMPLE_SZ=`wc -l $VECTOR_FILE | sed 's/ .*//'`

# Divide data set into train and learn subsets
TRAIN_COEF=0.9
TRAIN_NUM=`echo "$TRAIN_COEF * $SAMPLE_SZ / 1" | bc`
TEST_NUM=$(($SAMPLE_SZ - $TRAIN_NUM))

shuf $VECTOR_FILE > vec_tmp
head -n $TRAIN_NUM vec_tmp > ex_f
tail -n $TEST_NUM vec_tmp > test_f

./svm_learn $OPTIONS ex_f $MODEL_FILE
./svm_classify test_f $MODEL_FILE

# Remove tmp files
rm inp_tmp
rm vec_tmp
rm test_f
rm ex_f
