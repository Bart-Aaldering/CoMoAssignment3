 
# initial code to set up Python ACT-R
import ccm
from ccm.lib.actr import *
log=ccm.log(html=True)

# define the model
class ExpertCountingModel(ACTR):
    goal=Buffer()
    statePillar=Buffer()


    # ONLY ON MID AND BIG SOMETHING CAN BE PLACED!
    #
    # Update topOf for disk big if something has been placed ontop of it
    def checkStackDiskBig(statePillar='latest_disk:?x latest_pillar:?y big:?y clear:none'):
        # als er al een disk was op y dan 
        statePillar.modify(topOfBig=x)
        print 'Disk', x, 'on top of big'
        statePillar.modify(latest_disk='none')
        statePillar.modify(latest_pillar='none')

    # Update topOf for disk mid if something has been placed ontop of it
    def checkStackDiskMid(statePillar='latest_disk:?x latest_pillar:?y mid:?y clear:none'):
        # als er al een disk was op y dan 
        statePillar.modify(topOfMid=x)
        print 'Disk', x, 'on top of mid'
        statePillar.modify(latest_disk='none')
        statePillar.modify(latest_pillar='none')
        
    # Small could have been on top of mid and big
    def simpleExecutionSmallTopOfMid(statePillar='topOfSmall:free topOfMid:small selected_disk:small target_pillar:?y small:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk small', 'to pillar', y
        # small to pillar [y]
        statePillar.modify(small=y)

        # << clear top of disk below small
        # mid is now free
        statePillar.modify(topOfMid='free')

        # << select new goal
        # move mid to second pillar
        statePillar.modify(selected_disk='mid')
        statePillar.modify(target_pillar='second')

        # << 
        # Updated latest action
        statePillar.modify(latest_disk='small')
        statePillar.modify(latest_pillar=y)

    def simpleExecutionSmallTopOfBig(statePillar='topOfSmall:free topOfBig:small selected_disk:small target_pillar:?y small:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk small', 'to pillar', y
        # small to pillar [y]
        statePillar.modify(small=y)

        # << clear top of disk below small
        # big is now free
        statePillar.modify(topOfBig='free')

        # << select new goal
        # move mid to second pillar
        statePillar.modify(selected_disk='mid')
        statePillar.modify(target_pillar='second')

        # << 
        # Updated latest action
        statePillar.modify(latest_disk='small')
        statePillar.modify(latest_pillar=y)

    ## small disk was on 'floor' level
    def simpleExecutionSmallNotOnTop(statePillar='topOfSmall:free topOfBig:!small topOfMid:!small selected_disk:small target_pillar:?y small:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk small', 'to pillar', y
        # small to pillar [y]
        statePillar.modify(small=y)

        # << select new goal
        # move mid to second pillar
        statePillar.modify(selected_disk='mid')
        statePillar.modify(target_pillar='second')

        # << 
        # Updated latest action
        statePillar.modify(latest_disk='small')
        statePillar.modify(latest_pillar=y)

    # check if valid
    # execute
    # update state (which disk are ontop of eachother)

    # mid disk was on top of big
    def simpleExecutionMidTopOfBig(statePillar='topOfMid:free topOfBig:mid selected_disk:mid target_pillar:?y mid:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk mid', 'to pillar', y
        # mid to pillar [y]
        statePillar.modify(mid=y)

        # big is now free
        statePillar.modify(topOfBig='free')

        # << Select goal
        # move mid to second pillar
        statePillar.modify(selected_disk='small')
        statePillar.modify(target_pillar='second')

        # <<
        # Updated latest action
        statePillar.modify(latest_disk='mid')
        statePillar.modify(latest_pillar=y)

    ## mid disk was on 'floor' level
    def simpleExecutionMidNotOnTop(statePillar='topOfMid:free topOfBig:!mid selected_disk:mid target_pillar:?y mid:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk mid', 'to pillar', y
        # mid to pillar [y]
        statePillar.modify(mid=y)

        # << Select goal
        # move mid to second pillar
        statePillar.modify(selected_disk='small')
        statePillar.modify(target_pillar='second')

        # <<
        # Updated latest action
        statePillar.modify(latest_disk='mid')
        statePillar.modify(latest_pillar=y)
    
    def simpleExecutionBig(statePillar='topOfBig:free selected_disk:big target_pillar:?y big:!y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk big', 'to pillar', y
        # big to pillar [y]
        statePillar.modify(big=y)

        # << Select Goal
        # # move mid to second pillar
        # statePillar.modify(selected_disk='small')
        # statePillar.modify(target_pillar='second')

        # <<
        # Updated latest action
        statePillar.modify(latest_disk='big')
        statePillar.modify(latest_pillar=y)

        # need buffer which select what the next goal is
    
    def ifNotAllOnThird(goal='small:third mid:third big:third', statePillar='big:!third selected_disk:!big target_pillar:!third latest_disk:none latest_pillar:none clear:none'):
        # If big is not on third make placing big on third the goal
        print 'Biggest not on third'
        statePillar.modify(selected_disk='big')
        statePillar.modify(target_pillar='third')

    def clearThird(goal='small:third mid:third big:third', statePillar='selected_disk:big target_pillar:third big:!free latest_disk:none latest_pillar:none clear:none'):
        # Create subgoal to get big free
        print 'Set clearing big as goal'
        statePillar.modify(clear='big')

    # Clear disk on top of big if big is not free
    def execClearBigByRemoving(statePillar='clear:big topOfBig:?x latest_disk:none latest_pillar:none topOfBig:!free'):
        print 'CLearing big'
        statePillar.modify(clear=x)

    # Clear disk on top of mid if not free
    def execClearMidByRemoving(statePillar='clear:mid topOfMid:?x latest_disk:none latest_pillar:none topOfMid:!free'):
        print 'Clearing mid'
        statePillar.modify(clear=x)
    
    def moveSmall(statePillar='clear:small latest_disk:none latest_pillar:none topOfSmall:free'):
        print 'moving small to third'
        statePillar.modify(clear='none')
        statePillar.modify(selected_disk='small')
        statePillar.modify(target_pillar='third')

    def moveMid(statePillar='clear:mid topOfMid:free latest_disk:none latest_pillar:none third:!second'):
        print 'moving mid to second'
        statePillar.modify(clear='none')
        statePillar.modify(selected_disk='mid')
        statePillar.modify(target_pillar='second')



        
# run the model        
model=ExpertCountingModel()
ccm.log_everything(model)
model.goal.set('small:third mid:third big:third topOfBig:mid topOfMid:small topOfSmall:free')
model.statePillar.set('topOfBig:mid topOfMid:small topOfSmall:free selected_disk:none target_pillar:none big:first mid:first small:first latest_disk:none latest_pillar:none clear:none')
model.run()


