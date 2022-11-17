 
# initial code to set up Python ACT-R
import ccm
from ccm.lib.actr import *
log=ccm.log(html=True)

# define the model
class ExpertCountingModel(ACTR):
    goal=Buffer()
    selected=Buffer()
    target=Buffer()
    stateStack=Buffer()
    statePillar=Buffer()

    # def countFromOne(goal='action:counting current:one target:!one'):
    #     goal.modify(current='two')        
    # def countFromTwo(goal='action:counting current:two target:!two'):
    #     goal.modify(current='three')        
    # def countFromThree(goal='action:counting current:three target:!three'):
    #     goal.modify(current='four')        
    # def countFromFour(goal='action:counting current:four target:!four'):
    #     goal.modify(current='five')        
    # def countFromFive(goal='action:counting current:five target:!five'):
    #     goal.modify(current='six')        
    # def countFromSix(goal='action:counting current:six target:!six'):
    #     goal.modify(current='seven')        
    # def countFromSeven(goal='action:counting current:seven target:!seven'):
    #     goal.modify(current='eight')        
    # def countFromEight(goal='action:counting current:eight target:!eight'):
    #     goal.modify(current='nine')        
    # def countFromNine(goal='action:counting current:nine target:!nine'):
    #     goal.modify(current='ten')        
        
    # def countFinished(goal='action:counting current:?x target:?x'):
    #     print 'Finished counting to',x
    #     goal.clear()
    
    # grootste en een-na-grootste staan op de juiste positie.
    # def oneStepLeft(goal='action:solve first_pillar:two first_pos:zero second_pos:one second_pillar:two third_pillar:!two'):
    #     # plaats laatste puck op de rest.
    #     goal.modify(target='move_last')
    
    # # object = disk
    # # target = pillar
    # # ,current='pillar:?x'
    # def firstAction(selected='disk:small',target='pillar:third',stateStack='biggest:mid mid:small small:free',statePillar='biggest:first mid:first small:!third'):
    #     # move smallest to third

    #     # small sits on third
    #     statePillar.modify(small='third')
    #     # mid is free
    #     stateStack.modify(mid='free')
    #     # so mid is now selected
    #     selected.modify(disk='mid')
    #     # target is now second pillar
    #     target.modify(pillar='second')

    def simpleExecutionSmall(statePillar='topOfSmall:free selected_disk:small target_pillar:?y small:!?y lastest_disk:none latest_pillar:none'):
        print 'Moved disk small', 'to pillar', y
        # small on third
        statePillar.modify(small=y)
        # small placed as last
        statePillar.modify(latest='small')
        # mid is now free
        statePillar.modify(topOfMid='free')
        # move mid to second pillar
        statePillar.modify(selected_disk='mid')
        statePillar.modify(target_pillar='second')


    # check if valid
    # execute
    # update state (which disk are ontop of eachother)

    # when disk has been moved, update stack state
    def checkStack(statePillar='latest_disk:?x latest_pillar:?y ?y:'):
        # als er al een disk was op y dan 
        statePillar.modify(y=)
        print ''

    def simpleExecutionMid(statePillar='topOfMid:free selected_disk:mid target_pillar:?y mid:!?y lastest_disk:none latest_pillar:none'):
        print 'Moved disk mid', 'to pillar', y
        # mid on second
        statePillar.modify(mid=y)
        # big is now free
        statePillar.modify(topOfBig='free')
        # move mid to second pillar
        statePillar.modify(selected_disk='small')
        statePillar.modify(target_pillar='second')
    
    def simpleExecutionBig(statePillar='topOfBig:free selected_disk:big target_pillar:?y big:!y lastest_disk:none latest_pillar:none'):
        print 'Moved disk big', 'to pillar', y
        statePillar.set('big:?y')
    
    

    # def goalSolved(goal= 'action:solve target:solved'):
    #     print 'Solved'
    #     goal.clear()
        
        
# run the model        
model=ExpertCountingModel()
ccm.log_everything(model)
# first corresponds with first puck
# model.goal.set('action:solve first_pillar:zero second_pillar:zero third_pillar:zero first_pos:zero second_pos:one third_pos:two target:five')
# model.selected.set('disk:small')
# model.target.set('pillar:third')
model.stateStack.set('topOfBig:mid topOfMid:small topOfSmall:free')
model.statePillar.set('topOfBig:mid topOfMid:small topOfSmall:free selected_disk:small target_pillar:third big:first mid:first small:first latest:none')
model.run()


