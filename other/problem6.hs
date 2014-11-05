sumSquares x = sum $ map (^2) [1..x]

squareSum x = ((x * (x + 1)) / 2)^2

difference x = squareSum x - sumSquares x

main = print $ difference 100
