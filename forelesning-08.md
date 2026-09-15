### Avrunding
**TPM er ikke bra for OSS operativsystemer eks. Linux.**

# Sending av data: Nettverk

Utveksling av meldinger mellom A og B i løpet at tiden `t`

## Over lang

* Røyk, tromme, duer, bål, ...
* 1790: "Semaphores"
* Fra 1800-tallet: elektriske systermer
* Telegraf, 1837: morse, 1851: 30 000 km lange kabler i USA
* 1. Transatlanterkabel 1866
* Telefon 1878/1879
* Radiotelegraf 1894

## Circuit switching
* Analoge telefonsignaler brukte **_circuit switching_**
* Garantert lenke fra A til B
* Bytte fysisk kontakt for å snakke med flere enn én person
* Men kan kun snakke med en person om gangen, gjelder både mottagende og ringende side

## Digitale signaler
* digitale signaler kan deles opp
* **Packet switching - 1960-tallet**
* Store and forward

## Packet switched network

PC A -> Packets -> Router -> Packet -> ISP A -> ISP B -> PC B

Hvis en annen ruter er opptatt av en annen PC, sendes den gjennom den andre.

Packetene kommer i ulik rekkefølge til mottakeren, så de markeres med posisjon for å plassere dem tilbake i rett rekkefølge

* Packet-switching - tidlig 1960-tallet
* APRAnet 1969: 4 nodes, 1972: 15 nodes
* første epost 1972
* Mange uavhengige nettverksløsninger i 1970-tallet, krever felles utvekslingsprotokoll
* TCP/UDP/IP på plass i slutten av 1970-tallet
* Felles bytte til TCP/IP: 1983-01-01
* Slutten av 1980-tallet: 100 000 nodes, f.eks. NSFNET kobling blant US-universiteter
* 1991: kommersiell bruk av NSFNET tillat
* 1989-1991: utvikling av WWW (HTML/HTTP/server/browser) hos CERN
* fra 1995: tilgang til WWW er standard for studenter
* 1995-2001: økonomisk boble

## 5-layer modle

* Application: **HTTP**, SMTP, FTP, SSH, DNS, lett å lage nye protokoller her, end system <-> endsystem
* Transport: **TCP** (connection) eller **UDP** (connectionless) sender "segments" fra end system <-> end system
* Network: **IP** (ingen andre valg på Internet) sender "datagrams / packets" mellom end systems fra én router til den neste
* Link: Ethernet, Wi-Fi, PPP, sender "frames" fra én enhet til den neste
* Physical: elektriske signaler, radiosignaler, ..., sende bits fra én enhet til den neste

Brukes også: OSI-modell - 7 layers

* Application: innhold, filnanv, domenanavn
* Transport: TCP/UDP-ports
* Network: IP-adresse
* Link: MAC-adresse
* Physical

Eks:
 
Hello

Source 
Application -> transport -> network -> link -> physical -> **Switch** -> physical -> ... link ... -> physical -> **Router** -> physical -> link -> network -> link -> physical -> Destination -> physical -> link -> network -> transport -> application.



