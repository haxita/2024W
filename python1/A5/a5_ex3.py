def safe_list_access(lst, index):
    element = None
    try:
        # check list
        if not isinstance(lst, list):
            raise TypeError("First argument is not a list")
        
        # check index
        if not isinstance(index, int):
            print("Converting Index to integer")
            index = int(index)
        
        # visit elements
        element = lst[index]
    except TypeError as te:
        if str(te) == "First argument is not a list":
            return "First argument is not a list"
        else:
            # deal with index error
            return "Index cannot be converted to an integer"
    except ValueError:
        return "Index cannot be converted to an integer"
    except IndexError:
        return "Index out of range"
    finally:
        print("Operation completed")
    
    return element