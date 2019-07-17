import Control.Exception

main :: IO ()
main = do
---    result <- try $ readFile path
-- :: IO (Either IOException String)
    result <- xxx
    case result of
        Left exception -> putStrLn $ "Fault: " ++ show exception
        Right content -> putStrLn content
    where path = "Users/dshevchenko/test.c"
          xxx :: IO (Either IOException String)
          xxx = try $ readFile path
