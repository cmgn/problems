-- far from the best way of doing it but i wanted to try out
-- the any monoid
import Data.Monoid

stoi = (read :: String -> Int)

automaticEligibility :: [String] -> Any
automaticEligibility s = (validYear 2010 school) <> (validYear 1991 birth)
  where [_, school, birth, _] = s
        validYear x = Any . (>= x) . stoi . fst . break (=='/')

getStatus :: String -> String
getStatus s = let s' = words s; name = head s' in
  if getAny $ automaticEligibility s'
    then name ++ " eligible"
    else if (stoi $ last s') <= 40 
      then name ++ " coach petitions"
      else name ++ " ineligible"

main :: IO ()
main = interact  (unlines . map getStatus . tail . lines)
