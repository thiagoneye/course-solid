from .report.html_generator import HTMLGenerator
from .report.markdown_generator import MarkdownGenerator


class ReportGenerator():

    @classmethod
    def build(cls, type, repos):
        if type == "HTML":
            return HTMLGenerator.build(repos)
        if type == "Markdown":
            return MarkdownGenerator.build(repos)
        return "Invalid report type!"
