package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	population := 0
	counts := make(map[string]int)
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		if line[len(line)-1] == '\n' {
			line = line[:len(line)-1]
		}
		if line == "***" {
			break
		}
		counts[line]++
		population++
	}
	if err := scanner.Err(); err != nil {
		log.Fatalln(err)
	}
	bestKey := "Runoff!"
	bestVal := 0
	for key, val := range counts {
		if val == bestVal {
			bestKey = "Runoff!"
		} else if val > bestVal {
			bestVal = val
			bestKey = key
		}
	}
	fmt.Println(bestKey)
}
