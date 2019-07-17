import Control.Exception

main :: IO ()
main = do
    result <- try $ return $ 2 `div` 0 :: IO (Either SomeException Integer)
    case result of
        Left exception -> putStrLn $ "Fault: " ++ show exception
        Right value -> print value
