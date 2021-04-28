from .subgroup import Subgroup
class RandomSubgroupWithoutRepetition(Subgroup):
    
    def __init__(self, random):
        self.__random = random
        
    
    def create_subgroup(self, items, length_subgroup):
        super().create_subgroup(items, length_subgroup)
        selected_items = set()
        first_index = 0
        last_index = len(items) - 1
        while(len(selected_items) < length_subgroup):
            random_index = self.__random.randrange(first_index, last_index)
            selected_items.add(items[random_index])
        return selected_items
 