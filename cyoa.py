print('Welcome to CYOAQuest')
name = input('What is your name? ').capitalize()
adj = input('What is a word you would use to describe yourself? ').capitalize()

print('Hello,', name, 'the', adj)

ans = input('You enter a tavern and sit at the bar. You can order a beer, or ask the barkeep about any gossip, if you\'re looking for a quest. (INPUTS ACCEPTED(beer/gossip))').lower()

if ans == 'gossip':
    ans2 = input('The barkeep tells you that people have been disappearing from the town lately, and that they have heard strange noises coming from the woods at night. He gives you a greneral direction that the noises seem to be coming from, and you, being the brave adventurer that you are, set out to investigate. As you follow a trail you have found, the path forks. Do you go left or right? (left/right)').lower()
    
    if ans2 == 'right':
        ans3 = input('You reach the entrance of a cave. As you enter, you see a goblin attempting to start a fire. You can sneak up to him and attack from behind, or speak to him, to see if he can be reasoned with. (sneak/speak)').lower()
            
        if ans3 == 'sneak':
            print('Success! You find a key on him and go further into the cave. You find a cage holding a group of towspeople. You free them! Go back to the tavern and have a beer. YOU WIN! THE END!')
                
        elif ans3 == 'speak':
            print('The goblin turns and screaches "WAAAAAAAAAAAHH!" He then pulls out a dagger and stabs you. You die. THE END')
        
    elif ans2 == 'left':
        print('You fall in a trap and break your leg. THE END')
    
elif ans == 'beer':
    print('mmmm beer. You stay at the tavern and party. THE END')
