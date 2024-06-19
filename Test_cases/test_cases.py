import random

def generate_tree_test_case():
    # Set constraints
    n = random.randint(2, 50000)
    c1 = random.randint(1, n)
    c2 = random.randint(1, n)
    while c2 == c1:
        c2 = random.randint(1, n)

    # Generate a tree structure
    choice_vertex = [c1]
    current_vertices = []


    iter = 1

    while len(current_vertices) < n - 1:

        if(iter!=c1):

            parent_vertex = random.choice(choice_vertex)
            current_vertices.append(parent_vertex)
            choice_vertex.append(iter)
        iter+=1

    # Construct the input string
    input_str = f"{n} {c1} {c2}\n"
    input_str += " ".join(map(str, current_vertices))

    return input_str

# Number of test cases to generate
num_test_cases = 1

# Output file path
output_file_path = "test_cases2.txt"

# Generate and write test cases to the output file
with open(output_file_path, 'w') as output_file:
    for _ in range(num_test_cases):
        test_case = generate_tree_test_case()
        output_file.write(test_case + '\n\n')

print(f"Test cases written to {output_file_path}")
