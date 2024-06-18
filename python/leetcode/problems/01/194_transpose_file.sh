# Read from the file file.txt and print its transposed content to stdout.

cat file.txt       \
    | awk '
        BEGIN { first_time = 1 }
        {
            if (first_time) {
                first_time = 0
                for (i = 1; i <= NF; i++) {
                    data[i] = $i
                }
            } else {
                for (i = 1; i <= NF; i++) {
                    data[i] = data[i] " " $i
                }
            }
        }
        END {
            for (i in data) {
                print data[i]
            }
        }
    '

