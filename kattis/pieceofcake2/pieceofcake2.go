package main

import "fmt"

func max(xs ...int) int {
	x := xs[0]
	for i := 1; i < len(xs); i++ {
		if xs[i] > x {
			x = xs[i]
		}
	}
	return x
}

func main() {
	var n, h, v int
	fmt.Scanf("%d %d %d", &n, &h, &v)
	fmt.Println(4 * max((n-h)*(n-v), h*(n-v), (n-h)*v, h*v))
}
