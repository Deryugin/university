#!/bin/bash

if (($# < 2))
then
        echo "USAGE: $0 [Directory of the set]"
        echo "For example: $0 ./Exp_8564_8567"
        exit
fi

FOLDER=$1
VECTOR_FILE="$FOLDER/vectors.dat"
EXAMPLE_FILE=$VECTOR_FILE
MODEL_FILE="$FOLDER/model"

OPTIONS="-z c"

sed -i '/#./ d' $VECTOR_FILE

SAMPLE_SZ=`wc -l $VECTOR_FILE | sed 's/ .*//'`

grep \"^-1\" $VECTOR_FILE > c0
grep \"^1\" $VECTOR_FILE > c1

# Divide data set into train and learn subsets
TRAIN_COEF=0.75 # == TRAIN_NUM / (TRAIN_NUM + TEST_NUM)

TRAIN_NUM=`echo "$TRAIN_COEF * $SAMPLE_SZ / 1" | bc`
TEST_NUM=$(($SAMPLE_SZ - $TRAIN_NUM))

shuf $VECTOR_FILE > vec_tmp
head -n $TRAIN_NUM vec_tmp > ex_f
tail -n $TEST_NUM vec_tmp > test_f

./svm_learn $OPTIONS ex_f $MODEL_FILE

./svm_classify test_f $MODEL_FILE

rm vec_tmp
rm test_f
rm ex_f
