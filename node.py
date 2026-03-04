class Node:
    def __init__(self, node_id, elevation=0.0, demand=0.0):
        self.node_id = node_id
        self.elevation = elevation
        self.demand = demand
        self.connected_pipes = []

    def add_pipe(self, pipe):
        self.connected_pipes.append(pipe)

    def __repr__(self):
        return f"Node({self.node_id})"
