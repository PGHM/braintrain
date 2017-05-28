import System.IO
import Data.List
import Data.List.Split

-- Original input had "rotate column" and "rotate row", I replaced them with 
-- "rotate_column" and "rotate_row" to make the parsing sensible

data InstructionType = Rect | RotateRow | RotateColumn deriving (Enum, Eq, Show)

type Instruction = (InstructionType, Int, Int)
type Grid = [[Char]]

main = do
    contents <- readFile "8.txt"
    let rawInstructions = lines contents
    let instructions = reverse $ foldl' (\xs raw -> parseInstruction raw : xs) [] rawInstructions
    let grid = [[' ' | _ <- [1..50]] | _ <- [1..6]]
    let finalGrid = foldl' modifyGrid grid instructions
    let litPixelCount = show . sum $ map (length . filter (=='X')) finalGrid
    mapM_ print finalGrid
    print $ "The amount of pixels lit is: " ++ litPixelCount

modifyGrid :: Grid -> Instruction -> Grid
modifyGrid grid (instructionType, arg1, arg2)
    | instructionType == Rect = applyRect grid arg1 arg2
    | instructionType == RotateRow = applyRotate grid arg1 arg2
    | instructionType == RotateColumn = transpose $ applyRotate (transpose grid) arg1 arg2

-- Make the rect row by row going from bottom to top
applyRect :: Grid -> Int -> Int -> Grid
applyRect grid _ 0 = grid
applyRect grid width heigth = applyRect grid' width $ heigth - 1
    where
        index = heigth - 1
        newRow = (take width $ repeat 'X') ++ (drop width $ grid !! index)
        grid' = updateRow grid index newRow

applyRotate :: Grid -> Int -> Int -> Grid
applyRotate grid index amount = updateRow grid index newRow
    where newRow = rotate (grid !! index) amount

rotate :: [a] -> Int -> [a]
rotate row amount = snd parts ++ fst parts
    where parts = splitAt (length row - amount) row

updateRow :: Grid -> Int -> [Char] -> Grid
updateRow grid index row = head ++ (row : tail)
    where 
        head = take index grid
        tail = drop (index + 1) grid

parseInstruction :: String -> Instruction
parseInstruction raw
    | instructionType == "rect" = (Rect, columns, rows)
    | instructionType == "rotate_column" = (RotateColumn, index, amount)
    | instructionType == "rotate_row" = (RotateRow, index, amount)
    | otherwise = (Rect, 0, 0)
        where
            splitted = splitOn " " raw
            instructionType = splitted !! 0
            rectArgs = splitOn "x" $ splitted !! 1
            columns = read $ rectArgs !! 0
            rows = read $ rectArgs !! 1
            index = read . drop 2 $ splitted !! 1
            amount = read $ splitted !! 3
