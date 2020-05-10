# Copyright 2020 Alvaro Bartolome del Canto
# See LICENSE for details.

def sample_function(value=True):
    """
    This is a sample function which returns a different str depending on the 
    flag value.

    Args:
        - value (:obj:`bool`): it can either be True or False.

    Returns:
        :obj:`str` - result
            This function returns a :obj:`str` which has a different value depending 
            on the input parameter.
    """

    if value:
        return "This is a sample function"
    else:
        return "This is not a sample function"
