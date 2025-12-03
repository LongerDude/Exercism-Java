# TODO: define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

# TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining bake time.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    try:
        time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
        return time_remaining
    except TypeError:
        print('Please input a valid number for elapsed bake time.')
        return None


# TODO: Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the total preparation time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (in minutes).

    Function that takes the number of layers you want to add to the lasagna as
    an argument and returns how many minutes you would need to prepare them.
    """
    try:
        y = int(number_of_layers) * PREPARATION_TIME
        return y
    except TypeError:
        print('Please input a valid number of layers.')
        return None



# TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed minutes (prep + bake).

    Function that takes two arguments:
    - the number of layers you want to add to the lasagna
    - the number of minutes the lasagna has been in the oven
    and returns the total elapsed minutes spent cooking the lasagna.
    """
    try:
        x = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
        return x
    except TypeError:
        print('Please input valid numbers for the number of layers and elapsed bake time.')
        return None