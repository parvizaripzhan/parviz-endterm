def translateLetter(*letters):
    letter_points = {'A+': 4.3, 'A': 4.0, 'A-': 3.7,
                     'B+': 3.3, 'B': 3.0, 'B-': 2.7,
                     'C+': 2.3, 'C': 2.0, 'C-': 1.7,
                     'D+': 1.3, 'D': 1.0, 'D-': 0.7}

    return [letter_points.get(letter, 0) for letter in letters]


def translatePercentage(*percentages):
    return [translateLetter(score)[0] for score in percentages]


def calculateGPA(*args):
    point_credit_pairs = zip(args[::2], args[1::2])

    total_points = sum(point * credit for point, credit in point_credit_pairs)
    total_credits = sum(args[1::2])

    overall_gpa = total_points / total_credits if total_credits > 0 else 0

    return round(overall_gpa, 2)


letters = translateLetter('A+', 'B', 'C')
print("Translate Letter:", letters)

percentages = translatePercentage(100, 45, 55, 89)
print("Translate Percentage:", percentages)

gpa = calculateGPA(3.3, 4, 2.7, 3, 4.0, 4)
print("Overall GPA:", gpa)

import os


def process_grades(directory):
    with open(f"{directory}/credits.txt") as credits_file:
        credits = [int(line.strip()) for line in credits_file]

    overall_gpas = []

    for course_file in os.listdir(directory):

        if course_file.endswith(".txt") and course_file != "credits.txt":
            with open(f"{directory}/{course_file}") as file:
                scores = [int(line.strip()) for line in file]

            points = translatePercentage(*scores)

            gpa = calculateGPA(*points, *credits)

            overall_gpas.append(gpa)

    with open(f"{directory}/overallGPAs.txt", "w") as result_file:
        for gpa in overall_gpas:
            result_file.write(f"{gpa:.2f}\n")


process_grades("geades")


class Student:
    def init(self, name, scores):
        self.name = name
        self.scores = scores
        self.gpa = self.calculateGPA()
        self.status = self.setStatus()

    def calculateGPA(self):
        total_credits = sum(course['credits'] for course in self.scores.values())
        weighted_score = sum(course['score'] * course['credits'] for course in self.scores.values())
        return weighted_score / total_credits if total_credits > 0 else 0.0

    def setStatus(self):
        return "Passed" if self.gpa >= 1.0 else "Not Passed"

    def showGPA(self):
        print(f"{self.name}'s GPA: {self.gpa:.2f}")

    def showStatus(self):
        print(f"{self.name}'s Status: {self.status}")


student_data = {'math': {'score': 4.3, 'credits': 4}, 'chemistry': {'score': 3.3, 'credits': 3},
                'english': {'score': 4.0, 'credits': 4}}
student = Student("Parviz Aripzhan", student_data)
student.showGPA()
student.showStatus()

# 4
# Простыми словами API- это набор инструкций и инструментов, которые позволяют разным программам обмениваться информацией и взаимодействовать между собой. Этот инструментарий определяет, как различные программные компоненты могут общаться, ации. API можно представить как "окно", через которое разные программы обмениваются данными и командами для совместной работы.

# 5
# Socket — это как бы труба, через которую компьютеры могут общаться друг с другом. Он предоставляет способ передачи данных между программами, даже если они работают на разных устройствах. Sockets позволяют программам отправлять и получать информацию, делая возможной коммуникацию между компьютерами в сети.