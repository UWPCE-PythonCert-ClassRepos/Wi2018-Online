class SparseArray():
    def __init__(self, data):
        self.dataDict = {}
        self.length = len(data)
        for i in data:
            if i == 0:
                pass
            else:
                self.dataDict.update({data.index(i): i})

    def append(self, val):
        if val == 0:
            pass
        else:
            self.length += 1
            # key index is self.length -1 b/c length counts from 1 vs
            # index counts from 0
            self.dataDict.update({self.length - 1: val})

    def __getitem__(self, item):
        if type(item) is int:
            if item > self.length:
                raise IndexError("Index is out of bounds of the data")
            elif self.dataDict.get(item) is None:
                return 0
            else:
                return self.dataDict.get(item)
        elif type(item) is slice:
            # undefined slice start/end is a None by default
            if item.start is None:
                start = 0
            else:
                start = item.start
            if item.stop is None:
                stop = self.length - 1
            else:
                stop = item.stop

            if start < 0 or stop > self.length:
                raise IndexError("Index is out of bounds of the data")
            else:
                out_list = []
                dummy_list = [i for i in range(start, stop)]
                for i in dummy_list[::item.step]:
                    if self.dataDict.get(i) is None:
                        out_list.append(0)
                    else:
                        out_list.append(self.dataDict.get(i))
                return out_list
        else:
            raise TypeError("Input is not a int or slice")

    def __delitem__(self, index):
        try:
            self.dataDict.pop(index)
        except KeyError:
            raise KeyError("Index is out of bounds of the data")
        else:
            self.length -= 1

    def __len__(self):
        return self.length


if __name__ == "__main__":
    l1 = [1, 2, 0, 0, 0, 0, 3, 0, 0, 4]
    t1 = (1, 2, 0, 0, 0, 0, 3, 0, 0, 4)

    my_array = SparseArray(l1)
