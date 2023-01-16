import pcbnew
board = pcbnew.GetBoard()
def find_layer(board, layer_name):
    for i in range(128):
        if board.GetLayerName(i) == layer_name:
            return i
    return -1

def find_pad(module, padName):
    for pad in module.Pads():
        if pad.GetPadName() == padName:
            return pad
    return None

def add_text(board,text,x,y,size,angle):
    pcb_txt = pcbnew.PCB_TEXT(board)
    pcb_txt.SetText("Hellorld")
    pcb_txt.SetPosition(pcbnew.wxPointMM(x, y))
    pcb_txt.SetHorizJustify(pcbnew.GR_TEXT_HJUSTIFY_CENTER)
    pcb_txt.Rotate(pcbnew.wxPointMM(x, y), angle)
    pcb_txt.SetTextSize(pcbnew.wxSizeMM(size, size))
    pcb_txt.SetLayer(pcbnew.F_SilkS)
    board.Add(pcb_txt)
