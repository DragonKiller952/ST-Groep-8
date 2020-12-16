# Chosing blue
def standard_color(*args):
    return 'blue'

# Chosing random without duplicates
def unique_random(self, choices, used):
    choice = self.random.choice(choices)
    while choice in used:
        choice = self.random.choice(choices)
    used.append(choice)
    return choice

# Chosing color based on agent id
def id_color(self, choices, used):
    return choices[self.agentId]

# Chosing position based on agent id
def id_coord(self, choices, used):
    coords = [(12, 75), (30, 60), (40, 80), (40, 90), (60, 80), (50, 35), (60, 35), (65, 15), (75, 40), (90, 45)]
    return coords[self.agentId]