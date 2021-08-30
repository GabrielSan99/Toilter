from app import manager

if __name__ == "__main__":
    manager.run()





#python3 run.py runserver     ---->     this command run the file run.py to open web
#python3 run.py db init       ---->     create the imigrations folder
#python3 run.py db imigrate   ---->     imigrate the changes on database in the standby mode
#python3 run.py db upgrade    ---->     apply the changes on database after imigrate 