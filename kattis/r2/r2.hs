main :: IO ()
main = interact $ show . recoverR2 . map read . words
  where recoverR2 [a, b] = 2 * b - a