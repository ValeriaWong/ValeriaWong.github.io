
# 题目——练习：切片

实现 `Pic`。它应当返回一个长度为 `dy` 的切片，其中每个元素是一个长度为 `dx`，元素类型为 `uint8` 的切片。当你运行此程序时，它会将每个整数解释为灰度值（好吧，其实是蓝度值）并显示它所对应的图像。

图像的选择由你来定。几个有趣的函数包括 `(x+y)/2`, `x*y`, `x^y`, `x*log(y)` 和 `x%(y+1)`。

（提示：需要使用循环来分配 `[][]uint8` 中的每个 `[]uint8`；请使用 `uint8(intValue)` 在类型之间转换；你可能会用到 `math` 包中的函数。）

# 使用函数 $f(x, y) = (x\times y)/2$

![[Pasted image 20230717003716.png]]

```go
// 使用函数 f(x, y) = (x*y)/2，以下是实现代码：

package main

  

import "golang.org/x/tour/pic"

  

func Pic(dx, dy int) [][]uint8 {

picture := make([][]uint8, dy)

for y := range picture {

picture[y] = make([]uint8, dx)

for x := range picture[y] {

picture[y][x] = uint8((x * y) / 2)

}

}

return picture

}

  

func main() {

pic.Show(Pic)

}
```

# `(x+y)/2`：

![[Pasted image 20230717003910.png]]

```go
package main

import (
	"golang.org/x/tour/pic"
)

func Pic(dx, dy int) [][]uint8 {
	picture := make([][]uint8, dy)
	for y := range picture {
		picture[y] = make([]uint8, dx)
		for x := range picture[y] {
			picture[y][x] = uint8((x + y) / 2)
		}
	}
	return picture
}

func main() {
	pic.Show(Pic)
}

```

# $x\times y$

![[Pasted image 20230717004132.png]]

```go

package main

import (
	"golang.org/x/tour/pic"
)

func Pic(dx, dy int) [][]uint8 {
	picture := make([][]uint8, dy)
	for y := range picture {
		picture[y] = make([]uint8, dx)
		for x := range picture[y] {
			picture[y][x] = uint8(x * y) // Use x*y here
		}
	}
	return picture
}

func main() {
	pic.Show(Pic)
}

```


# x^y

![[Pasted image 20230717004201.png]]


# $x\times log(y)$

![[Pasted image 20230717004521.png]]
```go
package main

import (
	"golang.org/x/tour/pic"
	"math"
)

func Pic(dx, dy int) [][]uint8 {
	picture := make([][]uint8, dy)
	for y := range picture {
		picture[y] = make([]uint8, dx)
		for x := range picture[y] {
			picture[y][x] = uint8(float64(x) * math.Log(float64(y))) 
		}
	}
	return picture
}

func main() {
	pic.Show(Pic)
}


```


# x%(y+1)

![[Pasted image 20230717004350.png]]