#!/usr/bin/env python3
# -----------------------------------------------------------
# sparse_array.py
#  Class that represents a sparse array.
# -----------------------------------------------------------

class SparseArray(object):

    def __init__(self, sp_array):
        self._sparsearray = {}
        self._length = len(sp_array)
        for key, val in enumerate(sp_array):
            if val != 0:
                self._sparsearray[key] = val

    @property
    def sparsearray(self):
        return [ self._sparsearray.get(key, 0) for key in range(self._length) ]

    @sparsearray.setter
    def sparsearray(self, val):
        self._sparsearray = {}
        self._length = len(val)
        for k, v in enumerate(val):
            if v != 0:
                self._sparsearray[k] = v

    def __getitem__(self, key):
        if key not in range(self._length):
            raise ValueError("index out of range")
        return self._sparsearray.get(key, 0)

    def __setitem__(self, key, value):
        if value != 0:
            self._sparsearray[key] = value
        if key not in range(self._length):
            raise IndexError("index out of range")

    def __len__(self):
        return self._length

    def __delitem__(self, key):
        if key not in range(self._length):
            raise IndexError("index out of range")
        tlist = self.sparsearray
        tlist.pop(key)
        self.sparsearray = tlist

    def append(self, val):
        self._sparsearray[self._length] = val
        self._length += 1


if __name__ == "__main__":

    sa = SparseArray([1, 0, 2, 0, 3, 4, 0, 0, 0, 0, 10])
    sa2 = SparseArray([1, 0, 2, 0, 3, 4, 0, 0, 0, 0, 10, 0, 0, 0, 0])

    print(sa.sparsearray)
    print(sa2.sparsearray)

    print("Length:", len(sa))
    print("Length:", len(sa2))

    print("item 5:", sa[5])
    sa[5] = 10
    print("item 5:", sa[5])
    # sa[15] = 5
    print("Length:", len(sa))
    print(sa.sparsearray)
    # sa[20] = 0
    print(sa.sparsearray)
    print(sa._sparsearray)

    sa.sparsearray = [0, 1, 2, 3, 4, 0, 0, 0, 5, 0]
    print(f"pre del, virtual {sa.sparsearray}, actual {sa._sparsearray}, length {len(sa)} ")

    print("Deleting item at index 5:")
    del sa[5]
    print(f"post del, virtual {sa.sparsearray}, actual {sa._sparsearray}, length {len(sa)} ")
    # del sa[50]

    sa.append(88)
    print(f"post append, \nvirtual {sa.sparsearray}, \nactual {sa._sparsearray}, \nlength {len(sa)} ")