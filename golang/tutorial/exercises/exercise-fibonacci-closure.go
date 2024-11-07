package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
	// fibonacci numbers before zero:
	a := -1	// #-2	= #0(0) - #-1(1)
	b := 1	// #-1	= #1(1) - #0(0)
	c := 0	// #0	= #2(1) - #1(1)
	return func() int {
		c = a + b
		a = b
		b = c
		return b
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}

