#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":
    b1 = Base()
    print(b1.id)  # Should print 1

    b2 = Base()
    print(b2.id)  # Should print 2

    b3 = Base()
    print(b3.id)  # Should print 3

    b4 = Base(12)
    print(b4.id)  # Should print 12

    b5 = Base()
    print(b5.id)  # Should print 4
