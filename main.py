class ReflectionNode:
    def __init__(self, category, reflection):
        self.category = category
        self.reflection = reflection
        self.children = []

    def add_node(self, node):
        self.children.append(node)

# Step 1: Decision Logic Function
def categorize_reflection(text):
    # Deterministic Logic (Guardrails against hallucination)
    text = text.lower()
    if "good" in text or "achieved" in text or "proud" in text:
        return "Positive"
    elif "stuck" in text or "error" in text or "hard" in text or "scam" in text:
        return "Challenge"
    else:
        return "General"

# Step 2: Main Tree Execution
def build_reflection_tree():
    root = ReflectionNode("Daily Tree", "27-04-2026")
    
    # Simulating 3 reflections
    user_inputs = [
        "I recognized a scam and felt proud", 
        "Got stuck in C++ compiler setup",
        "Learned about recursion today"
    ]
    
    for inp in user_inputs:
        cat = categorize_reflection(inp)
        node = ReflectionNode(cat, inp)
        root.add_node(node)
        
    return root

# Step 3: Print Tree
def print_tree(node, level=0):
    print("  " * level + "|-- " + f"[{node.category}] {node.reflection}")
    for child in node.children:
        print_tree(child, level + 1)

my_tree = build_reflection_tree()
print_tree(my_tree)
