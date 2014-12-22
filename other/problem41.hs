 import qualified Data.Set as Set
 
digits :: Integer -> [Integer]
digits n = reverse (inverseDigits n)
           where inverseDigits n
                   | n == 0 = []
                   | otherwise = (n `mod` 10) : inverseDigits (n `div` 10)

numDigits :: Integer -> Integer
numDigits n
   | n == 0 = 0
   | otherwise = 1 + (numDigits (n `div` 10))
 
pandigital :: Integer -> Bool
pandigital x = (Set.fromList (digits x)) == digitsSet
               where digitsSet = Set.fromList [1..(numDigits x)]

prime :: Integer -> Bool
prime x = not $ any (\n -> (x `mod` n) == 0) [2..squareRoot]
          where squareRoot = (ceiling (sqrt (fromIntegral x)))

pandigitalPrime x = (pandigital x) && (prime x)
