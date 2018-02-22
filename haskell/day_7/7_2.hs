import System.IO
import Data.List
import Debug.Trace

type Address = String
type Hypernet = String
type IP = String

main = do
    contents <- readFile "7.txt"
    let ips = lines contents
    let separated = map (separateIpParts [] []) ips
    let abasGathered = map (\x -> (gatherAbas [] $ fst x, gatherAbas [] $ snd x)) separated
    let sslCount = show . length . filter (==True) $ map (isSSLIP) abasGathered
    print ("Number of SSL supported IP:s in the list is: " ++ sslCount)

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

gatherAbas :: [String] -> [String] -> [String]
gatherAbas abas [] = abas
gatherAbas abas (x:xs) = gatherAbas (abasFromString abas x) xs

abasFromString :: [String] -> String -> [String]
abasFromString abas (a : b : c : x) 
    | a == c && a /= b = abasFromString ((a : b : c : "") : abas) $ b : c : x
    | otherwise = abasFromString abas $ b : c : x
abasFromString abas _ = nub abas

isSSLIP :: ([String], [String]) -> Bool
isSSLIP (xs, ys) = or $ [isReverseAba x y | x <- xs, y <- ys]

isReverseAba :: String -> String -> Bool
isReverseAba (a : b : _) (c : d : _) = a == d && b == c
