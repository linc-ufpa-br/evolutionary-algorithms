import abc
class Subgroup(abc.ABC):
    
    def create_subgroup(self, items, length_subgroup):
        length_items = len(items)
        if length_items <= length_subgroup:
            raise ValueError("number of elements is small or equal then subgroup size")