# Asset list
asset_list = [
    "bg_final_v2.png",
    "character_main.psd",
    "effect_v1.jpg",
    "logo.png",
    "virus.exe",
    "effect_v1.jpg",
    "effect v2.JPG"
]

# Asset size database
asset_size = {
    "bg_final_v2.png": 40,
    "character_main.psd": 30,
    "effect_v1.jpg": 20,
    "logo.png": 15
}

# File type validation
def is_valid_file(asset):
    return asset.lower().endswith((".png", ".psd", ".jpg"))

# Size classification
def classify_size(asset, asset_dict):
    if asset not in asset_dict:
        return "MISSING"

    return "HEAVY" if asset_dict[asset] > 20 else "LIGHT"

# pipeline validation function
def validate_assets(asset_list, asset_dict):
    seen = set()

    for asset in asset_list:

        # Duplicate check
        if asset in seen:
            print(f"DUPLICATE FOUND: {asset}")
            continue
        seen.add(asset)

        # File type check
        if not is_valid_file(asset):
            print(f"Processing:{asset} | INVALID FILE TYPE")
            continue

        # Naming cleanliness validation
        if " " in asset or asset != asset.lower():
            print(f"WARNING: Unclean asset name -> {asset}")

        # Size classification
        status = classify_size(asset, asset_dict)

        if status == "MISSING":
            print(f"Processing:{asset} | SIZE INFO MISSING")
        else:
            size = asset_dict[asset]
            print(f"Processing:{asset} | Size:{size} MB | {status}")

# pipeline validation function
validate_assets(asset_list, asset_size)


