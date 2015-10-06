import qualified Data.Set as S

divisors :: Int -> [Int]
divisors x = filter ((== 0) . mod x) [1..(x `div` 2)]

divs :: [[Int]]
divs = map divisors [1..28123]

divisors' :: Int -> [Int]
divisors' i = divs !! (i-1)

main = do
  -- There should be a better way of doing this than converting it to
  -- a set but the current solution does solve the problem in under a
  -- minute so I might refactor this later some time.
  let abundant x = (sum (divisors' $ x)) > x
      abundants = filter abundant [12..28123]
      xs = S.fromList [x + y | x <- abundants, y <- abundants, x + y <= 28123]
      total = sum [1..28123]
  print $ total - (sum $ S.elems xs)

