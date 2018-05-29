main :: IO ()
main = interact $ unlines . map ((++" Abracadabra") . show) . enumFromTo 1 . read
