#Here we go!

class GodforsakenMusic(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def recite_music(self):
        for line in self.lyrics:
            print(line)
    
    def combine_music(self):
        print(" ".join(self.lyrics))
        

    def fibbonachi_ns(self,previous_adding_number,previous_result,times_done):
        print(f"{previous_adding_number + previous_result}")
        if times_done < 200:
            self.fibbonachi_ns(previous_result,(previous_adding_number + previous_result),times_done+1)


s_a_lyrics = ["And the science gets done","and you make a neat gun","for the people who are still alive"]

still_alive = GodforsakenMusic(s_a_lyrics)

lemons_rant_lyrics = ["I'll get my engineers","to invent a combustible lemon","THAT BURNS YOUR HOUSE DOWN!!11!1!!"]

#Music to my ears
lemons_rant = GodforsakenMusic(lemons_rant_lyrics)

still_alive.recite_music()
lemons_rant.recite_music()
print("\n","-"*10)

lemons_rant.fibbonachi_ns(0,1,0) #So I can write the function but that kind of recursion doesn't work in classes (at least, you don't write it that way)
#Also a neat discovery: no matter how large the number, it seems that a new digit is added every five iterations (1-8 is five numbers, 13-89 is five numbers, 144 to 1597 is five numbers, and 11812286801740393957266726453428020888948575827744560125782542771857200827110775109258994402139301895418273142575204123781-80962618193714031895056073532586929100700632223772064294846693785378138632320496195528151124350259251085346578405507826210 is five numbers, surprisingly. Did I just find a new pattern?)
print("\n","-"*10)
print("")
lemons_rant.combine_music()
print("\n","-"*10)



#def recursive(argument):
 #   print(argument)
  #  recursive(argument+1)

#recursive(0)