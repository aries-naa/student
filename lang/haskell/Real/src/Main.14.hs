import Data.Functor
import Control.Applicative

newtype Distance value = Distance value deriving Show

instance Functor Distance where
    fmap magicWand (Distance value) = Distance (magicWand value)

instance Applicative Distance where
    Distance magicWand <*> functor = fmap magicWand functor

obtainTwoTextsFromUser :: IO String
--obtainTwoTextsFromUser =
--    (++) <$> IO String <*> IO String
--obtainTwoTextsFromUser = do
--    putStrLn "Enter your text, please: "
--    firstText <- getLine
--    putStrLn "One more, please: "
--    secondText <- getLine
--    return $ firstText ++ secondText

obtainTwoTextsFromUser =
    (++) <$> getFirstText <*> getSecondText
    -- Складываем строки.
    where getFirstText  = putStrLn "Enter your text, please: " *> getLine
          getSecondText = putStrLn "One more, please: "        *> getLine

main :: IO ()
--main = print $ ((+) <$> Distance 20) <*> Distance 4
--main = print $ (\x -> x + 1) <$> Distance 19.76
--main = do
--    twoTexts <- obtainTwoTextsFromUser
--    putStrLn $ "You said " ++ twoTexts
main = print $ (*2) <$> [1, 2, 3]
