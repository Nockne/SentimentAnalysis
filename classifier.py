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
        self.percent_positive_sentences = 0
        self.percent_negative_sentences = 0
        self.file_length = 499
        self.file_sections = [self.file_length // 4, self.file_length // 3, self.file_length // 2]


    def getSum(words):
        total = 0
        for i in range(len(words)-1):
            if(words[i] > 1):
                total += (words[i]-1)
        return total


    def train(self, train_data, vocab):
        """
        This function builds the word counts and sentence percentages used for classify_text
        train_data: vectorized text
        train_labels: vectorized labels
        vocab: vocab from build_vocab
        """
        # get word counts
        goodWords = []
        badWords = []
        for i in range(0, len(vocab)):
            good = 1 # reset the count for each word
            bad = 1
            for x in range(0, len(train_data)):
                if(train_data[x][i] == "1"):
                    if(train_data[x][len(train_data[x])-1] == "1"): # good 
                        good += 1
                    if(train_data[x][len(train_data[x])-1] == "0"): # bad
                        bad += 1
            goodWords.append(good)
            badWords.append(bad)
        pSum = self.getSum(goodWords)
        nSum = self.getSum(badWords)
        goodPs = []
        badPs = []
        for i in range(len(vocab)):
            probability = goodWords[i] / pSum
            goodPs.append(probability)
            probability2 = badWords[i] / nSum
            badPs.append(probability2)
        self.positive_word_counts = goodPs
        self.negative_word_counts = badPs

        # get good vs bad sentence count
        good = 0
        bad = 0
        for i in range(len(train_data)):
            if(train_data[i][len(train_data[i])-1] == "1"):
                good += 1
            if(train_data[i][len(train_data[i])-1] == "0"):
                bad += 1
        
        self.percent_positive_sentences = good / len(train_data)
        self.percent_negative_sentences = bad / len(train_data)
        return 1


    def classify_text(self, vectors, vocab):
        """
        vectors: [vector1, vector2, ...]
        predictions: [0, 1, ...]
        """
        predictions = []
        for i in range(len(vectors)): # iterate through sentences
            pScore = self.percent_positive_sentences # prior probabilities
            nScore = self.percent_negative_sentences
            for x in range(len(vocab)):
                if(vectors[i][x] == "1"):
                    pScore *= self.positive_word_counts[x]
                    nScore *= self.negative_word_counts[x]
            if(pScore > nScore):
                prediction = "1"
            else:
                prediction = "0"
            predictions.append(prediction)

        return predictions
    