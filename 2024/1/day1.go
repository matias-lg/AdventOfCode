package day1

import (
	"aoc/utils"
	"fmt"
	"math"
	"sort"
	"strconv"
	"strings"
)

type solution struct{}

func New() solution {
	return solution{}
}

func (s solution) Solve() {
	fmt.Println("part 1", s.Part1())
	fmt.Println("part 2", s.Part2())
}

func (s solution) Part1() int {
	input, _ := utils.MultipleLines("2024/1/input1.txt")

	col1 := make([]int, 0)
	col2 := make([]int, 0)

	for _, line := range input {
		nums := strings.Split(line, "   ")
		n1, _ := strconv.Atoi(nums[0])
		n2, _ := strconv.Atoi(nums[1])
		col1 = append(col1, n1)
		col2 = append(col2, n2)
	}

	// sort the columns
	sort.Slice(col1, func(i, j int) bool {
		return col1[i] < col1[j]
	})

	sort.Slice(col2, func(i, j int) bool {
		return col2[i] < col2[j]
	})

	res := 0

	for i := 0; i < len(col1); i++ {
		res += int(math.Abs(float64(col1[i] - col2[i])))
	}
	return res
}

func (s solution) Part2() int {
	input, _ := utils.MultipleLines("2024/1/input1.txt")

	col1 := make([]int, 0)
	col2 := make([]int, 0)

	res := 0

	for _, line := range input {
		nums := strings.Split(line, "   ")
		n1, _ := strconv.Atoi(nums[0])
		n2, _ := strconv.Atoi(nums[1])
		col1 = append(col1, n1)
		col2 = append(col2, n2)
	}

	exists := make(map[int]bool)

	for i := 0; i < len(col1); i++ {
		exists[col1[i]] = true
	}

	freqs := make(map[int]int)

	for i := 0; i < len(col2); i++ {
		_, ok := exists[col2[i]]
		if ok {
			if _, ok := freqs[col2[i]]; !ok {
				freqs[col2[i]] = 1
			} else {
				freqs[col2[i]]++
			}
		}
	}

	for k, v := range freqs {
		res += k * v
	}

	return res
}
