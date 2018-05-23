import Data.List
import Data.Bits

binaryToDecimal :: String -> Int
binaryToDecimal = foldl' f 0
  where f x '0' = x * 2
        f x '1' = x * 2 + 1

processTestCase :: [String] -> String
processTestCase xs = fst . head . sortBy (\(_, a) (_, b) -> compare a b) . map f $ zip ys xs
  where f (a, b) = (b, sum [popCount . abs $ y - a | y <- ys])
        ys = map binaryToDecimal xs

inputConsumer :: [String] -> String
inputConsumer [] = ""
inputConsumer xs = (processTestCase . take n $ tail xs) ++ "\n" ++ (inputConsumer $ drop (n + 1) xs) 
  where n = (read . head . words $ head xs) :: Int

main :: IO ()
main = getContents >>= putStr . inputConsumer . tail . lines
