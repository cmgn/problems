{-
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
-}

generatePair :: (Integer, Integer, Integer)
generatePair = head $ dropWhile (not . prop) [euclid m n | m <- [1..100], n <- [1..m]]
  where euclid m n = (m^2 - n^2, 2 * m * n, m^2 + n^2 :: Integer)
        prop (a, b, c) = a + b + c == 1000

main :: IO ()
main = print . (\(a, b, c) -> a * b * c) $ generatePair
