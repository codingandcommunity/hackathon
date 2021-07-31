class Node:
    def __init__(self, name, choice, prompt):
        '''
        Create a new node in a story.

        `name`: (str) name of the Node
        `choice`: (str) text to use as a choice that leads to this Node
        `promopt`: (str) text displayed when this Node is reached.
        '''
        self.name = name
        self.choice = choice
        self.prompt = prompt
        self.choices = []

    def addChoice(self, node):
        '''
        Connect another Node to this one. This will add the passed Node
        as a possible destination from this Node.

        node: (Node) another point in the story for the player to visit
        '''
        self.choices.append(node)

    def do(self):
        '''
        Play through a Node in the story. Returns either None or the next
        Node in the story.
        '''
        if len(self.choices) == 0:
            # no choices, this Node is an ending
            print(self.prompt)
            return None
        else:
            # there are choices
            print(self.prompt)
            for i in range(len(self.choices)):
                print("({}):\t{}".format(i+1, self.choices[i].choice))
            inp = None
            while (inp is None) or (inp <= 0) or (inp > len(self.choices)):
                try:
                    inp = int(input("What is your choice? "))
                except ValueError:
                    inp = None

            return self.choices[inp-1]

clearScreen = lambda: print("\033[H\033[J", end="")

def playStory(node, clear=True):
    '''
    Play through a story, beginning with Node
    '''
    while node is not None:
        if clear: clearScreen()
        node = node.do()

    print("== THE END ==")

# test story
start  = Node("start", "", "You encounter a cave. Do you go in?")
go_in  = Node("go_in", "Yes", "The cave is dark and slimy. Go further?")
go_out = Node("go_out", "No", "You leave the cave alone and go about your day.")
start.addChoice(go_in)
start.addChoice(go_out)

treasure = Node("treasure", "Go further", "You find a treasure chest. You're rich!")

go_in.addChoice(treasure)
go_in.addChoice(go_out)

playStory(start)