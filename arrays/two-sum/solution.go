package main

import "fmt"

// twoSum retorna os índices de dois números em nums que somam target.
// Tempo: O(n) | Espaço: O(n)
func twoSum(nums []int, target int) []int {
	seen := make(map[int]int, len(nums))

	for i, n := range nums {
		complement := target - n
		if j, ok := seen[complement]; ok {
			return []int{j, i}
		}
		seen[n] = i
	}

	return nil
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9)) // [0 1]
	fmt.Println(twoSum([]int{3, 2, 4}, 6))      // [1 2]
	fmt.Println(twoSum([]int{3, 3}, 6))         // [0 1]
}
