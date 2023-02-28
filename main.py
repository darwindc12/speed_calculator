from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QComboBox, QPushButton
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Average Speed Calculator')
        grid = QGridLayout()

        # Create Widgets
        distance_label = QLabel("Distance: ")
        distance_line_edit = QLineEdit()

        time_label = QLabel("Time(hours): ")
        time_line_edit = QLineEdit()

        combo = QComboBox()
        combo.addItems(['Metric (km)', 'Imperial (miles)'])

        calculate_button = QPushButton('Calculate')
        output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(distance_line_edit, 0, 1)
        grid.addWidget(combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1, 1, 1)
        grid.addWidget(output_label, 3, 0, 1, 2)

        self.setLayout(grid)


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())