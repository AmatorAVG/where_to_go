# Site about the most interesting places in Moscow. 

![&#x41A;&#x443;&#x434;&#x430; &#x43F;&#x43E;&#x439;&#x442;&#x438;](.gitbook/assets/site.png)

The code is written for educational purposes - this is a lesson in the Python and web development course on the site [Devman Django course](https://dvmn.org/modules/django/).  

All requirements are listed in the file: `requirements.txt`.

Link on website: https://wtg.pythonanywhere.com/.

Link on admin site: https://wtg.pythonanywhere.com/admin/.

### For testing:
login: amator.

password: 123.

### Installing project

Install python.

Create virtual environment: 
```shell script
python -m venv env
```
Activate the virtual environment:
```shell script
source env/scripts/activate
```
Install requirements:
```shell script
pip install -r requirements.txt
```
Run the project:
```shell script
./manage.py runserver
```
Open in browser: http://localhost:8000.

## Libraries used

* [Leaflet](https://leafletjs.com/) — map rendering
* [loglevel](https://www.npmjs.com/package/loglevel) — for logging
* [Bootstrap](https://getbootstrap.com/) — CSS library
* [Vue.js](https://ru.vuejs.org/) — reactive templates on the frontend

Test data taken from the site [Kudago](https://kudago.com/).



