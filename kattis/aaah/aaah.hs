solution :: [String] -> String
solution [a, b] = if a <= b
                    then "go"
                    else "no"

main :: IO ()
main = interact (solution . words)
