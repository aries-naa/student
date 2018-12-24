data IPAddress = IP String Integer

type SHU = Integer
-- SHU (Scoville Heat Units), единица жгучести перца

class Pepper pepper where
    color :: pepper -> String
    pungency :: pepper -> SHU

data Poblano = Poblano
-- распространён в национальных блюдах Мексики
data TrinidadScorpion = TrinidadScorpion
-- самый жгучий перец в мире

instance Pepper Poblano where
    color Poblano = "green"
    pungency Poblano = 1500

instance Pepper TrinidadScorpion where
    color TrinidadScorpion = "red"
    pungency TrinidadScorpion = 855000

xxx = IP "123" 456

-- yyy :: IO Integer
-- yyy = return 123

main =
    putStrLn $ show (pungency trinidad) ++ ", " ++ color trinidad
    where trinidad = TrinidadScorpion
