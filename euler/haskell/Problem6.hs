{-
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
-}

sumN :: Integer -> Integer
sumN n = (n * (n + 1)) `div` 2

sumSquaresN :: Integer -> Integer
sumSquaresN n = (n * (n + 1) * (2 * n + 1)) `div` 6

main :: IO ()
main = print . abs $ (sumSquaresN 100) - ((sumN 100) ^ 2)