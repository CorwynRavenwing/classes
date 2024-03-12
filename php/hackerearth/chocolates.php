<?php

function solution ($N, $C)
{
    $stack = [];
    $retval = [];
    foreach ($C as $cmd) {
        print("cmd $cmd\n");
        if ($cmd == 0) {
            print("  popping\n");
            $size = array_pop($stack);
            array_push($retval, $size);
        } else {
            print("  pushing\n");
            array_push($stack, $cmd);
        }
    }
    return $retval;
}

$N = readline();
$C = readline();
$C = explode(" ", $C);

$out_ = solution($N, $C);
echo join(" ", $out_);
echo "
";
?>
