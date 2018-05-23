fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

sumEvenFibs :: Integer
sumEvenFibs = sum . filter ((==) 0 . (flip mod) 2) . takeWhile (<4000000) $ fibs

main :: IO ()
main = print sumEvenFibs