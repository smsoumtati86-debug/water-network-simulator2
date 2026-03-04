class Pipe:
    def __init__(self, pipe_id, start_node, end_node,
                 length, diameter, roughness):
        self.pipe_id = pipe_id
        self.start_node = start_node
        self.end_node = end_node
        self.length = length
        self.diameter = diameter
        self.roughness = roughness

        # ربط الأنابيب بالعقد
        start_node.add_pipe(self)
        end_node.add_pipe(self)

    def __repr__(self):
        return f"Pipe({self.pipe_id})"
