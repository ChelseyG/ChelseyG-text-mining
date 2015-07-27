# text-mining

## Requirements
- Python 2.7.6
- [Tweepy](https://github.com/tweepy/tweepy)
- Your very own Twitter apps. Register one [here](https://apps.twitter.com).

_Note: please follow the installation instruction found on the official Tweepy repo before continuing_

## Installation
- ``` git clone https://github.com/anthonymonori/text-mining.git ./text-mining ```
- ``` cd ./text-mining ```
- ``` open _conf.ini ```
- ``` mv _conf.ini conf.ini ```

## Usage
``` python text-mining.py hashtag1 hashtag2 ... ```

## Use cases
- Data mining of tweets for Big Data analysis
- Parse the stream into a live-feed of tweets
- Any other ideas? Let me know

## Todo
- [ ] Add mongoDB integration using PyMongo driver

## License
Copyright (c) 2015, Antal János Monori
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
