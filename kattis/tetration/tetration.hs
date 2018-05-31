main :: IO ()
main = interact $ show . (\x -> x ** (1/x)) . read