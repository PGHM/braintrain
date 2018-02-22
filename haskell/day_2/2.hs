import System.IO
import Data.List

main = do
    contents <- readFile "2.txt"
    let instructions = lines contents
    let code = show . drop 1 $ scanl' solveInstruction 5 instructions
    print ("The code to the bathroom is: " ++ code)

solveInstruction :: Int -> String -> Int
solveInstruction y [] = y
solveInstruction y (x:xs) = solveInstruction (nextNumber x y) xs

nextNumber :: Char -> Int -> Int
nextNumber 'U' x = if x - 3 < 1 then x else x - 3
nextNumber 'D' x = if x + 3 > 9 then x else x + 3
nextNumber 'L' x = if x `mod` 3 == 1 then x else x - 1
nextNumber 'R' x = if x `mod` 3 == 0 then x else x + 1
