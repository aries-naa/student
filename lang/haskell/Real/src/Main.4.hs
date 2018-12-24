import Data.Char

main = print [toUpper c | c <- "http", c /= 'h' && c /= 'p']
