# Spark Homes Repair Estimator Writeup

## 1. Most interesting design decision
I built the app as a mobile-first, field-ready estimator with a compact project toolbar, search-driven repair selection, and instant budget tracking. The goal was to make every walkthrough fast: agents can search repairs, add notes, set a budget target, capture photos, and export the entire estimate without leaving the page.

## 2. What is broken or fragile
- The service worker and manifest require HTTPS or a local server to register properly; file:// mode may not install the PWA.
- Large photo uploads can consume localStorage quota, so the app currently retries saving without photo blobs if storage is full.
- The JSON import helper expects a valid Spark Homes backup structure and will fail on unrelated JSON files.

## 3. Creative addition
I added an offline-ready project toolbar with:
- search filter for all repairs,
- project notes,
- budget target tracking with over/under alerts,
- JSON project backup/restore,
- duplicate project support,
- and dark mode.

This turns the estimator into a lightweight field operations assistant, not just a cost calculator.

## 4. What I would ship next with two more days
- Add bedroom and living-room instance support like the bathroom system.
- Add contractor/vendor contact cards and a materials supplier list.
- Add a PDF export summary and print-friendly estimate sheet.
- Add optional serial number recognition from photos.
- Add a deal analyzer that compares estimate cost against ARV and purchase price.

## Live Demo
[Open the app on GitHub Pages](https://dhaliwalp.github.io/Spark-Homes-Repair-Estimator/spark-homes-estimator.html)

## AI role
AI assisted in reading the reference app structure and generating the PWA and helper code scaffolding. All app logic and integration were adapted to ensure offline support, project persistence, and export capabilities.
