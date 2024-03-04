from nltk.tokenize import sent_tokenize, word_tokenize
from PyQt5.QtWidgets import *
import qdarkstyle
import sys


class TokenizerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Text Tokenizer')
        self.setGeometry(600, 200, 750, 500)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        self.text_edit = QTextEdit()
        self.text_edit.setStyleSheet("font-size: 14pt;")
        self.text_edit.setText("NLTK is a leading platform for building Python programs to work with human language "
                               "data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, "
                               "NLTK is a free, open source, community-driven project.")

        self.tokenized_output = QTextEdit()
        self.tokenized_output.setStyleSheet("font-size: 14pt;")
        self.tokenized_output.setReadOnly(True)

        self.token_count_label = QLabel()
        self.token_count_label.setStyleSheet("font-size: 12pt;")

        sent_tokenize_button = QPushButton('Sent Tokenize')
        sent_tokenize_button.setStyleSheet("font-size: 12pt;")
        sent_tokenize_button.setFixedSize(250, 50)
        sent_tokenize_button.clicked.connect(self.sent_tokenize)

        word_tokenize_button = QPushButton('Word Tokenize')
        word_tokenize_button.setStyleSheet("font-size: 12pt;")
        word_tokenize_button.setFixedSize(250, 50)
        word_tokenize_button.clicked.connect(self.word_tokenize)

        split_tokenize_button = QPushButton('Split Tokenize')
        split_tokenize_button.setStyleSheet("font-size: 12pt;")
        split_tokenize_button.setFixedSize(250, 50)
        split_tokenize_button.clicked.connect(self.split_tokenize)

        button_layout = QHBoxLayout()
        button_layout.addWidget(sent_tokenize_button)
        button_layout.addWidget(word_tokenize_button)
        button_layout.addWidget(split_tokenize_button)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addLayout(button_layout)
        layout.addWidget(self.tokenized_output)
        layout.addWidget(self.token_count_label)

        self.setLayout(layout)

    def sent_tokenize(self):
        text = self.text_edit.toPlainText()
        sent_tokens = sent_tokenize(text)
        tokenized_text = f'[\'{'\', \''.join(sent_tokens)}\']'
        self.token_count_label.setText(f"Number of tokens: {len(sent_tokens)}")
        self.tokenized_output.setText(tokenized_text)

    def word_tokenize(self):
        text = self.text_edit.toPlainText()
        word_tokens = word_tokenize(text)
        tokenized_text = f'[\'{'\', \''.join(word_tokens)}\']'
        self.token_count_label.setText(f"Number of tokens: {len(word_tokens)}")
        self.tokenized_output.setText(tokenized_text)

    def split_tokenize(self):
        text = self.text_edit.toPlainText()
        split_tokens = text.split()
        tokenized_text = f'[\'{'\', \''.join(split_tokens)}\']'
        self.token_count_label.setText(f"Number of tokens: {len(split_tokens)}")
        self.tokenized_output.setText(tokenized_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TokenizerApp()
    window.show()
    sys.exit(app.exec_())
