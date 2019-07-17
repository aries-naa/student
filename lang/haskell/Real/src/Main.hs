data IPAddress = IPAddress (String, Integer)
instance Show IPAddress where
  show (IPAddress address) = (show $ fst $ address) ++ " ===> " ++ (show $ snd $ address)

main = print $ show $ IPAddress ("127.0.0.1", 123)
