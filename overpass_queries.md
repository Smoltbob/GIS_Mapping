# All the shelters and huts in Sweden
```
[out:json];
(
area["ISO3166-1"="SE"][admin_level=2]->.sweden;
(
  node["shelter_type"="lean_to"](area.sweden);
  way["shelter_type"="lean_to"](area.sweden);
  relation["shelter_type"="lean_to"](area.sweden);
);
area["ISO3166-1"="SE"][admin_level=2]->.sweden;
(
  node["tourism"="wilderness_hut"](area.sweden);
  way["tourism"="wilderness_hut"](area.sweden);
  relation["tourism"="wilderness_hut"](area.sweden);
);
);
(._;>;);
out center;
```

# All the viewpoints in Sweden
```
[out:json];
area["ISO3166-1"="SE"][admin_level=2]->.sweden;
(
  node["tourism"="viewpoint"](area.sweden);
  way["tourism"="viewpoint"](area.sweden);
  relation["tourism"="viewpoint"](area.sweden);
);
out center;
```

# Bus stops
## In Sweden
```
[out:json];
area["ISO3166-1"="SE"][admin_level=2]->.sweden;
(
  node["highway"="bus_stop"](area.sweden);
  way["highway"="bus_stop"](area.sweden);
  relation["highway"="bus_stop"](area.sweden);
);
out center;
```

## In Skåne
```
[out:json];
area[name="Skåne län"]->.skane;
(
  node["highway"="bus_stop"](area.skane);
  way["highway"="bus_stop"](area.skane);
);
out center;
```

# Picninc sites
```
[out:json];
area["ISO3166-1"="SE"][admin_level=2]->.sweden;
(
  node["tourism"="picnic_site"](area.sweden);
  way["tourism"="picninc_site"](area.sweden);
  relation["tourism"="picnic_site"](area.sweden);
);
out center;
```

# Drinking water
```
[out:json];
area["ISO3166-1"="SE"][admin_level=2]->.sweden;
(
  node["amenity"="drinking_water"](area.sweden);
  way["amenity"="drinking_water"](area.sweden);
  relation["amenity"="drinking_water"](area.sweden);
);
out center;
```

# Ferry routes in Sweden
```
[out:json][timeout:25];
area["ISO3166-1"="SE"][admin_level=2]->.sweden;
(
  node["route"="ferry"](area.sweden);
  way["route"="ferry"](area.sweden);
  relation["route"="ferry"](area.sweden);
);
out body;
>;
out skel qt;
```