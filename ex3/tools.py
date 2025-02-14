class Tools:
    """
        Miscellaneous general tools.
    
        Copyright: Sami Pyöttilä, 2006
    """

    @staticmethod
    def repeat_string(string, n):
        """ Returns a string obtained by repeating the given string n times.

            Preconditions: string is not None and n >= 1
        """
        result = ""
        for i in range(1, n + 1):
            result += string
        return result


    @staticmethod
    def approximately_equal(d1, d2, precision):
        """ Do the numbers d1 and d2 differ by at most the absolute value of precision? """
        return abs(d1 - d2) <= abs(precision)
