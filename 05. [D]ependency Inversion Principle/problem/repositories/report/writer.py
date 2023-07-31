from .file_writer import ReportFileWriter

class ReportWriter():

    @staticmethod
    def write(report):
        ReportFileWriter.write_file(report)
