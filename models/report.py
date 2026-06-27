from abc import ABC, abstractmethod

class Report(ABC):

    @abstractmethod
    def generate_report(self):
        pass


class AttendanceReport(Report):

    def generate_report(self):
        return "Generating attendance report of interns..."


class PerformanceReport(Report):

    def generate_report(self):
        return "Generating performance report of interns..."
if __name__ == "__main__":
    attendance = AttendanceReport()
    performance = PerformanceReport()

    print(attendance.generate_report())
    print(performance.generate_report())    