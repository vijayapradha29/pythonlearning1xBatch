#cars
#attribute:name,colour,model,engine type,speed
#function:start engine,drive,stop engine,break,stearing
#objects:tesla,lamborgini

class Cars:
    name=None
    colour=None
    model=None
    engine_type=None
    speed=None

    def start_engine(self):
        print("Starting the Engine")
    def drive(self):
        print("Drive")
    def stop_engine(self):
        print("Stop the Engine")
    def apply_break(self):
        print("Apply the Break")

tesla_object=Cars()
tesla_object.name="Tesla"
tesla_object.model="I100"
tesla_object.speed=200
tesla_object.colour="Black"
tesla_object.engine_type="Dual Engine"
tesla_object.drive()
print(tesla_object)