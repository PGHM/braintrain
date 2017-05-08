{-# LANGUAGE NamedFieldPuns #-}
import System.IO
import Data.List
import Data.List.Split

-- Calculating if some node has been visited is inefficient and could be improved

type TurnDirection = Char

data CompassPoint = North | East | South | West deriving (Enum, Eq, Show)

data Walker = Walker { x :: Int
                     , y :: Int
                     , facing :: CompassPoint
                     , visited :: [(Int, Int)]
                     } deriving (Show)

main = do
    contents <- readFile "1.txt"
    let destination = foldl' walk (Walker 0 0 North []) . convertInstructions $ contents
    let distance = (abs . x $ destination) + (abs . y $ destination)
    print ("The HQ is " ++ show distance ++ " blocks away!")

walk :: Walker -> TurnDirection -> Walker
walk Walker {x, y, facing, visited} direction
    -- Comment next line to get the answer to part 1
    | length (nub visited) /= length visited = Walker x y facing visited
    | otherwise = Walker x' y' facing' visited'
    where
        facing' = nextCompassPoint (facing, direction)
        (x', y') = determineNextPoint (x, y) facing'
        visited' = (x', y') : visited

determineNextPoint :: (Int, Int) -> CompassPoint -> (Int, Int)
determineNextPoint (x, y) compassPoint
    | compassPoint == North = (x, y + 1)
    | compassPoint == East = (x + 1, y)
    | compassPoint == South = (x, y - 1)
    | compassPoint == West = (x - 1, y)

convertInstructions :: String -> [TurnDirection]
convertInstructions =  concatMap expandInstructions . splitOn ", "

-- Expand instructions so that we go one step at the time, to actually visit every square
expandInstructions :: String -> [TurnDirection]
expandInstructions (direction:amount) = 
    direction : (take repeatAmount . repeat $ 'S')
    where 
        repeatAmount = (read amount) - 1

nextCompassPoint :: (CompassPoint, TurnDirection) -> CompassPoint
nextCompassPoint (West, 'R') = North
nextCompassPoint (North, 'L') = West
nextCompassPoint (x, 'L') = pred x
nextCompassPoint (x, 'R') = succ x
nextCompassPoint (x, 'S') = x
