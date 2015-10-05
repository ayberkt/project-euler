quadratic :: Int -> Int -> (Int -> Int)
quadratic a b = \n -> n^2 + a*n + b

prime :: Int -> Bool
prime x = not $ any (\n -> (x `mod` n) == 0) [2..squareRoot]
          where squareRoot = (ceiling (sqrt (fromIntegral x)))

findMax :: (Int, Int, Int) -> (Int, Int, Int) -> (Int, Int, Int)
findMax val1@(s, a, b) val2@(s', a', b') = if s > s' then val1 else val2

primes :: [Int]
primes = filter prime [2..1000]

maxLength :: Int -> Int -> Int -> Int
maxLength a b n
  | not . prime' $ quadratic a b n = n
  | otherwise = maxLength a b (n + 1)
 where prime' = (`elem` primes)

main :: IO ()
main = do
  let sequences = [(maxLength a b 0, a, b) | a <- [(-1000)..1000]
                                           , b <- [(-1000)..1000]]
      (_, a, b) = foldr findMax (0, 0, 0) sequences
  print $ a * b
