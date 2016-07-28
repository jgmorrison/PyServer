PyServer
========

Pyserver is an example of a web server using the Python3 Socket module. It has been set up with logging to log connections and GET requests to the server.log file. For easier extension PyServer has also been setup with configparser to easily change things such as the BIND_IP, BIND_PORT, and the DEFAULT_HTML files in the conf.ini file.

**Usage:**

To start the server simply run the server.py file:

``python server.py``

Now you can navigate to the local URL in your browser:

``http://localhost:8080``
