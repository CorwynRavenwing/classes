# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt               \
    | sed -e 's,   *, ,g'   \
    | sed -e 's,^  *,,g'    \
    | sed -e 's,  *$,,g'    \
    | sed -e 's, ,\n,g'     \
    | sort                  \
    | uniq -c               \
    | sort -n -r            \
    | awk '{print $2, $1}'  \
    | cat

