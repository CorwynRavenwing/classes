#!/usr/bin/bash

# fail script on any error
set -e

PROG_NAME=$1
NUMBER=$2

if [ "$NUMBER" == "" ]; then
	echo "NUMBER is required"
	AVAIL=$(echo ${PROG_NAME}.tc*			\
		| xargs -n1 echo			\
		| sed -e "s,${PROG_NAME}[.]tc,,g"	\
		| sort -n				\
		| xargs echo		)
	if [ "$AVAIL" == "*" ]; then
		echo "No tests found"
	else
		echo "Available test numbers: ${AVAIL}"
	fi
	exit
fi

echo "Running ${PROG_NAME} test #${NUMBER}:"

PROGRAM="${PROG_NAME}.py"
TESTFILE="${PROG_NAME}.tc${NUMBER}"
ANSWERFILE="${PROG_NAME}.an${NUMBER}"
OUTFILE="${PROG_NAME}.out${NUMBER}"
TEMPOUT="${PROG_NAME}.out.temp${NUMBER}"
TEMPANS="${PROG_NAME}.an.temp${NUMBER}"
TEMPDIF="${PROG_NAME}.diff.temp${NUMBER}"
ACTUAL=/tmp/foo_ACTUAL
EXPECTED=/tmp/foo_EXPECTED
FAIL=0
FILES=""
if [ ! -f $PROGRAM ]; then
	echo "Python file ${PROGRAM} doesn't exist"
	FAIL=1
	FILES="${FILES}${PROGRAM} "
else
	python -m py_compile ${PROGRAM}
	# program will stop here on compilation failure
	# because of "set -e" above
	mypy ${PROGRAM}
	# program will also stop here on type error
fi
if [ ! -f $TESTFILE ]; then
	echo "Test file ${TESTFILE} doesn't exist"
	FAIL=1
	FILES="${FILES}${TESTFILE} "
fi
if [ ! -f $ANSWERFILE ]; then
	echo "Answer file ${ANSWERFILE} doesn't exist"
	FAIL=1
	FILES="${FILES}${ANSWERFILE} "
fi
if [ -f $OUTFILE ]; then
	echo "Output file ${OUTFILE} already exists, overwriting"
fi
if [ "1" = $FAIL ]; then
	echo "Quitting.  Fix missing files with:"
	echo "vi ${FILES}"
	exit 1
fi

ulimit -m 1024000	# physical memory hard limit 1G
ulimit -v 1024000	# virtual memory hard limit 1G

#time (			\
#	python $PROGRAM < $TESTFILE		\
#	|| (		\
#	    echo "Failed with exit code $?"	\
#	    && exit	\
#	)		\
#     ) | tee $OUTFILE
#
time  python $PROGRAM < $TESTFILE	\
	| tee $OUTFILE

echo ""
echo "Differences:"
echo ""
echo "ACTUAL" > $ACTUAL
echo "EXPECTED" > $EXPECTED

cat $OUTFILE						\
	| grep -v '^\s*[#]'				\
	| grep -n '.'					\
	> $TEMPOUT
cat $ANSWERFILE						\
	| grep -n '.'					\
	> $TEMPANS
diff -sq $TEMPOUT $TEMPANS				\
	| sed -e 's, and ,\n  and ,'			\
	| sed -e 's, are ,\n  are ,'			\
	| sed -e 's, differ,\n  differ,'		\
	| grep --color=always -E '(^|differ)'		\
	| sed -e 's,[.]temp,,g'
diff -q $TEMPOUT $TEMPANS > /dev/null			\
    || (						\
    diff -s -W $(tput cols) -y $ACTUAL $EXPECTED	\
    || diff -s -W $(tput cols) -y $TEMPOUT $TEMPANS	\
        | grep '\s[<|>]\s'				\
	| tee $TEMPDIF					\
	| head -n 20					\
	| grep --color=always -E '(^|[^|]*\|[^|]*)'	\
    || cat $TEMPDIF					\
	| tail -n +21					\
	| grep -c .					\
	| sed -e 's,\([0-9]*\),... \1 more lines,'	\
	| grep -v ' 0 '					\
    )

rm -f $TEMPOUT $TEMPANS $TEMPDIF

