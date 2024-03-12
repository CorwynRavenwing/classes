<?php
function sum($array) {
    $sum = 0;
    foreach ($array as $x) {
        $sum += $x;
    }
    return $sum;
}

// Write your code here
fscanf(STDIN, "%s\n", $T);
for ($i = 0; $i < $T; $i++) {
    fscanf(STDIN, "%s\n", $N);
    // print("i:" . $i . " saw:" . $N . "\n");
    $divisors = [];
    for ($d = 1; $d < ($N/2+1); $d++) {
        // print("  check d $d\n");
        if ($N % $d) {
            // print("    NOT DIVISOR\n");
        } else {
            // print("    $d DIVISOR\n");
            $divisors[] = $d;
        }
    }
    // print("  D:" . join(",", $divisors) . "\n");
    $sum = sum($divisors);
    // print("  S: $sum\n");
    echo (($sum == $N) ? "YES" : "NO") . "\n";
}
?>
