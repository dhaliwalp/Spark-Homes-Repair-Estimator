# Spark Homes Repair Estimator

This workspace contains a completed take-home assignment for the Spark Homes developer contest.

## Files
- `spark-homes-estimator.html` — main app
- `manifest.json` — PWA manifest
- `sw.js` — offline service worker
- `spark-logo.png` — app icon
- `pricing-list.csv` — reference price list
- `README.md` — this file
- `WRITEUP.md` — one-page project writeup draft

## How to run locally

### Option 1: Open directly
1. Open `spark-homes-estimator.html` in Chrome or Safari.
2. If you want reliable PWA installation and offline support, use a local server instead.

### Option 2: Run from a local static server
1. Open a terminal in this folder.
2. Run a simple server, for example:
   - `python -m http.server 8000`
3. Open `http://localhost:8000/spark-homes-estimator.html`

## Key features implemented
- Multi-project management with localStorage persistence
- Room-based bathroom instances and dynamic room renaming
- Search/filter repairs across categories and groups
- Project notes and budget target tracker
- Photo capture and thumbnail preview
- Export Excel + ZIP of estimate + photos
- Price CSV import and reset controls
- JSON project backup / restore and duplicate project
- Offline PWA support via `sw.js`
- Dark mode toggle
- Running total, category totals, and progress indicators
- Project last-saved timestamp and photo count

## How to submit
1. Create a GitHub repository and push these files.
2. Include a short README explaining how to run the app.
3. Share the repo URL with the contest reviewer.
4. Optionally deploy the app using GitHub Pages for easy mobile access.

## Extra submission notes
- `pricing-list.csv` is included as the source of truth for default repair costs.
- `manifest.json` and `sw.js` make the app installable and usable offline.
- `WRITEUP.md` can be exported as a one-page PDF for the required write-up.
