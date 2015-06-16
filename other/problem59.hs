import Data.Char (ord, chr, isAlpha, isSpace, isPunctuation)
import Data.Bits (xor)
import Data.List.Split (splitOn)
import System.IO
import Data.List

extendKey :: String -> Int -> String
extendKey key messageLength = let quotient = messageLength `div` length key
                                  remainder = messageLength `mod` length key in
  concat $ (replicate quotient key) ++ [(take remainder key)]

decrypt :: [Int] -> String -> String
decrypt crypt key = map chr $ zipWith xor crypt
                                      (map ord $ extendKey key (length crypt))

possibleDecryptions :: [Int] -> [String]
possibleDecryptions message = let alphabet = ['a'..'z']
                                  keys = [[a,b,c] | a <- alphabet, b <- alphabet, c <- alphabet] in
  map (decrypt message) keys

findAsciiSum text = sum $ map ord text
main = do
  handle <- openFile "cipher.txt" ReadMode
  contents <- hGetContents handle
  let cipher = map (\n -> read n :: Int) $ splitOn "," contents
      decryptedMessage = head $ filter (isInfixOf " and ") $ possibleDecryptions cipher
  putStrLn $ "ASCII sum is " ++ show (findAsciiSum decryptedMessage)
