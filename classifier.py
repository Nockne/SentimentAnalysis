# This file implements a Naive Bayes Classifier


class BayesClassifier():
    """
    Naive Bayes Classifier
    file length: file length of training file
    sections: sections for incremental training
    """
    def __init__(self):
        self.positive_word_counts = {}
        self.negative_word_counts = {}
        self.percent_positive_scentences = 0
        self.percent_negative_scentences = 0
        self.file_length = 499
        self.file_sections = [self.file_length // 4, self.file_length // 3, self.file_length // 2]


    def train(self, train_data, vocab):
        """
        This function builds the word counts and sentence percentages used for classify_text
        train_data: vectorized text
        train_labels: vectorized labels
        vocab: vocab from build_vocab
        """
        for i in range(len(vocab)):
            good = 0 # reset the count for each word
            bad = 0
            for x in range(len(train_data)):
                if(train_data[x][i] == 1):
                    if(train_data[x][len(train_data[x])-1] == "1"): # good 
                        good += 1
                    if(train_data[x][len(train_data[x])-1] == "0"): # bad
                        bad += 1
                print("Good: ", good)
                print("Bad: ", bad)
                break
        return 1


    def classify_text(self, vectors, vocab):
        """
        vectors: [vector1, vector2, ...]
        predictions: [0, 1, ...]
        """
        return predictions
    