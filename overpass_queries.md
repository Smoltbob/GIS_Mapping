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