import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap

class PhylaxAlertsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PHYLAX - Security Alerts")
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
            # Ensure all text and icons are white, highlight "Alerts" with a background
            if item == "Alerts":
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
        title = QLabel("Security Alerts")
        title.setFont(QFont("Arial", 24, QFont.Bold))  # Larger font for title
        subtitle = QLabel("Manage and respond to security threats")
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

        # Tabs (Active, Resolved, Dismissed)
        tabs_layout = QHBoxLayout()
        tabs = [("Active", 3, "#FF4D4F"), ("Resolved", 0, None), ("Dismissed", 0, None)]
        for tab_name, count, color in tabs:
            tab_layout = QHBoxLayout()
            tab_label = QLabel(tab_name)
            tab_label.setFont(QFont("Arial", 12))
            if color:
                tab_label.setStyleSheet("padding: 10px; color: #4682B4;")  # Active tab in blue
                count_label = QLabel(str(count))
                count_label.setStyleSheet(f"background-color: {color}; color: white; border-radius: 10px; padding: 2px 8px; font-size: 12px;")
                tab_layout.addWidget(count_label)
            else:
                tab_label.setStyleSheet("padding: 10px; color: gray;")  # Other tabs in gray
            tab_layout.addWidget(tab_label)
            tab_layout.addSpacing(5)  # Small spacing between count and label
            tabs_layout.addLayout(tab_layout)
        tabs_layout.addStretch()
        content_layout.addLayout(tabs_layout)
        content_layout.addSpacing(30)  # Add spacing after tabs

        # Alerts List
        alerts = [
            ("Ransomware Attempt Detected", "2025-06-16 10:23:14", "Endpoint Protection", "A potential ransomware attack was blocked from IP 203.45.123.9. Files were protected from encryption.", "Critical", "#FF4D4F"),
            ("Multiple Failed Login Attempts", "2025-06-16 09:15:22", "Authentication Service", "Five consecutive failed login attempts detected from unusual location.", "High", "#FF7F7F"),
            ("Outdated Software Detected", "2025-06-15 22:01:33", "Vulnerability Scanner", "Chrome browser (v110.0.5481.77) has known security vulnerabilities. Update recommended.", "Medium", "#FFA940"),
        ]

        for title, timestamp, source, description, severity, color in alerts:
            # Alert card with border and padding
            alert_widget = QWidget()
            alert_widget.setStyleSheet("background-color: white; border: 1px solid #e0e0e0; border-radius: 5px; padding: 15px;")
            alert_layout = QHBoxLayout(alert_widget)

            # Alert details
            alert_details_layout = QVBoxLayout()

            # Alert title and timestamp/source
            title_layout = QHBoxLayout()
            alert_title = QLabel(title)
            alert_title.setFont(QFont("Arial", 14, QFont.Bold))
            timestamp_label = QLabel(f"© {timestamp} • {source}")
            timestamp_label.setFont(QFont("Arial", 10))
            timestamp_label.setStyleSheet("color: gray;")
            title_layout.addWidget(alert_title)
            title_layout.addWidget(timestamp_label)
            title_layout.addStretch()

            # Alert description
            alert_description = QLabel(description)
            alert_description.setFont(QFont("Arial", 12))
            alert_description.setStyleSheet("color: #333;")
            alert_description.setWordWrap(True)  # Allow text wrapping

            # Status
            status_label = QLabel("⚠ Active")
            status_label.setFont(QFont("Arial", 10))
            status_label.setStyleSheet("color: #FFA940;")

            alert_details_layout.addLayout(title_layout)
            alert_details_layout.addWidget(status_label)
            alert_details_layout.addWidget(alert_description)

            # Severity and buttons
            buttons_layout = QVBoxLayout()
            severity_btn = QPushButton(severity)
            severity_btn.setStyleSheet(f"background-color: {color}; color: white; border-radius: 10px; padding: 5px; max-width: 100px; font-size: 12px;")
            resolve_btn = QPushButton("Resolve")
            resolve_btn.setStyleSheet("background-color: #4682B4; color: white; border-radius: 5px; padding: 5px; max-width: 100px; font-size: 12px;")
            dismiss_btn = QPushButton("Dismiss")
            dismiss_btn.setStyleSheet("background-color: transparent; color: gray; border: 1px solid gray; border-radius: 5px; padding: 5px; max-width: 100px; font-size: 12px;")
            details_btn = QPushButton("Details")
            details_btn.setStyleSheet("background-color: transparent; color: gray; border: 1px solid gray; border-radius: 5px; padding: 5px; max-width: 100px; font-size: 12px;")
            buttons_layout.addWidget(severity_btn)
            buttons_layout.addSpacing(10)
            buttons_layout.addWidget(resolve_btn)
            buttons_layout.addWidget(dismiss_btn)
            buttons_layout.addWidget(details_btn)

            alert_layout.addLayout(alert_details_layout)
            alert_layout.addStretch()
            alert_layout.addLayout(buttons_layout)

            content_layout.addWidget(alert_widget)
            content_layout.addSpacing(15)  # Add spacing between alerts

        content_layout.addStretch()

        # Add sidebar and content to main layout
        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PhylaxAlertsWindow()
    window.show()
    sys.exit(app.exec_())