---
name: real-estate-analysis
description: Analyze real estate listings, assess investment viability, and identify red flags for real property in Canada (primarily BC).
tags: [property, realtor.ca, investment, due-diligence, bca, real-estate]
---

# Real Estate Analysis

Analyze property listings, assess investment viability, and identify red flags for residential/commercial real estate in Canada (primarily BC).

## Workflow

When given a listing URL or screenshot to evaluate:

1. **Extract listing data** — get price, lot size, zoning, time on market, agent details
2. **Verify geography** — cross-reference listing description with actual coordinates (reverse geocode)
3. **Assess buildability** — zoning doesn't equal buildable; check access, services, slope, environmental constraints
4. **Run red flag check** — see "Red Flag Checklist" below
5. **Synthesize recommendation** — give a clear go/stop assessment

## Data Extraction from REALTOR.ca

The REALTOR.ca listing page embeds structured data in `window.dataLayer` within the HTML source. Extract via:

```bash
curl -s -L -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' 'https://realtor.ca/real-estate/<ID>/<slug>' -o listing.html
```

Then extract the `ListingModel` constructor (multi-line JS, do NOT use grep -oP):
```bash
python3 -c "
import re
with open('listing.html') as f: html = f.read()
m = re.search(r\"ListingModel\((.*?)\);\", html, re.DOTALL)
if m: print(m.group(1))
"
```

The `ListingModel` constructor has 10 positional args:
```
ListingModel(propertyID, marketID, listingID, individualID, latitude, longitude, provinceCode, communityID, price, communityName)
```

Also extract the `property:` dataLayer object for additional fields:
```bash
python3 -c "
import re, json
with open('listing.html') as f: html = f.read()
prop = re.search(r'property:\s*\{(.*?)\}', html, re.DOTALL)
if prop:
    d = {}
    for line in prop.group(1).split('\n'):
        line = line.strip()
        if ':' in line:
            k, v = line.split(':', 1)
            v = v.strip().rstrip(',').strip('\" \\')
            if v and not v.startswith('//'): d[k.strip()] = v
    print(json.dumps(d, indent=2))
"
```

Key fields to pull:
- `propertyID` / `listingID` / `listingType`
- `propertyType` (Vacant Land, Residential, etc.)
- `price`
- `landSize` (in sqft or acres)
- `zoningType` (RS-1, C-2, etc.)
- `landType`
- Agent and brokerage details

For deeper MLS data, the `listingID` (e.g., R2950139) maps to:
- https://www.realtor.ca/real-estate/<propertyID>/<listingID>

**Note:** The realtor.ca API (`api.realtor.ca`) is often blocked or requires auth — rely on HTML scraping instead.

## Verify Geography — STOP HERE IF MISMATCH

**Hard stop rule:** If the address listed on the page does NOT geocode to within ±100m of that address (or if the geocoded road/route is a trail, park feature, or recreational path), do NOT proceed to any other analysis. STOP and report: "Listing address and GPS coordinates do not match — likely fraudulent, misleading, or a strata land share. No further analysis warranted."

Common mismatch patterns (from live listings):
- Listed on "Indian River Drive" but coords point to "Three Chop Trail" (hiking path in Deep Cove)
- Listed as "North Vancouver" but coords geocode to Squamish / Sea-to-Sky corridor
- Listed as "Pacific Heights" but coords point to a provincial park boundary
- Street name looks real but is actually a minor alley or trail

Agent trick: use the reverse geocode response's `address.addresstype` field:
- If `addresstype` = "path" or "footway" or "trail" → **DO NOT BUY**
- If the geocoded suburb differs from the listed suburb → **DO NOT BUY**
- If the geocoded place is a park, trail, or undeveloped area → **DO NOT BUY**

Use:
```bash
curl 'https://nominatim.openstreetmap.org/reverse?format=json&lat=<LAT>&lon=<LON>&zoom=18&addressdetails=1' \
  -H 'User-Agent: real-estate-investor@email.com'
```

## Red Flag Checklist (STOP flags at top, dealbreakers below)

### Stop flags — do NOT buy
| Flag | What it means |
|------|------|
| **Address ≠ coordinates location** | The lot may not be where you think it is — STRONG STOP signal |
| **Coords geocode to a trail/park/path** | Land with no legal road access; likely a land-share or strata plot |
| **Tax amount = $0 or "not available"** | No taxable infrastructure, no utilities connected |
| **Zoning is blank or not listed** | Agent omitted it on purpose; investigate before proceeding |
| **Surrounded by CR/ES/SPRD zoning** | Environmental Sensitivity / Protected — development heavily restricted |

### Dealbreaker flags — investigate first
| Flag | What it means |
|------|------|
| Time on market > 90 days for land | Unusual — land sells faster than homes. Investigate why |
| "Walk to property" with no road access | Land you can't legally or physically reach |
| Surrounded by creeks/steep terrain | High slope/flood risk, especially in Deep Cove, West Vancouver, North Shore |
| Agent describes "wilderness" or "nature" | Probably not developable |
| Price seems too low for the area | There's a reason — usually access, zoning, or environmental |
| Vague description, few photos, no map | Probably a land share, strata lot, or problematic title |

## Zoning Translation

- **RS-1** = Single-family residential. Means houses are permitted, NOT that construction is approved.
- **RC-1/RC-2** = Rental/condo zoning. Multi-unit potential.
- **C-2/C-3** = Commercial with residential allowed.
- **OS/OP R** = Open Space / Environmental Reserve — DO NOT BUY. Protected green space.
- **ES/SPRD** = Environmental Sensitivity — heavy restrictions on any development.

## Recommendations

For land purchases:
1. Call the listing agent first — ask "why hasn't this sold?"
2. Check the municipality's zoning map online
3. Search BC Land Titles for encumbrances/easements
4. Walk the lot (if accessible) — check drainage, access, utilities
5. Contact the municipality's planning department for development requirements
6. Review environmental reports (slope stability, surface water)