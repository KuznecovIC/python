from dataclasses import dataclass, field
import json
from typing import Iterator, List, Dict, Optional

@dataclass
class TranscriptionChunk:
    text: str
    int_start: float
    int_end: float
    str_start: str = field(init=False)
    str_end: str = field(init=False)

    def __post_init__(self):
        self.str_start = self._int_to_str(self.int_start)
        self.str_end = self._int_to_str(self.int_end)

    def _int_to_str(self, int_time: float) -> str:
        hours = int_time // 3600
        minutes = (int_time % 3600) // 60
        seconds = int_time % 60
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

class TranscriptionIterator:
    def __init__(self, transcription_data: List[Dict[str, List[Optional[float]]]]):
        self.transcription_data = transcription_data
        self.index = 0
        self.data_len = len(self.transcription_data)
    def __iter__(self) -> Iterator[TranscriptionChunk]:
        return self
    
    def __next__(self) -> TranscriptionChunk:
        if self.index >= len(self.transcription_data):
            raise StopIteration
        data = self.transcription_data[self.index]
        self.index += 1
        return self._chunk_serialize(data)
    
    def _chunk_serialize(self, data: Dict[str, List[Optional[float]]|str]) -> TranscriptionChunk:
            text=data["text"],
            int_start=data["timestamp"][0],
            int_end=data["timestamp"][1] if data["timestamp"][1] is not None else data["timestamp"][0]
            instance = TranscriptionChunk(text=text, int_start=int_start, int_end=int_end)
            return instance
    
def main():
    with open(JSON_DATA, "r", encoding="utf-8") as file:
        DATA = json.load(file)

    iterator = TranscriptionIterator(DATA)
    for chunk in iterator:
        print(chunk)

if __name__ == "__main__":
    main()
    pass