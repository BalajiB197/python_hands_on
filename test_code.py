# class bool(int):
#     def __init__(self, o: object = ...) -> None: ...
#     @overload
#     def __and__(self, x: bool) -> bool: ...
#     @overload
#     def __and__(self, x: int) -> int: ...
#     @overload
#     def __or__(self, x: bool) -> bool: ...
#     @overload
#     def __or__(self, x: int) -> int: ...
#     @overload
#     def __xor__(self, x: bool) -> bool: ...
#     @overload
#     def __xor__(self, x: int) -> int: ...
#     @overload
#     def __rand__(self, x: bool) -> bool: ...
#     @overload
#     def __rand__(self, x: int) -> int: ...
#     @overload
#     def __ror__(self, x: bool) -> bool: ...
#     @overload
#     def __ror__(self, x: int) -> int: ...
#     @overload
#     def __rxor__(self, x: bool) -> bool: ...
#     @overload
#     def __rxor__(self, x: int) -> int: ...
#     def __getnewargs__(self) -> Tuple[int]: ...

    

# class bool(int):

#     def __new__(cls, val=0):
#         # This constructor always returns an existing instance
#         if val:
#             return True
#         else:
#             return False

#     def __repr__(self):
#         if self:
#             return "True"
#         else:
#             return "False"

#     __str__ = __repr__

#     def __and__(self, other):
#         if isinstance(other, bool):
#             return bool(int(self) & int(other))
#         else:
#             return int.__and__(self, other)

#     __rand__ = __and__

#     def __or__(self, other):
#         if isinstance(other, bool):
#             return bool(int(self) | int(other))
#         else:
#             return int.__or__(self, other)

#     __ror__ = __or__

#     def __xor__(self, other):
#         if isinstance(other, bool):
#             return bool(int(self) ^ int(other))
#         else:
#             return int.__xor__(self, other)

#     __rxor__ = __xor__

# # Bootstrap truth values through sheer willpower
# print(int.__new__(bool, 0))
# print(int.__new__(bool, 1))