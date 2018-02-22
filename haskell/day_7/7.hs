import System.IO
import Data.List

type Address = String
type Hypernet = String
type IP = String

main = do
    contents <- readFile "7.txt"
    let ips = lines contents
    let separated = map (separateIpParts [] []) ips
    let checked = map (\x -> (listHasAbba . fst $ x) && (not . listHasAbba . snd $ x)) separated
    let tlsCount = show . length . filter (==True) $ checked
    print ("Number of TLS supported IP:s in the list is: " ++ tlsCount)

separateIpParts :: [Address] -> [Hypernet] -> IP -> ([Address], [Hypernet])
separateIpParts addresses hypernets ip
    | ip == "" = (addresses, hypernets)
    | head ip == '[' = separateIpParts addresses hypernets' ip'
    | otherwise = separateIpParts addresses' hypernets ip''
        where
            ip' = drop 1 . dropWhile (/=']') $ ip
            ip'' = dropWhile (/='[') ip
            addresses' = (takeWhile (/='[') ip) : addresses
            hypernets' = (takeWhile (/=']') . drop 1 $ ip) : hypernets

listHasAbba :: [String] -> Bool
listHasAbba = or . map abbaCheck

abbaCheck :: String -> Bool
abbaCheck (a : b : c : d : x) 
    | a == d && b == c && a /= b = True
    | otherwise = abbaCheck $ b : c : d : x
abbaCheck x = False
