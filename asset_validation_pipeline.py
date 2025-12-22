#asset list
asset_list=["bg_final_v2.png", "character_main.psd", "effect_v1.jpg", "logo.png","virus.exe","effect_v1.jpg","effect v2.JPG"]


#asset size database
asset_size={
  "bg_final_v2.png": 25,
  "character_main.psd": 40,
  "effect_v1.jpg": 10,
  "logo.png": 5
}

#pipeline validation function
def validate_assets(asset_list,asset_dictionary):
    for asset_name in asset_list:

        # 1.File type validation
        if asset_name.lower().endswith((".png",".psd",".jpg")):

            # 2. Naming cleanliness validation
            if " " in asset_name or asset_name != asset_name.lower():
                print(f"WARNING: Unclean asset name -> {asset_name}")

            # 3.Size info check
            if asset_name in asset_dictionary:

                # 4.Classification:Heavy or Light
                size = asset_dictionary[asset_name]

                if size > 20:
                    print(f"Processing:{asset_name}|Size:{size} MB|HEAVY")
                else:
                    print(f"Processing:{asset_name}|Size:{size} MB|LIGHT")

            # Warning:size info missing
            else:    
                print(f"Processing:{asset_name}|SIZE INFO MISSING")
            
        # Warning:invalid file type
        else:
            print(f"Processing:{asset_name}|INVALID FILE TYPE")

# Run pipeline validation
validate_assets(asset_list,asset_size)       

