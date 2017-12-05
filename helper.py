def generate_random_points(num_points):
    import random
    node_list = []
    for i in range(num_points):
        x = random.random() * num_points
        y = random.random() * num_points
        node_list.append([i, x, y])
    random.shuffle(node_list)
    return node_list


def generate_and_write_random_points(filename, num_points):
    node_list = generate_random_points(num_points)
    with open(filename, 'w') as file:
        for node in node_list:
            file.write(str(node[0])+' '+str(node[1])+' '+str(node[2])+'\n')


def write_final_answer(filename, answer):
    with open('output_' + filename, 'w') as file:
        file.write(str(answer[0]) + ' ' + str(answer[1]))