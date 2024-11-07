package main

import (
	"golang.org/x/tour/wc"
	"strings"
)

func WordCount(s string) map[string]int {
	answer := make(map[string]int)
	for _, word := range strings.Fields(s) {
		answer[word] += 1
	}
	return answer
}

func main() {
	wc.Test(WordCount)
}

