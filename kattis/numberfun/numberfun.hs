isPossible :: String -> Bool
isPossible s = (a + b == c) || ((abs $ b - a) == c) || (a * b == c) || (a / b == c || b / a == c)
  where [a, b, c] = map (read :: String -> Double) $ words s

main :: IO ()
main = interact (unlines . map processCase . tail . lines)
  where processCase x = if isPossible x
                          then "Possible"
                          else "Impossible"
