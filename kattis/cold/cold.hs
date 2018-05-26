main :: IO ()
main = interact $ show . length . filter (<0) . map read . tail . words