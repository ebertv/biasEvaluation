import compare

def get_user_input():
    num_files = input("How many files do you want to compare? ")

    filenames = []
    for i in range(int(num_files)):
        filename = input("Enter the name of file " + str(i+1) + ": ")
        filenames.append(filename)

    minimum_length = input("Enter the minimum length of sequences to compare: ")

    return filenames, minimum_length

def give_summary_statistics(filenames, minimum_length):
    print()
    print("Comparing " + str(len(filenames)) + " files with minimum sequence length " + str(minimum_length) + "...")
    print()

    compared = []
    shared_words = []
    clean_shared_words = []
    percentage_words_shared = []
    longest_sequence = []
    clean_longest_sequence = []
    amount_of_shared_sequences = []
    for i in range(len(filenames)):
        for j in range(i+1, len(filenames)):
            if [filenames[i], filenames[j]] not in compared and [filenames[j], filenames[i]] not in compared:
                print("Comparing " + filenames[i] + " and " + filenames[j] + "...")
                compared.append([filenames[i], filenames[j]]) 
                shared_words.append(compare.shared_words(filenames[i], filenames[j]))
                temp = []
                for word in shared_words[-1]:
                    if word not in temp:
                        temp.append(word)
                clean_shared_words.append(temp)
                print(f'\tThere are {len(clean_shared_words[-1])} unique words shared.')
                percentage_words_shared.append(compare.percentage_words_shared(filenames[i], filenames[j]))
                print(f'\t{filenames[i]} has {percentage_words_shared[-1][0]*100:.2f}% of its words shared with {filenames[j]}.')
                print(f'\t{filenames[j]} has {percentage_words_shared[-1][1]*100:.2f}% of its words shared with {filenames[i]}.')
                print(f'\tThe shared words are: ', end='')
                for word in clean_shared_words[-1]:
                    print(word, end=', ')
                print()
                longest_sequence.append(compare.longest_sequence(filenames[i], filenames[j], int(minimum_length)))
                temp = []
                for sequence in longest_sequence[-1][0]:
                    if sequence not in temp:
                        temp.append(sequence)
                clean_longest_sequence.append(temp)
                print(f'\tThe longest sequence(s) of length shared between {filenames[i]} and {filenames[j]} is: ', end='')
                for sequence in clean_longest_sequence[-1]:
                    for word in sequence:
                        print(word, end=' ')
                    print(', ', end='')
                print(f'with length {longest_sequence[-1][1]}.')
                amount_of_shared_sequences.append(compare.amount_of_shared_sequences(filenames[i], filenames[j], int(minimum_length)))
                print(f'\tThere are {amount_of_shared_sequences[-1]} sequences of at least length {minimum_length} shared between {filenames[i]} and {filenames[j]}.')

def main():
    #filenames, minimum_length = get_user_input()
    filenames = ['architecture_man.txt', 'architecture_woman.txt', 'architecture_neutral.txt']
    minimum_length = 3
    give_summary_statistics(filenames, minimum_length)

if __name__ == '__main__':
    main()





exit()
compared = []
shared = []
for i in range(len(filenames)):
    for j in range(i+1, len(filenames)):
        if [filenames[i], filenames[j]] not in compared and [filenames[j], filenames[i]] not in compared:
            shared.append(compare.compare_sequences(filenames[i], filenames[j], int(minimum_length)))
            compared.append([filenames[i], filenames[j]])

clean_shared = []
for i in range(len(shared)):
    clean_shared.append([])
    for j in range(len(shared[i])):
        if shared[i][j] not in clean_shared[i]:
            clean_shared[i].append(shared[i][j])

for i in range(len(clean_shared)):
    print()
    print("Sequences in common between " + compared[i][0] + " and " + compared[i][1] + ":")
    for j in range(len(clean_shared[i])):
        print(" ".join(clean_shared[i][j]))


