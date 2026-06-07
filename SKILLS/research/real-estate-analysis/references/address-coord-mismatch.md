# Address/Coordinate Mismatch Detection

When analyzing real property listings, verify the listing address matches the GPS coordinates. Agents frequently use incorrect coordinates or describe land that doesn't exist at the listed location.

## Method

```bash
lat=49.340458 lon=-122.943608
curl "https://nominatim.openstreetmap.org/reverse?format=json&lat=$lat&lon=$lon&zoom=18&addressdetails=1" \
  -H 'User-Agent: real-estate-investor@email.com'
```

## Decision Rules

Check the `address` object in the geocode response:

### STOP — Walk Away
| Condition | Action |
|---|---|
| addresstype = path, footway, trail | DO NOT BUY |
| suburb != listed suburb | DO NOT BUY |
| town != listed town/muni | DO NOT BUY |
| Place is a park, trail, or undeveloped | DO NOT BUY |

### INVESTIGATE FIRST
| Condition | What to check |
|---|---|
| addresstype = road but minor/unknown road | Search municipal road registry |
| Place is District of not City of | Could be unincorporated - no services |
| Postal code starts with V7G/V7H but address says different area | Strata land-share territory |

## Common Deception Patterns

1. Trail instead of road - Coordinates point to Three Chop Trail but listing says Indian River Drive
2. Suburb mixing - Land in one municipality described as being in a prestige neighbourhood
3. Street name similarity - Indian River Drive vs Indian River Road vs Indian River Trail
4. Centroid coordinates - Agent uses the centroid of the area, not the actual lot
5. Land share or strata plot - Coordinates show a recreational/path area that cant be independently owned

## Sources

- Created 2026-06-04 from live analysis of Realtor.ca listing R2950139 (Lot 2 Indian River Drive, North Vancouver)
- The coords 49.340458 -122.943608 pointed to Three Chop Trail in Deep Cove
- Deep Cove is in the Sea-to-Sky corridor, heavily provincial park-constrained