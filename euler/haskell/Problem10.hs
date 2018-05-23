{-
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
-}

intSqrt :: Integer -> Integer
intSqrt = (ceiling :: Double -> Integer) . sqrt . fromIntegral

generatePrimes :: [Integer]
generatePrimes = [x | x <- [1..2000000], isPrime x]
  where isPrime x = null [y | y <- [2..intSqrt(x - 1)], mod x y == 0]

main :: IO ()
main = print $ sum generatePrimes