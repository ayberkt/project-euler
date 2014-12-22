We will be needing the `Set` type from Data.Set in order to compare whether the digits of a number contains all the numbers from 1 up to the number of digits of the number. If we take 2143 as an example, we see that its digits is the list [2, 1, 4, 3] and the list of numbers up to the number of digits is [1, 2, 3, 4]. When these two are regarded as sets they will be equal since order does not matter in sets.

> import qualified Data.Set as Set
 
Now, we need to implement a function that takes a number and returns the list of digits of the number.

> digits :: Integer -> [Integer]
> digits n = reverse (inverseDigits n)
>            where inverseDigits n
>                    | n == 0 = []
>                    | otherwise = (n `mod` 10) : inverseDigits (n `div` 10)

The following function counts the number of digits of the numbers. This could have been simply done with ``length digits num`` too but it would be inefficient due to the use of `length`. The following is a mathematical take on the same problem.

> numDigits :: Integer -> Integer
> numDigits n
>    | n == 0 = 0
>    | otherwise = 1 + (numDigits (n `div` 10))
 
Now we have test pandigitality, the aforementioned property that is our concern.
 
> pandigital :: Integer -> Bool
> pandigital x = (Set.fromList (digits x)) == digitsSet
>                where digitsSet = Set.fromList [1..(numDigits x)]

Simple primality check.

> prime :: Integer -> Bool
> prime x = not $ any (\n -> (x `mod` n) == 0) [2..squareRoot]
>           where squareRoot = (ceiling (sqrt (fromIntegral x)))

> pandigitalPrime x = (pandigital x) && (prime x)
