data User = User { firstName
                   , lastName
                   , email
                   , yearOfBirth :: String
                   , account
                   , uid :: Integer
                   } deriving (Show, Read, Eq)

main =
    let object = user
        serializedObject = show object
        deserializedObject = read serializedObject
    in
    print $ object == deserializedObject -- Не сомневайтесь, объекты равны.
    where user = User { firstName = "Denis"
                      , lastName = "Shevchenko"
                      , email = "me@dshevchenko.biz"
                      , yearOfBirth = "1981"
                      , account = 1234567890
                      , uid = 123
                      }
