import System.IO
import Data.List
import Data.List.Split

-- Okay, this is even worse than in the first part, I swear it is the last time I do it, but it is so neat to chain the function calls!
-- So first it takes the triangles as in part one, then it transposes the rows and columns and makes one big list out of the three columns
-- Then it splits it to chunks of three so now we have triangles again and we can filter them

main = do
    contents <- readFile "3.txt"
    let triangels = show . length . filter isTriangle . splitEvery 3 . concat . transpose 
                  . map (map read . filter (/="") . splitOn " ") . lines $ contents
    print ("Number of proper triangels is: " ++ triangels)

isTriangle :: [Int] -> Bool
isTriangle [x, y, z] = x + y > z && x + z > y && z + y > x
