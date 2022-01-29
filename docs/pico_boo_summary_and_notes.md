picoCTF design
---
* General skills section for connecting to servers and such
    * I think we can safely assume that most CS students will have experience connecting to servers, since it's required for stuff like 213 and 221
    * Though we potentailly could collab with the cs dept to put flags on the student servers for people to get

* They based their beginner/intermediate problem set on a report from the ACM which might be interesting to look at (what the fuck its 123 pages, [link](https://www.acm.org/binaries/content/assets/education/curricula-recommendations/csec2017.pdf))
* "The 2017 competition analysis showed sharp drop-off in student participation after they completed the first few easier introductory problems. We hypothesized that the introduction of more beginner and intermediate-level problems would keep students engaged longer in the competition and help them learn the concepts better
    * This seems to line up with what we've experienced as well
    * People like solving stuff but most people aren't ready to slam their heads against a wall for a dificult challenge
    * They give an example of how they did this with their binary exploit challenges
        -  Challenge 0: The most basic lack of array bounds checking in C causing data overwriting
        -  Challenge 1: Modification of return addresses (requires knowledge of the stack structure)
        -  Challenge 2: Modifying arguments as well (more knowledge of the stack layout)
        -  Challenge 3: A 4 byte canary (adding the idea of security protections)
    * Summarizing: "this is a large number of problems, but the focus allowed for depper understanding. Also incrementally more difficult challenges give the students confidence and a sense of achievement"
    * They note that reversing challenges are notoriously difficult to "ramp up" in difficulty
        * Since you essentially need to dive straight into x86
        * The ramp up for rev they chose was a series of assembly challenges where they asked for what the program would produce as a final result
        * This allowed them to add new types of instructions incrementally

    * Their general philosophy for the beginner challenges was to lower the barrier to entry as much as possible in the first challenge, then to ramp up the difficulty by adding concepts as they went

* "To help beginners who might not have much experience with programming, we developed a series of learning guides. These guides are not meant to be exhaustive guides or tutorials for solving problems; they simply introduce some high-level concepts and terms that students need to understand to begin participating and solving problems in the competition.
    * This seems to agree with our idea of having guides to point people in the right direction for challenges
    * They note that this was again important for lowering the barrier of entry
        * Encourages participation for those with no knowledge of security stuff
        * Centralizes information and makes finding resources easier
    * They generally structured them to go hand-in-hand with the ramp up challenges in each category
    * For the later intermediate/advanced challenges they left the research to the students

* There's also their classroom system but we won't be able to do that

* One of their charts shows student engagement (% of game completed vs % of students)
    * Less than 50% of students played more than 10% of the game
    * About 10% play more than 40%
    * This really drives home that the most important challenges by far will be the first few in each category 
        * We want to make the ramp up challenges really really accessible
        * We want the beginner challenges to entice people into playing more of the challenges
    * We do have the advantage of being in person that we could try to exploit
        * We have our kickoff event that hopefully people will play the ctf during

* Teams/Superteams
    * Our equivalent of the classroom system is going to be our small team + superteam structure
    * Hopefully superteams will have a similar effect as the classroom system where people have a place where they can ask questions
    * And hopefully the small teams will encourage cooperation and teamwork among the smaller groups

* Aside
    * We should try to track similar data so that we can do a retrospective of our own after the event, I think it would be a lot of fun and interesting to see

* Note: Misc
    * picoCTF seems to have a very small focus on misc
    * I think misc challenges will be a good hook for people into the ctf
        * Fun less security related challenges that are still rewarding to solve
        * Probably much more approachable than the main categories
        * Hopefully after people play a couple of them they might feel more motivated to try and tackle one of the main categories

My personal takeaways
---
1. People will play a lot less of the CTF than we would hope, and that's just something we should accept right away. A very very small % of teams will even attempt our advanced challenges
2. Because of point 1, I think we may want to go about our challenge writing more carefully, thinking about how our challenges in each category will ramp up into each other before we start going straight into writing challenges
3. Learning guides as a way of consolidating information, explaining jargon, and giving searchable terms is definitely something we should do
4. Teams + Superteams will hopefully give us a similar effect to classrooms in picoCTF