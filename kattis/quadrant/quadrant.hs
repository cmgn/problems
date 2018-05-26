main :: IO ()
main = interact $ show . quadrant . map (read :: String -> Integer) . words
  where quadrant [x, y]
          | x > 0 && y > 0 = 1
          | x < 0 && y > 0 = 2
          | x < 0 && y < 0 = 3
          | otherwise      = 4