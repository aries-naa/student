data IPAddress = IPAddress String
                 deriving Show

data Tt = X1 String | X2 Integer

--instance Show IPAddress where
--  show (IPAddress address) =
--    if address == "127.0.0.1" then "localhost" else address

main = putStrLn $ show $ IPAddress "127.0.0.1"
