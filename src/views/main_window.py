from PySide6.QtCore import Qt
from PySide6.QtWidgets  import QMainWindow, QLineEdit, QPushButton, QProgressBar, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("YouTube Downloader")
        self.setFixedSize(400, 400)

        # Widgets for input
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter the URL of the video")
        self.url_input.setMaximumHeight(30)

        # Widgets for Url validation
        self.valide_url = QLabel("invalid URL")
        self.valide_url.setAlignment(Qt.AlignCenter)
        self.valide_url.setVisible(False)

        # Widgets for resolution selector
        self.resolution_selector = QComboBox(self)
        self.resolution_selector.setMaximumWidth(150)

        # Widgets for download button
        self.download_button = QPushButton("Download", self)
        self.download_button.clicked.connect(self.test)

        # Widgets for progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setVisible(False)

        # Widgets for status label
        self.status_label = QLabel("Done")
        self.status_label.setVisible(False)
        self.status_label.setAlignment(Qt.AlignCenter)

        # Widgets for video details
        self.video_details = QLabel("Video Details")
        self.video_details.setAlignment(Qt.AlignCenter)
        self.video_name = QLabel("Video Name")
        self.video_name.setAlignment(Qt.AlignCenter)
        self.video_author = QLabel("Video Author")
        self.video_duration = QLabel("Video Duration")
        self.video_details.setVisible(False)
        self.video_name.setVisible(False)
        self.video_author.setVisible(False)
        self.video_duration.setVisible(False)

        # layout for resolution selector
        resolution_layout = QHBoxLayout()
        label = QLabel("Resolution")
        resolution_layout.addWidget(label)
        resolution_layout.addWidget(self.resolution_selector)
        resolution_layout.setAlignment(Qt.AlignCenter)

        # layout for video details
        video_details_layout = QVBoxLayout()
        video_details_layout.addWidget(self.video_details)
        video_details_layout.addWidget(self.video_name)
        video_details_layout.addWidget(self.video_author)
        video_details_layout.addWidget(self.video_duration)
        video_details_layout.setAlignment(Qt.AlignCenter)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.url_input)
        layout.addWidget(self.valide_url)
        layout.addLayout(resolution_layout)
        layout.addLayout(video_details_layout)
        layout.addWidget(self.download_button)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.status_label)
        layout.setAlignment(Qt.AlignTop)

        # Container
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def test(self):
        self.video_details.setVisible(not self.video_details.isVisible())
        self.video_name.setVisible(not self.video_name.isVisible())
        self.video_author.setVisible(not self.video_author.isVisible())
        self.video_duration.setVisible(not self.video_duration.isVisible())
