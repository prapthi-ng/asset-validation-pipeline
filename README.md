# Asset Validation Pipeline (Python)

This project is a simple Python program that validates asset files used in animation or game pipelines.

## It checks:

File type

Duplicate assets

Asset naming issues

Asset size (Heavy / Light)


## Features:

Valid file types: .png, .psd, .jpg

Detects invalid files

Detects duplicate assets

Warns for unclean names (spaces / uppercase)

Classifies assets as HEAVY or LIGHT

Handles missing size information

## Example Input

asset_list = [
   "bg_final_v2.png",
    "character_main.psd",
    "effect_v1.jpg",
    "logo.png",
    "virus.exe",
    "effect_v1.jpg",
    "effect v2.JPG"

]

asset_size = {
    "bg_final_v2.png": 40,
    "character_main.psd": 30,
    "effect_v1.jpg": 20,
    "logo.png": 15
}

## Example Output:

Processing:bg_final_v2.png | Size:40 MB | HEAVY

Processing:character_main.psd | Size:30 MB | HEAVY

Processing:effect_v1.jpg | Size:20 MB | LIGHT

Processing:logo.png | Size:15 MB | LIGHT

Processing:virus.exe | INVALID FILE TYPE

DUPLICATE FOUND: effect_v1.jpg

WARNING: Unclean asset name -> effect v2.JPG

Processing:effect v2.JPG | SIZE INFO MISSING


This project is inspired by animation pipeline validation, where assets must follow strict rules to avoid errors.

## Tech Used
Python 3

## Author:
Prapthi
|CSE Student | Learning Pipeline Development
