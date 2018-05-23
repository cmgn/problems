import Data.List

cartesianProd :: [String] -> [(String, String)]
cartesianProd xs = filter (uncurry (/=)) $ (,) <$> xs <*> xs

main :: IO ()
main = interact (unlines . sort . nub . map (uncurry (++)) . cartesianProd . words)
