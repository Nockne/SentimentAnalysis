# CS331 Sentiment Analysis Assignment 3
# This file contains the processing functions
import re
from classifier import BayesClassifier

def process_text(text):
    """
    Preprocesses the text: Remove apostrophes, punctuation marks, etc.
    Returns a list of text
    """
    processed = []

    for x in range(len(text)):
        s = re.sub(r'[^a-zA-Z ]', '', text[x])
        s = s.lower()
        processed.append(s)
    return processed


def build_vocab(preprocessed_text):
    """
    Builds the vocab from the preprocessed text
    preprocessed_text: output from process_text
    Returns unique text tokens
    """
    temp = []

    for i in range(len(preprocessed_text)):
        text = preprocessed_text[i].split()
        for x in range(len(text)):
            temp.append(text[x])
    vocab = [*set(temp)] #remove duplicates
    vocab.sort()
    return list(vocab)


def vectorize_text(text, vocab, originalText):
    """
    Converts the text into vectors
    text: preprocess_text from process_text
    vocab: vocab from build_vocab
    Returns the vectorized text and the labels
    """
    vector = []
    for i in range(len(text)):
        temp = [0] * len(vocab)
        for x in range(len(vocab)):
            if vocab[x] in text[i]:
                temp[x] = "1"
            else:
                temp[x] = "0"
        temp.append(getSentiment(originalText, i))
        vector.append(temp)
    vectorized_text = vector
    
    return vectorized_text


def accuracy(predicted_labels, true_labels):
    """
    predicted_labels: list of 0/1s predicted by classifier
    true_labels: list of 0/1s from text file
    return the accuracy of the predictions
    """
    count = 0
    for i in range(len(true_labels)-1):
        if(true_labels[i][len(true_labels[i])-1] == predicted_labels[i]):
            count += 1
    accuracy_score = count / len(predicted_labels)
    return accuracy_score


def getSentiment(text, index):
    return text[index][len(text[index])-3]


def createFile(inputFile, outputFile):
    with open(inputFile) as f:
        text = f.readlines()
    processed = process_text(text) # remove everything but letters from file
    vocab = build_vocab(processed) # get all words in alphabetical order
    vectored = vectorize_text(processed, vocab, text)

    file = open(outputFile, 'w')
    for i in vocab:
        file.write(i)
        file.write(", ")
    file.write("classlabel\n")

    for i in range(len(vectored)):
        for x in range(len(vectored[i])):
            file.write(str(vectored[i][x]))
            if(x < len(vectored[i])-1):
                file.write(",")
            else:
                file.write("\n")
    file.close()
    return vectored, vocab

def main():
    # Take in text files and outputs sentiment scores
    # -------------Training Set-----------------
    outputFile = "preprocessed_train.txt"
    inputFile = "trainingSet.txt"
    vectorized, vocab = createFile(inputFile, outputFile)

    #---------------Test Set--------------------
    outputFile = "preprocessed_test.txt"
    inputFile = "testSet.txt"
    vectorized2, vocab2 = createFile(inputFile, outputFile)
    
    bayes = BayesClassifier
    bayes.train(bayes, vectorized, vocab)
    predictions = bayes.classify_text(bayes, vectorized, vocab)
    print(accuracy(predictions, vectorized) * 100)
    
    return 1

    

if __name__ == "__main__":
    main()