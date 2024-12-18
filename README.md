# Matsuri Finder (お祭りファインダー)

An automated system for aggregating and tracking traditional Japanese festivals (お祭り).

## Features
- Automated collection of festival information from various sources
- Filtering system to identify genuine traditional festivals
- Annual event tracking and prediction
- Geolocation support (planned)

## Project Structure
```
./
├── scrapers/           # Data collection modules
│   ├── government.py   # Local government website scrapers
│   ├── twitter.py      # Twitter API integration
│   └── pdf.py         # PDF parsing utilities
├── processors/         # Data processing modules
│   ├── classifier.py   # Festival type classification
│   ├── geocoder.py    # Location processing
│   └── date.py        # Date standardization
├── database/          # Database models and migrations
└── api/               # API endpoints
```

## Installation
[TBD]

## Usage
[TBD]
