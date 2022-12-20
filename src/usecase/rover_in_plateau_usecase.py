import logging
from model.plateau_model import PlateauModel
from model.rover_model import RoverModel
from database.config_db import coordinates, coordinates_config

logger = logging.getLogger(__name__)

def read_file(file_path):
    try:
        result = []
        with open(file_path) as arquivo:
            plateau = _create_plateau(arquivo.readline().replace('\n', ''))
            if(plateau):
                for linha in arquivo:
                    rover = _create_rover(linha.replace('\n', ''))
                    if rover:
                        _move_rover(arquivo.readline().replace('\n', ''), rover, plateau)
                        result.append(str(rover))
        return result
    except FileNotFoundError as error:
        logger.error(error)
        raise
    except Exception as error:
        logger.error(error)
        raise
    
                

def _create_plateau(size_palteau):
    try:
        iten =size_palteau.split(" ")
        plateau = PlateauModel(int(iten[0]), int(iten[1]))
        return plateau

    except ValueError as error:
        logger.error(error)
        return None
    except Exception as error:
        logger.error(error)
        return None

def _create_rover(initrover) -> RoverModel:
    try:
        iten =initrover.split(" ")
        rovermodel = RoverModel(int(iten[0]), int(iten[1]), iten[2])
        return rovermodel
    except ValueError as error:
        logger.error(error)
        return None
    except Exception as error:
        logger.error(error)
        return None


"""
 R = Direita soma no array
 L = Esquerda subtrai no array
 M = move soma 1 no Y quando for N e subritai 1  do Y quando for S
 M = move soma 1 no X quando for E e subritai 1  do X quando for O
"""

def _move_rover(moverover, rovermodel: RoverModel, plateau: PlateauModel):
    indice = 0
    while indice < len(moverover):
        if moverover[indice] == "R":
            rovermodel.turn_right(coordinates)
        elif moverover[indice] == "L":
            rovermodel.turn_left(coordinates)
        elif moverover[indice] == "M":
            rovermodel.move(coordinates_config, plateau)
        else:
            logger.warning("invalid value")
        indice = indice +1