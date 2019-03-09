package main

import "fmt"

func main() {
	slots := make([]int, 100)
	var A, B, C int
	fmt.Scanf("%d %d %d", &A, &B, &C)
	for i := 0; i < 3; i++ {
		var S, E int
		fmt.Scanf("%d %d", &S, &E)
		S--
		E--
		for j := S; j < E; j++ {
			slots[j]++
		}
	}
	total := 0
	for i := 0; i < 100; i++ {
		switch slots[i] {
		case 1:
			total += A
		case 2:
			total += B * 2
		case 3:
			total += C * 3
		default:
		}
	}
	fmt.Println(total)
}
