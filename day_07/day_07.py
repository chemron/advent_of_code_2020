class bag(object):
    def __init__(self, name, parent_bag=None):
        self.contained_in = []
        self.contains = []
        self.name = name
        if parent_bag is not None:
            self.add_parent_bag(parent_bag)

    def add_parent_bag(self, parent_bag):
        if parent_bag not in self.contained_in:
            self.contained_in.append((parent_bag))

    def add_child_bag(self, child_bag):
        if child_bag not in self.contains:
            self.contains.append((child_bag))

    def __str__(self):
        p_string = [b.name for b in self.contained_in]
        c_string = [b.name for b in self.contains]
        return f'{p_string} -> {self.name} -> {c_string}'


f = open('input.txt', 'r')
rules = f.read().split('\n')[:-1]
rules = [rule.split(' contain ') for rule in rules]

bags = {}
# TODO: remove bag/bags from end of name (the s causes problems)
for rule in rules:
    current_bag = rule[0]
    # add current bag to bags dict if not already in
    if current_bag not in bags:
        bags[current_bag] = bag(current_bag)

    # get bag object
    current_bag = bags[current_bag]

    for child_bag in rule[1][:-1].split(', '):
        n = child_bag[0]
        bag_name = child_bag[2:]
        if bag_name not in bags:
            bags[bag_name] = bag(bag_name)

        child_bag = bags[bag_name]
        child_bag.add_parent_bag(current_bag)
        current_bag.add_child_bag(child_bag)

for bag_name in bags:
    print(bags[bag_name].name)
