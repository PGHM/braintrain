import System.IO
import Data.List
import Data.Hash.MD5

main = do
    let input = "ojvtpuvg"
    let password = getPassword input "" 1
    print password

getPassword :: String -> String -> Int -> String
getPassword input password index
    | length password >= 8 = password
    | take 5 hash == "00000" = getPassword input nextPassword nextIndex
    | otherwise = getPassword input password nextIndex
        where
            hash = md5s . Str $ input ++ (show index)
            nextPasswordCharacter = hash !! 5
            nextPassword = password ++ [nextPasswordCharacter]
            nextIndex = index + 1
