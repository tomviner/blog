Title: February Dojo Debrief
Tags: python, dojo
Date: 2013-02-14

Well the dojo was great fun last week. [Gautier](https://twitter.com/Gowtier) did a great job in his first time as cat herder and we had some great solutions. Some of them even worked!

The task was that tile sliding game where you have to make the picture appear, or in our case, make the numbers appear back in order. Here's the [results from 3 of the teams](https://github.com/ldnpydojo/slider-puzzle) on the LdnPyDojo Github repo. The remaining 2 teams can submit pull requests if they'd like.

Those who were at the dojo will remember my team's code not really working, and me asking if anyone could see any bugs. Well I [found_one](https://github.com/tomviner/slider-puzzle/compare/master...single_fix)! Let me show it here, in snippet form:

    :::python
    class Board:
        # ...
        def slide(self, tile):
            gap = b.find_gap()
            # ...

    if __name__ == "__main__":
        b = Board(3)
        # ...


That `b.find_gap()` should be `self.find_gap()`, so I think this just goes to show the danger of non-obvious global variables. Once that was fixed, this brute force approach works every time.

I then went on to [add an a* search](https://github.com/tomviner/slider-puzzle/blob/master/team2/sliding_with_astar.py) for those solving sliding puzzles in a hurry. When choosing the next move, each potential future is evaluated by its distance to the solution. I use the _sum of squares of the taxi distance of each tile from it's solved location_.
<strike>To help avoid loops, I penalise a potential move in proportion to how many times we've seen that move before.</strike>

**Update:**
I've added proper recording of the search graph so at each step, we check every board on the horizon and pick the best one we haven't seen before.

I've also added some funky output to watch along the way:

![slider output](http://i.imgur.com/XesHd1r.png)