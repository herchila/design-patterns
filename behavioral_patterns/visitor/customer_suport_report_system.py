from abc import ABC, abstractmethod


# Element Interface
class CustomerQuery(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


# Concrete Elements
class TechnicalSupportQuery(CustomerQuery):
    def accept(self, visitor):
        visitor.visit_technical_support(self)


class BillingQuery(CustomerQuery):
    def accept(self, visitor):
        visitor.visit_billing(self)


class GeneralInquiry(CustomerQuery):
    def accept(self, visitor):
        visitor.visit_general_inquiry(self)


# Visitor Interface
class ReportVisitor(ABC):
    @abstractmethod
    def visit_technical_support(self, query):
        pass

    @abstractmethod
    def visit_billing(self, query):
        pass

    @abstractmethod
    def visit_general_inquiry(self, query):
        pass


# Concrete Visitors
class PerformanceReportVisitor(ReportVisitor):
    def visit_technical_support(self, query):
        # Perform operations specific to performance report for technical support
        pass

    def visit_billing(self, query):
        # Perform operations specific to performance report for billing
        pass

    def visit_general_inquiry(self, query):
        # Perform operations specific to performance report for general inquiries
        pass


class FeedbackReportVisitor(ReportVisitor):
    def visit_technical_support(self, query):
        # Perform operations specific to feedback report for technical support
        pass

    def visit_billing(self, query):
        # Perform operations specific to feedback report for billing
        pass

    def visit_general_inquiry(self, query):
        # Perform operations specific to feedback report for general inquiries
        pass


#Usage
# Client code
technical_query = TechnicalSupportQuery()
billing_query = BillingQuery()
general_query = GeneralInquiry()

performance_report_visitor = PerformanceReportVisitor()
feedback_report_visitor = FeedbackReportVisitor()

technical_query.accept(performance_report_visitor)
billing_query.accept(feedback_report_visitor)
