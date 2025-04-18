colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black']
states = ['Andhra', 'Karnataka', 'TamilNadu', 'Kerala']
neighbors = {}
neighbors['Andhra'] = ['Karnataka', 'TamilNadu']
neighbors['Karnataka'] = ['Andhra', 'TamilNadu', 'Kerala']
neighbors['TamilNadu'] = ['Andhra', 'Karnataka', 'Kerala']
neighbors['Kerala'] = ['Karnataka', 'TamilNadu']
colors_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state, []):
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color
    return None

def map_coloring():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)
        if colors_of_states[state] is None:
            return False
    return True

def main():
    if map_coloring():
        print("The coloring of states:")
        print(colors_of_states)
    else:
        print("No solution exists.")

main()
