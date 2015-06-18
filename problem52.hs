import Data.Set (Set, fromList, union, empty)

consistsOfSameDigits :: Int -> Int -> Bool
consistsOfSameDigits x y
  | x == y = True
  | otherwise = digits x == digits y

digits :: Int -> Set Int
digits x = fromList $ makeDigitList x
  where makeDigitList n
          | n == 0 = []
          | otherwise = (n `rem` 10) : (makeDigitList $ n `div` 10)

allConsistOfSameDigits :: [Int] -> Bool
allConsistOfSameDigits (x:xs) = let targetDigits = digits x in
  all (targetDigits ==) $ map digits xs

main = do
  print $ head $ dropWhile (not . allConsistOfSameDigits) [[a, 2*a, 3*a, 4*a, 5*a, 6*a] | a <- [2..]]
