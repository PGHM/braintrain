import System.IO
import Data.List
import Data.List.Split

-- The oneliner might be over the top but I just had to. Basically it reads the lines, removes whitespace and converts strings to numbers, then the list is filtered and counted.

main = do
    contents <- readFile "3.txt"
    let triangels = show . length . filter isTriangle . map (map read . filter (/="") . splitOn " ") . lines $ contents
    print ("Number of proper triangels is: " ++ triangels)

isTriangle :: [Int] -> Bool
isTriangle [x, y, z] = x + y > z && x + z > y && z + y > x
