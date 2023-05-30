#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if two squares have equal areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares have different areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are different, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Compare if one square has a greater area than the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if one square has a greater or equal area than the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """Compare if one square has a smaller area than the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is smaller, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if one square has a smaller or equal area than the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is smaller or equal, False otherwise.
        """
        return self.area() <= other.area()
