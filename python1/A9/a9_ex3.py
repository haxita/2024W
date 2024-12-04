import os

class Reader:
    def __init__(self, path: str):
        """
        Initializes the Reader object by opening the specified file in binary read mode.
        
        Args:
            path (str): The path to the file to be read.
        
        Raises:
            ValueError: If the provided path does not point to a valid file.
            TypeError: If the provided path is not a string.
        """
        if not isinstance(path, str):
            raise TypeError(f"Path must be a string, not '{type(path).__name__}'")
        
        if not os.path.isfile(path):
            raise ValueError(f"The path '{path}' does not point to a valid file.")
        
        self._path = path
        try:
            self._file = open(path, "rb")
        except Exception as e:
            raise ValueError(f"Failed to open the file: {e}")
        
        # Determine the size of the file in bytes
        self._file.seek(0, os.SEEK_END)
        self._size = self._file.tell()
        self._file.seek(0)  # Reset the file pointer to the beginning

    def close(self):
        """
        Closes the opened file. After calling this method, the Reader instance
        cannot be used to read data from the file anymore.
        """
        if not self._file.closed:
            self._file.close()

    def __len__(self) -> int:
        """
        Returns the total number of bytes in the opened file.
        
        Returns:
            int: The size of the file in bytes.
        """
        return self._size

    def __getitem__(self, key):
        """
        Enables index-based access to the bytes of the opened file.
        
        Args:
            key (int): The index of the byte to retrieve. Supports negative indices.
        
        Returns:
            bytes: A single byte from the file as a bytes object of size 1.
        
        Raises:
            TypeError: If the key is not an integer.
            IndexError: If the key is out of the valid range.
        """
        if not isinstance(key, int):
            raise TypeError(f"indexing expects 'int', not '{type(key).__name__}'")
        
        # Handle negative indices
        if key < 0:
            key += self._size
        
        if key < 0 or key >= self._size:
            raise IndexError("Reader index out of range")
        
        try:
            self._file.seek(key, os.SEEK_SET)
            byte = self._file.read(1)
            if not byte:
                raise IndexError("Reader index out of range")
            return byte
        except OSError as e:
            raise IndexError(f"Error accessing index {key}: {e}")

    def __del__(self):
        """
        Ensures that the file is closed when the Reader object is garbage collected.
        """
        self.close()