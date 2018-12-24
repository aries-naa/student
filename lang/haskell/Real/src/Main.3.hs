removeAllEmptyNamesFrom :: [String] -> [String]
removeAllEmptyNamesFrom listOfNames =
  filter notEmptyName listOfNames
  where notEmptyName = not . null

main =
  print $ removeAllEmptyNamesFrom listOfNames
  where listOfNames = ["John", "", "Ann"]
