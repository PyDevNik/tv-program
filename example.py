from xmltv import TVProgram

tv = TVProgram()

tv.install_xml()
xml = tv.load_xml()
tv.load_parser(xml[:1000])
data = tv.load_data()
tv.upload_to_db(data)