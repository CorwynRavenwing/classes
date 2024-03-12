<?php

function solution ($N, $K, $seat)
{
    $retval = [];
    $res = array_fill(0, $N, 0);
    foreach ($seat as $cmd) {
        print(join("-", $res)."\n");
        if ($cmd == 0) {
            print("cmd $cmd zero\n");
            for ($i = 0; $i < $N; $i++) {
                print("check seat ".($i+1).": ".$res[$i]."\n");
                if ($res[$i] == 0) {
                    print("first unreserved seat:".($i+1)."\n");
                    $res[$i] = 1;
                    $retval[] = ($i+1);
                    break;
                }
            }
        } else {
            print("cmd $cmd non-zero\n");
            $res[$cmd-1] = 0;
            # no change to $retval
        }
    }
    print(join("-", $res)."\n");
    return $retval;
}

$N = readline();
$K = readline();
$seat = readline();
$seat = explode(" ", $seat);

$out_ = solution($N, $K, $seat);
echo join(" ", $out_);
echo "
";
?>
