import os
import array

## SETTINGS
window_size_x, window_size_y = 15,15
## SETTINGS


class Block():
    def __init__(self, block_id, block_symbol, block_name, block_isSolid, block_isBrakeble):
        self.id = block_id
        self.symbol = block_symbol
        self.name = block_name
        self.isSolid = block_isSolid
        self.isBrakeble = block_isBrakeble

    def GetBlockPosition():
        return [0,0]
    def GetBlockData():
        return self.id, self.symbol, self.name, self.isSolid, self.isBrakeble
    def GetBlockId(self):
        return self.id
    def GetBlock(self):
        return self.symbol
    def GetBlock(self):
        return self.name
    def GetBlock(self):
        return self.isSolid
    def GetBlock(self):
        return self.isBrakeble

class Chunk():
    def __init__(self, chunk_global_position_x, chunk_global_position_y):
        _blocks = array.array("H", [0] * (x*y*z))
        self.size_x = 16
        self.size_y = 16
        self.size_z = 256
        self.chunk_position_x = chunk_global_position_x
        self.chunk_position_y = chunk_global_position_y
        #size is fixed by 16*16*100
       #pass 
    def DestroyBlock(self, x,y,z, block):
        # block in position x,y,z changed on block
        position = x * (y * size_x) + (z * size_x * size_y)
        _blocks[position] = 0
    def GetBlockByPosition(self, x,y,z):
        position = x * (y * size_x) + (z * size_x * size_y)
        return _blocks[position]
    def SetBlock(self,x,y,z):
        position = x * (y * size_x) + (z * size_x * size_y)
    def FillBlocksDev(self, z_max_level):
        for z in range(z_max_level):
            for x in range(16):
                for Y in range(16):
                    position = x * (y * size_x) + (z * size_x * size_y)
                    _blocks[position] = 1

    


class World():
    def __init__(self, chunks):
        self.Chunks = chunks
    def GenerateDevWorld(self):
        Chunks = [Chunk(-1,-1),Chunk(-1,0),Chunk(-1,1),Chunk(0,-1),Chunk(0,0),Chunk(0,1),Chunk(1,-1),Chunk(1,0),Chunk(1,1)]
        for c in Chunks:
            c.FillBlocksDev(100)
        print("Generated dev world")
    def GetChunk(self, x,y):
        ## Get chunk by position x and y
        return 0

class Scene():
    def __init__(self, world, linear_array):
        self.linear_array = 1
        #need to know all game objects, cameras, chunks, etc



class Transform():
    def __init__(self, position_x, position_y, position_z):
        self.X = position_x
        self.Y = position_y
        self.Z = position_z
    def Move(self, x,y,z):
        self.X += x
        self.Y += y
        self.Z += z
    def GetPosition(self):
        return x,y,z


class GameObject(Transform):

    def __init__(self, id_, transform_):
        self.id = id
        self.transform = transform_
    
    def GetId(self):
        return self.id





class Camera(Transform):
    def __init__(silf, camera_render_size_x, camera_render_size_y):
        self.render_size_x = camera_render_size_x
        self.render_size_y = camera_render_size_y
    #def GetCameraPosition():
    #    pass
    #def Move():
    #    pass

    
def Render(world2_dev,current_z):
    videoBuffer = ""
    #for y in range(window_size_y):
    #    for x in range(window_size_x):
    #        videoBuffer += ".."
    #    videoBuffer += "\n"
    #print(videoBuffer)

    #videoBuffer = ""
    for z in range(current_z):
        for x in range(16):
            for y in range(16):
                world2_dev.
                videoBuffer
    










##Main LOOP
#while (True):
#    Render()
#    
#    input()

#game initiation/start

def init():
    camera1 = ""

    chunks1 = Chunk(0,0)
    world1 = World(chunks1)
    world1.GenerateDevWorld()
    scene1 = ""
    scene1 = Scene()

    while (True):
        Render(world1)
        input()
