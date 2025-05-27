import os 
from   pathlib                     import Path
import csv
import dateutil.parser             as     dup
import numpy                       as     np
#import pandas                      as pd
from   emulsion.agent.managers     import MetapopProcessManager
from emulsion.agent.managers import MultiProcessManager
from   emulsion.tools.preprocessor import EmulsionPreprocessor
from   emulsion.tools.debug        import debuginfo
import random
from itertools import chain


class Multipen(MetapopProcessManager):

    """Level of the population.

    """
    def initialize_level(self, **others):
        """Initialize an instance of Multipen. Especially, after all regular
        initial conditions have been applied, pick random animals
        according to initial prevalence to infect them.

        """
        nb_vax = round(self.get_model_value('prop_vax_on_arrival') * self.get_model_value('pen_size')* self.get_model_value('number_pens'))
        nb_non_vax = round((1-(self.get_model_value('prop_vax_on_arrival'))) * self.get_model_value('pen_size')* self.get_model_value('number_pens'))
        temp_pen=self.new_atom()
        #temp_pen.new_atom(prototype='default_calf')
        concat_list=[]
        list_non_vax = [temp_pen.new_atom(prototype='default_calf',execute_actions=True) for i in range(nb_non_vax)]
        for animal in list_non_vax:
            animal.apply_prototype("initial_NonVax",execute_actions=True)
        concat_list+=list_non_vax
        list_vax = [temp_pen.new_atom(prototype='default_calf',execute_actions=True) for i in range(nb_vax)]
        for animal in list_vax:
            animal.apply_prototype("initial_Vax",execute_actions=True)
        concat_list+=list_vax
        pens = self.get_populations()
        if self.get_model_value('sorted_pens')==1:
            for i in range(len(pens)):
                set_atom=list(concat_list[int(i*self.get_model_value('pen_size')):int((i+1)*self.get_model_value('pen_size'))])
                vax_status = str(set_atom[0].get_information('vax_status')).split('.')[1]
                pens[i].add_atoms(atom_set=set_atom)
        else:
            np.random.shuffle(concat_list)
            for i in range(len(pens)):
                set_atom=set(concat_list[int(i*self.get_model_value('pen_size')):int((i+1)*self.get_model_value('pen_size'))])
                pens[i].add_atoms(atom_set=set_atom)

        







#===============================================================
# CLASS Pen (LEVEL 'pen')
#===============================================================
class pen(MultiProcessManager):

    """Level of the pen.

    """

    #----------------------------------------------------------------
    # Level initialization
    #----------------------------------------------------------------
        

