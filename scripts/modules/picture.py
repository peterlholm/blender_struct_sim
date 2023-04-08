"Render a picture of current scene"
from  time import sleep
import bpy


class render_picture():
    "Render a single picture of current scene"
    rendering = False
    
    def myrender_complete(self, scene, depsgraph):
        #self.rendering = False
        self.rendering = False
        print("render_complete")

    
    def start_render(self, outpath):
        print("Start render:", outpath)
        self.rendering = True
        bpy.app.handlers.render_complete.clear()
        bpy.app.handlers.render_complete.append(self.myrender_complete) 
        sc = bpy.context.scene
        sc.render.filepath = outpath
        res = bpy.ops.render.render("INVOKE_DEFAULT", write_still=True)
        print(res)

    def wait_finish(self):
        while self.rendering:
            print('.', end="", flush=True )
            sleep(1)
        bpy.app.handlers.render_complete.remove(self.myrender_complete) 
        print("render_end")





if __name__ == '__main__':
    rp = render_picture()
    rp.start_render("ud.png")
    rp.wait_finish()

