import unittest
import sys
sys.path.append("../")
from ga.parent_selection.subgroup.random_subgroup_without_repetition import RandomSubgroupWithoutRepetition
from ga.parent_selection.random.random import Random
from unittest.mock import MagicMock

class TestRandomSubgroupWithoutRepetition(unittest.TestCase):
    
    """
        inicialição de váriaveis e instâncias antes de cada execução de teste
    """
    def setUp(self):
        self.length_population = 4
        self.individuals = [] # lista com elementos distintos
        indexes = [] # lista contendo elementos duplicados
        for x in range(self.length_population):
            individual = MagicMock(fitness=x)
            self.individuals.append(individual)
            indexes.extend([x, x])
        
        index_of_first_element = 0
        self.random = Random(MagicMock())
        self.random.randrange = MagicMock(side_effect = lambda n,p: indexes.pop(index_of_first_element))
        
        self.length_subgroup = 3
        self.subgroup = RandomSubgroupWithoutRepetition(self.random)
        
    """
        deve lançar uma exceção se o tamanho do subgrupo for maior que o tamanho dos elementos passados
    """
    def test_raises_exception_if_length_subgroup_is_greater_then_length_list(self):
        length_subgroup = 5
        with self.assertRaises(ValueError):
            self.subgroup.create_subgroup(self.individuals, length_subgroup)
        self.random.randrange.assert_not_called()
        
    """
        deve lançar uma exceção se o tamanho do subgrupo for igual que o tamanho dos elementos passados, já que
        o resultado seria o mesmo que os próprios elementos passados
    """
    def test_raises_exception_if_length_subgroup_is_equal_then_length_list(self):
        length_subgroup = 4
        with self.assertRaises(ValueError):
            self.subgroup.create_subgroup(self.individuals, length_subgroup)
        self.random.randrange.assert_not_called()
    
    """
        Testa se o método de seleção da classe Random Selection foi chamado n vezes
    """
    def test_subgroup_call_selection_method_of_class_random_selection_in_n_times(self):
        self.subgroup.create_subgroup(self.individuals, self.length_subgroup)
        calls = self.random.randrange.call_count
        self.assertGreaterEqual(calls, self.length_subgroup)
        first_index = 0
        last_index = self.length_population - 1
        self.random.randrange.assert_called_with(first_index, last_index)
        
    """
        o subgrupo deve ter a quantidade de individuos passado como parâmetro
    """
    def test_number_of_subgroup_is_equal_then_subgroup_size(self):
        members = self.subgroup.create_subgroup(self.individuals, self.length_subgroup)
        self.assertEqual(self.length_subgroup, len(members))
        
    """
        não pode ter individuos repetidos no subgrupo
    """
    def test_cannot_have_duplications_of_individuals(self):
        members = self.subgroup.create_subgroup(self.individuals, self.length_subgroup)
        self.assertIs(type(members), set)
        self.assertSetEqual(set(self.individuals[:-1]), members)
        
        
    """
        deve retornar o primeiro e o terceiro elemento da lista como subgroup
    """    
    def test_return_random_subgroup_without_repetition(self):
        indexes = [0, 2] # dois indices da lista de individuos pulado em 2 casas na leitura
        
        index_of_first_element = 0
        random = Random(MagicMock())
        random.randrange = MagicMock(side_effect = lambda n,p: indexes.pop(index_of_first_element))
        
        length_subgroup = 2
        subgroup = RandomSubgroupWithoutRepetition(random)
        
        members = subgroup.create_subgroup(self.individuals, length_subgroup)
        
        subgroup_expected = set(self.individuals[::2])
        
        self.assertSetEqual(subgroup_expected, members)
        
        
    