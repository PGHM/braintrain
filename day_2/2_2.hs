import System.IO
import Data.List

type Position = (Int, Int)
type PositionValue = (Position, Char)

-- Did not find a fancy way to move in this keypad like in first part, so just use 2D array here :/
keypad = ["0000000"
         ,"0001000"
         ,"0023400"
         ,"0567890"
         ,"00ABC00"
         ,"000D000"
         ,"0000000"
         ]

main = do
    contents <- readFile "2.txt"
    let instructions = lines contents
    let codeMaker = (\ s@(x:xs) y -> solveInstruction y x : s)
    let code = snd . unzip . drop 1 . reverse $ foldl' codeMaker [((1, 3), '5')] instructions
    print ("The code to the bathroom is: " ++ code)

solveInstruction :: String -> PositionValue -> PositionValue
solveInstruction [] (position@(x, y), value) =  (position, keypad !! y !! x)
solveInstruction (direction:xs) (position, value) = solveInstruction xs $ (nextPosition direction position, value)

nextPosition :: Char -> Position -> Position
nextPosition direction (x, y) = if keypad !! y' !! x' == '0' then (x, y) else (x', y')
    where x' = case direction of 'L' -> x - 1
                                 'R' -> x + 1
                                 _ -> x
          y' = case direction of 'U' -> y - 1
                                 'D' -> y + 1
                                 _ -> y
