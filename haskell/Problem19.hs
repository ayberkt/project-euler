module Problem19 where

data Month = January    -- 1
           | February   -- 2
           | March      -- 3
           | April      -- 4
           | May        -- 5
           | June       -- 6
           | July       -- 7
           | August     -- 8
           | September  -- 9
           | October    -- 10
           | November   -- 11
           | December   -- 12
           deriving (Eq, Show, Enum, Bounded)

type Year = Int

isLeapYear :: Year -> Bool
isLeapYear y
  | y `rem` 400 == 0 = True
  | y `rem` 100 == 0 = False
  | y `rem` 4   == 0 = True
  | otherwise        = False

numberOfDays :: Year -> Month -> Int
numberOfDays _ September  = 30
numberOfDays _ April      = 30
numberOfDays _ June       = 30
numberOfDays _ November   = 30
numberOfDays y February   = if isLeapYear y then 29 else 28
numberOfDays _ _          = 31

data Day = Monday
         | Tuesday
         | Wednesday
         | Thursday
         | Friday
         | Saturday
         | Sunday
         deriving (Eq, Show, Enum, Bounded)

type Date = Int

(<+>) :: Day -> Int -> Day
(<+>) d k = toEnum $ (fromEnum d + k) `rem` 7

nextFirstDay :: Day -> Month -> Year -> (Day, (Month, Year))
nextFirstDay d December y = (d <+> numberOfDays y December, (January, y+1))
nextFirstDay d m        y = (d <+> numberOfDays y m, (succ m, y))

type Count = Int

countSundaysFrom :: (Day, Count) -> Month -> Year -> (Day, Count)
countSundaysFrom (d, c) m y
  | y >= 2001 = (d, c)
  | otherwise = let
                  (d', (m', y')) = nextFirstDay d m y
                in
                  if y >= 1901 && d == Sunday then
                    countSundaysFrom (d', (c + 1)) m' y'
                  else
                    countSundaysFrom (d', c) m' y'

main :: IO ()
main = putStrLn $ "Result: " ++ show result
  where
    result = snd $ countSundaysFrom (Monday, 0) January 1900
