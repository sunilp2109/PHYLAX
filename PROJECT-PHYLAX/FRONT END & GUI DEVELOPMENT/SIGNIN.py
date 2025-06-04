import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt


class PhylaxSigninUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PHYLAX Firewall Security")
        self.setFixedSize(1200, 700)
        self.init_ui()

    def add_centered_widget(self, parent_layout,widget):
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(widget)
        hbox.addStretch()
        parent_layout.addLayout(hbox)

    def init_ui(self):
        self.setStyleSheet("background-color: #ffffff;")

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # --- Left Logo Panel ---
        logo_panel = QFrame()
        logo_panel.setFixedWidth(500)
        logo_panel.setStyleSheet("background-color: #2C3E50;")
        logo_layout = QVBoxLayout(logo_panel)
        logo_layout.setContentsMargins(0, 0, 0, 0)

        logo_label = QLabel()
        pixmap = QPixmap("logo.png")
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

        # Outer layout to center vertically
        outer_layout = QVBoxLayout(form_panel)
        outer_layout.setContentsMargins(60, 0, 60, 0)
        outer_layout.setSpacing(0)

        # Inner layout containing actual form elements
        form_layout = QVBoxLayout()
        form_layout.setSpacing(25)
        form_layout.setAlignment(Qt.AlignTop)

        # Centered heading
        self.heading = QLabel("SIGNIN", self)
        self.heading.setFont(QFont("Arial", 18, QFont.Bold))
        self.heading.setStyleSheet("QLabel { color: #2C3E50; }")
        self.heading.setAlignment(Qt.AlignHCenter)

        # Input fields
        self.email= QLineEdit(self)
        self.email.setPlaceholderText("Email")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        for field in [self.email, self.password]:
            field.setFixedHeight(40)
            field.setFixedWidth(400)
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
        self.signin_btn = QPushButton("SIGN IN")
        self.signin_btn.setFont(QFont("Arial", 8, QFont.Bold))
        self.signin_btn.setFixedHeight(45)
        self.signin_btn.setFixedWidth(200)
        self.signin_btn.setStyleSheet("""
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

        # Utility to center widgets horizontally
        def add_centered_widget(layout, widget):
            hbox = QHBoxLayout()
            hbox.addStretch()
            hbox.addWidget(widget)
            hbox.addStretch()
            layout.addLayout(hbox)

        # Add widgets to form layout

        form_layout.addWidget(self.heading)
        self.add_centered_widget(form_layout, self.email)
        self.add_centered_widget(form_layout, self.password)
        self.add_centered_widget(form_layout, self.signin_btn)

        # Add vertical stretching to center the form vertically
        outer_layout.addStretch()
        outer_layout.addLayout(form_layout)
        outer_layout.addStretch()


        # Combine panels
        main_layout.addWidget(logo_panel)
        main_layout.addWidget(form_panel)


        # Signup link
        self.link_label = QLabel('<a href="login">Don`t have an account?    Sign Up</a>')
        self.link_label.setAlignment(Qt.AlignCenter)
        self.link_label.setFont(QFont("Arial", 8, QFont.Bold))
        self.link_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.link_label.setOpenExternalLinks(False)
        self.link_label.linkActivated.connect(self.open_login_window)
        form_layout.addWidget(self.link_label, alignment=Qt.AlignCenter)

    # Page link
    def open_login_window(self):
        print("Navigating to Login page...")
        self.login_window = PhylaxSignupUI()
        self.login_window.show()
        self.close()

# --- Run App ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhylaxSigninUI()
    window.show()
    sys.exit(app.exec_())
