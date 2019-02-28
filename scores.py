school_marks = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
                {'school_class': '4b', 'scores': [4,4,5,2,2]},
                {'school_class': '4c', 'scores': [2,1,4,3,2]},
                {'school_class': '5a', 'scores': [3,4,5,4,2]}]

# i = school_marks['scores']
for score in school_marks:
    print(score['school_class'])
    for marks in score['scores']:
        print(marks)


print(*school_marks[0]['scores'])
