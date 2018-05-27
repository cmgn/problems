import Data.List

main :: IO ()
main = interact $ (\x -> if x == True then "yes" else "no") . isUnique . words
  where isUnique x = length x == length (nub x)