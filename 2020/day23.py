from itertools import chain

INPUT = [9,5,2,4,3,8,7,1,6]

def part1():
    circle = CircularLinkedList()
    for value in INPUT:
        circle.add_to_end(value)

    play(circle, 100)


def part2():
    circle = CircularLinkedList()

    for value in INPUT:
        circle.add_to_end(value)

    for i in range(1000001):
        circle.add_to_end(i)

    play(circle, 10000000)
    

def play(circle, iterations):

    current_cup = circle.head.next_node

    for _ in range(iterations):

        print(f'-- move {_} --')
        circle.print_list()
        print(f'current cup: {current_cup.value}')

        # remove 3 cups after current
        removed = []
        for _ in range(3):
            if current_cup.next_node == circle.head:
                removed.append(circle.head.next_node.value)
                circle.remove_node(circle.head.next_node.value)
            else:
                removed.append(current_cup.next_node.value)
                circle.remove_node(current_cup.next_node.value)

        print(f'pick up: {removed}')

        # determine destination
        destination = current_cup.value - 1
        if destination < min(INPUT):
            destination = max(INPUT)
        while destination in removed:
            destination -= 1
            if destination < min(INPUT):
                destination = max(INPUT)


        print(f'destination: {destination}')


        # add cups back
        for cup in removed:
            circle.add_after(cup, destination)
            destination = cup

        # set current cup
        if current_cup.next_node == circle.head:
            current_cup = circle.head.next_node
        else:
            current_cup = current_cup.next_node

    circle.print_list()


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class CircularLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.head.next_node = self.head


    def add_to_end(self, value):
        current_node = self.head.next_node

        while current_node.next_node != self.head:
            current_node = current_node.next_node
        new_node = Node(value, current_node.next_node)
        current_node.next_node = new_node


    def add_after(self, value, target_value):
        current_node = self.head.next_node

        while current_node.value != target_value:
            current_node = current_node.next_node
            if current_node == self.head:
                current_node = self.head.next_node
        
        new_node = Node(value, current_node.next_node)
        current_node.next_node = new_node


    def remove_node(self, value):
        current_node = self.head.next_node
        previous_node = self.head

        while current_node.value != value:
            previous_node = current_node
            current_node = current_node.next_node
            if current_node == self.head:
                current_node = self.head.next_node

        previous_node.next_node = current_node.next_node
        

    def print_list(self):
        current_node = self.head.next_node

        nodes = []

        while current_node.next_node != self.head:
            nodes.append(str(current_node.value))
            current_node = current_node.next_node
        
        nodes.append(str(current_node.value))
        
        print('->'.join(nodes))



if __name__ == '__main__':
    part1()
    part2()
