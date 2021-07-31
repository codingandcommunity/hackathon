# Choose Your Own Adventure Project

This tutorial shows you how to use the file `cyoa.py` to make a choose your own adventure style game. While we encourage you to write a short version of your story using only `if` statements, this code allows you to make more complex stories easily.

## Getting Started
To start, open a new Python repl and create two files: `cyoa.py` and `main.py`. In `cyoa.py`, copy the contents of `cyoa.py` from this Git repository. Then, in `main.py`, add the following to the top of your file.

```
from cyoa import Node, playStory
```

You have now imported all that you need to get your game running. Run `main.py` to make sure that the import statement works. You should not see any errors.

## Example Story
The first step to writing your story is to write it out on paper. No, seriously, we mean it. Write out all the choices the player can make like a flowchart. As an example, we will walk you through making a story that looks like this:

![Story Diagram](cyoa_images/Blank%20diagram.png)

Each box represents a choice the player makes in the story. Arrows show how the player can move from one box to another. The text above each arrow indicates the choice the player makes to follow that arrow. We will call each of these boxes a `Node`. 

### Making `Node`s
Let's make all of the `Node`s we will need for the example story. Creating a node looks like this:

```
start  = Node(name, choice, prompt)
```
`name` is the name we are going to give this `Node`. `choice` is the selection the player must make to arrive at this `Node`. `prompt` is the message displayed to the player when they reach this `Node`.

For example, look at the `Node` that starts with "The cave is dark and slimy". A good name for this `Node` would be "cave". In order to get to this `Node`, we would have to make the choice "Yes". And finally, the prompt is "The cave is dark and slimy. Do you go further?". So, to create this `Node`, we would write (in `main.py`):

```
cave = Node("cave", "Yes", "The cave is dark and slimy. Do you go further?")
```

We can do something similar for the `Node` when the player leaves the cave and when they find the treasure.

```
leave    = Node("leave", "No", "You leave the cave alone and go about your day.")
treasure = Node("treasure", "Go further", "You find a treasure chest. You're rich!")
```

What about the start `Node`. This `Node` is the starting point of the story, so we do not need to make a choice to access it. So, we can just ignore its choice and pass an empty string.

```
start = Node("start", "", "You encounter a cave. Do you go in?")
```

Your `main.py` file should now look like this.

```
from cyoa import Node, playStory

start    = Node("start", "", "You encounter a cave. Do you go in?")
cave     = Node("cave", "Yes", "The cave is dark and slimy. Do you go further?")
leave    = Node("leave", "No", "You leave the cave alone and go about your day.")
treasure = Node("treasure", "Go further", "You find a treasure chest. You're rich!")
```

We now have the main elements of the story and we need to connect them together.

### Connecting `Node`s
`node1` is connected to `node2` by writing `node1.addChoice(node2)`. This is equivalent to drawing an arrow from `node1` to `node2` on the diagram. Let's add the two options for the start `Node`.

```
start.addChoice(cave)
start.addChoice(leave)
```

We can now run the game by putting `playStory(start)` at the end of `main.py`. If you do so, you will get the option to enter the cave or leave it alone. Entering a choice will look like this.

```
You encounter a cave. Do you go in?
(1):    Yes
(2):    No
What is your choice?
```

You can then type a number corresponding to a choice. The program will not accept non-number input nor a number that is not a valid choice. Make sure that either option works before continuing to our last two connections.

We now need to finish the story by adding connections to the `cave` `Node`. We can reach two other `Node`s from here: `leave` and `treasure`. Like before, we add them with `node1.addChoice(node2)`.

```
cave.addChoice(treasure)
cave.addChoice(leave)
```

The story should now have two possible endings: the player leaves the cave (either from the start or after venturing in) or they find the treasure in the cave.

### Customization
As your story gets longer, you may find the amount of text in the console annoying. To wipe all text from the console at each `Node`, start the story with `playStory(start, clear=True)`. This will keep the console clean.

## Writing Longer Stories

**Plan your story out with a flowchart before you start writing code.** The clearer your vision is, the easier this will be. You can incorporate money, items, etc. into the game by including these in the prompts for each node. Or, you might modify `playStory` to include a variable that tracks what the player has. Get creative! We are excited to see what you make :)