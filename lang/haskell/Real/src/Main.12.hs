data Year value = Year value deriving Show

instance Functor Year where
    fmap f (Year value) = Year (f value)

increase :: Int -> Int
increase year = year + 1

xxx = Year "1230"

main :: IO ()
main =
    print $ fmap increase year
    where year = Year 1981
