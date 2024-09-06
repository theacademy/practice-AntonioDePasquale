import http.server
import json
import mysql.connector
from urllib.parse import urlparse

# Database Config
db_config = {
    'user': 'root',
    'password': 'Ascalon357673!',
    'host': 'localhost', #127.0.0.1
    'database': 'contactList2'

}

class ContactList:
    def __init__(self):
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor(dictionary = True)

    def createContact(self, fullName, phone, email):
        query = "insert into contacts (fullName, phone, email) values (%s, %s, %s)"
        self.cursor.execute(query, (fullName, phone, email))
        self.conn.commit()
        return {"id": self.cursor.lastrowid, "fullName": fullName, "phone": phone, "email": email}
    
    def readContacts(self):
        self.cursor.execute("Select * from contacts")
        return self.cursor.fetchall()
    
    def getContactsById(self, contactId):
        query = "select * from contacts where id = %s"
        self.cursor.execute(query, (contactId,))
        return self.cursor.fetchone()
    
    def updateContact(self, contactId, newPhone=None, newEmail=None ):
        query = "update contacts set phone = %s, email = %s where id = %s"
        self.cursor.execute(query, (newPhone, newEmail, contactId))
        self.conn.commit()
        return self.cursor.rowcount > 0 #acts as a boolean
    
    def deleteContact(self, contactId):
        query = "delete from contacts where id = %s"
        self.cursor.execute(query, (contactId,))
        self.conn.commit()
        return self.cursor.rowcount > 0 #acts as a boolean
    
contactList = ContactList()

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsedPath = urlparse(self.path)
        pathParts = parsedPath.path.split("/")

        if len(pathParts) == 2 and pathParts[1] == "contacts":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(contactList.readContacts()).encode())

        elif len(pathParts) == 3 and pathParts[1] == "contacts":
            contactId = pathParts[2]
            contact = contactList.getContactsById(contactId)
            if contact:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(contact).encode())
            else:
                self.send_response(404)
                self.end_headers()

        else:
                self.send_response(404)
                self.end_headers()


    def do_POST(self):
        if self.path == "/contacts":
            contentLength = int(self.headers["Content-length"])
            postData = self.rfile.read(contentLength)
            data = json.loads(postData)
            newContact = contactList.createContact(data["fullName"], data["phone"], data["email"])
            self.send_response(201)
            self.end_headers()
            self.wfile.write(json.dumps(newContact).encode())

    def do_PUT(self):
        parsedPath = urlparse(self.path)
        pathParts = parsedPath.path.split("/")

        if len(pathParts) == 3 and pathParts[1] == "contacts":
            contactId = pathParts[2]
            contentLength = int(self.headers["Content-length"])
            putData = self.rfile.read(contentLength)
            data = json.loads(putData)
            updated = contactList.updateContact(contactId, data.get("phone"), data.get("email"))

            if updated:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"message": "Content updated successfully"}).encode())
            else:
                self.send_response(404)
                self.end_headers()
        
        else:
                self.send_response(404)
                self.end_headers()

    def do_DELETE(self):
        parsedPath = urlparse(self.path)
        pathParts = parsedPath.path.split("/")

        if len(pathParts) == 3 and pathParts[1] == "contacts":
            contactId = pathParts[2]

            if contactList.deleteContact(contactId):
                self.send_response(200)
                self.end_headers()
            else:
                self.send_response(404)
                self.end_headers()

        else:
                self.send_response(404)
                self.end_headers()
    
def run(serverClass=http.server.HTTPServer, handlerClass=RequestHandler, port=8080):
    serverAddress = ('', port)
    httpd = serverClass(serverAddress, handlerClass)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()