# asset list
asset_list=["bg_final_v2.png", "character_main.psd", "effect_v1.jpg", "logo.png","virus.exe","effect_v1.jpg","effect v2.JPG"]


#asset size database
asset_size={
  "bg_final_v2.png": 25,
  "character_main.psd": 40,
  "effect_v1.jpg": 10,
  "logo.png": 5
}

def validate_assets(asset_list, asset_dictionary):
    total_assets = len(asset_list)
    # initialising counter
    valid_assets = 0
    invalid_files = 0
    heavy = 0
    light = 0
    missing_info = 0

    seen = set()

    for asset in asset_list:

        # Duplicate check
        if asset in seen:
            print(f"DUPLICATE FOUND: {asset}")
            continue
        seen.add(asset)

        # File type check
        if not asset.lower().endswith((".png", ".psd", ".jpg")):
            print(f"Processing:{asset} | INVALID FILE TYPE")
            invalid_files += 1
            continue

        valid_assets += 1

        # Size check
        if asset in asset_dictionary:
            size = asset_dictionary[asset]

            if size > 20:
                heavy += 1
                print(f"Processing:{asset} | Size:{size} MB | HEAVY")
            else:
                light += 1
                print(f"Processing:{asset} | Size:{size} MB | LIGHT")
        else:
            missing_info += 1
            print(f"Processing:{asset} | SIZE INFO MISSING")

    # Summary
    print("\n----- PIPELINE SUMMARY -----")
    print(f"Total assets: {total_assets}")
    print(f"Valid assets: {valid_assets}")
    print(f"Invalid assets: {invalid_files}")
    print(f"Heavy assets: {heavy}")
    print(f"Light assets: {light}")
    print(f"Missing size info: {missing_info}")
    print("----------------------------")
validate_assets(asset_list,asset_size)
