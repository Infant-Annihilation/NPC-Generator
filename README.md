The purpose of this project is to generate random NPCs, given new and already existing names and ages. The user first inputs a series of names, ages, and the program then fully runs. Each NPC has a list that pulls randomly from other lists or defined functions, such as namelist or COD_KD_ratio. The NPCs are then compiled into a list simply called NPCs, and then a function called info runs that prints each attribute in the NPC's list. I then had a loop command that looped the printing of each different NPC for the user to see. Going more into the random choices, each NPC has its own list, and in that list, each index has something to do with randomness. While a simple “IQ()” doesn’t seem random, if you look into the IQ function, you can see that the IQ is a random value from 50-170. 
The first two things that come up in the code, inputting names and ages, aren’t just inputting, they are appending to already existing lists of names and ages. Those lists are also shown above the input, letting the user know what names and ages already exist so they don’t accidentally input a duplicate. 
The info function combined with the loop is what allows the information of the NPCs to actually be shown. The info function is a series of steps the loop has to carry out, that being printing out all the information. The loop then does that for however many NPCs there are, that being 10.
