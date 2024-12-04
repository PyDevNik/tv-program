TV-Program

Overview

TV-Program is a Python-based application designed to fetch, parse, and store TV program data from a remote XML source. The project automates the process of retrieving program schedules, mapping them to structured objects, and storing them in a MongoDB database for further use.

Features

Fetch Data: Downloads compressed XML files from a specified URL.

Decompress and Parse: Extracts and parses TV program data using gzip and BeautifulSoup.

Data Mapping: Converts XML data into structured Python objects based on predefined schemas (Channel, Program).

Database Storage: Uploads processed data into a MongoDB database.


File Structure

tv-program/
├── config.py             # Contains configuration values like XML_URL, DB_URL, DB_NAME, and COLLECTION_NAME.
├── schemas.py            # Defines the data structures for `Channel` and `Program`.
├── main.py               # Entry point of the application.
├── requirements.txt      # Lists all the Python dependencies.
└── README.md             # Project documentation.

Installation

1. Clone the repository:

git clone https://github.com/your-username/tv-program.git
cd tv-program


2. Install dependencies:

pip install -r requirements.txt


3. Configure the application:
Update the config.py file with the following values:

XML_URL: URL of the TV program XML file.

DB_URL: MongoDB connection string.

DB_NAME: Name of the MongoDB database.

COLLECTION_NAME: Name of the MongoDB collection.




Usage

1. Run the script to download, parse, and store data:

python main.py


2. The application will:

Download the XML file.

Parse and extract channel and program details.

Store the data in the specified MongoDB database.




Code Description

TVProgram Class

The main class responsible for the application's workflow:

install_xml()
Downloads the compressed XML file from the specified XML_URL.

load_xml()
Decompresses the downloaded file and loads its content as raw XML.

load_parser(xml)
Parses the XML using BeautifulSoup to prepare it for data extraction.

load_data()
Extracts Channel and Program details from the XML, maps them to Python objects, and organizes them by channel.

upload_to_db(channels)
Inserts the processed channel data into the MongoDB collection.


Dependencies

Python libraries:

requests

beautifulsoup4

pymongo


MongoDB (local or remote instance)


Example Configuration (config.py)

XML_URL = "https://example.com/tv-schedule.xml.gz"
DB_URL = "mongodb://localhost:27017"
DB_NAME = "tv_programs"
COLLECTION_NAME = "channels"

Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

Special thanks to the developers and contributors of the libraries used in this project.

