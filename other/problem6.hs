sumSquares x = sum $ map (^2) [1..x]

squareSum x = ((x * (x + 1)) / 2)^2

main = print $  (\x -> squareSum x - sumSquares x) 100
