from typing import Dict, List

class GradeBook:
    """Sistema de calificaciones de estudiantes"""

    def __init__(self) -> None:
        self._students: Dict[str, List[float]] = {}
    
    def add_student(self, student_name: str) -> None:
        """
        Adds new student to the gradebook.

        Args:
            student_name(str): The name of the student to be added.
        """
        self._students[student_name] = []
    
    def add_grade(self, student_name: str, grade: float) -> None:
        """
        Adds grade to the list of grade corresponding to an specific student.

        Args:
            student_name(str): The name of the student to whom the grade will be added.
            grade(float): The grade to be added to the list
        """
        if grade < 0 or grade > 10:
            raise ValueError(f"The grade: {grade}. Is not a valid grade.")
        self._students[student_name].append(grade)
    
    def get_average(self, student_name: str) -> float:
        """
        Calculates the average of an specific student

        Args:
            student_name(str): The name of the student whose average will be calculated

        Returns:
            If dictionary not empty, returns average calculated
            If dictionary is empty, returns 0.0
        """
        if not self._students[student_name]:
            return 0.0
        return sum(self._students[student_name]) / len(self._students[student_name])
    
    def get_top_students(self, limit: int = 1) -> List[str]:
        """
        Sorts by students' average grade from higher to lower with a limit set

        Args:
            limit(int, optional): the amount of students to be returned. Default value: 1

        Returns:
            List with the students names ordered from higher to lower grade.
        """
        if limit > len(self._students):
            limit = len(self._students)
        
        return sorted(self._students, key=self.get_average, reverse=True)[:limit]
    
    def get_all_students(self) -> List[str]:
        """
        Returns all of the students names in a list
        """
        return list(self._students.keys())

def main():
    gradebook = GradeBook()
    gradebook.add_student("Valentina")
    gradebook.add_grade("Valentina", 9.2)
    gradebook.add_grade("Valentina", 9.8)
    gradebook.add_grade("Valentina", 10.0)
    gradebook.add_student("Laura")
    gradebook.add_grade("Laura", 10.0)
    gradebook.add_grade("Laura", 9.8)
    gradebook.add_grade("Laura", 9.0)
    gradebook.add_student("Bob")
    gradebook.add_grade("Bob", 9.2)
    gradebook.add_grade("Bob", 7.8)
    gradebook.add_grade("Bob", 9.6)
    gradebook.add_student("Juan")
    gradebook.add_grade("Juan", 9.9)
    gradebook.add_grade("Juan", 9.8)
    gradebook.add_grade("Juan", 9.6)
    gradebook.get_top_students(2)
    print(gradebook._students)
    print(gradebook.get_top_students(2))
    print(gradebook.get_top_students(4))
    print(gradebook.get_top_students(1))

if __name__ == "__main__":
    main()
