import System.IO
import Data.List
import Data.Ord
import Data.Function

main = do
    contents <- readFile "6.txt"
    let columns = transpose . lines $ contents
    let occurances = [[(char, length $ filter (==char) column) | char <- (nub column)] | column <- columns]
    let message = map (fst . head . sortDescOnSecond) occurances
    print ("The message is: " ++ message)

sortDescOnSecond :: Ord b => [(a, b)] -> [(a, b)]
sortDescOnSecond = sortBy (flip compare `on` snd)
