# Site about the most interesting places in Moscow. 

![Alt text](./screen.png?raw=true "Screen example")

The code is written for educational purposes - this is a lesson in the Python and web development course on the site [Devman Django course](https://dvmn.org/modules/django/).  

All requirements are listed in the file: `requirements.txt`.

Link on website: https://amatoravg.pythonanywhere.com/.

Link on admin site: https://amatoravg.pythonanywhere.com/admin/.

### For testing:
login: admin.

password: devmanwhere1.

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

### Loading data from json

For loading data use command load_place:

```shell script
python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json
```
For loading data from several files, links must be separated by a space.

## Libraries used

* [Leaflet](https://leafletjs.com/) — map rendering
* [loglevel](https://www.npmjs.com/package/loglevel) — for logging
* [Bootstrap](https://getbootstrap.com/) — CSS library
* [Vue.js](https://ru.vuejs.org/) — reactive templates on the frontend

Test data taken from the site [Kudago](https://kudago.com/).



