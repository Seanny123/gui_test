import nengo_gui
import threading
import traceback as tb
import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)
port = 8080
model_path= "model_basic.py"

gui = None
def do_gui():
    logging.info("Launching nengo_gui (port=%d)", port)
    #print("Launching nengo_gui (port=%d)", port)
    gui = nengo_gui.GUI(model_path)
    try:
        gui.start(port=port, browser=False)
    except:
        logging.debug("Server raised exception, suppressed:\n%s",
                      tb.format_exc(()))

# start the server in it's own thread
threading.Thread(target=do_gui).start()

d = webdriver.Firefox()
d.get(gui)