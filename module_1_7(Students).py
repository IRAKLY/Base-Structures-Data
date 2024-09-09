grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades_average = []
students_sort = []
students_grades = {}
grades_average.append(sum(grades[0])/len(grades[0]))
grades_average.append(sum(grades[1])/len(grades[1]))
grades_average.append(sum(grades[2])/len(grades[2]))
grades_average.append(sum(grades[3])/len(grades[3]))
grades_average.append(sum(grades[4])/len(grades[4]))
print('Средние оценки:', grades_average)
students_sort.append(sorted(students))
students_grades.update({students_sort[0][0] : grades_average[0],
                       students_sort[0][1] : grades_average[1],
                       students_sort[0][2] : grades_average[2],
                       students_sort[0][3] : grades_average[3],
                       students_sort[0][4] : grades_average[4]
                        })
print(sorted(students))
print(students_sort)
print('Таблица успеваемости учеников:', students_grades)

