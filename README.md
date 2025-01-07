# Control Charts

**Control Charts** is a Python-based GUI application designed for visualizing and monitoring control chart data in real-time. It leverages PyQt5 for an interactive and user-friendly interface, allowing users to dynamically explore data trends, calculate averages, and view control limits for various parameters. This tool is customizable and can be connected to databases and files for flexible data sourcing.

#### Key Features:
- **Dynamic Charts**: Displays up to four control charts in a 2x2 grid layout, each customizable with unique data sources and control limits.
- **Real-Time Data Updates**: Automatically refreshes data at configurable intervals to ensure up-to-date monitoring.
- **Interactive Visualization**: Allows users to zoom, pan, and inspect data points on each chart.
- **Database Integration**: Connects to a MySQL database to fetch data dynamically.
- **Excel Support**: Reads additional data, such as Ic values, from an Excel file for advanced visualization.
- **Customizable Control Limits**: Displays upper and lower control limits for each chart with clearly labeled thresholds.
- **Built-in Configurations**: Flexible configuration for database credentials, file paths, and chart settings.

#### Usage
This tool is ideal for:
- Engineers and quality control teams monitoring process parameters.
- Researchers analyzing trends in experimental data.
- Professionals needing a visual interface for control charts.

#### Python Branch and Complexity
- **Python Branch**: Built using PyQt5 for GUI, `mysql.connector` for database connectivity, and `pandas` for handling Excel data.
- **Complexity**: Manages live database queries, dynamic chart rendering, and interactive GUI features, making it moderately complex.

#### Code Structure
- **Main Interface**: Displays four interactive control charts in a 2x2 layout.
- **Data Sources**: Retrieves data from a MySQL database and Excel files.
- **Control Limits**: Visualizes upper and lower control limits on each chart.
- **Customization**: Configurable settings for chart titles, data ranges, and control limits.

#### Screenshots:

![grafik](https://github.com/user-attachments/assets/0943f627-a0d4-4050-8f66-7adfd616c22b)

#### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/control-charts.git
   cd control-charts
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

#### Usage
Run the main application:
```sh
python main.py
```

#### Freezing
To package the application as a standalone executable:
```sh
pyinstaller --onefile --windowed --icon=icon.png --add-data "icon.png;." --name "Control Charts" main.py
```

#### Dependencies
- Python 3.x
- PyQt5
- pandas
- mysql-connector-python

#### Future Enhancements
- **Dynamic Control Limits**: Allow users to configure control limits directly from the GUI.
- **Additional Chart Types**: Add support for scatter plots or bar charts.
- **Data Export**: Provide options to export chart data and visuals.
- **Notifications**: Include alert systems for threshold breaches.

#### License
This project is licensed under the MIT License for non-commercial use.
