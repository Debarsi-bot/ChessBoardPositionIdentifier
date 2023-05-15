import chess
import chess.svg
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

def convertToIndex(cell):
    row = ord(cell[0])-97
    col = ord(cell[1])-48
    index = (col-1)*8 + (row)
    return index

def createImage(fenstring, bestMove):
    move_from = convertToIndex(bestMove[:2])
    move_to = convertToIndex(bestMove[2:])
    board = chess.Board()
    board.set_fen(fenstring)

    svg = chess.svg.board(
     board,
     arrows=[chess.svg.Arrow(move_from, move_to, color="#0000cccc")],
     size=350,
    )
    with open("chessboard.svg", "w") as f:
        f.write(svg)
    drawing = svg2rlg("chessboard.svg")
    renderPM.drawToFile(drawing, "temp.png", fmt="PNG")
    return svg


