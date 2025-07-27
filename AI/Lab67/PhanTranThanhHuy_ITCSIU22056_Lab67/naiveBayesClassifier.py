import pandas as pd
import numpy as np
import sys

class NaiveBayesFilter:
    def __init__(self):
        self.data = pd.DataFrame()
        self.vocabulary = set()  # returns tuple of unique words
        self.p_spam = 0  # Probability of Spam
        self.p_ham = 0  # Probability of Ham
        # Initiate parameters
        self.parameters_spam = {unique_word: 0 for unique_word in self.vocabulary}
        print('parameters_spam: ', self.parameters_spam)
        self.parameters_ham = {unique_word: 0 for unique_word in self.vocabulary}
        print('parameters_ham: ', self.parameters_spam)

    def fit(self, X, y):
        "*** YOUR CODE HERE ***"
        rows = []
        vocabulary = set()
        self.word_counts_spam = {}
        self.word_counts_ham = {}
        self.total_words_spam = 0
        self.total_words_ham = 0

        for message, label in zip(X, y):
            word_counts = {}
            for word in message:
                vocabulary.add(word)
                word_counts[word] = word_counts.get(word, 0) + 1

                if label == 'spam':
                    self.word_counts_spam[word] = self.word_counts_spam.get(word, 0) + 1
                    self.total_words_spam += 1
                else:
                    self.word_counts_ham[word] = self.word_counts_ham.get(word, 0) + 1
                    self.total_words_ham += 1

            word_counts['Label'] = label
            rows.append(word_counts)

        self.vocabulary = vocabulary
        self.data = pd.DataFrame(rows).fillna(0)

        total = len(self.data)
        self.p_spam = (self.data['Label'] == 'spam').sum() / total
        self.p_ham = (self.data['Label'] == 'ham').sum() / total

        return self.data

    def predict(self, X):
        prob = []
        "*** YOUR CODE HERE ***"
        predictProba = self.predict_proba(X)
        for p_ham, p_spam in predictProba:
            if p_spam > p_ham:
                prob.append('spam')
            else:
                prob.append('ham')
        return prob

    def predict_proba(self, X):
        proba = []
        "*** YOUR CODE HERE ***"
        alpha = 1
        V = len(self.vocabulary)

        for message in X:
            log_p_spam = np.log(self.p_spam)
            log_p_ham = np.log(self.p_ham)

            for word in message:
                if word in self.vocabulary:
                    count_spam = self.word_counts_spam.get(word, 0)
                    prob_word_spam = (count_spam + alpha) / (self.total_words_spam + alpha * V)
                    log_p_spam += np.log(prob_word_spam)

                    count_ham = self.word_counts_ham.get(word, 0)
                    prob_word_ham = (count_ham + alpha) / (self.total_words_ham + alpha * V)
                    log_p_ham += np.log(prob_word_ham)

            max_log = max(log_p_spam, log_p_ham)
            p_spam = np.exp(log_p_spam - max_log)
            p_ham = np.exp(log_p_ham - max_log)
            total = p_spam + p_ham

            norm_p_spam = p_spam / total
            norm_p_ham = p_ham / total

            proba.append([norm_p_ham, norm_p_spam])

        return proba

    def score(self, true_labels, predict_labels):
        recall = 0
        "*** YOUR CODE HERE ***"
        true_positives = sum((t == "spam") and (p == "spam") for t, p in zip(true_labels, predict_labels))
        possible_positives = sum(t == "spam" for t in true_labels)
        if possible_positives == 0:
            return 0.0
        recall = true_positives / possible_positives
        return recall

