import Data.List (elemIndex)

data Day = Monday
         | Tuesday
         | Wednesday
         | Thursday
         | Friday
         | Saturday
         | Sunday
         deriving (Show, Eq, Ord)
                    
instance Enum Day where
    succ Monday    = Tuesday
    succ Tuesday   = Wednesday
    succ Wednesday = Thursday
    succ Thursday  = Friday
    succ Friday    = Saturday
    succ Saturday  = Sunday
    succ Sunday    = Monday

    pred Monday    = Sunday
    pred Sunday    = Saturday
    pred Saturday  = Friday
    pred Friday    = Thursday
    pred Thursday  = Wednesday
    pred Wednesday = Tuesday
    pred Tuesday   = Monday

    enumFrom day = iterate succ day
    
    fromEnum day = case day `elemIndex` [Monday ..] of
      Just n  -> n

    toEnum n = (enumFrom Monday) !! n


daysAfter :: Int -> Day -> Day
daysAfter n day = [day ..] !! n
             
           
leapYear :: Int -> Bool
leapYear year
  | year `rem` 10 == 0 = year `rem` 400 == 0
  | otherwise = year `rem` 4 == 0
