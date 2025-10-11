class Solution {

    function prefix_nocache($i) {
        global $n;
        global $s;
        if ($i == 0) {
            // print("prefix($i): free\n");
            return(0);
        }
        $so_far = $this->prefix($i - 1);
        if ($s[$i] == $s[$i - 1]) {
            // print("prefix($i): same as prior\n");
            return $so_far;
        }
        $answer = ($i - 1) + 1;     # === $i
        // print("prefix($i): swap prior: $answer\n");
        return $so_far + $answer;
    }

    function prefix($i) {
        # cost of making all characters left of s[i] equal to it
        global $prefix_cache;
        if (is_null($prefix_cache[$i])) {
            $prefix_cache[$i] = $this->prefix_nocache($i);
        // } else {
        //     print("prefix($i): CACHE HIT\n");
        }
        return $prefix_cache[$i];
    }

    function suffix_nocache($i) {
        global $n;
        global $s;
        if ($i == $n - 1) {
            // print("suffix($i): free\n");
            return(0);
        }
        $so_far = $this->suffix($i + 1);
        if ($s[$i] == $s[$i + 1]) {
            // print("suffix($i): same as next\n");
            return $so_far;
        }
        $answer = $n - ($i + 1);
        // print("suffix($i): swap next: $answer\n");
        return $so_far + $answer;
    }

    function suffix($i) {
        # cost of making all characters right of s[i] equal to it
        global $suffix_cache;
        if (is_null($suffix_cache[$i])) {
            $suffix_cache[$i] = $this->suffix_nocache($i);
        // } else {
        //     print("suffix($i): CACHE HIT\n");
        }
        return $suffix_cache[$i];
    }

    function dump_array($label, $array) {
        print("$label=[");
        foreach ($array as $x) {
            print(($x ?? 'null') . ',');
        }
        print("]\n");
    }

    /**
     * @param String $s
     * @return Integer
     */
    function minimumCost($local_s) {
        global $prefix_cache;
        global $suffix_cache;
        global $n;
        global $s;
        $s = $local_s;    # globalize
        $n = strlen($s);
        $prefix_cache = array_fill(0, $n, NULL);
        $suffix_cache = array_fill(0, $n, NULL);
        // $this->dump_array('P', $prefix_cache);
        // $this->dump_array('S', $suffix_cache);

        $answers = array();
        for ($i = 0; $i < $n; $i++) {
            $answer = $this->prefix($i) + $this->suffix($i);
            // print("MC($i): $answer\n");
            array_push($answers, $answer);
        }
        return min($answers);
    }
}

# NOTE: Acceptance Rate 53.7%

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (edge case; Output Exceeded)
# NOTE: Runtime 459 ms Beats 100.00%
# NOTE: Memory 78.63 MB Beats 100.00%
