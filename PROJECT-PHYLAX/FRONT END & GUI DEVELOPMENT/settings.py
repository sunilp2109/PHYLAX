import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QCheckBox, QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap

class PhylaxSettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PHYLAX - Settings & Configuration")
        self.setGeometry(100, 100, 1200, 600)

        # Main widget and layout
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        # Sidebar (Navigation)
        sidebar = QWidget()
        sidebar.setStyleSheet("background-color: #0A1B2F; color: white;")  # Dark blue background
        sidebar.setFixedWidth(200)
        sidebar_layout = QVBoxLayout(sidebar)

        # Add PHYLAX logo at the top of the sidebar
        logo_label = QLabel()
        logo_pixmap = QPixmap("phylax_logo.png")  # Replace with the path to your PHYLAX logo image
        if not logo_pixmap.isNull():  # Check if the image loaded successfully
            logo_label.setPixmap(logo_pixmap.scaled(150, 50, Qt.KeepAspectRatio))  # Scale the logo to fit
        else:
            logo_label.setText("PHYLAX Logo")  # Fallback text if the image fails to load
        logo_label.setAlignment(Qt.AlignCenter)
        logo_label.setStyleSheet("padding: 10px;")
        sidebar_layout.addWidget(logo_label)

        # Sidebar items with symbols (icons are white)
        sidebar_items = [
            ("🏠 Dashboard", "Dashboard"),
            ("📜 Logs", "Logs"),
            ("📊 Analytics", "Analytics"),
            ("🔔 Alerts", "Alerts"),
            ("⚙️ Settings", "Settings"),
            ("❓ Help Center", "Help Center"),
            ("👤 Account", "Account"),
            ("🚪 Logout", "Logout")
        ]
        for symbol_text, item in sidebar_items:
            label = QLabel(symbol_text)
            label.setFont(QFont("Arial", 12))
            # Ensure all text and icons are white, highlight "Settings" with a background
            if item == "Settings":
                label.setStyleSheet("padding: 10px; color: white; background-color: #00C4B4; border-radius: 5px;")
            else:
                label.setStyleSheet("padding: 10px; color: white;")
            sidebar_layout.addWidget(label)

        sidebar_layout.addStretch()

        # Main content area
        content = QWidget()
        content_layout = QVBoxLayout(content)

        # Header
        header_layout = QHBoxLayout()
        title = QLabel("Settings & Configuration")
        title.setFont(QFont("Arial", 24, QFont.Bold))  # Larger font for title
        subtitle = QLabel("Manage your security preferences")
        subtitle.setFont(QFont("Arial", 14))  # Slightly larger subtitle
        subtitle.setStyleSheet("color: gray;")

        # Search bar and user profile
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search...")
        search_bar.setStyleSheet("padding: 5px; border: 1px solid #ccc; border-radius: 5px; max-width: 300px;")
        user_profile = QPushButton("Sandhiya Velmurugan")
        user_profile.setStyleSheet("background-color: transparent; color: black; border: none;")

        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(search_bar)
        header_layout.addWidget(user_profile)

        content_layout.addWidget(title)
        content_layout.addWidget(subtitle)
        content_layout.addLayout(header_layout)
        content_layout.addSpacing(20)  # Add spacing after header

        # Tabs (General, Firewall, API Keys, 2FA, Integrations)
        tabs_layout = QHBoxLayout()
        tabs = ["⚙️ General", "🔥 Firewall", "🔑 API Keys", "🔒 2FA", "☁️ Integrations"]
        for tab in tabs:
            tab_label = QLabel(tab)
            # Set all tab icons and text to white, highlight "General" with a background
            if tab == "⚙️ General":
                tab_label.setStyleSheet("padding: 10px; color: white; background-color: #4682B4; border-radius: 5px;")
            else:
                tab_label.setStyleSheet("padding: 10px; color: white;")
            tab_label.setFont(QFont("Arial", 12))
            tabs_layout.addWidget(tab_label)
        tabs_layout.addStretch()
        content_layout.addLayout(tabs_layout)
        content_layout.addSpacing(30)  # Add spacing after tabs

        # General Settings Section
        settings_title = QLabel("General Settings")
        settings_title.setFont(QFont("Arial", 18, QFont.Bold))  # Adjusted font size
        settings_subtitle = QLabel("Manage general system configuration")
        settings_subtitle.setFont(QFont("Arial", 12))
        settings_subtitle.setStyleSheet("color: gray;")
        content_layout.addWidget(settings_title)
        content_layout.addWidget(settings_subtitle)
        content_layout.addSpacing(20)  # Add spacing after section title

        # Settings Options with Toggle Switches
        settings_options = [
            ("Real-time Protection", "Enable continuous monitoring and protection", False),
            ("Automatic Updates", "Keep the system updated with latest security definitions", True),
            ("Threat Analytics", "Send anonymous threat data to improve detection", False),
            ("Notifications", "Show alerts for important security events", True),
        ]

        for title, description, checked in settings_options:
            option_layout = QHBoxLayout()
            option_label_layout = QVBoxLayout()
            option_title = QLabel(title)
            option_title.setFont(QFont("Arial", 12, QFont.Bold))
            option_description = QLabel(description)
            option_description.setFont(QFont("Arial", 10))
            option_description.setStyleSheet("color: gray;")
            option_label_layout.addWidget(option_title)
            option_label_layout.addWidget(option_description)
            toggle = QCheckBox()
            toggle.setChecked(checked)
            option_layout.addLayout(option_label_layout)
            option_layout.addStretch()
            option_layout.addWidget(toggle)
            content_layout.addLayout(option_layout)
            content_layout.addSpacing(20)  # Add spacing between options

        # Scan Frequency Dropdown
        scan_layout = QHBoxLayout()
        scan_label = QLabel("Scan Frequency")
        scan_label.setFont(QFont("Arial", 12, QFont.Bold))
        scan_dropdown = QComboBox()
        scan_dropdown.addItems(["Daily", "Weekly", "Monthly"])
        scan_dropdown.setCurrentText("Daily")
        scan_dropdown.setStyleSheet("padding: 5px; border: 1px solid #ccc; border-radius: 5px; max-width: 200px;")
        scan_layout.addWidget(scan_label)
        scan_layout.addStretch()
        scan_layout.addWidget(scan_dropdown)
        content_layout.addLayout(scan_layout)
        content_layout.addSpacing(30)  # Add spacing before button

        # Save Changes Button
        save_button = QPushButton("Save Changes")
        save_button.setStyleSheet("background-color: #4682B4; color: white; padding: 10px; border-radius: 5px; max-width: 150px;")
        content_layout.addWidget(save_button, alignment=Qt.AlignRight)

        content_layout.addStretch()

        # Add sidebar and content to main layout
        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PhylaxSettingsWindow()
    window.show()
    sys.exit(app.exec_())