type Login = String
type Password = String
type AvatarURL = String
type UserId = Integer

userInfo :: Login -> Password -> AvatarURL -> UserId -> String
userInfo login password avatarURL userId =
  "Full info about user @" ++ (show userId) ++ ":" ++
  "\n login: " ++ login ++
  "\n password: " ++ password ++
  "\n avatar URL: " ++ avatarURL

type EmptyInfo        = Login -> Password -> AvatarURL -> UserId -> String
type WithLogin        =          Password -> AvatarURL -> UserId -> String
type AndWithPassword  =                      AvatarURL -> UserId -> String
type AndWithAvatarURL =                                   UserId -> String

storeLoginIn :: EmptyInfo -> WithLogin
storeLoginIn emptyInfo =
  emptyInfo "denis"
{- В реальности логин будет получен
в соответствии с переданным userId -}

storePasswordIn :: WithLogin -> AndWithPassword
storePasswordIn infoWithLogin = infoWithLogin "123456789abc"
{- В реальности пароль будет получен
в соответствии с переданным userId -}

storeAvatarURLIn :: AndWithPassword -> AndWithAvatarURL
storeAvatarURLIn infoWithPassword =
  infoWithPassword "http://dshevchenko.biz/denis_avatar.png"
{- В реальности URL будет получен
в соответствии с переданным userId -}

main =
  let userId = 1234
      infoWithLogin = storeLoginIn userInfo
      infoWithPassword = storePasswordIn infoWithLogin
      infoWithAvatarURL = storeAvatarURLIn infoWithPassword
      fulInfoAboutUser = infoWithAvatarURL userId
  in
  putStrLn fulInfoAboutUser
