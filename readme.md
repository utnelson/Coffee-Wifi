# Flask Project to track ratings for cafe's

## How to start
Install requirements from "requirements.txt"
```
$ pip install -r requirements.txt
```
Start Flask Server
```
$ flask --app main run
 * Serving Flask app 'main'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 ```
## Screenshot
![image](2024-01-01%2000_45_07-Coffee%20and%20Wifi.png)
![image](2024-01-01%2000_46_41-Restaurants.png)

## Explanation
- Shows all data rows from the csv file in the bootstrap table
- with route /add you can add new cafe's and it will be stored in the csv

## Why I made this
My main goal was to practice the following Python concepts:
- Using libraries Flask, WTForms, Flask Bootstrap
- Template Inheritance
- Routing
- POST & GET methods

## License
MIT License

Copyright (c) 2003 utnelson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.