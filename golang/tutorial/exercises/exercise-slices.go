package main

import "golang.org/x/tour/pic"

func Pic(dx, dy int) [][]uint8 {
	var answer [][]uint8
	for y := 0; y < dy; y++ {
		var row []uint8
		for x := 0; x < dx; x++ {
			var zVal int = x * y
			var z = uint8(zVal)
			row = append(row, z)
		}
		answer = append(answer, row)
	}
	return answer
}

func main() {
	pic.Show(Pic)
}

