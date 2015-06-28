import Data.List (elemIndex, sort)
import Data.Char (digitToInt)

assessNext :: [Int] -> [Int] -> [Int]
assessNext xs ys = [(xs !! i) + if (ys !! i) > (ys !! (i+1))
                                then (ys !! i)
                                else (ys !! (i+1)) | i <- [0..(length xs) - 1]]
pathWeights :: [[Int]] -> [[Int]]
pathWeights (x1:x2:xs)
  | null xs = (assessNext x2 x1) : xs
  | otherwise = x1 : (pathWeights $ (assessNext x2 x1):xs)

main = do
  triangle <- readFile "problem18-triangle.txt"
  let rows = lines triangle
      numStrs = map words rows
      stringToInt :: [Char] -> Int
      stringToInt xs = read xs
      nums = map (map stringToInt) numStrs
  print . last . pathWeights . reverse $ nums
