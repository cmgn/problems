{-
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

only have to check 11, 13, 14, 16, 17, 18, 19, 20

C solution works far better
-}

validNumber :: Integer -> Bool
validNumber n = all ((==) 0) $ fmap (mod n) [11, 13, 14, 16, 17, 18, 19, 20]

getSmallest :: Integer
getSmallest = head $ dropWhile (not . validNumber) (tail [20,40..])

main :: IO ()
main = print getSmallest