import re

def validate_user_input(first_name, last_name, age):
  """Validates user input to ensure first_name, last_name, and age are not null,
     first_name and last_name are strings without special characters,
     and age is an integer."""

  if not (first_name and last_name and age):
    return False

  # Check if first_name and last_name are strings without special characters
  if not isinstance(first_name, str) or not isinstance(last_name, str):
    return False
  if re.search(r"[^a-zA-Z ]", first_name) or re.search(r"[^a-zA-Z ]", last_name):
    return False

  # Check if age is an integer
  try:
    age = int(age)
  except ValueError:
    return False

  return True
