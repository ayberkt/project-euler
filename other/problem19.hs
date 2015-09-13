data Day = Monday
         | Tuesday
         | Wednesday
         | Thursday
         | Friday
         | Saturday
         | Sunday
         deriving (Show)

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
    pred Thursday   = Wednesday
    pred Wednesday = Tuesday
    pred Tuesday   = Monday

    enumFrom day = iterate succ day


after :: Int -> Day -> Day
after numDays = let shift = (numDays `rem` 7) + 1 in
  last . take shift . iterate succ
             
           
leapYear :: Int -> Bool
leapYear year
  | year `rem` 10 == 0 = year `rem` 400 == 0
  | otherwise = year `rem` 4 == 0
