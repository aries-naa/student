import Control.Exception

tryToOpenFile :: FilePath -> IO String
tryToOpenFile path =
    readFile path `catch` possibleErrors
    where
        possibleErrors :: IOException -> IO String
        possibleErrors error = return $ show error ++ "!!!"

main :: IO ()
main = do
    fileContent <- tryToOpenFile "Users/shevchenko/test.c"
    putStrLn fileContent
