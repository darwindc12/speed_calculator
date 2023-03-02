from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QComboBox, QPushButton
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Average Speed Calculator')
        grid = QGridLayout()

        # Create Widgets
        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time(hours): ")
        self.time_line_edit = QLineEdit()

        self.combo = QComboBox()
        self.combo.addItems(['Metric (km)', 'Imperial (miles)'])

        calculate_button = QPushButton('Calculate')
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):

        if self.combo.currentText() == "Metric (km)":
            distance_km = float(self.distance_line_edit.text()) * 1.60934
            km_per_hour = distance_km / float(self.time_line_edit.text())
            self.output_label.setText(f"Average Speed km/h")

        if self.combo.currentText()() == "Imperial (miles)":
            distance_km = float(self.distance_line_edit.text()) * 0.621371
            miles_per_hour = distance_km / float(self.time_line_edit.text())

        self.output_label.setText(f"Average Speed {miles_per_hour} mph")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())