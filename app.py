import os
os.system(f"git lfs install")
os.system(f"git clone -b lambda https://github.com/camenduru/Radiata /home/demo/source/Radiata")
os.chdir(f"/home/demo/source/Radiata")
os.system(f"sed -i 's/runwayml\/stable-diffusion-v1-5/uf\/dark-sushi-25d/g' /home/demo/source/Radiata/modules/config.py")
os.system(f"python launch.py --port 8266 --tensorrt")
