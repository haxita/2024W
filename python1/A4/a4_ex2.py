def compose(*functions):

    def composed_function(x):
        result = x
        for func in reversed(functions):
            result = func(result)
        return result

    return composed_function
































































