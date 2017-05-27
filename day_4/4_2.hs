import System.IO
import Data.List
import Data.Char
import Data.Ord
import Data.Function
import Data.Maybe

main = do
    let notNumber = not . isDigit
    let readInt = read :: String -> Int

    contents <- readFile "4.txt"
    let rooms = lines contents
    let names = map (filter (/='-') . takeWhile notNumber) rooms
    let sectorIDs = map (readInt . take 3 . dropWhile notNumber) rooms
    let checksums = map (take 5 . drop 1 . dropWhile (/='[')) rooms
    let realRooms = filter realRoom $ zip3 names sectorIDs checksums
    let decryptedRooms = map decryptedRoom realRooms
    let northPoleObjectsRoom = fromJust . find ((=="northpoleobjectstorage") . fst) $ decryptedRooms
    print ("North pole object storage room is in sector: " ++ (show . snd $ northPoleObjectsRoom))

realRoom :: (String, Int, String) -> Bool
realRoom (name, _, checksum) = fiveMostCommon == checksum
    where 
        uniqueLetters = sort . nub $ name
        occurances = map (\x -> length $ filter (==x) name) uniqueLetters
        fiveMostCommon = snd . unzip . take 5 . sortDescOnFirst $ zip occurances uniqueLetters

decryptedRoom :: (String, Int, String) -> (String, Int)
decryptedRoom (name, sectorID, _) = (decryptedName, sectorID)
    where
        decryptedName = map (\x -> iterate shiftCipher x !! sectorID) name

sortDescOnFirst :: Ord a => [(a, b)] -> [(a, b)]
sortDescOnFirst = sortBy (flip compare `on` fst)

shiftCipher :: Char -> Char
shiftCipher x
    | x == 'z' = 'a'
    | otherwise = succ x
