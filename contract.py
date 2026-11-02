from dataclasses import dataclass
from enum import Enum
from typing import Annotated

from slimconfig import Output


class Tool(Enum):
    COMPUTE = "recover_hamming"
    SAVE = "save_result"


class Task(Enum):
    RUN = "hamming-recover"


@dataclass
class ComputeInput(Output):
    codewords: Annotated[list[str], "codewords"]


@dataclass
class ComputeOutput(Output):
    syndromes: Annotated[list[int], "syndromes"]
    corrected_positions: Annotated[list[int], "corrected positions"]
    corrected: Annotated[list[str], "corrected"]
    payloads: Annotated[list[str], "payloads"]


@dataclass
class SaveInput(Output):
    result: Annotated[ComputeOutput, "result"]


@dataclass
class SaveOutput(Output):
    path: Annotated[str, "path"]
    result: Annotated[ComputeOutput, "result"]


TOOLS = {Tool.COMPUTE: (ComputeInput, ComputeOutput), Tool.SAVE: (SaveInput, SaveOutput)}
TASKS = {Task.RUN: (ComputeInput, SaveOutput)}
