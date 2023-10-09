#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """invert == and !="""
    def __eq__(self, __value: object) -> bool:
        """switch == opeartor with !="""
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        """switch != opeartor with =="""
        return super().__eq__(__value)
