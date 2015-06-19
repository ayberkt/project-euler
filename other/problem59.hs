import Data.Char (ord, chr, isAlpha, isSpace, isPunctuation)
import Data.Bits (xor)
import Data.List.Split (splitOn)
import Data.List

type Cipher = [Int]

extendKey :: String -> Int -> String
extendKey key messageLength = concat $ (replicate quotient key) ++ [(take remainder key)]
  where quotient = messageLength `div` length key
        remainder = messageLength `mod` length key


decrypt :: Cipher -> String -> String
decrypt cipher key = map chr $ zipWith xor cipher $
                                       map ord $ extendKey key $ length cipher

possibleDecryptions :: Cipher -> [String]
possibleDecryptions message = map (decrypt message) keys
  where keys = [[a,b,c] | a <- ['a'..'z'], b <- ['a'..'z'], c <- ['a'..'z']]

main = do
  contents <- readFile "cipher.txt"
  let cipher = map (\n -> read n :: Int) $ splitOn "," contents
      decryptedMessage = head $ filter (isInfixOf " and ") $ possibleDecryptions cipher
  putStrLn decryptedMessage
  -- putStrLn $ "ASCII sum is " ++ show (sum $ map ord decryptedMessage)
