main :: IO ()
main = interact $ (flip(++)) "\n" . show . sum . map (read :: String -> Integer) . lines
