module Nat where

data Nat = Zero | Succ Nat
    deriving (Show, Eq, Ord)

