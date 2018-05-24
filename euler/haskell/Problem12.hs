import Data.List

getDivisors :: Integer -> [(Integer, Integer)]
getDivisors n = [(x, div n x) | x <- [1..(ceiling . sqrt $ fromIntegral n)], mod n x == 0]

divisorCount :: Integer -> Int
divisorCount = length . nub . foldl (++) [] . map (\(a, b) -> [a, b]) . getDivisors

-- solution :: Integer
solution = head $ dropWhile ((< 500) . divisorCount) triangular
  where triangular = scanl1 (+) [1..]
