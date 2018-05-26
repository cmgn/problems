main :: IO ()
main = interact $ show . (^2) . (+1) . (2^) . (read :: String -> Integer)
