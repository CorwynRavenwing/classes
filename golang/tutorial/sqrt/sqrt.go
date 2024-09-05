package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	z := float64(1)
	epsilon := 0.00001
	delta := float64(z*z - x)
	for math.Abs(delta) > epsilon {
		fmt.Println("x", x, "z", z, "z^2", z*z, "delta", delta)
		z -= delta / (2 * z)
		delta = float64(z*z - x)
	}
	return z
}

func main() {
	fmt.Println(Sqrt(2))
}

