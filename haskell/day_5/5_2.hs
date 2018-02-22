import System.IO
import Data.Hash.MD5
import Data.Char
import Data.Foldable hiding (length)
import Data.Sequence hiding (take)
import Prelude hiding (length, filter)

main = do
    let input = "ojvtpuvg"
    let password = getPassword input (fromList "--------") 1
    print ("The password is: " ++ (toList password))

getPassword :: String -> Seq Char -> Int -> Seq Char
getPassword input password idx
    | passwordReady password = password
    | take 5 hash == "00000" = getPassword input nextPassword nextIdx
    | otherwise = getPassword input password nextIdx
        where
            nextIdx = idx + 1
            hash = md5s . Str $ input ++ (show idx)
            nextPosition = digitToInt $ hash !! 5
            nextCharacter = hash !! 6
            nextPositionValid = nextPosition >= 0 && nextPosition < 8
            nextPassword = 
                if nextPositionValid && index password nextPosition == '-'
                then update nextPosition nextCharacter password
                else password

passwordReady :: Seq Char -> Bool
passwordReady password = (length $ filter (/='-') password) >= 8
