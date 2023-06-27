import string

def read_file(filename):
    file = []
    with open(filename) as f:
        for line in f:
            line = line.translate(str.maketrans('', '', string.punctuation))
            line = line.lower()
            for word in line.split():
                file.append(word)

    return file

def shared_words(filename1, filename2):
    file1 = read_file(filename1)
    file2 = read_file(filename2)
    shared = []
    for word in file1:
        if word in file2:
            shared.append(word)

    return shared

def percentage_words_shared(filename1, filename2):
    file1 = read_file(filename1)
    file2 = read_file(filename2)
    shared = []
    for word in file1:
        if word in file2:
            shared.append(word)

    return len(shared)/len(file1), len(shared)/len(file2)

def get_indicies(item, list):
    indicies = []
    for i in range(len(list)):
        if list[i] == item:
            indicies.append(i)

    return indicies

def compare_sequences(filename1, filename2, minimum_length=3):
    file1 = read_file(filename1)
    file2 = read_file(filename2)
    
    shared = []
    i = 0
    while i in range(len(file1)):
        seq = []
        if file1[i] in file2:
            indicies = get_indicies(file1[i], file2)
            for index in indicies:
                seq = [file1[i]]
                for j in range(1, len(file1)-i):
                    if file1[i+j] == file2[index+j]:
                        seq.append(file1[i+j])
                    else:
                        break
        if len(seq) >= minimum_length:
            shared.append(seq)
            i += len(seq)
        else:
            i += 1
    return shared

def longest_sequence(filename1, filename2, minimum_length=3):
    shared = compare_sequences(filename1, filename2, minimum_length=3)
    longest = []
    for seq in shared:
        if len(seq) > len(longest):
            longest = seq
    
    all_longest = []
    for seq in shared:
        if len(seq) == len(longest):
            all_longest.append(seq)

    return all_longest, len(longest)                       

def amount_of_shared_sequences(filename1, filename2, minimum_length=3):
    shared = compare_sequences(filename1, filename2, minimum_length)
    return len(shared)



def main():
    pass

if __name__ == '__main__':
    main()