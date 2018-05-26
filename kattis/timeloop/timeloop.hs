main :: IO ()
main = interact (\x -> (unlines . map ((++" Abracadabra") . show)) [1..((read :: String -> Int) x)])
