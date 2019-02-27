#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:41:53 2019

@author: rafael
"""
class Questions:
    answers_correct = 0
    number_of_questions = 0
    correct_answers = []

    def __init__(self):
        pass

    def validation(self, type_, value):
        if type_ == 'float':
            user_input = float(input('Type your answer here!'))
            if user_input == value:
                print('Your answer is correct, congratulations!!')
                return 'question_correct'
            else:
                print('Your answer is not correct, try again!!')
        elif type_ == 'int':
            user_input = int(float(input('Type your answer here!')))
            if user_input == value:
                print('Your answer is correct, congratulations!!')
                return 'question_correct'
            else:
                print('Your answer is not correct, try again!!')
        else:
            user_input = str(input('Type your answer here!'))
            if user_input == value:
                print('Your answer is correct, congratulations!!')
                return 'question_correct'
            else:
                print('Your answer is not correct, try again!!')

    def question_one(self):
        message = """
        What is the RMSE of the linear regression model in the test set?
        (2 decimal places)
        """
        print(message)
        output = self.validation('float', 9.99)
        if output == 'question_correct':
            self.correct_answers.append('Answer One')

    def question_two(self):
        print('What is the weight of woman with 75 inches of the model?')
        output = self.validation('int', 202)
        if output == 'question_correct':
            self.correct_answers.append('Answer Two')

    def question_three(self):
        print('What is the RMSE of the KNN model in the test set')
        print('(2 decimal places)')
        output = self.validation('float', 10.94)
        if output == 'question_correct':
            self.correct_answers.append('Answer Three')

    def question_four(self):
        message = """
        What is the RMSE of the KNN model on the training set, 
        using n_neighbors as parameter of the model?
        (two decimal places)
        """
        print(message)
        output = self.validation('float', 0.0)
        if output == 'question_correct':
            self.correct_answers.append('Answer Four')

    def question_five(self):
        message = """
        What is the RMSE of the KNN model on the test set, using n_neighbors
        as parameter of the model?
        (two decimal places)
        """
        print(message)
        output = self.validation('float', 14.09)
        if output == 'question_correct':
            self.correct_answers.append('Answer Five')

    def question_six(self):
        message = """
        Why the performance of the model is almost perfect in the training set,
        but the model performance is worst than using five neighbors in the
        test set?

        Press 1 for: The model has memorized the training set, but does not
        generalize well on the test set (Overfitting)

        Press 2 for: The model is not able to capture the underlying patterns
        on the data (Underfitting)

        This question is not graded!!
        """
        print(message)
        answer = int(input('Press 1 or 2'))
        message2 = """
        The correct answer is 1!
        What happened is one of the most common symptoms of overfitting.

        The model that you have created is very complex and this model
        doesn't generalize well on unseen data.

        """
        if answer == 1:
            print('Your answer is correct!')
            print(message2)
        else:
            print(message2)
     
    def print_results(self):
        a = len(set(self.correct_answers))
        if a == 5:
            print('Congratulations, you have answered all answers correctly!!')
        else:
            print('Keep working! You have answered correctly {} out of 5 questions!'.format(a))
    