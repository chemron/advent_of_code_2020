import re


class bag(object):
    def __init__(self, name, parent_bag=None):
        self.parents = []
        self.children = []
        self.children_count = []  # indexed the same as self.children
        self.child_count = None  # total number of children
        # ^ (only calculate when tree is full)
        self.name = name
        if parent_bag is not None:
            self.add_parent_bag(parent_bag)

    def add_parent_bag(self, parent_bag):
        if parent_bag not in self.parents:
            self.parents.append((parent_bag))

    def add_child_bag(self, child_bag, n):
        self.children.append(child_bag)
        self.children_count.append(n)

    def __str__(self):
        p_string = [b.name for b in self.parents]
        c_string = [b.name for b in self.children]
        return f'{p_string} -> {self.name} -> {c_string}'

    def __repr__(self):
        return f'<{self.name} bag>'

    def get_all_parents(self, parent_list=[]):
        for parent in self.parents:
            if parent not in parent_list:
                parent_list.append(parent)
                parent_list = parent.get_all_parents(parent_list)
        return parent_list

    def count_children(self):
        if self.child_count is None:
            count = 0
            for i in range(len(self.children)):
                child = self.children[i]
                n = self.children_count[i]
                count += n + n*(child.count_children())
            self.child_count = count
        return self.child_count


f = open('input.txt', 'r')
rules = f.read().split('\n')[:-1]
f.close()
rules = [rule.split(' contain ') for rule in rules]

bags = {}
for rule in rules:
    current_bag = rule[0]
    current_bag = re.sub(' bags?', '', current_bag)
    # add current bag to bags dict if not already in
    if current_bag not in bags:
        bags[current_bag] = bag(current_bag)

    # get bag object
    current_bag = bags[current_bag]

    if rule[1] != 'no other bags.':
        for child_bag in rule[1][:-1].split(', '):
            n = int(child_bag[0])
            bag_name = child_bag[2:]
            bag_name = re.sub(' bags?', '', bag_name)
            if bag_name not in bags:
                bags[bag_name] = bag(bag_name)

            child_bag = bags[bag_name]
            child_bag.add_parent_bag(current_bag)
            current_bag.add_child_bag(child_bag, n)


shiny_gold_bags_parents = bags['shiny gold'].get_all_parents()
print(f'# shiny gold bag parents: {len(shiny_gold_bags_parents)}')

shiny_gold_bags_child_count = bags['shiny gold'].count_children()
print(f'# shiny gold bag children: {shiny_gold_bags_child_count}')
# for bag_name in bags:
#     print(bags[bag_name])
