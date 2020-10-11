## What is VIRUS_CHECKER ?

* **It is an open source script which written with python.**

* **The script depend on and use www.virustotal.com.**

* **The script communicate with virustotal with it's public API.**


## But wait What is virustotal ?

* **VirusTotal is a website created by the Spanish security company Hispasec Sistemas.**
* **VirusTotal aggregates many antivirus products and online scan engines to check for viruses that the user's own antivirus may have missed, or to verify against any false positives.**
* **Files up to 550 MB can be uploaded to the website, or sent via email (max. 32MB).**
* **Anti-virus software vendors can receive copies of files that were flagged by other scans but passed by their own engine, to help improve their software and, by extension, VirusTotal's own capability.**
* **Users can also scan suspect URLs and search through the VirusTotal dataset.**
* **VirusTotal for dynamic analysis of malware uses the Cuckoo sandbox.**

## How does Virus Scan work?
 
* **it works in a very traditional way, it uses a database called a virus dictionary like(virustotal database) which has lots of codes from different known viruses.**
* **When virus scanner scan a file, it will take a snippet of that code and compare it with the codes in their virustotal database, if the files match then the virus attack on a computer is confirmed.**
* **In simple words, the entire scan and detection process relies on the repository (virus dictionary/signature) of known viruses.**
* **A robust virus scanner is more capable of tracking down Viruses, Worms, Trojans, Spyware and Malware software often circulated by Cyber criminals for their personal gains.**
* **When an intruder is identified to exist in the system files, the virus scanner secures the computer by blocking all activities of the virus.**

## What is API?

 * **An application-programming interface (API) is a set of programming instructions and standards for accessing a Web-based software application or Web tool.**
* **A software company releases its API to the public so that other software developers can design products that are powered by its service.**

## VIRUSTOTAL Public API :-

* **VirusTotal provides as a free service a public API that allows for automation of some of its online features**
* **such as "upload and scan files, submit and scan URLs, access finished scan reports and make automatic comments on URLs and samples".**
* **Some restrictions apply for requests made through the public API, such as requiring an individual API key freely obtained by online signing up, low priority scan queue, limited number of requests per time frame, etc.**

## How does VIRUS_CHECKER work?

**When You start the script**
* **it call the file Shape.py and print VIRUS_CHECKER with stars you will see it in the following lines**
* **it ask you for input URL OR Domain OR IP OR File Hash.**
* **Pass the input into Cheak.py to know if it is (URL OR Domain OR IP OR File Hash).**
* **And submit the input to virustotal.com for analysis using their API.**
* **And returns the result as the input type (to make sure that it search about right thing.) and either Malicious or Clean.**
* **A single detection qualifies for being marked as malicious.**

## Installation :-

**First of all make sure to download the latest version of VIRUS_CHECKER using the following command :**

git clone https://github.com/ElmasreyKhaled/VIRUS_CHECKER.git

### Requirements :-

**You can install all of VIRUS_CHECKER requirements via :**

pip install -r requirements.txt

### Start

**You can start using VIRUS_CHECKER by running**

.\VIRUS_CHECKER.py

**script starts with**


![View](https://user-images.githubusercontent.com/71513744/95667002-3c37fc00-0b60-11eb-8dd5-8d7b3da102cb.jpg)


**The output You get talks about two things**
* **The Type of the input**
* **The result if it (Clean or malicious)**


![View1](https://user-images.githubusercontent.com/71513744/95667064-e9127900-0b60-11eb-8657-ce4c3e78f78e.jpg)


## Usage :-

**after starting the script you just need to write**


**1- URL**

**ex: 'https://www.google.com'**


![usage1](https://user-images.githubusercontent.com/71513744/95667072-ffb8d000-0b60-11eb-8bea-7c37060bf508.jpg)


**2-Domain**

* **ex: 'www.google.com'**

![usage2](https://user-images.githubusercontent.com/71513744/95667097-7d7cdb80-0b61-11eb-9912-3461d7845d88.jpg)


* **OR ex: 'google.com'**


![usage21](https://user-images.githubusercontent.com/71513744/95667102-95545f80-0b61-11eb-9a32-547d81971a93.jpg)



**3-File Hash**

**ex: '36F9CA40B3CE96FCEE1CF1D4A7222935536FD25B'**


![usage3](https://user-images.githubusercontent.com/71513744/95667108-ae5d1080-0b61-11eb-8a0e-983ff1eaf7c0.jpg)



**4-IP**

**ex: '172.217.17.110'**


![usage4](https://user-images.githubusercontent.com/71513744/95667110-c03eb380-0b61-11eb-82ff-e2ecacff6c01.jpg)


## End_Words :-

*I hope oneday i will back to improve this script as a result for the progress I achieved and things I learned.*
