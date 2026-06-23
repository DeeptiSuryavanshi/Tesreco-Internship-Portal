from abc import ABC, abstractmethod

class Report(ABC):

    @abstractmethod
    def generate_report(self):
        pass


class AttendanceReport(Report):

    def generate_report(self):
        print("Attendance Report")


class PerformanceReport(Report):

    def generate_report(self):
        print("Performance Report")