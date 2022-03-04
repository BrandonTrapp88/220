def weighted_average(in_file_name,out_file_name):

    #open files
    input_file = open(in_file_name,"r")
    students = input_file.readlines()
    input_file.close()
    output_file = open(out_file_name,"w")
    class_average = 0
    #split students and grades
    for i in range(len(students)):
        person = students[i].split(":")
        grade = person[1].split()
        answer = 0
        answer_grade = 0
        #split grades and do math
        for j in range(0,len(grade),2):
            total = int(grade[j])
            total_grade = int(grade[j+1])
            answer_grade = answer_grade + (total * total_grade)
            answer = answer + total
        if answer > 100:
            output_file.write(person[0]+" average: "+"The weights are more than 100 \n")
        elif answer < 100 :
            output_file.write(person[0]+" average: " +"This weight is less \n ")
        else:
            output_file.write(person[0] + " average: " + str(answer_grade/100) + "\n")
            class_average = class_average + (answer_grade/100)

    output_file.write("Class average: " + str(class_average/3))
    output_file.close()




def main():
    #This part of the instructions confused me hope its right.
    weighted_average("grades.txt","avg.txt")
main()