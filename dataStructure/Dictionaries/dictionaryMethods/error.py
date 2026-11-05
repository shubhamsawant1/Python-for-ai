# Wrong - lists can't be keys

bad_dict = {(1, 2): "value"}  # TypeError!

# Right - use immutable types
good_dict = {(1, 2): "value"}   # Tuple is OK
good_dict = {"1, 2": "value"}   # String is OK



