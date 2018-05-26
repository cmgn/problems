main :: IO ()
main = interact $ show . (+1) . (\[a, b] -> a * (b - 1)) . map (read :: String -> Integer) . words
