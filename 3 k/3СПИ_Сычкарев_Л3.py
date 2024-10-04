from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def save(self):
        pass


class PDFDocument(Document):
    def save(self):
        print("Сохранение документа в формате PDF.")


class WordDocument(Document):
    def save(self):
        print("Сохранение документа в формате Word.")


class ExcelDocument(Document):
    def save(self):
        print("Сохранение документа в формате Excel.")


class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == 'pdf':
            return PDFDocument()
        elif doc_type == 'word':
            return WordDocument()
        elif doc_type == 'excel':
            return ExcelDocument()
        else:
            raise ValueError("Неизвестный тип документа")


def main():
    pdf_doc = DocumentFactory.create_document('pdf')
    word_doc = DocumentFactory.create_document('word')
    excel_doc = DocumentFactory.create_document('excel')

    pdf_doc.save()
    word_doc.save()
    excel_doc.save()
