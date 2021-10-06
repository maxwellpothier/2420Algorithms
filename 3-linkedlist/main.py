from course import Course
from courselist import CourseList

# python3 -m venv tutorial-env
# source tutorial-env/bin/activate


def main():

    f = open('data.txt', 'r')
    lines = f.readlines()
    for i in range(len(lines)):
        temp_string = lines[i].strip('\n')
        string_list = temp_string.split(',')

    cl = CourseList()
    cl.insert(Course(2300, "Discrete Math", 3.0, 4.0))
    print(cl.size())
    cl.insert(Course(2420, "Algorithms", 3.0, 4.0))
    print(cl.size())
    cl.insert(Course(2600, "Computer Networks", 3.0, 4.0))
    print(cl.size())
    cl.insert(Course(3710, "Applied Probability", 3.0, 4.0))
    print(cl.size())


if __name__ == "__main__":
    main()
