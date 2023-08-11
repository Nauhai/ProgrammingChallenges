import args
import markov


if __name__ == "__main__":
    arguments = args.parse_args()

    input_text = arguments.input_text
    if arguments.input_file:
        with open(arguments.input_file, "r", encoding="utf-8") as file:
            input_text = file.read()
    
    graph = markov.get_graph(input_text)
    sentence = markov.compute_sentence(graph)
    print(' '.join(sentence) + '.')
