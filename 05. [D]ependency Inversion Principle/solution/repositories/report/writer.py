from .file_writer import ReportFileWriter

class ReportWriter():

    @staticmethod
    def write(report, writer):
        writer.write(report)
