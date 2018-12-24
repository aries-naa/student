main :: IO ()

main = do
    fileContent <- readFile "Users/shevchenko/test.c"
    -- неверный путь
    putStrLn fileContent
