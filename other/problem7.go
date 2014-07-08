package main

import (
    "fmt"
    "math"
)

func is_prime(num int) bool {
    num_sqrt := int(math.Sqrt(float64(num)))
    for i := 2; i <= num_sqrt; i++ {
        if num % i == 0 { return false }
    }
    return true
}

func main () {
    prime_counter, index := 1, 3
    for {
        if is_prime(index) { prime_counter += 1 }
        if prime_counter == 10001 {
            fmt.Println(index)
            break
        }
        index += 2
    }
}
