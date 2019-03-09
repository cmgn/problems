package main

import (
	"fmt"
)

func main() {
	n := 0
	fmt.Scanf("%d", &n)
	for i := 0; i < n; i++ {
		var word string
		fmt.Scanf("%s", &word)
		digits := toDigitArray(word)
		for i := len(digits) - 2; i >= 0; i -= 2 {
			prod := digits[i] * 2
			if prod >= 10 {
				digits[i] = prod/10 + prod%10
			} else {
				digits[i] = prod
			}
		}
		if sum(digits)%10 == 0 {
			fmt.Println("PASS")
		} else {
			fmt.Println("FAIL")
		}
	}
}

func toDigitArray(s string) []int {
	output := make([]int, len(s))
	for i := 0; i < len(s); i++ {
		output[i] = int(s[i] - '0')
	}
	return output
}

func sum(ints []int) int {
	total := 0
	for i := 0; i < len(ints); i++ {
		total += ints[i]
	}
	return total
}
