 
# initial code to set up Python ACT-R
import ccm
from ccm.lib.actr import *
log=ccm.log(html=True)

# define the model
class ExpertCountingModel(ACTR):
    goal=Buffer()
    statePillar=Buffer()

    # Update topOftwo if three was placed ontop of two. [Only allowed possibility]
    def checkStackDiskTwo(statePillar='latest_disk:three latest_pillar:?y two:?y latest_pillar:!none latest_disk:!none latest_disk:!two clear:none'):
        # als er al een disk was op y dan 
        print 'Disk three on top of Disk two'
        statePillar.modify(topOftwo='three')
        statePillar.modify(latest_disk='none')
        statePillar.modify(latest_pillar='none')
        statePillar.modify(target_pillar='none')
        statePillar.modify(selected_disk='none')

    # Update topOfone if something was placed ontop of one
    def checkStackDiskone(statePillar='latest_disk:?x latest_pillar:?y one:?y latest_pillar:!none latest_disk:!none latest_disk:!one clear:none'):
        print 'Disk', x, 'on top of Disk one'
        statePillar.modify(topOfone=x)
        statePillar.modify(latest_disk='none')
        statePillar.modify(latest_pillar='none')
        statePillar.modify(target_pillar='none')
        statePillar.modify(selected_disk='none')

    # three disk has been place on the 'floor' level
    def checkStackDiskResetthree(statePillar='latest_disk:three latest_pillar:?y two:!?y one:!?y latest_pillar:!none clear:none'):
        # als er al een disk was op y dan 
        print 'Disk three on floor'
        statePillar.modify(latest_disk='none')
        statePillar.modify(latest_pillar='none')
        statePillar.modify(target_pillar='none')
        statePillar.modify(selected_disk='none')

    # two disk has been place on the 'floor' level
    def checkStackDiskResettwo(statePillar='latest_disk:two latest_pillar:?y three:!?y one:!?y latest_pillar:!none latest_disk:!none clear:none'):
        # als er al een disk was op y dan 
        print 'Disk two on floor'
        statePillar.modify(latest_disk='none')
        statePillar.modify(latest_pillar='none')
        statePillar.modify(target_pillar='none')
        statePillar.modify(selected_disk='none')

    # one disk has been place on the 'floor' level
    def checkStackDiskResetone(statePillar='latest_disk:one latest_pillar:?y two:!?y three:!?y latest_pillar:!none latest_disk:!none clear:none'):
        # als er al een disk was op y dan 
        print 'Disk one on floor'
        statePillar.modify(latest_disk='none')
        statePillar.modify(latest_pillar='none')
        statePillar.modify(target_pillar='none')
        statePillar.modify(selected_disk='none')

        
    # three could have been on top of two and one
    def simpleExecutionthreeTopOftwo(statePillar='topOfthree:free topOftwo:three selected_disk:three target_pillar:?y three:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk three to pillar', y
        # three to pillar [y]
        statePillar.modify(three=y)

        # two is now free
        statePillar.modify(topOftwo='free')
        statePillar.modify(target_pillar='none')

        # Update based on latest action
        statePillar.modify(latest_disk='three')
        statePillar.modify(latest_pillar=y)

    def simpleExecutionthreeTopOfone(statePillar='topOfthree:free topOfone:three selected_disk:three target_pillar:?y target_pillar:!none three:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk three', 'to pillar', y
        # three to pillar [y]
        statePillar.modify(three=y)

        # one is now free
        statePillar.modify(topOfone='free')
        statePillar.modify(target_pillar='none')

        # Update based on latest action
        statePillar.modify(latest_disk='three')
        statePillar.modify(latest_pillar=y)

    ## three disk was on 'floor' level
    def simpleExecutionthreeNotOnTop(statePillar='topOfthree:free topOfone:!three topOftwo:!three selected_disk:three target_pillar:?y three:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk three', 'to pillar', y
        # three to pillar [y]
        statePillar.modify(three=y)

        # Update based on latest action
        statePillar.modify(latest_disk='three')
        statePillar.modify(latest_pillar=y)

    # two disk was on top of one
    def simpleExecutiontwoTopOfone(statePillar='topOftwo:free topOfone:two selected_disk:two target_pillar:?y two:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk two', 'to pillar', y
        # two to pillar [y]
        statePillar.modify(two=y)

        # one is now free
        statePillar.modify(topOfone='free')

        # Update based on latest action
        statePillar.modify(latest_disk='two')
        statePillar.modify(latest_pillar=y)
        

    ## two disk was on 'floor' level
    def simpleExecutiontwoNotOnTop(statePillar='topOftwo:free topOfone:!two selected_disk:two target_pillar:?y two:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk two', 'to pillar', y
        # two to pillar [y]
        statePillar.modify(two=y)
        statePillar.modify(target_pillar='none')


        # Update based on latest action
        statePillar.modify(latest_disk='two')
        statePillar.modify(latest_pillar=y)
    
    def simpleExecutionone(statePillar='topOfone:free selected_disk:one target_pillar:?y one:!y three:!?y two:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk one', 'to pillar', y
        # one to pillar [y]
        statePillar.modify(one=y)
        statePillar.modify(target_pillar='none')

        # Update based on latest action
        statePillar.modify(latest_disk='one')
        statePillar.modify(latest_pillar=y)

    def ifNotAllOnC(goal='three:C two:C one:C', statePillar='one:!C selected_disk:!one target_pillar:none latest_disk:none latest_pillar:none clear:none'):
        # If one is not on C make placing one on C the goal
        print 'Disk One not on Peg C'
        statePillar.modify(selected_disk='one')
        statePillar.modify(target_pillar='C')

    def twoMissingOnC(goal='three:C two:C one:C', statePillar='one:C two:!C selected_disk:!two target_pillar:none latest_disk:none latest_pillar:none clear:none'):
        # If one is not on C make placing one on C the goal
        print 'Disk Two not on Peg C'
        statePillar.modify(selected_disk='two')
        statePillar.modify(target_pillar='C')

    def lastDiskMissingOnC(goal='three:C two:C one:C', statePillar='one:C two:C three:!C selected_disk:!three target_pillar:none latest_disk:none latest_pillar:none clear:none'):
        # If one is not on C make placing one on C the goal
        print 'Disk Three not on Peg C'
        statePillar.modify(selected_disk='three')
        statePillar.modify(target_pillar='C')

    def clearCPillar(goal='three:C two:C one:C', statePillar='selected_disk:one target_pillar:C one:?x topOfone:free latest_disk:none latest_pillar:none clear:none three:C'):
        print 'Disk Three is on Peg C, moving Disk Three to the other peg (which is not Peg C or Peg',x,')'
        statePillar.modify(selected_disk='three')
        statePillar.modify(target_pillar='B') 

    # Clear Disk Two if Disk One is on C
    def clearTwoWhenOneAndTwoOnA(goal='three:C two:C one:C', statePillar='selected_disk:one target_pillar:C one:A topOftwo:!free topOfone:two  latest_disk:none latest_pillar:none clear:none'):
        # Create subgoal to get one free
        print 'Disk Two is not clear. Set clearing Disk Two as goal'
        statePillar.modify(clear='two')

    # Clear Disk Two if Disk One is on C
    def cleartwo(goal='three:C two:C one:C', statePillar='selected_disk:two target_pillar:C one:C topOftwo:!free latest_disk:none latest_pillar:none clear:none'):
        # Create subgoal to get one free
        print 'Disk Two is not clear. Set clearing Disk Two as goal'
        statePillar.modify(clear='two')

    def clearone(goal='three:C two:C one:C', statePillar='selected_disk:one target_pillar:C topOfone:!free latest_disk:none latest_pillar:none clear:none'):
        # Create subgoal to get one free
        print 'Disk One is not clear. Set clearing Disk One as goal'
        statePillar.modify(clear='one')

    # Clear disk on top of one if one is not free
    def execClearoneByRemoving(statePillar='clear:one topOfone:?x latest_disk:none latest_pillar:none topOfone:!free'):
        print 'Disk One is not free, clearing disk', x , 'which is above Disk One'
        statePillar.modify(clear=x)

    # Clear disk on top of one if one is not free
    def execCleartwoByRemoving(statePillar='clear:two topOftwo:?x latest_disk:none latest_pillar:none topOftwo:!free'):
        print 'Disk Two is not free, clearing Disk', x , 'which is above Disk Two'
        statePillar.modify(clear=x)        

    # three to C
    def movethreeToC(statePillar='clear:three latest_disk:none latest_pillar:none topOfthree:free one:A'):
        print 'moving Disk Three to peg C'
        statePillar.modify(clear='none')
        statePillar.modify(selected_disk='three')
        statePillar.modify(target_pillar='C')

    # three to A
    def movethreeToA(statePillar='clear:three latest_disk:none latest_pillar:none topOfthree:free one:C'):
        print 'moving Disk three to peg A'
        statePillar.modify(clear='none')
        statePillar.modify(selected_disk='three')
        statePillar.modify(target_pillar='A')
        
    # Move two to B
    def movetwo(statePillar='clear:two topOftwo:free latest_disk:none latest_pillar:none three:!B'):
        print 'moving Disk Two to peg B'
        statePillar.modify(clear='none')
        statePillar.modify(selected_disk='two')
        statePillar.modify(target_pillar='B')

    # all disk are placed on the C pillar
    def finished(goal='three:C two:C one:C',statePillar='three:C two:C one:C'):
        print 'All disks are placed on the C pillar'
        goal.clear()
        statePillar.clear()
        
# run the model        
model=ExpertCountingModel()
ccm.log_everything(model)
model.goal.set('three:C two:C one:C')
model.statePillar.set('topOfone:two topOftwo:three topOfthree:free selected_disk:none target_pillar:none one:A two:A three:A latest_disk:none latest_pillar:none clear:none')
model.run()


