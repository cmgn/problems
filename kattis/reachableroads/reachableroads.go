package main

import "fmt"

type UnionFind struct {
	Parents   []int
	Sizes     []int
	NumGroups int
}

func NewUnionFind(n int) *UnionFind {
	uf := &UnionFind{
		Parents:   make([]int, n),
		Sizes:     make([]int, n),
		NumGroups: n,
	}
	for i := 0; i < n; i++ {
		uf.Sizes[i] = 1
		uf.Parents[i] = i
	}
	return uf
}

func (uf *UnionFind) Parent(x int) int {
	if uf.Parents[x] != x {
		uf.Parents[x] = uf.Parent(uf.Parents[x])
	}
	return uf.Parents[x]
}

func (uf *UnionFind) Union(x, y int) {
	x = uf.Parent(x)
	y = uf.Parent(y)
	if x == y {
		return
	}
	uf.NumGroups--
	if uf.Sizes[x] < uf.Sizes[y] {
		x, y = y, x
	}
	uf.Sizes[x] += uf.Sizes[y]
	uf.Parents[y] = x
}

func main() {
	var numCities, numEndpoints, numRoads int
	fmt.Scanf("%d", &numCities)
	for i := 0; i < numCities; i++ {
		fmt.Scanf("%d", &numEndpoints)
		unionFind := NewUnionFind(numEndpoints)
		fmt.Scanf("%d", &numRoads)
		var start, end int
		for j := 0; j < numRoads; j++ {
			fmt.Scanf("%d %d", &start, &end)
			unionFind.Union(start, end)
		}
		fmt.Println(unionFind.NumGroups - 1)
	}
}
