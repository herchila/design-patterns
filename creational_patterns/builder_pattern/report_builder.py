from abc import ABC, abstractmethod

# The abstract Builder class
class ReportBuilder(ABC):
    @abstractmethod
    def set_report_type(self, report_type):
        pass

    @abstractmethod
    def set_data(self, data):
        pass

    @abstractmethod
    def add_charts(self):
        pass

    @abstractmethod
    def add_tables(self):
        pass

    @abstractmethod
    def apply_formatting(self):
        pass

    @abstractmethod
    def get_report(self):
        pass

# Concrete Builder
class DataReportBuilder(ReportBuilder):
    def __init__(self):
        self.report = DataReport()

    def set_report_type(self, report_type):
        self.report.type = report_type
        return self

    def set_data(self, data):
        self.report.data = data
        return self

    def add_charts(self):
        self.report.add_charts()
        return self

    def add_tables(self):
        self.report.add_tables()
        return self

    def apply_formatting(self):
        self.report.apply_formatting()
        return self

    def get_report(self):
        return self.report

# Product
class DataReport:
    def __init__(self):
        self.type = None
        self.data = None
        self.contents = []

    def add_charts(self):
        self.contents.append("Charts")

    def add_tables(self):
        self.contents.append("Tables")

    def apply_formatting(self):
        self.contents.append("Formatted")

    def __str__(self):
        return f"{self.type} Report with contents: {', '.join(self.contents)}"

# Director
class ReportDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_simple_report(self, data):
        return self.builder.set_report_type("Simple").set_data(data).add_tables().get_report()

    def construct_detailed_report(self, data):
        return self.builder.set_report_type("Detailed").set_data(data).add_charts().add_tables().apply_formatting().get_report()

# Client code
builder = DataReportBuilder()
director = ReportDirector(builder)

simple_report = director.construct_simple_report("Sample Data")
print(simple_report)

detailed_report = director.construct_detailed_report("Sample Data")
print(detailed_report)
