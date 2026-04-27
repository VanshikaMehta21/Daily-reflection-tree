class ReflectionNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def show_tree(self, level=0):
        prefix = "  " * level + "|-- " if level > 0 else ""
        print(prefix + self.data)
        for child in self.children:
            child.show_tree(level + 1)

# 1. Create Root (Date)
root = ReflectionNode("Daily Reflection: 27-04-2026")

# 2. Create Branches
pos = ReflectionNode("Positive Highlights")
neg = ReflectionNode("Challenges/Mistakes")
learn = ReflectionNode("New Learnings")

# 3. Add data (Leaves)
pos.add_child(ReflectionNode("Recognized a scam internship (Proud moment!)"))
neg.add_child(ReflectionNode("Felt a bit overwhelmed with assignments"))
learn.add_child(ReflectionNode("Learned about Tree Data Structures"))

# Assemble the tree
root.add_child(pos)
root.add_child(neg)
root.add_child(learn)

# Final display
root.show_tree()
