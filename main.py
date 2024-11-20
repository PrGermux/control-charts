import sys
import os
import numpy as np
import pandas as pd
import mysql.connector
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QPen, QFont, QIcon
from PyQt5.QtChart import (
    QChart,
    QChartView,
    QLineSeries,
    QValueAxis,
    QCategoryAxis,
)

# Configuration: replace placeholders with actual values
DATABASE_CONFIG = {
    "host": "your_database_host",
    "database": "your_database_name",
    "user": "your_database_user",
    "password": "your_database_password",
}
EXCEL_FILE_PATH = r"path_to_your_excel_file.xlsx"
EXCEL_SHEET_NAME = "your_sheet_name"
EXCEL_COLUMNS = {"label": "x_Column", "value": "y_Column"}
REFRESH_INTERVAL_MS = 3600000  # Refresh every 1 hour

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class ControlChartsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control Charts")
        self.setGeometry(100, 100, 1600, 800)
        self.initUI()
        self.refresh_interval = REFRESH_INTERVAL_MS

        # Set up a QTimer to update the data periodically
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(self.refresh_interval)

        # Call update_data immediately to fetch data on startup
        self.update_data()

    def initUI(self):
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        row1_layout = QHBoxLayout()
        row2_layout = QHBoxLayout()

        # Create a 2x2 grid layout for 4 charts
        self.charts = [self.create_chart() for _ in range(4)]

        # Place charts in the layout
        row1_layout.addWidget(self.charts[0])  # First plot (top-left)
        row1_layout.addWidget(self.charts[1])  # Second plot (top-right)
        row2_layout.addWidget(self.charts[2])  # Third plot (bottom-left)
        row2_layout.addWidget(self.charts[3])  # Fourth plot (bottom-right)

        main_layout.addLayout(row1_layout)
        main_layout.addLayout(row2_layout)

        # Configure individual charts
        self.setup_first_chart()
        self.setup_second_chart()
        self.setup_third_chart()
        self.setup_fourth_chart()

    def create_chart(self):
        chart = QChart()
        chart.setBackgroundBrush(Qt.white)
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        return chart_view

    def setup_chart(self, chart, title, y_axis_range, y_axis_title, upper_limit=None, lower_limit=None):
        chart.setTitle(title)
        title_font = chart.titleFont()
        title_font.setBold(True)
        chart.setTitleFont(title_font)

        # Add upper and lower limits if specified
        if upper_limit is not None and lower_limit is not None:
            upper_line = QLineSeries()
            lower_line = QLineSeries()
            upper_line.setPen(QPen(Qt.red, 2, Qt.DashLine))
            lower_line.setPen(QPen(Qt.red, 2, Qt.DashLine))
            for i in range(10):  # Example for 10 data points
                upper_line.append(i, upper_limit)
                lower_line.append(i, lower_limit)
            chart.addSeries(lower_line)
            chart.addSeries(upper_line)

        # Configure Y-axis
        y_axis = QValueAxis()
        y_axis.setRange(*y_axis_range)
        y_axis.setTitleText(y_axis_title)
        chart.addAxis(y_axis, Qt.AlignLeft)

        # Configure X-axis
        x_axis = QCategoryAxis()
        x_axis.setTitleText("x Axis Title")
        x_axis.setLabelsPosition(QCategoryAxis.AxisLabelsPositionOnValue)
        chart.addAxis(x_axis, Qt.AlignBottom)

        return y_axis, x_axis

    def setup_first_chart(self):
        # Example: "Temperature BHZ"
        chart = self.charts[0].chart()
        self.y_axis_bhz, self.x_axis_bhz = self.setup_chart(
            chart, title="Title", y_axis_range=(950, 1010),
            y_axis_title="y Axis Title", upper_limit=995, lower_limit=965
        )
        self.bhz_series = QLineSeries()
        chart.addSeries(self.bhz_series)
        self.bhz_series.attachAxis(self.y_axis_bhz)
        self.bhz_series.attachAxis(self.x_axis_bhz)

    def setup_second_chart(self):
        # Example: "Temperature VHZ"
        chart = self.charts[1].chart()
        self.y_axis_vhz, self.x_axis_vhz = self.setup_chart(
            chart, title="Temperature VHZ", y_axis_range=(565, 635),
            y_axis_title="Temperature [°C]", upper_limit=620, lower_limit=580
        )
        self.vhz_series = QLineSeries()
        chart.addSeries(self.vhz_series)
        self.vhz_series.attachAxis(self.y_axis_vhz)
        self.vhz_series.attachAxis(self.x_axis_vhz)

    def setup_third_chart(self):
        # Example: "Average Ic"
        chart = self.charts[2].chart()
        self.y_axis_ic, self.x_axis_ic = self.setup_chart(
            chart, title="Title", y_axis_range=(300, 700),
            y_axis_title="y Axis Title"
        )
        self.ic_series = QLineSeries()
        chart.addSeries(self.ic_series)
        self.ic_series.attachAxis(self.y_axis_ic)
        self.ic_series.attachAxis(self.x_axis_ic)

    def setup_fourth_chart(self):
        # Example: "Pressure"
        chart = self.charts[3].chart()
        self.y_axis_p, self.x_axis_p = self.setup_chart(
            chart, title="Title", y_axis_range=(5, 7),
            y_axis_title="y Axis Title", upper_limit=6.5, lower_limit=5.5
        )
        self.pressure_series = QLineSeries()
        chart.addSeries(self.pressure_series)
        self.pressure_series.attachAxis(self.y_axis_p)
        self.pressure_series.attachAxis(self.x_axis_p)

    def fetch_data(self):
        # Placeholder for database fetching logic
        pass

    def update_data(self):
        # Placeholder for update logic
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ControlChartsApp()
    window.showMaximized()
    sys.exit(app.exec_())
