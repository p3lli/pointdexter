# Pointdexter #
This is a really simple API Rest service which calculates equally distribuited grids  
of points, given the top left point (`Latitude` and `Longitude`), a `Distance` in km,  
the number of points in a row (`Width`) and the number of points in a column (`Height`).  

Every subsequent couple of points in the same row have distance `2*Distance`, while  
every subsequent couple of points in the same (zig-zag) column have distance `sqrt(2)*Distance`.  

## Endpoints
```
GET /pointdexter/api/v1/points/<Latitude>/<Longitude>/scatter/<Distance>/<Width>/<Height>
```

Example: /pointdexter/api/v1/points/41.905561/12.482357/scatter/0.5/2/2  


## Setting Up
Locally:  
```
virtualenv env-grid
source env-grid/bin/activate
pip install -r requirements.txt
python app.py
```
Docker Container:
```
./build.sh
docker run -p 127.0.0.1:2817:5000 CONTAINER_ID
```

_work in progress..._
