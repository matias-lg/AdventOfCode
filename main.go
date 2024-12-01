package main

import (
	"aoc/2024/1"
	"fmt"
	"os"
	"strconv"
)

type Solution interface {
	Solve()
}

// to add a day:

// create a new folder for the day in the year folder
// implement the Solution interface and import the file
// add a solution instance to the solutions map


func main() {

	solutions := map[string]Solution{
		"2024-1": day1.New(),
	}

	if len(os.Args) != 3 {
		fmt.Println("Usage: go run main.go <year> <day>")
		fmt.Println("Example: go run main.go 2024 1")
		os.Exit(1)
	}

	year, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Printf("Invalid year format: %s\n", os.Args[1])
		os.Exit(1)
	}

	day, err := strconv.Atoi(os.Args[2])
	if err != nil {
		fmt.Printf("Invalid day format: %s\n", os.Args[2])
		os.Exit(1)
	}

	key := fmt.Sprintf("%d-%d", year, day)
	solution, ok := solutions[key]
	if !ok {
		fmt.Printf("Solution for %s not found\n", key)
		os.Exit(1)
	}

	solution.Solve()

}
