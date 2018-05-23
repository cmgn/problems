{-
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

100 100
100 101
101 100 <- duplicate
from n = 100 to 999
  from m = n to 999
    ...
-}

pairs :: [(Integer, Integer)]
pairs = [(x, y) | x <- [100..999], y <- [x..999]]

isPalindrome :: Integer -> Bool
isPalindrome n = s == reverse s
  where s = show n

largestPalindrome :: Integer
largestPalindrome = maximum $ filter (isPalindrome) $ map (uncurry (*)) pairs

main :: IO ()
main = print largestPalindrome