import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QPixmap

class PhylaxWindow(QMainWindow):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("PHYLAX - Security Logs")
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

        # Sidebar items with symbols
        sidebar_items = [
            ("🏠 Dashboard", "Dashboard"),
            ("📜 Logs", "Logs"),
            ("📊 Analytics", "Analytics"),
            ("🔔 Alerts", "Alerts"),
            ("⚙ Settings", "Settings"),
            ("❓ Help Center", "Help Center"),
            ("👤 Account", "Account"),
            ("🚪 Logout", "Logout")
        ]
        for symbol_text, item in sidebar_items:
            label = QLabel(symbol_text)
            label.setFont(QFont("Arial", 12))
            label.setStyleSheet("padding: 10px; color: white;" if item != "Logs" else "padding: 10px; color: #00C4B4; font-weight: bold;")
            sidebar_layout.addWidget(label)

        sidebar_layout.addStretch()

        # Main content area
        content = QWidget()
        content_layout = QVBoxLayout(content)

        # Header
        header_layout = QHBoxLayout()
        title = QLabel("Security Logs")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        subtitle = QLabel("View and manage detected threats")
        subtitle.setFont(QFont("Arial", 12))
        subtitle.setStyleSheet("color: gray;")

        # Search bar and user profile
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search logs...")
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

        # Table
        table = QTableWidget()
        table.setRowCount(8)
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["Timestamp", "Threat Name", "Source IP", "Severity", "Action"])
        
        # Table data
        data = [
            ("2025-06-16 14:32:51", "Trojan.Win32.Injector", "192.168.1.105", "High", "Blocked"),
            ("2025-06-16 13:27:15", "XSS Attempt", "203.45.123.9", "Medium", "Blocked"),
            ("2025-06-16 11:05:42", "Suspicious PowerShell Command", "LOCAL SYSTEM", "Medium", "Quarantined"),
            ("2025-06-16 10:18:33", "Ransomware.CryptoLocker", "172.16.0.57", "Critical", "Blocked"),
            ("2025-06-15 23:41:19", "Prompt Injection Attempt", "45.33.101.246", "High", "Blocked"),
            ("2025-06-15 21:15:33", "Suspicious Login Attempt", "91.234.56.78", "High", "Blocked"),
            ("2025-06-15 19:09:12", "Malicious URL Access", "LOCAL SYSTEM", "Medium", "Blocked"),
            ("2025-06-15 17:47:29", "Adware.Win32.Agent", "LOCAL SYSTEM", "Low", "Quarantined"),
        ]

        for row, (timestamp, threat, ip, severity, action) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(timestamp))
            table.setItem(row, 1, QTableWidgetItem(threat))
            table.setItem(row, 2, QTableWidgetItem(ip))
            
            # Severity button with reduced intensity colors
            severity_btn = QPushButton(severity)
            severity_color = {"High": "#FF7F7F", "Medium": "#FFC107", "Critical": "#FF7F7F", "Low": "#80D4FF"}
            severity_btn.setStyleSheet(f"background-color: {severity_color[severity]}; color: white; border-radius: 10px; padding: 5px;")
            table.setCellWidget(row, 3, severity_btn)

            # Action button with reduced intensity colors
            action_btn = QPushButton(action)
            action_color = {"Blocked": "#FF7F7F", "Quarantined": "#FFC107"}
            action_btn.setStyleSheet(f"background-color: {action_color[action]}; color: white; border-radius: 10px; padding: 5px;")
            table.setCellWidget(row, 4, action_btn)

        # Table styling
        table.setStyleSheet("QTableWidget { border: none; } QHeaderView::section { background-color: #f5f5f5; padding: 5px; }")
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setVisible(False)
        table.setShowGrid(False)
        table.setAlternatingRowColors(True)

        content_layout.addWidget(table)

        # Add sidebar and content to main layout
        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)

if _name_ == '_main_':
    app = QApplication(sys.argv)
    window = PhylaxWindow()
    window.show()
    sys.exit(app.exec_())
