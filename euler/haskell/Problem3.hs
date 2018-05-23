intSqrt :: Integer -> Integer
intSqrt = (ceiling :: Double -> Integer) . sqrt . fromIntegral

primeFactors :: Integer -> [Integer]
primeFactors 1 = []
primeFactors n
  | factors == [] = [n]
  | otherwise     = factors ++ primeFactors (div n (head factors))
  where factors = take 1 . filter ((==) 0 . mod n) $ [2..intSqrt(n - 1)]

main :: IO ()
main = print $ last $ primeFactors 600851475143