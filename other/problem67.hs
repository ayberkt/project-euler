import Data.List (elemIndex, sort)
import Data.Char (digitToInt)

-- | This is *exactly* the same as problem 18, with the only
-- | difference being the name of the file from which the
-- | triangle is loaded. The reason I copied and pasted the
-- | solution for problem 18 is that I don't maintain a module
-- | system in Project Euler solutions.

assessNext :: [Int] -> [Int] -> [Int]
assessNext xs ys = [(xs !! i) + if (ys !! i) > (ys !! (i+1))
                                then (ys !! i)
                                else (ys !! (i+1)) | i <- [0..(length xs) - 1]]
pathWeights :: [[Int]] -> [[Int]]
pathWeights (x1:x2:xs)
  | null xs = (assessNext x2 x1) : xs
  | otherwise = x1 : (pathWeights $ (assessNext x2 x1):xs)

main = do
  triangle <- readFile "problem67-triangle.txt"
  let rows = lines triangle
      numStrs = map words rows
      stringToInt :: [Char] -> Int
      stringToInt xs = read xs
      nums = map (map stringToInt) numStrs
  print . last . pathWeights . reverse $ nums
