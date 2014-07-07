package main

import "fmt"
import "math"

func is_prime(num int) bool {
    num_sqrt := int(math.Sqrt(float64(num)))
    for i := 2; i <= num_sqrt; i++ {
        if num % i == 0 { return false }
    }
    return true
}

func main() {
    total := 2
    for i := 3; i <= 2000000; i += 2 {
        if is_prime(i) { total += i }
    }
    fmt.Println(total)
}
