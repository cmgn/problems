import Data.List

main :: IO ()
main = interact (show . length . nub . map ((flip mod) 42) . map (read :: String -> Integer) . words)