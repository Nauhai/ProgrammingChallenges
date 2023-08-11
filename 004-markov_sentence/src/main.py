import args
import markov    


def retrieve_input(arguments):
    if arguments.input_file:
        with open(arguments.input_file, "r", encoding="utf-8") as file:
            return file.read()

    return arguments.input_text


def print_sentences(sentences, total):
    print(f"{total} sentences generated.")
    for s, n in sentences:
        prob = n / total
        print(f"{round(prob*100, 2)}%: {' '.join(list(s))}.")


if __name__ == "__main__":
    arguments = args.parse_args()
    input_text = retrieve_input(arguments)
    
    graph = markov.get_graph(input_text)
    sentences = markov.compute_all_sentences(graph, max_length=arguments.max_length)
    most_frequent = sentences.most_common(arguments.max_number)
    total = sum(sentences.values())

    print_sentences(most_frequent, total)
    
