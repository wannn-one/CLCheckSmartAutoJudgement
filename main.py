# main.py
from src.model.model import LogicTracerModel
from src.view.view import LogicTracerView
from src.controller.controller import LogicTracerController

def main():
    model = LogicTracerModel()
    view = LogicTracerView()
    controller = LogicTracerController(model=model, view=view)
    
    view.set_controller(controller)
    view.mainloop()

if __name__ == "__main__":
    main()