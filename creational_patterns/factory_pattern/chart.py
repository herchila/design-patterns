class Chart:
    def draw(self): pass

class BarChart(Chart):
    def draw(self):
        return "Drawing a bar chart"

class PieChart(Chart):
    def draw(self):
        return "Drawing a pie chart"

def chart_factory(chart_type):
    charts = {
        "bar": BarChart,
        "pie": PieChart
    }
    return charts[chart_type]()

# Usage
chart = chart_factory("bar")
print(chart.draw())  # Output: Drawing a bar chart
