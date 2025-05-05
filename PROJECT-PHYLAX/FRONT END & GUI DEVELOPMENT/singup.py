import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt


class PhylaxSignupUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PHYLAX Firewall Security")
        self.setFixedSize(900, 500)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #ffffff;")

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # --- Left Logo Panel ---
        logo_panel = QFrame()
        logo_panel.setFixedWidth(400)
        logo_panel.setStyleSheet("background-color: #1C2833;")
        logo_layout = QVBoxLayout(logo_panel)
        logo_layout.setContentsMargins(0, 0, 0, 0)

        logo_label = QLabel()
        pixmap = QPixmap("LOGO.jpeg")
        if pixmap.isNull():
            logo_label.setText("LOGO NOT FOUND")
            logo_label.setStyleSheet("color: white; font-size: 20px;")
        else:
            pixmap = pixmap.scaled(400, 500, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        logo_layout.addWidget(logo_label)

        # --- Right Signup Form Panel ---
        form_panel = QFrame()
        form_panel.setStyleSheet("QFrame { background-color: #F8F9F9; }")
        form_layout = QVBoxLayout(form_panel)
        form_layout.setContentsMargins(60, 80, 60, 80)
        form_layout.setSpacing(10)

        # Centered heading
        heading = QLabel("Signup")
        heading.setFont(QFont("Arial", 22, QFont.Bold))
        heading.setAlignment(Qt.AlignCenter)
        heading.setStyleSheet("color: #2C3E50;")

        # Input fields
        self.fullname = QLineEdit()
        self.fullname.setPlaceholderText("Full Name")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")

        for field in [self.fullname, self.password, self.email]:
            field.setFixedHeight(40)
            field.setStyleSheet("""
                QLineEdit {
                    font-size: 14px;
                    padding: 10px;
                    background: #ffffff;
                    border: none;
                    border-radius: 10px;
                }
                QLineEdit:focus {
                    background-color: #f0f0f0;
                }
            """)

        # Button
        self.signup_btn = QPushButton("SIGN UP")
        self.signup_btn.setFixedHeight(45)
        self.signup_btn.setStyleSheet("""
            QPushButton {
                background-color: #2C3E50;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #1A252F;
            }
        """)

        # Add widgets to form layout
        form_layout.addWidget(heading)
        form_layout.addSpacing(20)
        form_layout.addWidget(self.fullname)
        form_layout.addWidget(self.password)
        form_layout.addWidget(self.email)
        form_layout.addSpacing(15)
        form_layout.addWidget(self.signup_btn)

        # Combine panels
        main_layout.addWidget(logo_panel)
        main_layout.addWidget(form_panel)


# --- Run App ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhylaxSignupUI()
    window.show()
    sys.exit(app.exec_())
