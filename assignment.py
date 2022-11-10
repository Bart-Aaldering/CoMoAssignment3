# initial code to set up Python ACT-R
import ccm
from ccm.lib.actr import *
log=ccm.log(html=True)
 
# define the model
class ExpertCountingModel(ACTR):
    pegs=Buffer()
    goal=Buffer()
    subgoal=Buffer()
    # pegs.set('A:123 B:000 C:000')
    pegs.set('A1:1 A2:2 A3:3 B1:0 B2:0 B3:0 C1:0 C2:0 C3:0')
    # subgoal.set('A1:0 A2:0 A3:0 B1:0 B2:0 B3:0 C1:3 C2:0 C3:0')
    subgoal.set('from:A to:B')

    def atob(subgoal='from:A to:B', pegs='A3:!0 B3:!0'):
        pegs.set()


        




# run the model        
model=ExpertCountingModel()
ccm.log_everything(model)
model.goal.set('action:counting current:one target:five')
model.run()