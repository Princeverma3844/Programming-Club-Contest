import random

def generate_tree_test_case():
    # Set constraints
    n = random.randint(100000, 199999)
    k = random.randint(2, 50000)

    # Generating random hostel indices
    hostel_indices = random.sample(range(1, n + 1), k)

    c1 = 1

    # Generate a tree structure
    choice_vertex = [c1]
    current_vertices = []


    iter = 1

    edges = []

    while len(current_vertices) < n - 1:

        if(iter!=c1):

            parent_vertex = random.choice(choice_vertex)
            current_vertices.append(parent_vertex)
            choice_vertex.append(iter)
            u = min(parent_vertex, iter)
            v = max(parent_vertex, iter)
            edges.append((u,v))
        iter+=1



    # Construct the input string
    input_str = f"{n} {k} \n"
    input_str += " ".join(map(str, hostel_indices)) + "\n"

    for edge in edges:
        input_str += f"{edge[0]} {edge[1]} \n"

    return input_str

# Number of test cases to generate
num_test_cases = 1

# Output file path
output_file_path = "test_cases_tree.txt"

# Generate and write test cases to the output file
with open(output_file_path, 'w') as output_file:
    for _ in range(num_test_cases):
        test_case = generate_tree_test_case()
        output_file.write(test_case + '\n\n')

print(f"Test cases written to {output_file_path}")
