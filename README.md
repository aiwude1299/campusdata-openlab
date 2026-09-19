# CampusData-OpenLab

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Development-blue.svg)]()

CampusData-OpenLab is an open-source environmental data pipeline and academic sandbox designed for university research and students' thesis experiments.

## System Architecture

```text
+------------------+      +------------------+      +-------------------+
|  FastAPI Backend | ---> | PostgreSQL/GIS   | ---> | Redis Cache Layer |
+------------------+      +------------------+      +-------------------+
