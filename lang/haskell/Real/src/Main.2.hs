import Data.Char
import Data.String.Utils

addPrefix :: String -> String
addPrefix url =
    if url `startsWith` prefix then url else prefix ++ url
    where prefix = "http://"

startsWith url prefix = startswith prefix url


encodeAllSpaces = replace " " "%20"

makeItLowerCase = map toLower
-- Заменяем все пробелы на %20.
-- Переводим символы строки в нижнийрегистр.

main =
    putStrLn . addPrefix . encodeAllSpaces . makeItLowerCase $ url
    where url = "www.SITE.com/test me/Start page"
