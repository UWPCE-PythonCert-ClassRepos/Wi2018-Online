
# This class is designed mainly to create sparse array ###
#!/usr/bin/env python3

class SparseArray(object):
    def __init__(self, sparse_array):
        self._sparsearray = {}
        self._length = len(sparse_array)
        for key, value in enumerate(sparse_array):
            if value != 0:
                self._sparsearray[key] = value

    @property
    def sparsearray(self):
        return [self._sparsearray.get(key, 0) for key in range(self._length)]

    def __getitem__(self, key):
        if key not in range(self._length):
            raise IndexError("Index Out of range")
        return self._sparsearray.get(key, 0)

    def __setitem__(self, key, value):
        if key not in range(self._length):
            raise IndexError("Index Out of range")
        if value != 0:
            self._sparsearray[key] = value

    def __delitem__(self, key):
        if key not in range(self._length):
            raise IndexError("Index Out of range")
        self._sparsearray.pop(key)

    def length(self):
        return self._length

    def append(self, value):
        self._sparsearray[self._length] = value
        self._length += 1

    if __name__ == "__main__":
        sp = SparseArray((1,0,0,0,2,0,0,0,5))
        print(f"before appending, virtual sparse array {sp.sparsearray}, actual array {sp._sparsearray}")
        print(f"before appending, length of virtual sparse array {sp.length()}, length of actual array {len(sp._sparsearray)}")
        print(f"Appending element {6} to array")
        sp.append(6)
        print(f"after appending, virtual sparse array {sp.sparsearray}, actual array {sp._sparsearray}")
        print(f"after appending, length of virtual sparse array {sp.length()}, length of actual array {len(sp._sparsearray)}")
        print(f"deleting element {6} from array")
        del sp[sp.length() - 1]
        print(f"after deleting, virtual sparse array {sp.sparsearray}, actual array {sp._sparsearray}")
        print(f"after deleting, length of virtual sparse array {sp.length()}, length of actual array {len(sp._sparsearray)}")
