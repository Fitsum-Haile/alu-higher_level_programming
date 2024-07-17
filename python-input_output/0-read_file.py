#!/usr/bin/python3
"""This module provides a function to read a text file
(UTF8) and print its content to stdout."""


def read_file(filename=""):
  """
  Reads a text file (UTF8) and prints its content to stdout.

  Args:
      filename (str, optional): The name of the file to read. Defaults to "".
  """
  # Open the file in read mode with UTF-8 encoding
  with open(filename, "r", encoding="utf-8") as file:
    # Read the entire content of the file
    content = file.read()
    # Print the content to stdout
    print(content)
