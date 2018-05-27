main :: IO ()
main = interact $ show . (\[a, b] -> a * (b - 1) + 1) . map read . words
