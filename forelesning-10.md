# HTTP

## 5-layer model
* **Application**: **HTTP,** SMTP, FTP, SSH, DNS
* etc.

## HTTP:
* Ideen: mars 1989
* CERN: Tim Berners-Lee
* [First website](https://info.cern.ch/hypertext/WWW/TheProject.html) 

* HyperMedia Browser og Editor (alt i et)
* HyperText Markup Language (HTML)

Tidlig beskrivelse av HTTP

## Client:
* Grafisk web browser: Firefox, Vivaldi, Safari, ...
* Tekstbasert browser: w3m, lynx, ...
* Kommandolinje-verktøy: curl, wcurl, wget
* 

## Server:
* mange ulike implementasjoner, tilpasset formål
* store, fleksible: nginx, apache, ...
* lette: lighttpd, ...
* Biblioteker til bruk i programmer:
    * Python `http.server`

## en URL - uniform resource locator
* http://
* www.inf105.org
* /lab4/index.html

Protokoll:

* http
* https
* ftp
* gopher

Server:
* Domenenavn
* ip-adresse
* host:port

`http://*********:8000/`

Port
* http: bruker port 80 som standard
* https: 443

Ressurs:
* mappe-sti til en fil
* serveren ofte tolker den internt:
    * rewrites
    * navn til et generert ressurs (dynamiske nettsider)

På Linux-serveren:
* `/var/www/html/{fil}`

### Server
Client: local port 12345 connected
Server: Connected on 158.39.201.59 port 80

```python
print("Hello, world!")
```

* `GET /fil.txt HTTP/1.1`

### Status codes
* Informational responses (100 - 199)
* Successful responses (200 - 299)
    * 200 OK
* Redirection responses (300 - 399)
    * 301 Moved Permanently
    * 302 Found \[temporary redirect\]
* Client-side responses (400 - 499)
    * 404 Not Found
    * 403 Forbidden
    * 451 Unavailable for legal reasons (Ray Bradbury, "Fahrenheit 451")
* Server-side responses (500 - 599)
    * 500 Internal Server Error \[ofte: feil med generering av dynamisk innhold\]




