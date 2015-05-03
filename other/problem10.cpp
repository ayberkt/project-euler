#include <iostream>
#include <vector>
#include <math.h>

void printVector(std::vector<int> vec) {
    for (auto i: vec) {
        std::cout << i;
    }
}

std::vector<int> genRange(int begin, int end) {
    std::vector<int> range;
    for (int i = begin; i <= end; i++) {
        range.push_back(i);
    }
    return range;
}

bool isPrime(int x) {
    std::vector<int> testNums = genRange(2, ceil(sqrt(x)));
    if (x == 1) { 
        return false;
    } else if (x == 2) {
        return true;
    }

    for (auto i: testNums) {
        if (x % i == 0)
            return false;
    }

    return true;
}

std::vector<int> primes(int bound) {
    std::vector<int> primes;
    for (int i = 2; i < bound; i++) {
        if ((isPrime(i)))
            primes.push_back(i);
    }
    return primes;
}

int main() {
    long sum = 2;
    for (int i = 3; i < 2000000; i += 2) {
        if (isPrime(i))
            sum += i;
    }
    std::cout << sum;
    return 0;
}
