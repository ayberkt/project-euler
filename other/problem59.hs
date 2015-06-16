import Data.Char (ord, chr, isAlpha, isSpace, isPunctuation)
import Data.Bits (xor)
import Data.List.Split (splitOn)
import Data.List

extendKey :: String -> Int -> String
extendKey key messageLength = let quotient = messageLength `div` length key
                                  remainder = messageLength `mod` length key in
  concat $ (replicate quotient key) ++ [(take remainder key)]

decrypt :: [Int] -> String -> String
decrypt crypt key = map chr $ zipWith xor crypt $
                                      map ord $ extendKey key $ length crypt

possibleDecryptions :: [Int] -> [String]
possibleDecryptions message = map (decrypt message) keys
  where keys = [[a,b,c] | a <- ['a'..'z'], b <- ['a'..'z'], c <- ['a'..'z']]

main = do
  contents <- readFile "cipher.txt"
  let cipher = map (\n -> read n :: Int) $ splitOn "," contents
      decryptedMessage = head $ filter (isInfixOf " and ") $ possibleDecryptions cipher
  putStrLn $ "ASCII sum is " ++ show (sum $ map ord decryptedMessage)
