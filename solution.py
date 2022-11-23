 
# initial code to set up Python ACT-R
import ccm
from ccm.lib.actr import *
log=ccm.log(html=True)

# define the model
class ExpertCountingModel(ACTR):
    goal=Buffer()
    statePillar=Buffer()

    # Update topOfMid if small was placed ontop of mid. [Only allowed possibility]
    def checkStackDiskMid(statePillar='latest_disk:small latest_pillar:?y mid:?y latest_pillar:!none latest_disk:!none latest_disk:!mid clear:none'):
        # als er al een disk was op y dan 
        print 'Disk small on top of mid'
        statePillar.modify(topOfMid='small')
        statePillar.modify(latest_disk='none')
        statePillar.modify(latest_pillar='none')
        statePillar.modify(target_pillar='none')
        statePillar.modify(selected_disk='none')

    # Update topOfBig if something was placed ontop of big
    def checkStackDiskBig(statePillar='latest_disk:?x latest_pillar:?y big:?y latest_pillar:!none latest_disk:!none latest_disk:!big clear:none'):
        print 'Disk', x, 'on top of big'
        statePillar.modify(topOfBig=x)
        statePillar.modify(latest_disk='none')
        statePillar.modify(latest_pillar='none')
        statePillar.modify(target_pillar='none')
        statePillar.modify(selected_disk='none')

    # Small disk has been place on the 'floor' level
    def checkStackDiskResetSmall(statePillar='latest_disk:small latest_pillar:?y mid:!?y big:!?y latest_pillar:!none clear:none'):
        # als er al een disk was op y dan 
        print 'Disk small on top of floor'
        statePillar.modify(latest_disk='none')
        statePillar.modify(latest_pillar='none')
        statePillar.modify(target_pillar='none')
        statePillar.modify(selected_disk='none')

    # Mid disk has been place on the 'floor' level
    def checkStackDiskResetMid(statePillar='latest_disk:mid latest_pillar:?y small:!?y big:!?y latest_pillar:!none latest_disk:!none clear:none'):
        # als er al een disk was op y dan 
        print 'Disk mid on top of floor'
        statePillar.modify(latest_disk='none')
        statePillar.modify(latest_pillar='none')
        statePillar.modify(target_pillar='none')
        statePillar.modify(selected_disk='none')

    # Big disk has been place on the 'floor' level
    def checkStackDiskResetBig(statePillar='latest_disk:big latest_pillar:?y mid:!?y small:!?y latest_pillar:!none latest_disk:!none clear:none'):
        # als er al een disk was op y dan 
        print 'Disk big on top of floor'
        statePillar.modify(latest_disk='none')
        statePillar.modify(latest_pillar='none')
        statePillar.modify(target_pillar='none')
        statePillar.modify(selected_disk='none')

        
    # Small could have been on top of mid and big
    def simpleExecutionSmallTopOfMid(statePillar='topOfSmall:free topOfMid:small selected_disk:small target_pillar:?y small:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk small to pillar', y
        # small to pillar [y]
        statePillar.modify(small=y)

        # mid is now free
        statePillar.modify(topOfMid='free')
        statePillar.modify(target_pillar='none')

        # Update based on latest action
        statePillar.modify(latest_disk='small')
        statePillar.modify(latest_pillar=y)

    def simpleExecutionSmallTopOfBig(statePillar='topOfSmall:free topOfBig:small selected_disk:small target_pillar:?y target_pillar:!none small:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk small', 'to pillar', y
        # small to pillar [y]
        statePillar.modify(small=y)

        # big is now free
        statePillar.modify(topOfBig='free')
        statePillar.modify(target_pillar='none')

        # Update based on latest action
        statePillar.modify(latest_disk='small')
        statePillar.modify(latest_pillar=y)

    ## small disk was on 'floor' level
    def simpleExecutionSmallNotOnTop(statePillar='topOfSmall:free topOfBig:!small topOfMid:!small selected_disk:small target_pillar:?y small:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk small', 'to pillar', y
        # small to pillar [y]
        statePillar.modify(small=y)

        # Update based on latest action
        statePillar.modify(latest_disk='small')
        statePillar.modify(latest_pillar=y)

    # mid disk was on top of big
    def simpleExecutionMidTopOfBig(statePillar='topOfMid:free topOfBig:mid selected_disk:mid target_pillar:?y mid:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk mid', 'to pillar', y
        # mid to pillar [y]
        statePillar.modify(mid=y)

        # big is now free
        statePillar.modify(topOfBig='free')

        # Update based on latest action
        statePillar.modify(latest_disk='mid')
        statePillar.modify(latest_pillar=y)
        

    ## mid disk was on 'floor' level
    def simpleExecutionMidNotOnTop(statePillar='topOfMid:free topOfBig:!mid selected_disk:mid target_pillar:?y mid:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk mid', 'to pillar', y
        # mid to pillar [y]
        statePillar.modify(mid=y)
        statePillar.modify(target_pillar='none')


        # Update based on latest action
        statePillar.modify(latest_disk='mid')
        statePillar.modify(latest_pillar=y)
    
    def simpleExecutionBig(statePillar='topOfBig:free selected_disk:big target_pillar:?y big:!y small:!?y mid:!?y latest_disk:none latest_pillar:none clear:none'):
        print 'Moved disk big', 'to pillar', y
        # big to pillar [y]
        statePillar.modify(big=y)
        statePillar.modify(target_pillar='none')

        # Update based on latest action
        statePillar.modify(latest_disk='big')
        statePillar.modify(latest_pillar=y)

    def ifNotAllOnThird(goal='small:third mid:third big:third', statePillar='big:!third selected_disk:!big target_pillar:none latest_disk:none latest_pillar:none clear:none'):
        # If big is not on third make placing big on third the goal
        print 'Big not on third'
        statePillar.modify(selected_disk='big')
        statePillar.modify(target_pillar='third')

    def twoMissingOnThird(goal='small:third mid:third big:third', statePillar='big:third mid:!third selected_disk:!mid target_pillar:none latest_disk:none latest_pillar:none clear:none'):
        # If big is not on third make placing big on third the goal
        print 'mid not on third'
        statePillar.modify(selected_disk='mid')
        statePillar.modify(target_pillar='third')

    def lastDiskMissingOnThird(goal='small:third mid:third big:third', statePillar='big:third mid:third small:!third selected_disk:!small target_pillar:none latest_disk:none latest_pillar:none clear:none'):
        # If big is not on third make placing big on third the goal
        print 'small not on third'
        statePillar.modify(selected_disk='small')
        statePillar.modify(target_pillar='third')

    def clearThirdPillar(goal='small:third mid:third big:third', statePillar='selected_disk:big target_pillar:third big:?x topOfBig:free latest_disk:none latest_pillar:none clear:none small:third'):
        print 'Small is on third, moving small to the other pillar (which is not third or',x,')'
        statePillar.modify(selected_disk='small')
        statePillar.modify(target_pillar='second') 

    # Clear mid if big is on third, and so next up.
    def clearMidWhenBigAndMidOnFirst(goal='small:third mid:third big:third', statePillar='selected_disk:big target_pillar:third big:first topOfMid:!free topOfBig:mid  latest_disk:none latest_pillar:none clear:none'):
        # Create subgoal to get big free
        print 'Mid is not clear. Set clearing mid as goal'
        statePillar.modify(clear='mid')

    # Clear mid if big is on third, and so next up.
    def clearMid(goal='small:third mid:third big:third', statePillar='selected_disk:mid target_pillar:third big:third topOfMid:!free latest_disk:none latest_pillar:none clear:none'):
        # Create subgoal to get big free
        print 'Mid is not clear. Set clearing mid as goal'
        statePillar.modify(clear='mid')

    def clearBig(goal='small:third mid:third big:third', statePillar='selected_disk:big target_pillar:third topOfBig:!free latest_disk:none latest_pillar:none clear:none'):
        # Create subgoal to get big free
        print 'Big is not clear. Set clearing big as goal'
        statePillar.modify(clear='big')

    # Clear disk on top of big if big is not free
    def execClearBigByRemoving(statePillar='clear:big topOfBig:?x latest_disk:none latest_pillar:none topOfBig:!free'):
        print 'Big is not free, clearing disk', x , 'which is above big'
        statePillar.modify(clear=x)

    # Clear disk on top of big if big is not free
    def execClearMidByRemoving(statePillar='clear:mid topOfMid:?x latest_disk:none latest_pillar:none topOfMid:!free'):
        print 'Mid is not free, clearing disk', x , 'which is above mid'
        statePillar.modify(clear=x)        

    # Small to third
    def moveSmallToThird(statePillar='clear:small latest_disk:none latest_pillar:none topOfSmall:free big:first'):
        print 'moving small to third'
        statePillar.modify(clear='none')
        statePillar.modify(selected_disk='small')
        statePillar.modify(target_pillar='third')

    # Small to first
    def moveSmallToFirst(statePillar='clear:small latest_disk:none latest_pillar:none topOfSmall:free big:third'):
        print 'moving small to first'
        statePillar.modify(clear='none')
        statePillar.modify(selected_disk='small')
        statePillar.modify(target_pillar='first')
        
    # Move mid to second
    def moveMid(statePillar='clear:mid topOfMid:free latest_disk:none latest_pillar:none small:!second'):
        print 'moving mid to second'
        statePillar.modify(clear='none')
        statePillar.modify(selected_disk='mid')
        statePillar.modify(target_pillar='second')

    # all disk are placed on the third pillar
    def finished(goal='small:third mid:third big:third',statePillar='small:third mid:third big:third'):
        print 'All disk are placed on the third pillar'
        goal.clear()
        statePillar.clear()
        
# run the model        
model=ExpertCountingModel()
ccm.log_everything(model)
model.goal.set('small:third mid:third big:third topOfBig:mid topOfMid:small topOfSmall:free')
model.statePillar.set('topOfBig:mid topOfMid:small topOfSmall:free selected_disk:none target_pillar:none big:first mid:first small:first latest_disk:none latest_pillar:none clear:none')
model.run()


