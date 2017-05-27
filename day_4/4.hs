import System.IO
import Data.List
import Data.Char
import Data.Ord
import Data.Function

main = do
    let notNumber = not . isDigit
    let readInt = read :: String -> Int

    contents <- readFile "4.txt"
    let rooms = lines contents
    let names = map (filter (/='-') . takeWhile notNumber) rooms
    let sectorIDs = map (readInt . take 3 . dropWhile notNumber) rooms
    let checksums = map (take 5 . drop 1 . dropWhile (/='[')) rooms
    let sectorSum = show . sum $ map roomValue $ zip3 names sectorIDs checksums
    print ("Sum of the real room sector IDs is: " ++ sectorSum)

roomValue :: (String, Int, String) -> Int
roomValue (name, sectorID, checksum) = if realRoom name checksum then sectorID else 0

realRoom :: String -> String -> Bool
realRoom name checksum = fiveMostCommon == checksum
    where 
        uniqueLetters = sort . nub $ name
        occurances = map (\x -> length $ filter (==x) name) uniqueLetters
        fiveMostCommon = snd . unzip . take 5 . sortDescOnFirst $ zip occurances uniqueLetters

sortDescOnFirst :: Ord a => [(a, b)] -> [(a, b)]
sortDescOnFirst = sortBy (flip compare `on` fst)
